import pandas as pd
import os
import json
with open('config_rel.json') as f:
    config=json.load(f)
acquire = config.get('acquire')
funding = config.get('funding')
fire = config.get('hire')
new_offer = config.get('new_offering')
def reading_text_file_and_assigning_label(path,label):
    path=os.path.join(path)
    with open(path) as f:
        f=f.readlines()
    df=pd.DataFrame()
    df['v2']=f
    df['v1']='__label__'+label
    df.drop_duplicates(subset='v2',keep='first',inplace=True)
    df=df[['v1','v2']].rename(columns={v1:label, v2:text})
    return(df)
df_acquire=reading_text_file_and_assigning_label(acquire,acquisition)
df_funding=reading_text_file_and_assigning_label(funding,funding)
df_hire=reading_text_file_and_assigning_label(fire,hiring)
df_launch=reading_text_file_and_assigning_label(new_offer,new_offering)
df=df_acquire.append([df_launch,df_hire, df_funding],ignore_index=True)
df=df.sample(frac=1).reset_index(drop=True)
df.iloc[0:int(len(df)*0.8)].to_csv('train.csv', sep='\t', index = False, header = False)
df.iloc[int(len(df)*0.8):int(len(df)*0.9)].to_csv('test.csv', sep='\t', index = False, header = False)
df.iloc[int(len(df)*0.9):].to_csv('dev.csv', sep='\t', index = False, header = False)