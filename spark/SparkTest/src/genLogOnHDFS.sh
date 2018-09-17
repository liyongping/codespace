#!/bin/bash 

# HDFS命令 
HDFS="$HADOOP_HOME/bin/hadoop fs"

# Streaming程序监听的目录，注意跟后面Streaming程序的配置要保持一致 
streaming_dir="/spark/streaming"

# 清空旧数据 
$HDFS -rm "${streaming_dir}"'/tmp/*' > /dev/null 2>&1 
$HDFS -rm "${streaming_dir}"'/*'     > /dev/null 2>&1 

# 一直运行 
while [ 1 ]; do 
    ./sample_web_log.py > test.log  

    # 给日志文件加上时间戳，避免重名 
    tmplog="access.`date +'%s'`.log" 

    # 先放在临时目录，再move至Streaming程序监控的目录下，确保原子性
    # 临时目录用的是监控目录的子目录，因为子目录不会被监控
    $HDFS -put test.log ${streaming_dir}/tmp/$tmplog 
    $HDFS -mv           ${streaming_dir}/tmp/$tmplog ${streaming_dir}/ 
    echo "`date +"%F %T"` put $tmplog to HDFS succeed"
    sleep 1
done 
