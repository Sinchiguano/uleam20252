import pandas as pd


serData=pd.Series(data=[10,20,30,40,50],index=[
    
'tom','bob','nancy','daniel','cesar'
])

print(serData)

serData=pd.Series([10,20,30,40,50],[
    
'tom','bob','nancy','daniel','cesar'
])

print(serData)


print(serData.index)
print(serData['nancy'])


print('bob' in serData)


serData=serData*2


print(serData)

serData=serData**2

print(serData)

print('******************HERE********************')
myDictionary={
    'one':pd.Series(data=[10,20,30,40],index=['apple','ball','clock','desk']),
    'two':pd.Series(data=[11,22,33,44],index=['apple','ball','cerill','chair'])
}

df=pd.DataFrame(myDictionary)
print(df)
print(df.index)
print('**************************************')

print(df.columns)
print(df.shape)
print(df)
print('**************************************')

testingDf=pd.DataFrame(myDictionary,index=('dancy','ball','apple'))
print(testingDf)


testingDf1=pd.DataFrame(myDictionary,index=['dancy','ball','apple'],columns=['two','five'])
print(testingDf1)



print('**************************************')

data=[{'alex':1, 'joe':2},{'ema':5,'dora':10,'alice':30}]
df=pd.DataFrame(data)
print(df)


df1=pd.DataFrame(data,index=['orange','red'])
print(df1)

df2=pd.DataFrame(data,columns=['joe','dora','alice'])
print(df2)


print('******************HERE********************')
myDictionary={
    'one':pd.Series(data=[10,20,30,40],index=['apple','ball','clock','desk']),
    'two':pd.Series(data=[11,22,33,44],index=['apple','ball','cerill','chair'])
}

df=pd.DataFrame(myDictionary)
print(df)

print(df['one'])
df['three']=df['one']*df['two']
print(df)



df['filter']=df['one']>20
print(df)

df.insert(2,'copy of one',df['one'])
print(df)