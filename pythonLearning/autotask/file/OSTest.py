import os

# mo = os.path.join("usr","bin","span")
# print(mo)
#
# myfiles=['accounts.txt', 'details.csv', 'invite.docx']
# for name in myfiles:
#     print(os.path.join("c:\\users\\wyb",name))
#
# curdir = os.getcwd()
# print(curdir)

# totalSize = 0
# for name in os.listdir("c:\\windows\\system32"):
#     filename = os.path.join("c:\\windows\\system32", name)
#     if os.path.isfile(filename):
#         size = os.path.getsize(os.path.join("c:\\windows\\system32", name))
#         print(name + ": size =" + str(size))
#         totalSize += os.path.getsize(os.path.join("c:\\windows\\system32", name))
#     else:
#         print(filename + " is folder")
#
# print(totalSize)
# temp=os.path.join(os.getcwd(), '../')
# print(temp)
# grandparent_directory = os.path.abspath(os.path.join(os.getcwd(), '../'))
# print(grandparent_directory)
# file_path = os.path.join(grandparent_directory, 'reg', 'phoneAndEmail.py')
# print(file_path)
# # 检查文件是否存在
# if os.path.exists(file_path):
#     # 打开文件并读取内容
#     with open(file_path, 'r') as file:
#         file_contents = file.read()
#         print(file_contents)
# else:
#     print("文件不存在")

baconFile = open('bacon.txt', 'w')
baconFile.write("hello,world！\n")
baconFile.close()
baconFile = open('bacon.txt', 'a')
baconFile.write('bacon is not a vegetable.')
baconFile.close()
baconFile =open('bacon.txt')
content = baconFile.read()
baconFile.close()
print(content)
