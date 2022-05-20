price = int(input('何円ですか'))
count = int(input('何個ですか'))

sale_count = int(input('なんこから割引しまっか？')

if count >= sale_count:
    sale = int(price * count * 0.9)
    print ('割引した後の金額は、',sale,'です')
    sum_product = price * count
    print ('代金は',sum_product,'です')
else:
    sum_product = price * count
    print ('代金は',sum_product,'です')
    
print ('終了')

