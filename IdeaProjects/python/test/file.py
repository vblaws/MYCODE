f = open('C:/Users/32394/OneDrive/桌面/python用/测试.txt', 'r', encoding='UTF-8')
# 一次性读取整个文件夹,将返回一个列表,一行作为一个元素给content
content = f.readlines()

print(content)
print(f"读取十个字节内容是{f.read(10)}")
f.close()
