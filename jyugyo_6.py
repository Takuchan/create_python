price = int(input('何円ですか'))
count = int(input('何個ですか'))

if count >= 2:
    sale = price * count * 0.9
    print ('割引した後の金額は、',sale,'です')
    sum_product = price * count
    print (f'代金は{sum_product}です')