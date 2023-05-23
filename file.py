import os
path = "C:\Dev\CSV\input"
lists = []
for (root, dirs, file) in os.walk(path):
    for f in file:
        if '.XLSX' in f:
            print(f)
        else:
            print(f"{f} is with the wrong file format, it must be ended with XLSX from SAP")
lists.append(f)
print(lists)
for list in lists:
    list1 = f'"{list}"'
    print(list1)
    print(list)

