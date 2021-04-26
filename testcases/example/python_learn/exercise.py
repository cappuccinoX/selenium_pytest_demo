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
    yield L

    L = [1, 1]
    yield L

    while True:
        yield 
    L = [1, 2, 1]
    yield L
    yield [1, 3, 3, 1]

def test_triangles():
    pass
    
if __name__ == "__main__":
    t = triangles()
