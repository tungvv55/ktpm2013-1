'''
Created on Sep 17, 2013

@author: HoaHoang
'''
import unittest
import math
import decimal

#---------------------
# UnitTest
# This pulls our function in form the other file:
from triangle import detect_triangle 

class classifyTriangleTest (unittest.TestCase):
    
    #--------------------------------------
    # mien gia tri giua
    #--------------------------------------
    # test tam giac can tai A
    def testIsoscelesA(self):
        result = detect_triangle(5, 5, 1)
        self.assertEqual(result, 'isosceles')
    
    # test tam giac can tai B
    def testIsoscelesB(self):
        result = detect_triangle(5, 1, 5)
        self.assertEqual(result, 'isosceles')
    
    # test tam giac can tai C
    def testIsoscelesC(self):
        result = detect_triangle(1, 5, 5)
        self.assertEqual(result, 'isosceles')
    
    #--------------
    # test tam giac deu
    def testEquilateral(self):
        result = detect_triangle(5, 5, 5)
        self.assertEqual(result, 'equilateral')
        
    #-----------------
    # test tam giac vuong tai A
    def testRightAngledA(self):
        result = detect_triangle(3, 4, 5)
        self.assertEquals(result, 'rightAngled')
        
    # test tam giac vuong tai B
    def testRightAngledB(self):
        result = detect_triangle(4, 5, 3)
        self.assertEquals(result, 'rightAngled')
        
    # test tam giac vuong tai C
    def testRightAngledC(self):
        result = detect_triangle(5, 3, 4)
        self.assertEquals(result, 'rightAngled')
    
    #-------------
    # test tam giac vuong can tai A
    def testRightAngledIsoscelesA(self):
        result = detect_triangle(3, math.sqrt(18), 3)
        self.assertEqual(result, 'rightAngledIsosceles')
    
    # test tam giac vuong can tai B
    def testRightAngledIsoscelesB(self):
        result = detect_triangle(3, 3, math.sqrt(18))
        self.assertEqual(result, 'rightAngledIsosceles')
        
    # test tam giac vuong can tai C
    def testRightAngledIsoscelesC(self):
        result = detect_triangle( math.sqrt(18), 3, 3)
        self.assertEqual(result, 'rightAngledIsosceles')
        
    #-------------
    # test tam giac thuong
    def testScalene(self):
        result = detect_triangle(3, 2, 4)
        self.assertEqual(result, 'scalene')
    
    #----------------------
    # test khong phai la 3 canh cua 1 tam giac
    def testNotValid(self):
        result = detect_triangle(3, 2, 1)
        self.assertEqual(result, 'notValid')
        
    #------------
    #test tham so thu 1 truyen vao la chuoi  
    def testString1(self):
        result = detect_triangle("a", 2, 2)
        self.assertEqual(result, 'Error input is string')
        
    #test tham so thu 2 truyen vao la chuoi  
    def testString2(self):
        result = detect_triangle(2, "a", 2)
        self.assertEqual(result, 'Error input is string')
    
    #test tham so thu 3 truyen vao la chuoi  
    def testString3(self):
        result = detect_triangle(2, 2, "a")
        self.assertEqual(result, 'Error input is string')
          
    #-------------
    # Mien gia tri bien tren
    def testIsoscelesAMax(self):
        result = detect_triangle(pow(2,32) - 1, pow(2,32) - 1, 1)
        self.assertEqual(result, 'isosceles')
        
    def testIsoscelesBMax(self):
        result = detect_triangle(pow(2,32) - 1, 1, pow(2,32) - 1)
        self.assertEqual(result, 'isosceles')
        
    def testIsoscelesCMax(self):
        result = detect_triangle(1, pow(2,32) - 1, pow(2,32) - 1)
        self.assertEqual(result, 'isosceles')
    
    # test tam giac vuong can tai A
    def testRightAngledIsoscelesAMax(self):
        result = detect_triangle(pow(2,32) - 1, pow(2,32) - 1, float(decimal.Decimal('4.0')))
        self.assertEqual(result, 'rightAngledIsosceles')  
        
    # test tam giac vuong can tai B
    def testRightAngledIsoscelesBMax(self):
        result = detect_triangle(pow(2,32) - 1, float(decimal.Decimal('4.0')), pow(2,32) - 1 )
        self.assertEqual(result, 'rightAngledIsosceles')  
        
    # test tam giac vuong can tai C
    def testRightAngledIsoscelesCMax(self):
        result = detect_triangle(float(decimal.Decimal('4.0')), pow(2,32) - 1,  pow(2,32) - 1 )
        self.assertEqual(result, 'rightAngledIsosceles')
    
    # test mien gia tri
    def testMienGiaTri1(self):
        result = detect_triangle(-1, 5, 5 )
        self.assertEqual(result, 'notMienxacdinh')
   
    def testMienGiaTri2(self):
        result = detect_triangle(1, -5, 5 )
        self.assertEqual(result, 'notMienxacdinh')
    
    def testMienGiaTri3(self):
        result = detect_triangle(1, 5, -5 )
        self.assertEqual(result, 'notMienxacdinh')
        
    def testMienGiaTri4(self):
        result = detect_triangle(pow(2,32) + 1, 5, 5 )
        self.assertEqual(result, 'notMienxacdinh')
    
    def testMienGiaTri5(self):
        result = detect_triangle(5, pow(2,32) + 1, 5 )
        self.assertEqual(result, 'notMienxacdinh')
        
    def testMienGiaTri6(self):
        result = detect_triangle(5,5,pow(2,32) + 1)
        self.assertEqual(result, 'notMienxacdinh')
    
    #--------------------
    # test tham so truyen vao Null
    # khong co tham so truyen vao
    def testNullNoValue(self):
        result = detect_triangle()
        self.assertEqual(result, 'inputNull')
    
    # co 1 tham so truyen vao
    def testNullOneValue(self):
        result = detect_triangle(1)
        self.assertEqual(result, 'inputNull')
        
    # co 2 tham so truyen vao
    def testNullTwoValue(self):
        result = detect_triangle(2,2)
        self.assertEqual(result, 'inputNull')
        
        
    #test chuyen doi kieu du lieu string -> float
    def testStringToNumber1(self):
        result = detect_triangle('3', 3, 3)
        self.assertEqual(result, 'equilateral')
        
    def testStringToNumber2(self):
        result = detect_triangle(3, '3', 3)
        self.assertEqual(result, 'equilateral')
        
    def testStringToNumber3(self):
        result = detect_triangle(3, 3, '3')
        self.assertEqual(result, 'equilateral')
        
    def testStringToNumber4(self):
        result = detect_triangle('3', '3', '3')
        self.assertEqual(result, 'equilateral')
        
    
#--------------------------------------
# main
if __name__ == '__main__':
    unittest.main()