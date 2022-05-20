print('ﾄﾞｼﾀﾝﾊﾅｼｷｺｶ?')
hour = int(input('ｼｭｳｺﾞｳｽﾙﾉ何時？'))
while hour >= 24:
    if hour >= 24:
        hour =int(input('24時間表記でお願いします。小学生からやり直しだねって感じだね'))

minute = int(input('何分？'))        
while minute > 59:
    if minute > 59:
        minute = int(input('５９分までの数字で入力してください。もう一回言おか？'))

if hour > 12:
    print ('集合時刻は{}時{}分AMです'.format(hour - 12,minute))
else:
    print(f'集合時刻は{hour}時{minute}分PMです')
    

    
