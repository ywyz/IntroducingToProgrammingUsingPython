'''
@Date: 2019-09-02 19:54:06
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-09-02 20:02:47
'''
print("------------------------------")
print("公斤                   磅")
count = 1
while count < 200:
    print(count, "               ", format(count * 2.2, "6f"))
    count = count + 1
