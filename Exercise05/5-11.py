'''
@Date: 2019-09-06 18:04:57
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-09-06 18:05:52
'''
number = eval(input("Enter the number of students: \n"))
studentsnumber = number
maxscore = 0
nextmaxscore = 0
while number != 0:
    score = eval(input("Enter the score: \n"))
    maxscore = max(maxscore, score)
    if score < maxscore:
        nextmaxscore = max(nextmaxscore, score)
    number -= 1

print("The number of Students is ", studentsnumber)
print("The max score is ", maxscore)
print("The next max score is ", nextmaxscore)
