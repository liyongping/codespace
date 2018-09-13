

import org.apache.spark.{SparkConf, SparkContext}
import org.apache.log4j.{Level, Logger}

object WordCount {
    def main(args: Array[String]): Unit = {

        Logger.getLogger("org").setLevel(Level.WARN)


        val sc = new SparkContext(new SparkConf().setAppName("WordCount").setMaster("local[4]"))
        //val sc = new SparkContext(new SparkConf().setAppName("WordCount").setMaster("spark://yongpili-mac:7077"))
        //val line = sc.textFile("hdfs://localhost:8020//user/vincent/README.md")
        val line = sc.textFile(args(0))

        val word_counts = line.flatMap(x => x.split(""))
            .map(word => (word, 1))
            .reduceByKey((a,b) => a+b)
        //            .collect()

        //word_counts.saveAsTextFile("hdfs://localhost:8020//user/vincent/README.md_word_counts5")
        word_counts.saveAsTextFile(args(1))

        sc.stop()

    }
}