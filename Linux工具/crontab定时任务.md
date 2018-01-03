#### crontab介绍
	通过crontab 命令，我们可以在固定的间隔时间执行指定的系统指令或 shell script脚本。时间间隔的单位可以是分钟、小时、日、月、周及以上的任意组合。这个命令非常适合周期性的日志分析或数据备份等工作

#### crontab命令格式
	crontab [-u user] file crontab [-u user] [-e|-l|-r]

#### crontab参数
	-u user：用来设定某个用户的crontab服务
	file：   file是命令文件的名字,表示将file做为crontab的任务列表文件并载入crontab。如果在命令行中没有指定这个文件，crontab命令将接受标准输入（键盘）上键入的命令，并将它们载入crontab
	-e：     编辑某个用户的crontab文件内容。如果不指定用户，则表示编辑当前用户的crontab文件
	-l：     显示某个用户的crontab文件内容，如果不指定用户，则表示显示当前用户的crontab文件内容
	-r：     从/var/spool/cron目录中删除某个用户的crontab文件，如果不指定用户，则默认删除当前用户的crontab文件
	-i：     在删除用户的crontab文件时给确认提示

#### crontab的文件格式
	第1列分钟0～59
	第2列小时0～23（0表示子夜）
	第3列日1～31
	第4列月1～12
	第5列星期0～7（0和7表示星期天）
	第6列要运行的命令

#### crontab常用方法
![crontab-0](http://img.zcool.cn/community/01ffb05a4ca8d4a801206ed3d44a23.png@1280w_1l_2o_100sh.png)
![crontab-1](http://img.zcool.cn/community/01412e5a4ca8d4a801206ed3b96509.png@1280w_1l_2o_100sh.png)

#### crontab使用示例
![crontab-2](http://img.zcool.cn/community/0122f65a4ca8d4a801206ed351e882.png@1280w_1l_2o_100sh.png)
![crontab-3](http://img.zcool.cn/community/01d1655a4ca8d4a801219741a6f8d4.png@1280w_1l_2o_100sh.png)

#### crontab注意事项
![crontab-4](http://img.zcool.cn/community/012ddc5a4ca8d4a80121974164e9f1.png@1280w_1l_2o_100sh.png)
![crontab-5](http://img.zcool.cn/community/01098b5a4ca8d4a801206ed3123fb5.png@1280w_1l_2o_100sh.png)
![crontab-6](http://img.zcool.cn/community/017f745a4ca8d4a801219741d08dc3.png@1280w_1l_2o_100sh.png)

