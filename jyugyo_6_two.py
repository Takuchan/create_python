hour = int(input('何時？'))
while hour >= 24:
    if hour >= 24:
        hour =int(input('24時間表記でお願いします'))

minute = int(input('何分？'))        
while minute > 59:
    if minute > 59:
        minute = int(input('５９分までの数字で入力してください'))

if hour > 12:
    print ('現在時刻は{}時{}分です'.format(hour - 12,minute))
else:
    print(f'現在時刻は{hour}時{minute}分です')
    
