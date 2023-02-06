import pandas as pd  
df=pd.read_csv('data.csv')
df["hourly"]=df["Salary Estimate"].apply(lambda x:1 if 'per hour'in x.lower() else 0)
df["emloyer_provied"]=df["Salary Estimate"].apply(lambda x:1 if 'emloyer provided salary'in x.lower()else 0)
df = df[df['Salary Estimate'] != '-1']
salary = df['Salary Estimate'].apply(lambda x: x.split('(')[0])
minus_Kd = salary.apply(lambda x: x.replace('K','').replace('$',''))

min_hr = minus_Kd.apply(lambda x: x.lower().replace('per hour','').replace('employer provided salary:',''))

df['min_salary'] = min_hr.apply(lambda x: int(x.split('-')[0]))
df['max_salary'] = min_hr.apply(lambda x: int(x.split('-')[1]))
df['avg_salary'] = (df.min_salary+df.max_salary)/2



#company name
df['company_txt']=df.apply(lambda x:x['Company Name'] if x['Rating']<0 else x['Company Name'][:-3],axis=1)



