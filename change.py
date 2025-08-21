

insert_price = input('投入金額 >> ')
product_price = input('購入金額 >> ')

# 単純なお釣りの計算：お釣り = 投入金額 - 購入金額
change = int(insert_price) - int(product_price)
total_change = change

# できるだけ少ない枚数でお釣りを返す
cahnge_100 = change//100        # 百円玉の枚数
change = change%100
cahnge_10 = change//10           # 十円玉の枚数
change = change%10
cahnge_1 = change//1              # 一円玉の枚数

print('お釣り {}円\n'.format(total_change))
print('\n100円玉：{}枚\n10円玉：{}枚\n1円玉：{}枚\n'
      .format(cahnge_100, cahnge_10, cahnge_1))

