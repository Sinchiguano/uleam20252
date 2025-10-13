import pandas as pd

print('ok......')


serData=pd.Series(data=[10,20,30,40],index=['carlos', 'juan','pepe','lucas'])

print(serData)
print(serData.index)
print(serData['lucas'])
print('yusseppe' in serData)
serData1=serData*2
print(serData1)

print('*************DATAFRAME***************')
dictionary={'one':pd.Series(data=[1,2,3,4,5],index=['carlos', 'juan','pepe','lucas','yusseppe']),
            'two':pd.Series(data=[10,20,30,40,50],index=['carlos', 'juan','pepe','lucas','yusseppe'])}

df=pd.DataFrame(dictionary)
print(df)
print(df.index)
print(df.columns)


df['three']=df['one']*df['two']
print(df)

df['filter']=df['three']>45
print(df)


del df['filter']

print(df)

df.insert(1,'copy of one',df['one'])

print(df)



print('//////////IMPORTING CSV FILES///////////////')
movies=pd.read_csv('movies.csv')
# print(movies.head(3))
print(movies.columns)
print(movies.shape)

print('//////////IMPORTING CSV FILES///////////////')
ratings=pd.read_csv('ratings.csv')
# print(movies.head(3))
print(ratings.columns)
print(ratings.shape)
print(ratings.head(2))

print('//////////IMPORTING CSV FILES///////////////')
tags=pd.read_csv('tags.csv')
# print(movies.head(3))
print(tags.columns)
print(tags.shape)

print(tags.tail(2))
del ratings['timestamp']
del tags['timestamp']
print('variables of tags')
print(tags.columns)
print('variables of ratings')
print(ratings.columns)
print('---------------')
print(tags.iloc[0])


print(tags.iloc[[0,22,500]])
print(tags.index)


print('++++++++++RATINGS++++++')
print(ratings.head(5))
print('++++++++++RATINGS++++++')
print(ratings['rating'].describe())
print(ratings['rating'].mean())
print(ratings['rating'].min())
print(ratings['rating'].max())

is_highly_rated=ratings['rating']>=4
print(ratings[is_highly_rated].head(4))
print(ratings.shape)
print(ratings[is_highly_rated].shape)
print(movies.columns)
print(movies.head(2))

is_animation=movies['genres'].str.contains('Animation')
print(movies.shape)
print(movies[is_animation].shape)

print('movies')
print(movies.columns)
print('ratings')
print(ratings.columns)