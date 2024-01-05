

import os
os.environ["PYSPARK_PYTHON"] = f"C:/Users/32394/AppData/Local/Programs/Python/Python312/python.exe"


def some_function():
    from pyspark import SparkConf, SparkContext
    conf = SparkConf().setAppName("myApp").setMaster("local")
    sc = SparkContext(conf=conf)
    # Your code using SparkConf and SparkContext here


some_function()


def func(data):
    return data * 2


rdd = sc.parallelize([1, 2, 3, 4, 5])
rdd1 = rdd.map(func)
print(rdd1.collect())
