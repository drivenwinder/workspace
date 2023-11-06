import re


def isPhoneNumber(input):
    if len(input) != 12:
        return False
    for i in range(0, 3):
        if not input[i].isdecimal():
            return False
    if input[3] != '-':
        return False
    for i in range(4, 7):
        if not input[i].isdecimal():
            return False
    if input[7] != '-':
        return False
    if i in range(8, 12):
        if not input[i].isdecimal():
            return False
    return True


# print('415-555-4242 is a phone number:')
# print(isPhoneNumber('415-555-4242'))
# print('Moshi moshi is a phone number:')
# print(isPhoneNumber('Moshi moshi'))

# message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
# for i in range(len(message)):
#     chunk = message[i:i + 12]
#     if isPhoneNumber(chunk):
#         print('Phone number found: ' + chunk)
# print('Done')

# 利用括号分组 字符|称为“管道”。希望匹配许多表达式中的一个时， 就可以使用它。例如，
# 正则表达式 r'Batman|Tina Fey'将匹配'Batman'或'Tina Fey'
# patternStr = r"(\d{3})-(\d{3}-\d{4})"
# phoneNumRegex = re.compile(patternStr)
# mo = phoneNumRegex.search('My number is 415-555-4242.')
# print('Phone number found: ' + mo.group())
# print('Phone number found: ' + mo.group(1))
# print('Phone number found: ' + mo.group(2))
# (areaCode,mainNumber) = mo.groups()
# print('Phone number found: ' + areaCode)

# 用管道匹配多个分组 希望匹配许多表达式中的一个时， 就可以使用它。例如，
# 正则表达式 r'Batman|Tina fey'将匹配'Batman'或'Tina fey'
# heroRegex =re.compile(r'Batman|Tina fey')
# mo1 = heroRegex.search('Batman and Tina fey.')
# print(mo1.group())
# mo2 = heroRegex.search('Tina fey and Batman.')
# print(mo2.group())
#
# batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
# mo3 = batRegex.search('Batmobile lost a wheel')
# print(mo3.group())

# 用问号实现可选匹配 有时候， 想匹配的模式是可选的。就是说， 不论这段文本在不在， 正则表达式
# 都会认为匹配。字符?表明它前面的分组在这个模式中是可选的
# batRegex = re.compile(r'Bat(wo)?man')
# mo1 = batRegex.search('The Adventures of Batman')
# print(mo1.group())
# mo2 = batRegex.search('The Adventures of Batwoman')
# print(mo2.group())

# ?是在说，“匹配这个问号之前的分组零次或一次
# phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
# mo1 = phoneRegex.search('My number is 415-555-4242')
# print(mo1.group())
# mo2 = phoneRegex.search('My number is 555-4242')
# print(mo2.group())

# 用星号匹配零次或多次
# *（称为星号）意味着“匹配零次或多次”，即星号之前的分组，可以在文本中出现任意次。它可以完全不存在，或一次又一次地重复
# batRegex = re.compile(r'Bat(wo)*man')
# mo1 = batRegex.search('The Adventures of Batman')
# mo2 = batRegex.search('The Adventures of Batwoman')
# mo3 = batRegex.search('The Adventures of Batwowowowoman')
# print(mo1.group())
# print(mo2.group())
# print(mo3.group())

# 用加号匹配一次或多次*意味着“匹配零次或多次”， +（加号） 则意味着“匹配一次或多次”。 星号不要求
# 分组出现在匹配的字符串中， 但加号不同， 加号前面的分组必须“至少出现一次”。

# batRegex = re.compile(r'Bat(wo)+man')
# mo1 = batRegex.search('The Adventures of Batman')
# mo2 = batRegex.search('The Adventures of Batwoman')
# mo3 = batRegex.search('The Adventures of Batwowowowoman')
# print(mo1 == None)
# print(mo2.group())
# print(mo3.group())

# 用花括号匹配特定次数 如果想要一个分组重复特定次数，就在正则表达式中该分组的后面，跟上花括
# 号包围的数字。例如，正则表达式(Ha){3}将匹配字符串'HaHaHa'，但不会匹配'HaHa'，
# 因为后者只重复了(Ha)分组两次。除了一个数字，还可以指定一个范围，即在花括号中写下一个最小值、一个逗号和
# 一个最大值。例如，正则表达式(Ha){3,5}将匹配'HaHaHa'、 'HaHaHaHa'和'HaHaHaHaHa'。
# 也可以不写花括号中的第一个或第二个数字， 不限定最小值或最大值。例如，(Ha){3,}将匹配 3 次或更多次实例， (Ha){,5}将匹配 0 到 5 次实例

# haRegex = re.compile(r'(Ha){3}')
# mo1 = haRegex.search('HaHaHa')
# mo2 = haRegex.search('Ha')
# print(mo2== None)
# print(mo1.group())

# 贪心和非贪心匹配 Python 的正则表达式默认是“贪心” 的， 这表示在有二义的情况下，它们会尽
# 可能匹配最长的字符串。花括号的“非贪心” 版本匹配尽可能最短的字符串，即在
# 结束的花括号后跟着一个问号
# greedyHaRegex = re.compile(r'(Ha){3,5}')
# mo1 = greedyHaRegex.search('HaHaHaHaHa')
# nongreedyHaRegex = re.compile(r'(Ha){3,5}?')
# mo2 = nongreedyHaRegex.search('HaHaHaHaHa')
# print(mo1.group())
# print(mo2.group())

# findall()方法
# 除了 search方法外，Regex对象也有一个 findall()方法。search()将返回一个 Match
# 对象， 包含被查找字符串中的“第一次” 匹配的文本，而 findall()方法将返回一组
# 字符串， 包含被查找字符串中的所有匹配。为了看看 search()返回的 Match 对象只
# 包含第一次出现的匹配文本
# phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# mo = phoneNumRegex.search('Cell: 415-555-9999 Work: 212-555-0000')
# print(mo.group())
# mo1 =phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
# print(mo1)
#
# phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)') # has groups
# mo1 =phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
# print(mo1)

# xmasRegex = re.compile(r'\d+\s\w+')
# mo = xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge')
# print(mo)


# 建立自己的字符分类
# vowelRegex = re.compile(r'[aeiouAEIOU]')
# mo = vowelRegex.findall('RoboCop eats baby food. BABY FOOD.')
# print(mo)
#
# consonantRegex = re.compile(r'[^aeiouAEIOU]')
# mo = consonantRegex.findall('RoboCop eats baby food. BABY FOOD.')
# print(mo)

# beginsWithHello = re.compile(r'^Hello')
# mo =beginsWithHello.search('Hello world!')
# print(mo.group())

# 通配字符 在正则表达式中， .（句点）字符称为“通配符”。它匹配除了换行之外的所有字符 句点字符只匹配一个字符
atRegex = re.compile(r'.at')
mo = atRegex.findall('The cat in the hat sat on the flat mat.')
print(mo)



# ?匹配零次或一次前面的分组。
# *匹配零次或多次前面的分组。
# +匹配一次或多次前面的分组。
# {n}匹配 n 次前面的分组。
# {n,}匹配 n 次或更多前面的分组。
# {,m}匹配零次到 m 次前面的分组。
# {n,m}匹配至少 n 次、至多 m 次前面的分组。
# {n,m}?或*?或+?对前面的分组进行非贪心匹配。
# ^spam 意味着字符串必须以 spam 开始。
# spam$意味着字符串必须以 spam 结束。
# .匹配所有字符，换行符除外。
# \d、 \w 和\s 分别匹配数字、单词和空格。
# \D、 \W 和\S 分别匹配出数字、单词和空格外的所有字符。
# [abc]匹配方括号内的任意字符（诸如 a、 b 或 c）。
# [^abc]匹配不在方括号内的任意字符
