import math
import random


a  = 9
count = 0
print(math.pi)

janken = ['goo','choki','pa']


#choiceで配列の中身を取れる。
for a in range(10000):
    print (random.choice(janken))
    print (f'{count}')
    count += 1
    

   

