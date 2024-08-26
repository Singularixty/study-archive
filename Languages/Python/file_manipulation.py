with open('./test.txt', 'w') as NewFile:
    NewFile.write("Hello World c:")
    NewFile.write("Hello World 2 c:")
    NewFile.close()

with open('./test.txt', 'r') as NewFile:
    FileContent = NewFile.read()
    print(FileContent)

with open('./test.txt', 'r') as NewFile:
    FileContent = NewFile.read(5)
    print(FileContent)