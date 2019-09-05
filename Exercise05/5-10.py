'''
@Date: 2019-09-05 19:17:02
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-09-05 20:10:40
'''
number = eval(input("Enter the number of students: \n"))
studentsnumber = number
maxscore = 0
while number != 0:
    score = eval(input("Enter the score: \n"))
    maxscore = max(maxscore, score)
    number -= 1

print("The number of Students is ", studentsnumber)
print("The max score is ", maxscore)
