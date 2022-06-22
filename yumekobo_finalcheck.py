from operator import ge
from webbrowser import Mozilla


class PersonData:
    def __init__(self,getddata):
        self.getddata = getddata

    def getData(self):
        with open('student_data.txt') as f:
            result = []
            result.append(self.getddata[0])
            n = f.readlines()[int(self.getddata[0]) - 1] #ファイルの行番号を指定する
            l = n.split() #行の部分のデータをリストに変換
            del self.getddata[0]
            serch = 6
            

            for a in range(len(self.getddata)):
                if(self.getddata[a] == 'name'):
                    serch = 1
                elif self.getddata[a] == 'old':
                    serch = 2
                elif self.getddata[a] == 'gender':
                    serch = 3
                elif self.getddata[a] == 'height':
                    serch = 4
                elif self.getddata[a] == 'weight':
                    serch = 5
                
                
                result.append(l[serch])
            
            


            return result #サーチで検索したデータを取得

element = ['name','old','gender','height','weight']
match_list = []
load = input('番号　欲しい情報(name,old,gender,height,weight)を空白を開けて入力してください:')
loader = load.split()

ichizihozon = loader[0]
del loader[0]

for elem in loader:
    if elem in  element:
        match_list.append(elem)

match_list = [ichizihozon] + match_list
result = PersonData(match_list)




mojiretsu = ' '.join(result.getData())
print(mojiretsu)
# result = PersonData()



# if(want != 1 or want != 2 or want != 3 or want != 4 or want != 5):
#     n0 = PersonData(studentnumber,want)
#     print(n0.getData())
# else:
#     print('金沢工業大学って感じだね')


