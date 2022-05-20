# #問題1

# loop_start = int(input('物語の始まりへ'))
# loop_end = 100

# for n in range(loop_start,loop_end,1):
#     if(n%3 == 0):
#         print(n,'Fizz')
#         if(n % 15 == 0):
#             print(n,'FizzBuzz')
#     elif(n%5 == 0):
#         print(n,'Buzz')
#         if(n % 15 == 0):
#             print(n,'FizzBuzz')

#問題2
# count = 0

# print ('カレーを召し上がれ♪')
# while True:
    
#     judge = input("お代わり？ y/n")
#     if(judge == 'n'):
#         break
#     elif judge == 'y':
#         count += 1
#         continue
   
# print ('君が食べたカレーの皿は',count)        


#問題３

hp = int(input('敵のHPを操作せよ！なんぼ攻撃する？'))
set_Health = 100;
if  hp <= 100:
    while hp <= 0:
        print (f'魔王OKUSEに{hp}のダメージ!')
        set_Health -= hp
        print(f'ボスのHPは{set_Health}')
    
