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

# hp = int(input('敵のHPを操作せよ！なんぼ攻撃する？'))
# set_Health = 100;
# if  hp <= 100:
#     while hp >= 0:
#         print (f'魔王OKUSEに{hp}のダメージ!')
#         set_Health -= hp
#         print(f'ボスのHPは{set_Health}')
#         hp = int(input('HPなんぼ攻撃する？'))
#         if set_Health - hp <= 0:
#             break
# else:
#     print("お前強すぎ。一発でおくせ死んだで。")    
    
# print('おめでとう！You win!')

# print('{}'.format(1))]

# print('魔王Okuseが現れた')
# hp = 100
# while hp > 0:
#     a = int(input('魔王Okuseに与えたいダメージを入力せよ'))
#     hp = hp - a
#     print('魔王OKuseに'+ str(a) + 'ダメージ与えた')
#     if hp < 0:
#         print('OKUSEは力尽きた。晴れた、晴れたっ！夜に晴れたっWOWOWO少年みたいに（サカナクション風）')
#         break
#     print('現在のOKUSEのHPは',hp)
    
# print('You Win!')

print('魔王Okuseが現れた')
hp = 100
while hp<101:
    a = int(input('魔王Okuseに与えたいダメージを入力せよ'))
    hp -= a
    if a < 100:
        print('魔王Okuseに'+str(hp)+'与えた')
    if a >= 100:
        print('ダメージを与えられない')
    if hp <=0:
        print('魔王Okuseは倒れた')
        quit()