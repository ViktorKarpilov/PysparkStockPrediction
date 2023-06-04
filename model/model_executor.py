from pyspark.sql import SparkSession, types
from pyspark.ml import Pipeline, PipelineModel
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.regression import DecisionTreeRegressor
from pyspark.ml.evaluation import RegressionEvaluator
from pyspark.sql.functions import lit

import pandas as pd
from datetime import timedelta


class ModelExecutor():
    def __init__(self):
        self.__spark = SparkSession.builder \
            .appName("Decision Tree Regression with PySpark") \
            .getOrCreate()
        self.__model = PipelineModel.load("./model/tree_regressor")

    def __prepare_df(self, data):
        df = pd.DataFrame(data)
        df['DateTime'] = pd.to_datetime(df['DateTime'])
        df[["Open", "High", "Low", "Close", "Volume"]] = df[["Open", "High", "Low", "Close", "Volume"]].pct_change()
        df["EMA-8"] = df["Close"].ewm(span=8, adjust=False).mean()
        df["EMA-32"] = df["Close"].ewm(span=32, adjust=False).mean()
        df.dropna(inplace=True)

        spark_df = self.__spark.createDataFrame(df)
        spark_df = spark_df.orderBy("DateTime", ascending=False).limit(1)
        spark_df = spark_df.withColumn("Target", lit(None).cast(types.NullType()))

        return spark_df

    def __calc_ema(self, current_close_price, previous_ema, lag):
        k = 2 / (lag + 1)
        current_ema = (current_close_price * k) + (previous_ema * (1 - k))
        return current_ema
    
    def __get_next_df(self, prediction: dict, schema):
        price = prediction['prediction']
        return self.__spark.createDataFrame([
            (
                prediction['DateTime'],
                price, price, price, price,
                prediction['Volume'],
                self.__calc_ema(price, prediction['EMA-32'], 32),
                self.__calc_ema(price, prediction['EMA-8'], 8),
                None
            )
        ], schema=schema)

    def __restore(self, first_close_price: float, prc: list):
        prices = [first_close_price * (1 + prc[0])]
        for p in prc[1:]:
            prices.append( prices[-1] * (1 + p) )
        return prices

    def predict(self, data: dict, hours: int):
        '''
        data = {
            'DateTime': [...],
            'Open': [...],
            'High': [...],
            'Low': [...],
            'Close': [...],
            'Volume': [...]
        }
        '''
        result = []

        df = self.__prepare_df(data)
        prediction = [r.asDict() for r in self.__model.transform(df).collect()][0]
        result.append(prediction['prediction'])

        for _ in range(hours - 1):
            next_df = self.__get_next_df(prediction, df.schema)
            prediction = [r.asDict() for r in self.__model.transform(next_df).collect()][0]
            result.append(prediction['prediction'])

        return self.__restore(result, data['Close'][-1])

model_executor = ModelExecutor()