'''
@Date: 2019-09-02 19:54:06
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-11-09 23:57:08
'''
print("------------------------------")
print("公斤                   磅")
count = 1
while count < 200:
    if count > 99:
        print(count, "               ", format(count * 2.2, "6f"))
    elif count <= 99 and count >= 10:
        print(count, "                ", format(count * 2.2, "6f"))
    else:
        print(count, "                 ", format(count * 2.2, "6f"))
    count = count + 1
