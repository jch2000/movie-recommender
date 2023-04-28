from pyspark.sql import SparkSession
from pyspark.ml.recommendation import ALS
from pyspark.ml.evaluation import RegressionEvaluator
from pyspark.sql.functions import col

# Initialize SparkSession
spark = SparkSession.builder.appName('25m_movie_lens').getOrCreate()

# Load both the ratings and movies data into a pandas DataFrame
ratings_df = spark.read.csv('gs://dataproc-staging-us-central1-155139700371-liojrpb3/ml-25m/ratings.csv', header=True, inferSchema=True)
movies_df = spark.read.csv('gs://dataproc-staging-us-central1-155139700371-liojrpb3/ml-25m/movies.csv', header=True, inferSchema=True)
ratings_df.show()
movies_df.show()

# Left join ratings on movies
join_df = ratings_df.join(movies_df, on='movieId', how='left') \
    .select(col('userId'), col('movieId'), col('rating'), col('title'), col('genres')) \
    .sort('userId')
join_df.show()

(train_df, test_df) = join_df.randomSplit([0.8, 0.2])

# Define ALS model
als = ALS(maxIter=15, regParam=0.01, userCol="userId", itemCol="movieId", ratingCol="rating",
          coldStartStrategy="drop", nonnegative=True)

# Fit data and make predictions
model = als.fit(train_df)
predictions = model.transform(test_df)
predictions.show()

# Evaluate model using RMSE
evaluator = RegressionEvaluator(metricName="rmse", labelCol="rating", predictionCol="prediction")
rmse = evaluator.evaluate(predictions)
print("Root Mean Squared Error = {:.4f}".format(rmse))

# Stop SparkSession
spark.stop()