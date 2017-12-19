#### 在Mac下，先安装[homebrew](https://github.com/tianyuningmou/daily/blob/master/homebrew的使用.md),在终端执行命令
	/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

#### 利用hombrew安装nginx
	brew install nginx

#### 修改本地hosts文件，在文件内添加域名解析
	sudo vi /etc/hosts

#### 修改nginx配置文件，设置反向代理
	sudo vim /usr/local/etc/nginx/nginx.conf
	
#### 找到server ---> location块，在块内添加如下内容：
	proxy_pass [网址]

#### 启动nginx，如安装了apache，请确保apache处于关闭状态
	sudo nginx
	
	


