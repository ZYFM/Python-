#1、列表生成式 list comprehensions
#列表生成式性能高于列表操作

#0到10循环并对每次循环的值做平方操作
print([x*x for x in range(11)])

#在循环的基础上做条件判断，只输出除3不为0的值
print([x*x for x in range(11) if not x%3==0])

#2、字典生成式

#例如颠倒字典的key和value
mydict = {"name":"age", "bob":"23", "mary":"24", "jim":"25"}
revers_dict = {value:key for key, value in mydict.items()}
print(revers_dict)

#3、集合生成式

myset = {key for key, value in mydict.items()}
print(myset)

#4、生成器表达式

#将列表生成式最外的[]换为()则为生成器
print((x*x for x in range(11)))
for item in ((x*x for x in range(11))):
    print(item)

#也可将生成器改为列表
print(list((x*x for x in range(11))))
