import pandas as pd
# read_file = pd.read_excel("billing_320942.xlsx")

dataframe1 = pd.read_excel("test522a.xlsx")


# dataframe1.to_excel("test522ab.xlsx")
dataframe1.rename(columns=({'Bill.Doc.':'VIA_B2B_BillNumber__c','BillT':'VIA_B2B_Type__c','Billing Date':'EPD_Invoice_Date__c','PayT':'VIA_B2B_PaymentTermCode__c','DstC':'VIA_B2B_CountryCode__c', 'Net Value':'VIA_B2B_TotalBillAmount__c','Sold-to pt':'VIA_B2B_CustomerCodeSoldTo__c'}), inplace=True)


print(dataframe1)
dataframe1.to_excel("test522a1.xlsx", index=False)

# read_file.to_csv("billing_320942.csv", index=False)
