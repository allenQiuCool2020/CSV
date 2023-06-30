import pandas as pd
import shutil

import os
path = "C:\\Dev\\CSV\\input"
lists = []
for (root, dirs, file) in os.walk(path):
    for f in file:
        if '.XLSX' in f:
            lists.append(f)
        else:
            print(f"{f} is with the wrong file format, it must be ended with XLSX from SAP")

print(lists)
for list in lists:
    print(list)

def exceltocsv(f1, *args, **kwargs):
    
    # Read the file and converting it to dataframe
    # dataframe1 = pd.read_excel("315103.xlsx")
    dataframe1 = pd.read_excel(f"C:\\Dev\\CSV\\input\\{f1}")

    # Delete last row
    dataframe1.drop(dataframe1.tail(1).index, inplace=True)

    # Updating the description of the first row of columns
    dataframe1.rename(columns=({'Bill.Doc.':'VIA_B2B_BillNumber__c','BillT':'VIA_B2B_Type__c','Billing Date':'EPD_Invoice_Date__c','PayT':'terms','DstC':'VIA_B2B_CountryCode__c', 'Net Value':'VIA_B2B_TotalBillAmount__c','Sold-to pt':'VIA_B2B_CustomerCodeSoldTo__c'}), inplace=True)

    # Converting below two columns to integer
    dataframe1["VIA_B2B_BillNumber__c"] = dataframe1["VIA_B2B_BillNumber__c"].astype(int)
    dataframe1["VIA_B2B_CustomerCodeSoldTo__c"] = dataframe1["VIA_B2B_CustomerCodeSoldTo__c"].astype(int)

    # Adding leading zero to billing number column 
    dataframe1["VIA_B2B_BillNumber__c"] = dataframe1["VIA_B2B_BillNumber__c"].astype(str).apply(lambda x:x.zfill(10))
    print(dataframe1)

    # Delete currency column
    del dataframe1["Curr."]

    

    # Prepare for generating output file name
    listcsv = list.replace("XLSX", "csv")
    print(listcsv)

    # Left join 2 tables
    payment_dataframe = pd.read_excel('payment_terms.XLSX')
    df_merged = pd.merge(dataframe1, payment_dataframe, on='terms', how='left')

    # Update description of 2 fields
    df_merged.rename(columns=({'terms':'VIA_B2B_PaymentTermCode__c', 'description':'VIA_B2B_PaymentTerm__c'}), inplace=True)

    # find duplicated records
    df_merged['duplicated1'] = df_merged.duplicated()


    # Sort sequence of columns
    df_merged = df_merged.loc[:,['VIA_B2B_BillNumber__c', 'VIA_B2B_Type__c', 'EPD_Invoice_Date__c', 'VIA_B2B_PaymentTermCode__c',
                     'VIA_B2B_PaymentTerm__c', 'VIA_B2B_CountryCode__c', 'VIA_B2B_TotalBillAmount__c', 'VIA_B2B_CustomerCodeSoldTo__c', 'duplicated1']]

    
    # Exporting to CSV file
    df_merged.to_csv(f"C:\\Dev\\CSV\\output\\{listcsv}", index=False)

    # Moving input file to archive folder after processing
    processed_file = f"C:\\Dev\\CSV\\input\\{f1}"
    destination = 'C:\\Dev\\CSV\\archive'
    shutil.move(processed_file,destination)

for list in lists:
    exceltocsv(list)


