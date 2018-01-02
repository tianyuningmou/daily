#### 什么是ipcs
	ipcs是Linux下显示进程间通信设施状态的工具。可以显示消息队列、共享内存和信号量的信息

#### ipcs的常见用法
	ipcs -m 查看系统使用的IPC共享内存资源
	ipcs -q 查看系统使用的IPC队列资源
	ipcs -s 查看系统使用的IPC信号量资源

#### 修改IPC系统参数
###### 以linux系统为例，在root用户下修改/etc/sysctl.conf 文件，保存后使用sysctl -p生效
	$cat /etc/sysctl.conf
	# 一个消息的最大长度
	kernel.msgmax = 524288

	# 一个消息队列上的最大字节数
	# 524288*10
	kernel.msgmnb = 5242880

	# 最大消息队列的个数
	kernel.msgmni=2048

	# 一个共享内存区的最大字节数
	kernel.shmmax = 17179869184

	# 系统范围内最大共享内存标识数
	kernel.shmmni=4096

	# 每个信号灯集的最大信号灯数 系统范围内最大信号灯数 每个信号灯支持的最大操作数 系统范围内最大信号灯集数
	# 此参数为系统默认，可以不用修改
	# kernel.sem = <semmsl> <semmni>*<semmsl> <semopm> <semmni>
	kernel.sem = 250 32000 32 128
	
#### 清除IPC资源
###### 使用ipcrm 命令来清除IPC资源：这个命令同时会将与ipc对象相关联的数据也一起移除。当然，只有root用户，或者ipc对象的创建者才有这项权利
	ipcrm -M shmkey   移除用shmkey创建的共享内存段
	ipcrm -m shmid    移除用shmid标识的共享内存段
	ipcrm -Q msgkey   移除用msqkey创建的消息队列
	ipcrm -q msqid    移除用msqid标识的消息队列
	ipcrm -S semkey   移除用semkey创建的信号
	ipcrm -s semid    移除用semid标识的信号

