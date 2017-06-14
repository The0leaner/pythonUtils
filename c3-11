# -*- encoding=UTF-8 -*-
import re
import requests
import random

from operator import sub, add

from bs4 import BeautifulSoup


def qiushibaike():
    content = requests.get('https://www.qiushibaike.com/').content
    soup = BeautifulSoup(content, 'html.parser')

def demo_controlflow():
    score = 65
    if score > 99:
        print 1 ,'A'
    elif score > 60:
        print 2 , 'B  '
    else:
        print 3, 'C'
    while score < 80:
        print score
        score += 10
        if score > 80:
            break
#for (int i = 0 i < 10 i++)
for i in range(0, 10):
    if i == 0:
        pass
    if i == 3:
        continue
    if i < 5:
        print i * i
    if i == 7:
        break
    # print i
def demo_list():
    lista = [1, 2, 3] #vector<int> ArrayList<Integer>
    print 1, lista
    print dir(list)
    listb = ['a', 1, 1.1]
    print 2, listb
    lista.extend(listb)
    print 3, lista
    print 4, len(lista)
    print 5, 'a' in lista, 'b' in lista
    lista = lista + listb
    print lista
    listb.insert(0, 'wwwwwww')
    print listb
    listb.pop(1)
    print listb
    listb.sort()
    print listb
    print listb[1], listb[2]
    print listb * 2
    print [0] * 10 #memset
    listb.append('xxx')
    print listb
    listb.reverse()
    print listb
    t = (1, 2, 3)#pair(int, xxx)
    print t
    print t.count(1), len(t)

def demo_dict():
    dicta = {4: 16, 1: 1, 2: 4, 3: 9, 'a':'b'}
    print 1, dicta
    print 2, dicta.keys(), dicta.values()
    for key, value in dicta.items():
        print 3, key, value
    for key in dicta.keys():
        print 4, key
    print 5, dicta.has_key(1), dicta.has_key(11)

    dictb = {'+': add ,'-':sub}
    print 6, dictb['+'](1, 2)
    print 6, dictb.get['-'](6, 2)
    del dictb['+']
    print 9, dictb

def demo_set():
    lista = (1, 2, 3)
    seta = set(lista)
    print 1, seta
    setb = set((2, 3, 4))
    print 2, seta.intersection(setb)#交集
    print 3, seta & setb
    print seta | setb, seta.union(setb)
    print 5, seta -setb, setb - seta
    seta.add('xxx')
    print 6, seta
    print 7, len(seta)
    print seta.isdisjoint(set(('a', 'b')))
    print 1 in seta

class User:#封装
    type = 'USER'
    def __init__(self, name, uid):
        self.name = name
        self.uid = uid
    def __repr__(   self):
        return 'im' + self.name + ' ' + str(self.uid)
        #toString()
class Admin(User):
    type = 'ADMIN'
    def __init__(self, name, uid, group):
        User.__init__(self, name, uid)#继承
        self.group = group #继承
    def __repr__(self):#多态，重写方法，调用不同
        return 'im admin' + self.name + ' ' + str(self.uid) + self.group

def create_user(type):
    if type == 'USER':
        return User('u1', 1)
    elif type == 'ADMIN':
        return Admin('admin', 2 , 'root')


def demo_exception():
    try:
        print 2/0
        #print 2/1
        raise Exception('Raise Error', 'XXXX')
    except Exception as e:
        print 'error', e
    finally:
        print 'clean up'

def demo_object():
    user1 = User
    print user1
    admin1 = Admin('admin', 3, 'root')
    print admin1

def demo_random():
    random.seed(1)
    # x = prex * 100007 * xxxx
    # prex = x
    for i in range(0, 5):
        print random.randint(0, 100)
    print 2, int(random.random() * 100)
    print 3, random.choice(range(0, 100, 5))
    print 4, random.sample(range(0, 100, 5), 5)

    lista = [1, 2, 3, 4, 5]
    random.shuffle(lista)
    print lista

# choice 取一个
# sample取多个

def demo_regex():#正则表达式
    str = 'abc123def12gh15'
    pl = re.compile('[\d]+')
    p2 = re.compile('\d')
    print 1, pl.findall(str)
    print 2, p2.findall(str)

    str = 'a@163.com, bcc@google.com'
    p3 = re.compile('[\w]+@[163|qq]+\.com')
    print 3, p3.findall(str)

    str = '<html><h>title</h><body>content</body></html>'
    p4 = re.compile('<h>[^<]+</h>')
    print 4, p4.findall(str)
    p4 = re.compile('<h>[^<]+</h><body>[^<]+</body>')
    print 5, p4.findall(str)

    str = 'xx2016-08-22zzz'
    p5 = re.compile('\d{4}-\d{2}-\d{2}')
    print 5, p4.findall(str)

    #\d 取数字 \s数字 \w单词
    #\D 非数字，大写取非
     # |两个里面取一个
    # ^表示以这个开头
     # \\转义

#mian function
if __name__ == '__main__':
    # demo_set()
    demo_exception()


