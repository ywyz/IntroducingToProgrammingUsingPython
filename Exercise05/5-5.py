'''
@Date: 2019-09-02 20:14:41
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-09-02 20:32:31
'''
print("------------------------------ ------------------------------")
print("公斤                   磅     公斤                   磅")
count = 1
newcount = 9.09
while count < 200:
    print(count, "               ", format(count * 2.2, ".2f"), "   |  ",
          format(newcount, ".2f"), "               ", format(newcount * 2.2, ".2f"), )
    count = count + 1
    newcount += 3.27
