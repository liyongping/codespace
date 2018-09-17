// refer to https://www.shiyanlou.com/courses/812/labs/2855/document

import org.apache.spark.{SparkConf, SparkContext}
import org.apache.log4j.{Level, Logger}
import org.apache.spark.streaming._

object streaming_log_analyze {
    def main(args: Array[String]): Unit = {
        Logger.getLogger("org").setLevel(Level.WARN)


        val sc = new SparkContext(new SparkConf().setAppName("WordCount").setMaster("local[4]"))
        
        val ssc = new StreamingContext(sc,Seconds(5))
        
        val lines = ssc.textFileStream("hdfs://localhost//spark/streaming")
        
        // 1. 总PV
        lines.count().print()
        
        
        // 2. 各IP的PV，按PV倒序
        //   空格分隔的第一个字段就是IP
        lines.map(line => {(line.split(" ")(0), 1)}).reduceByKey(_ + _).transform(rdd => {
          rdd.map(ip_pv => (ip_pv._2, ip_pv._1)).
          sortByKey(false).
          map(ip_pv => (ip_pv._2, ip_pv._1))
        }).print()
        
        
        // 3. 搜索引擎PV
        val refer = lines.map(_.split("\"")(3))
        
        // 先输出搜索引擎和查询关键词，避免统计搜索关键词时重复计算
        // 输出(host, query_keys)
        val searchEnginInfo = refer.map(r => {
        
            val f = r.split('/')
        
            val searchEngines = Map(
                "www.google.cn" -> "q",
                "www.yahoo.com" -> "p",
                "cn.bing.com" -> "q",
                "www.baidu.com" -> "wd",
                "www.sogou.com" -> "query"
            )
        
            if (f.length > 2) {
                val host = f(2)
        
                if (searchEngines.contains(host)) {
                    val query = r.split('?')(1)
                    if (query.length > 0) {
                        val arr_search_q = query.split('&').filter(_.indexOf(searchEngines(host)+"=") == 0)
                        if (arr_search_q.length > 0)
                            (host, arr_search_q(0).split('=')(1))
                        else
                            (host, "")
                    } else {
                        (host, "")
                    }
                } else
                    ("", "")
            } else
                ("", "")
        
        })
        
        // 输出搜索引擎PV
        searchEnginInfo.filter(_._1.length > 0).map(p => {(p._1, 1)}).reduceByKey(_ + _).print()
        
        
        // 4. 关键词PV
        searchEnginInfo.filter(_._2.length > 0).map(p => {(p._2, 1)}).reduceByKey(_ + _).print()
        
        
        // 5. 终端类型PV
        lines.map(_.split("\"")(5)).map(agent => {
            val types = Seq("iPhone", "Android")
            var r = "Default"
            for (t <- types) {
                if (agent.indexOf(t) != -1)
                    r = t
            }
            (r, 1)
        }).reduceByKey(_ + _).print()
        
        
        // 6. 各页面PV
        lines.map(line => {(line.split("\"")(1).split(" ")(1), 1)}).reduceByKey(_ + _).print()
        
        
        
        // 启动计算,等待执行结束（出错或Ctrl-C退出）
        ssc.start()
        ssc.awaitTermination()
        
        ssc.start()
        ssc.awaitTermination()
        
    }
}