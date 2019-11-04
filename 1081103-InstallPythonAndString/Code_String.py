# 變數命名名稱
first_name = 'Rory'

print(first_name)
print()

first_name = 'Rory'
last_name = 'Wang'

# 字串的串連符號是 ＋ 
print(first_name + last_name)
print('Hello ' + first_name + ' ' + last_name)
print()

sentence = 'The dog is named Rory'

print(sentence.upper())
print(sentence.lower())
print(sentence.capitalize()) #字首大寫
print(sentence.count('o')) # 計算多少的 o

# input 

first_name = input('你的姓：')
last_name = input('你的名：')

print(first_name)
print(last_name)

# \ 是呈現的斷行
print('你好，' + first_name + last_name + ' ' \
    + '歡迎進來。')

# 初學者
output = "Hello," + first_name + last_name
print(output)
print()

# 超級懶惰
output = "Hello, {} {} ".format(first_name , last_name)
print(output)
print()
# 參數
output = "Hello, {1} {0} ".format(first_name , last_name)
print(output)
print()

# 偷懶 python 3.5 上
output = f'Hello, {first_name} {last_name}'
print(output)
print()

# 推薦吹毛求疵
output = '{name} is {age} years old !!'.format( name ='王永盛', age = 31)
print(output)
print()

#進階版
output = '%d %.2f %s' % (1,99.3,'Justin')
print(output)
print()
# https://openhome.cc/Gossip/Python/StringFormat.html
