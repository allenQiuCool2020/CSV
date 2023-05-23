import pandas as pd

import os
path = "C:\Dev\CSV\input"
lists = []
for (root, dirs, file) in os.walk(path):
    for f in file:
        if '.XLSX' in f:
            print(f)
            lists.append(f)
        else:
            print(f"{f} is with the wrong file format, it must be ended with XLSX from SAP")

print(lists)
for list in lists:
    list1 = f'"{list}"'
    print(list1)
    print(list)

def exceltocsv(f1, *args, **kwargs):
    # Read the file and converting it to dataframe
    # dataframe1 = pd.read_excel("315103.xlsx")

    dataframe1 = pd.read_excel(f1)
    # Count rows
    # count_rows = len(dataframe1.index)
    # print(count_rows)

    # Delete last row
    dataframe1.drop(dataframe1.tail(1).index, inplace=True)

    # Updating the description of the first row of columns
    dataframe1.rename(columns=({'Bill.Doc.':'VIA_B2B_BillNumber__c','BillT':'VIA_B2B_Type__c','Billing Date':'EPD_Invoice_Date__c','PayT':'VIA_B2B_PaymentTermCode__c','DstC':'VIA_B2B_CountryCode__c', 'Net Value':'VIA_B2B_TotalBillAmount__c','Sold-to pt':'VIA_B2B_CustomerCodeSoldTo__c'}), inplace=True)

    # Converting below two columns to integer
    dataframe1["VIA_B2B_BillNumber__c"] = dataframe1["VIA_B2B_BillNumber__c"].astype(int)
    dataframe1["VIA_B2B_CustomerCodeSoldTo__c"] = dataframe1["VIA_B2B_CustomerCodeSoldTo__c"].astype(int)

    # Adding leading zero to billing number column 
    dataframe1["VIA_B2B_BillNumber__c"] = dataframe1["VIA_B2B_BillNumber__c"].astype(str).apply(lambda x:x.zfill(10))
    print(dataframe1)

    # Delete currency column
    del dataframe1["Curr."]

    # Exporting to CSV file
    dataframe1.to_csv("test11.csv", index=False)

exceltocsv(list1)


