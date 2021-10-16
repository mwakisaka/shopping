# 衣類ECサイトで服を購入するアプリケーション

items = [
    {'name':'Tシャツ', 'price': 1200, 'color':'ブラック', 'size': 'S'},
    {'name':'Tシャツ', 'price': 1200, 'color':'ブラック', 'size': 'M'},
    {'name':'Tシャツ', 'price': 1200, 'color':'ブラック', 'size': 'L'},
    {'name': 'Tシャツ', 'price':1200, 'color':'ホワイト', 'size': 'S'},
    {'name': 'Tシャツ', 'price':1200, 'color':'ホワイト', 'size': 'M'},
    {'name': 'Tシャツ', 'price':1200, 'color':'ホワイト', 'size': 'L'},
    {'name': 'パーカー', 'price':2500, 'color':'レッド', 'size': 'S'},
    {'name': 'パーカー', 'price':2500, 'color':'レッド', 'size': 'M'},
    {'name': 'パーカー', 'price':2500, 'color':'レッド', 'size': 'L'},
    {'name': 'パーカー', 'price':2500, 'color':'ブルー', 'size': 'S'},
    {'name': 'パーカー', 'price':2500, 'color':'ブルー', 'size': 'M'},
    {'name': 'パーカー', 'price':2500, 'color':'ブルー', 'size': 'L'}
]

guest = input('お名前をご入力ください。：')
print('いらっしゃいませ、' + guest + '様。')

print('当店の商品ラインナップはこちらです。')
index = 0
for item in items:
    print(str(index) + ':' + item['name'] + '/' + str(item['price']) + '円/' + item['color'] + '/' + item['size'])
    index += 1

interest = int(input('ご興味のある商品はございましたか？（0：ある、1：ない）：'))
if interest == 0:
    number_of_interest = int(input('いくつの商品を購入されますか？:'))
    total_price = 0
    for _ in range(number_of_interest):
        item_selection = int(input('商品ラインナップの中から購入される商品番号をご入力ください。：'))
        print('ご選択いただいた商品は' + '【' + items[item_selection]['name'] + '/' + str(items[item_selection]['price']) + '円/' + items[item_selection]['color'] + '/' + items[item_selection]['size'] + '】' + 'です。')
        total_price += items[item_selection]['price']
    print('合計金額は' + str(total_price) + '円です。ご利用ありがとうございました。')
else:
    print('またのご利用をお待ちしております。')