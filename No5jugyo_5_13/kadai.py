height = int(input('身長[cm]: '))
print ('身長は',height,'cm')
weight = int(input('体重[kg]: '))
print('体重は',weight,'kg')
print(height/100)

bmi = float((weight / (height/100) ** 2))
print ('BMIは',bmi)
x