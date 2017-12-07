## Homebrew
#### 1.homebrew的安装
	homebrew安装：/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
	homebrew更新：brew update
#### 2.包的安装与卸载
	列出已安装的包：brew list
	包的安装：brew install <package>
	包的卸载：brew uninstall <package>
#### 3.更新包
	查看过期的包：brew outdated
	更新所有的包：brew upgrade
	更新指定的包：brew upgrade <package>
#### 4.清理旧版本
	清理所有包的旧版本：brew cleanup
	清理指定包的旧版本：brew cleanup <package>
	查看可清理的旧版本：brew cleanup -n
#### 5.锁定不想更新的包
	锁定某个包：brew pin <package>
	取消锁定：brew unpin <package>
#### 6.链接的设置
	创建链接：brew link <package>
	取消链接：brew unlink <package>
#### 7.其他命令
	显示某个包的信息：brew info <package>
	显示安装的包的汇总信息：brew info
	查看包依赖：brew deps --installed --tree
	

