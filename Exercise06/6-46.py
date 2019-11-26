'''
@Date: 2019-11-26 20:31:42
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-11-26 20:39:46
'''
from UsefulTurtleFunctions import drawLine
import turtle

drawLine(40, -69.28, -40, -69.28)
drawLine(-40, -69.28, -80, -9.8)
drawLine(-80, -9.8, -40, 69)
drawLine(-40, 69, 40, 69)
drawLine(40, 69, 80, 0)
drawLine(80, 0, 40, -69.28)
drawLine(40, -69.28, -80, -9.8)
drawLine(40, -69.28, -40, -69)
drawLine(40, -69.28, 40, 69)
drawLine(-40, -69.28, -40, 69)
drawLine(-40, -69.28, 40, 69)
drawLine(-40, -69.28, 80, 0)
drawLine(-80, -9.8, -40, 69)
drawLine(-80, -9.8, 40, 69)
drawLine(-80, -9.8, 80, 0)
drawLine(-40, 69, 80, 0)
turtle.done()
