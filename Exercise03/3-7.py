'''
@Date: 2019-08-19 17:47:51
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-08-19 17:58:37
'''
import time
currenttime = time.time()
code = chr(int(currenttime) % ord("z"))
print("The chapter is ", code.upper())
