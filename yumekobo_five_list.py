# xs = [1,2,3]
# ys = [3,4,5]
# #末尾に数字を配置
# xs.append(4)
# xs[0] = 5

# xs.extend(ys)
# xs += [9,3]
# print (xs)

# print ('出現回数は',xs.count(4),xs.index(2))
# xs.sort()
# print('整列!',xs)

    


# # print (xs)
# xs = [3,1,5,2,1]
# print(len(xs))
# print (sum(xs))


# print (3 in xs)
# print _

# f = ["ren","red","fd","fdfd","rd","art","sad"]
# for i,x in enumerate(f,1):
#     print('{}の{}'.format(i,x))
    
    
# names = ['Alice','Chart','Bob']
# ages = [24,50,18]
# for name,age in zip(names,ages):
#     print(name,age)
    

# days = ['Sun','Mon','Tue','Wed','Thu','Fri','Sat']
# del days[0]
# days.append('Sun')

# print (days)
# print (sorted(days))

 
n = [1,2,3,4,5]

for i,x in enumerate(n):
    if(i % 2 != 0):
        print ('{}の{}'.format(i,x))