capitals = {'日本':'東京','フランス':'パリ','アメリカ':'カリフォルニア','日本':'大阪'}
empty = {}
print ('{}'.format(capitals))
capitals['中国'] = '北京'
capitals['日本'] = '東京特許許可局'
print (capitals['フランス'],capitals['アメリカ'],capitals['中国'])
print(f'({capitals}です')
del capitals['日本']
print (capitals)