## 文件的读写

```
# 文件的写入
filename = "out/data.txt"
with open(filename, 'w', encoding='utf-8') as myfile:
    myfile.write("你好， Python!\n")
    myfile.write("hello Python!\n")

```
