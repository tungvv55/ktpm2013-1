'''
Created on Sep 17, 2013

@author: HoaHoang
'''

#------------------------------
# function 
#----------------------------------
#ham chuyen doi kieu du lieu dau vao
    
def toNumber(val):
    if isinstance(val, str):
        try:
            return int(val)
        except ValueError:
            try:
                return float(val)
            except ValueError:
                return False
    else:
        return val

#---------------------------------
# define function classifyTriangle: check 3 edge of triangle 
def detect_triangle(a , b , c ):
    
    a = toNumber(a)
    b = toNumber(b)
    c = toNumber(c)
    
    #gan gia tri epsilone
    EPSILONE = 1e-10      
    if (a is None) or (b is None) or (c is None):
            return 'inputNull'
    
    else:
    
        if ((a == False) or (b == False) or (c == False)):
            return 'Error input is string'
        else:
            # du lieu dau vao la chuoi
            if  (a <= 0 or b <= 0 or c <= 0 or a > (pow(2,32) - 1) or b > (pow(2,32) - 1) or c > (pow(2,32) - 1)):
                return 'notMienxacdinh'
            
            
            # du lieu dau vao la float hoac da duoc chuyen kieu
            else: 
                # Do dai 3 canh nhap vao thoa man tam giac 
                if ((a+b > c) and (a+c > b) and (b+c >a)):
                    if ((abs(a - b) < EPSILONE) or (abs(b - c) < EPSILONE) or (abs(c - a) < EPSILONE)):
                        if (abs(a * a + b * b - c * c) < EPSILONE) or (abs(b * b + c * c - a * a) < EPSILONE) or (abs(a * a + c * c - b * b) < EPSILONE):
                            return 'rightAngledIsosceles'
                        else:
                            if (a == b and b == c):
                                return 'equilateral'
                            else:
                                return 'isosceles'
                    else:
                        if ((pow(a, 2)+pow(b, 2) == pow(c, 2)) or (pow(b, 2)+pow(c, 2) == pow(a, 2)) or (pow(a, 2)+pow(c, 2) == pow(b, 2))):
                            return 'rightAngled'
                        else:
                            return 'scalene'
                else:
                    return 'notValid'
             
