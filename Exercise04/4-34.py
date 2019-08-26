'''
@Date: 2019-08-26 20:17:08
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-08-26 20:26:10
'''
character = input("Enter a hex character: ")
if character >= 'A' and character <= 'F':
    print("The decimal value is ", ord(character) - ord('A') + 1 + 9)
elif character >= '0' and character <= '9':
    print("The decimal value is ", character)
elif character >= 'a' and character <= 'f':
    print("The decimal value is ", ord(character) - ord('a') + 1 + 9)
else:
    print("Invaild input")
