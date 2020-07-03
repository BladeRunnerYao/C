# This Python file uses the following encoding: utf-8
# 第一行是为了保证汉字被识别，reference https://www.python.org/dev/peps/pep-0263/ 
# https://docs.python.org/2.4/lib/standard-encodings.html 


# Square brackets - Option-5 and Option-6; Curly braces - Option-8 and Option-9
# vs code shortcuts: https://code.visualstudio.com/shortcuts/keyboard-shortcuts-macos.pdf
# open terminal cmd+space search ternimal 
''' 简单的说类是对象的模版。首先我们可以来理解一下对象的概念，面向对象编程的程序实际就是多个对象的集合，我们可以把所有的事物都抽象成对象，在程序设计中可以看作：对象=属性+方法。
属性就是对象的数据，而方法就是对象的行为。下面来说类，就像我开头所说类是对象的模版，而对象是类的实例化。
举个例子，饼干模子可以看作是类，而具体的饼干就是对象。再比如有一个类是表示人，然后可以通过人这个模版来实例化出张三、李四。。。

作者：蓬蒿人
链接：https://www.zhihu.com/question/21006207/answer/19162819
来源：知乎
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。'''

# 面向过程
'''std1 = { 'name': 'Michael', 'score': 98 }
std2 = { 'name': 'Bob', 'score': 81 }
std3 = { 'name': 'Tiyao', 'score': 100,}

def print_score(std):
    print ('%s: %s' % (std['name'], std['score']))

print_score(std3)'''

# 面向对象
class student(object):
    def __init__(self, name, score, age, color):
        self.name = name
        self.score = score
        self.age = age
        self.color = color
    
    def Print_Score(self):
        print('%s: %s' % (self.name, self.score))

Stefan = student('Stefan Müller', 95, 23, 'white')
Bob = student('Bob Dylan', 33, 21, 'black')
Xiaoming = student ('Xiaoming Liu', 100, 18, 'yellow')

Student_List = [Stefan, Bob, Xiaoming]
for std in Student_List:
    std.Print_Score()
