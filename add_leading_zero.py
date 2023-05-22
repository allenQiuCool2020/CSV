import pandas as pd
import csv
df = pd.read_csv("test522a.csv")
df["VIA_B2B_BillNumber__c"] = df["VIA_B2B_BillNumber__c"].astype(str).apply(lambda x:x.zfill(10))
# df["EPD_Invoice_Date__c"] = pd.to_datetime(df["EPD_Invoice_Date__c"].astype(str),format='%Y-%m-%d')
df.to_csv("test522a1.csv", index=False)
