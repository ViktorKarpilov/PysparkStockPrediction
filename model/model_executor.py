from pyspark.sql import SparkSession
from pyspark.ml import Pipeline
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.regression import DecisionTreeRegressor
from pyspark.ml.evaluation import RegressionEvaluator
from pyspark.sql import SparkSession
from pyspark.ml import Pipeline
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.regression import DecisionTreeRegressor
from pyspark.ml.evaluation import RegressionEvaluator

class ModelExecutor():
    def __init__(this):
        spark = SparkSession.builder \
            .appName("Decision Tree Regression with PySpark") \
            .getOrCreate()
        # __model = DecisionTreeRegressor.load("./tree_regressor")

    def predict(this, previousData, period):
        result = [previousData]

        for i in range(period):
            result.append(__model.transform(result[-1]))

        return result

model_executor = ModelExecutor()