import pandas as pd
# read the file

dataframe1 = pd.read_excel("test522a.xlsx")


# updating the description of the first column, converting to integer and adding leading zero
dataframe1.rename(columns=({'Bill.Doc.':'VIA_B2B_BillNumber__c','BillT':'VIA_B2B_Type__c','Billing Date':'EPD_Invoice_Date__c','PayT':'VIA_B2B_PaymentTermCode__c','DstC':'VIA_B2B_CountryCode__c', 'Net Value':'VIA_B2B_TotalBillAmount__c','Sold-to pt':'VIA_B2B_CustomerCodeSoldTo__c'}), inplace=True)

dataframe1["VIA_B2B_BillNumber__c"] = dataframe1["VIA_B2B_BillNumber__c"].astype(int)
dataframe1["VIA_B2B_CustomerCodeSoldTo__c"] = dataframe1["VIA_B2B_CustomerCodeSoldTo__c"].astype(int)

dataframe1["VIA_B2B_BillNumber__c"] = dataframe1["VIA_B2B_BillNumber__c"].astype(str).apply(lambda x:x.zfill(10))
print(dataframe1)

# exporting to CSV file
dataframe1.to_csv("test522a1.csv", index=False)


