### To run with PySpark locally:
* Download or fetch repository
* Make sure that you have necessary libraries installed
* Run 'get_25m_data.py' file to download and unzip data
* Run 'spark_movie_recommendation.ipynb' file (add '.limit(numrows)' to the end of the 'spark.read.csv' lines to run with less data)

### To run using PySpark on the cloud:
* There are many different options; See paper to see how we used Google Cloud Dataproc
