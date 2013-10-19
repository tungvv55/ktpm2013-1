'''
Created on Oct 12, 2013

@author: HoaHoang
'''
from input import main
import re
import unittest
import collections
import itertools

# lay gia tri trong docstring
def getValue():
    a = main.__doc__
    b = a.split('\n')
    b.pop(0)
    
    array = []
    for i in range(0,len(b)):
        number = re.findall(r'\d+', '%s' %(b[i]))
        number = map(int,number)
        array.append(number)
        
    array.pop(len(array) -1 )
    return array

def sort_input(arr):
    for i in range(len(arr)):
        for j in range(0,len(arr[i]),2):
            if(arr[i][j] >= arr[i][j+1]):
                raise Exception, "Wrong input"
                break
        
def check_input(arr):
    a = []
    sort_input(arr)
    for i in range(len(arr)):
        a.append(len(arr[i]))
        if (a[i]%2!=0) or (a[i] == 0) or (a[i]>6) or (len(arr)>10) or (len(arr) <1):
            raise Exception, "Wrong input"
            break
        
    return True

def check_equivalence(arr):
    if check_input(arr):
        d = []
        for a in range(0,len(arr)):
            q = []
            for b in range(0,len(arr[a]),2):
                q.extend(range(arr[a][b],arr[a][b+1]+1))
            d.append(q)
            t=collections.Counter(d[a])
            if len(([i for i in t if t[i]>1])) > 0:
                raise Exception, "Wrong input"
                break
        return True
        
def get_input_test (arr):
    if check_equivalence(arr):
        l = []
        for i in range(0,len(arr)):
            p = []
            for j in range(0,len(arr[i]),2):
                p.append(arr[i][j+1])
            l.append(p)
        return l
        
class MainTest (unittest.TestCase):
    pass
def test_generator(a):
    def wrapper (func,args):
        func(*args)
    params = len(a)
    def test(self):
        try:
            if params == 0:
                result = main(*a)
                self.assertEqual(result,result)
            elif params > 0:
                test = []
                for i in range(0,params):
                    test.append(a[i])
                result = wrapper(main,a)
                self.assertEquals(result,result)
        except:
            self.fail("Raised an exception")
    return test

if __name__ == '__main__':
    array = []
    array.extend(getValue())
    input_ = get_input_test(array)
    output = list (itertools.product(*input_))
    i = 0
    for arr in output:
        test_name = 'test_%d' % i
        i = i + 1
        test = test_generator(arr)
        setattr(MainTest, test_name, test)
    
    unittest.main()

