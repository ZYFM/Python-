# os模块提供访问操作系统的功能
import os

# 获取系统类型，windows系统的返回是nt，linux系统的返回是posix
print(os.name)

# 执行系统命令
os.system('date')

# 获取执行命令后的结果
content = os.popen('ls -l').read()
print(content)

# 获得当前工作路径
print(os.getcwd())
pwd = os.getcwd()

# 切换到目的路径
os.chdir('/usr/local/')
print(os.getcwd())
os.chdir(pwd)
os.getcwd()

# 创建目录
os.system('rm -r test')
os.mkdir('test')

# 判断目录是否存在
print(os.path.exists('test'))

# 拼接多级目录
p = os.path.join(os.getcwd(), 'x', 'y', 'z')
b = os.path.join('/', 'a', 'b', 'c')
print(p)
print(b)

#把最后一个目录或文件和上级目录分开，返回tuple
print(os.path.split(os.getcwd()))

#把文件的后缀和前面分开
print(os.path.splitext('haha.py'))
