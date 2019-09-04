'''
@Date: 2019-09-04 20:02:43
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-09-04 20:02:54
'''
print("------------------------------ ------------------------------")
print("英里                   公里     英里                   公里")
count = 1
newcount = 12.430
while count < 10:
    print(
        count,
        "               ",
        format(count * 1.609, ".3f"),
        "   |  ",
        format(newcount, ".2f"),
        "               ",
        format(newcount * 1.609, ".2f"),
    )
    count = count + 1
    newcount += 3.108
