from functools import reduce
import re

# 利用切片操作，实现一个trim()函数，去除字符串首尾的空格，注意不要调用str的strip()方法
def trim(s):
    if len(s) == 0:
        return s
    elif s[:1] == " ":
        return trim(s[1:])
    elif s[-1:] == " ":
        return trim(s[:-1])
    return s

def test_trim():
    if trim('hello  ') != 'hello':
        print('测试失败! 1')
    elif trim('  hello') != 'hello':
        print('测试失败! 2')
    elif trim('  hello  ') != 'hello':
        print('测试失败! 3')
    elif trim('  hello  world  ') != 'hello  world':
        print('测试失败! 4')
    elif trim('') != '':
        print('测试失败! 5')
    elif trim('    ') != '':
        print('测试失败! 6')
    else:
        print('测试成功!')

# 请使用迭代查找一个list中最小和最大值，并返回一个tuple：
def findMinAndMax(L):
    max = None
    min = None
    if len(L) == 1:
        return (L[0], L[0])
    if len(L) == 0:
        return (None, None)
    for idx, val in enumerate(L):
        if idx == 0:
            if L[idx] > L[idx + 1]:
                max = L[idx]
                min = L[idx + 1]
            else:
                max = L[idx + 1]
                min = L[idx]
        else:
            if val > max:
                max = val
            elif val < min:
                min = val
    return (min, max)

def test_findMinAndMax():
    if findMinAndMax([]) != (None, None):
        print('测试失败!')
    elif findMinAndMax([7]) != (7, 7):
        print('测试失败!')
    elif findMinAndMax([7, 1]) != (1, 7):
        print('测试失败!')
    elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
        print('测试失败!')
    else:
        print('测试成功!')

def generate_list():
    L1 = ['Hello', 'World', 18, 'Apple', None]
    L2 = [x.lower() for x in L1 if isinstance(x, str)]
    return L2

def test_generate_list():
    if generate_list() == ['hello', 'world', 'apple']:
        print('测试通过!')
    else:
        print('测试失败!')

def triangles():
    L = [1]
    while True:
        yield L[:len(L)]
        L.append(0)
        L = [L[x - 1] + L[x] for x in range(len(L))]

def test_triangles():
    n = 0
    results = []
    for t in triangles():
        results.append(t)
        n = n + 1
        if n == 10:
            break

    for t in results:
        print(t)

    if results == [
        [1],
        [1, 1],
        [1, 2, 1],
        [1, 3, 3, 1],
        [1, 4, 6, 4, 1],
        [1, 5, 10, 10, 5, 1],
        [1, 6, 15, 20, 15, 6, 1],
        [1, 7, 21, 35, 35, 21, 7, 1],
        [1, 8, 28, 56, 70, 56, 28, 8, 1],
        [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
    ]:
        print('测试通过!')
    else:
        print('测试失败!')

# 请编写一个prod()函数，可以接受一个list并利用reduce()求积 
def prod(L):
    return reduce(lambda x, y: x * y, L)

def test_prod():
    print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
    if prod([3, 5, 7, 9]) == 945:
        print('测试成功!')
    else:
        print('测试失败!')

# 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456
def str2float(s):
    dict = {"1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, ".": "."}
    L = s.split(".")
    part_1 = reduce(lambda x, y: x * 10 + y , list(map(lambda x: dict[x], L[0])))
    part_2 = reduce(lambda x, y: x * 10 + y, list(map(lambda x: dict[x], L[1])))
    return part_1 + part_2/(10 ** len(L[1]))

def test_str2float():
    print('str2float(\'123.456\') =', str2float('123.456'))
    if abs(str2float('123.456') - 123.456) < 0.00001:
        print('测试成功!')
    else:
        print('测试失败!')

# 回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()筛选出回数
def is_palindrome(n):
    l = list(map(lambda x: x, str(n)))
    copy_l = l.copy()
    l.reverse()
    return l  == copy_l
    # 法2
    # 字符串反转 eg: s = '12321' => s[::-1]

def test_is_palindrome():
    output = filter(is_palindrome, range(1, 1000))
    print('1~1000:', list(output))
    if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
        print('测试成功!')
    else:
        print('测试失败!')

'''
假设我们用一组tuple表示学生名字和成绩：
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
请用sorted()对上述列表分别按名字排序：
'''
def by_name(t):
    return t[0].lower()

def by_grade(t):
    return t[1]

def test_by_name_and_grade():
    L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
    L2 = sorted(L, key = by_name)
    print(L2)
    if L2 == [('Adam', 92), ('Bart', 66), ('Bob', 75), ('Lisa', 88)]:
        print("测试通过")
    else:
        print("测试失败")
    L3 = sorted(L, key = by_grade)
    print(L3)
    if L3 == [('Bart', 66), ('Bob', 75), ('Lisa', 88), ('Adam', 92)]:
        print("测试通过")
    else:
        print("测试失败")


# 利用闭包返回一个计数器函数，每次调用它返回递增整数
def createCounter():
    s = [0] 
    def counter():
        s[0] = s[0]+1
        return s[0]
    return counter

# 请设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间
def metric(fn):
    print('%s executed in %s ms' % (fn.__name__, 10.24))
    return fn

if __name__ == "__main__":
    # def now():
    #     print("2021")

    # def log(func):
    #     def wrapper(*args, **kw):
    #         print('call %s():' % func.__name__)
    #         return func(*args, **kw)
    #     return wrapper

    import time, functools
    def log(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            t1=time.time()
            r=func(*args, **kw)
            print('%s excute in %s ms' %(func.__name__, 1000*(time.time()-t1)))
            return r
        return wrapper


    @log
    def fast(x, y):
        time.sleep(3)
        return x*y

    fast(3, 5)