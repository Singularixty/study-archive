with open('./bin/finance_data.csv', 'r') as file:
    print(f'File Path: {file.name}')
    print(f'Mode: {file.mode}')
    file_content = file.read()
    print(file_content)
    file_readline = file.readline()
    print(file_readline)
    file_readlines = file.readlines()
    print(file_readlines)