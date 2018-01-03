#### sar命令介绍
	sar是System Activity Reporter（系统活动情况报告）的缩写。sar工具将对系统当前的状态进行取样，然后通过计算数据和比例来表达系统的当前运行状态。它的特点是可以连续对系统取样，获得大量的取样数据；取样数据和分析的结果都可以存入文件，所需的负载很小。sar是目前Linux上最为全面的系统性能分析工具之一，可以从14个大方面对系统的活动进行报告，包括文件的读写情况、系统调用的使用情况、串口、CPU效率、内存使用状况、进程活动及IPC有关的活动等。
	sar是查看操作系统报告指标的各种工具中，最为普遍和方便的；它有两种用法；
		①追溯过去的统计数据（默认）
		②周期性的查看当前数据

#### sar安装
	①有的linux系统下，默认可能没有安装这个包，使用apt-get install sysstat 来安装；
	②安装完毕，将性能收集工具的开关打开：vi /etc/default/sysstat   设置 ENABLED=”true”
	③启动这个工具来收集系统性能数据：/etc/init.d/sysstat start

#### sar参数
	-A 汇总所有的报告
	-a 报告文件读写使用情况
	-B 报告附加的缓存的使用情况
	-b 报告缓存的使用情况
	-c 报告系统调用的使用情况
	-d 报告磁盘的使用情况
	-g 报告串口的使用情况
	-h 报告关于buffer使用的统计数据
	-m 报告IPC消息队列和信号量的使用情况
	-n 报告命名cache的使用情况
	-p 报告调页活动的使用情况
	-q 报告运行队列和交换队列的平均长度
	-R 报告进程的活动情况
	-r 报告没有使用的内存页面和硬盘块
	-u 报告CPU的利用率
	-v 报告进程、i节点、文件和锁表状态
	-w 报告系统交换活动状况
	-y 报告TTY设备活动状况

#### sar使用示例
![追溯过去的统计数据](http://img.zcool.cn/community/01fe5e5a4c7a9ea801206ed328a539.png@1280w_1l_2o_100sh.png)

![查看CPU使用率](http://img.zcool.cn/community/0140315a4c7a9ea801206ed36c3558.png@1280w_1l_2o_100sh.png)

![查看平均负载](http://img.zcool.cn/community/01c42b5a4c7a9ea801206ed3f63f1d.png@1280w_1l_2o_100sh.png)

![查看内存使用情况](http://img.zcool.cn/community/012cf75a4c7a9ea801206ed3c217db.png@1280w_1l_2o_100sh.png)

![查看页面交换发生情况](http://img.zcool.cn/community/01320e5a4c7a9ea801219741edd2d8.png@1280w_1l_2o_100sh.png)

