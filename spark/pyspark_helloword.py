## Spark Application - execute with spark-submit

from pyspark import SparkConf, SparkContext



def main(sc):
    nums = sc.parallelize([1, 2, 3, 4])
    squared = nums.map(lambda x: x * x).collect()
    for num in squared:
        print "%i " % (num)
 
if __name__ == "__main__":
    # Configure Spark
    conf = SparkConf().setMaster("local").setAppName("My App")
    sc = SparkContext(conf = conf)
 
    # Execute Main functionality
    main(sc)
