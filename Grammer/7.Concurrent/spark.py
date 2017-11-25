
''' 
	基于Map reduce算法实现的分布式计算框架：
	
	1.中间输出和结果的输出都可以保存在内存中，不需要读HDFS
	2.Spark可以更好的执行迭代类的操作

	 ________________________________________
     | Spark  | Spark 	  | MLib   | GraphX |
     |  SQL	  | Streaming | (ML)   | (parph)|
	 |________|___________|________|________|
	 |										|
	 |		Apache Spark					|
	 |______________________________________|

	
	Spark与Hadoop结合：
		1.Spark可以直接对HDFS进行数据读写,支持Spark on YARN
		2.Spark可以与MapReduce运行于同集群中，共享存储资源与计算

	核心：RDD 弹性分布式数据集
		Datasets:
			1.集群节点上不可变，
			2.可序列化
			3.可控制存储级别

'''	 



