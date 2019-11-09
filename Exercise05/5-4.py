'''
@Date: 2019-09-02 20:03:53
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-11-09 23:58:47
'''
print("------------------------------")
print("英里                   公里")
count = 1
while count < 11:
    if count >= 10:
        print(count, "              ", format(count * 2.2, "4f"))
    else:
        print(count, "               ", format(count * 2.2, "4f"))
    count = count + 1
