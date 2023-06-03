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
from pyspark.ml import PipelineModel

class ModelExecutor():
    def __init__(this):
        print("init")
        # spark = SparkSession.builder \
        #     .appName("Decision Tree Regression with PySpark") \
        #     .getOrCreate()
        # __model = PipelineModel.load("./model/tree_regressor")

    def predict(this,ticker, open, hight, low, closed, hours):
        # result = [previousData]

        # for i in range(period):
        #     result.append(__model.transform(result[-1]))

        return [1,2,3,4,5,6,7,8,9,1,4]

model_executor = ModelExecutor()