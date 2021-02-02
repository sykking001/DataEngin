#!/usr/bin/env python
# coding: utf-8

# ![image.png](attachment:image.png)

# In[31]:


import pandas as pd

# 数据加载
data = pd.read_csv('./car_complain.csv')


# In[32]:


# 删除problem列，并对其进行get_dummies操作
data = data.drop('problem', axis=1).join(data.problem.str.get_dummies(',')) # 这行的写法不是很理解
data


# In[34]:


# 数据清洗
def apply_replace(x):
    x = x.replace('一汽-大众','一汽大众')
    return x
data['brand'] = data['brand'].apply(apply_replace)
data


# In[54]:


# 统计品牌投诉总数
result = data.groupby('brand')['id'].agg(['count'])
result


# In[36]:


# 统计车型投诉总数
result2 = data.groupby('car_model')['id'].agg(['count'])
result2.sort_values('count', ascending=False)


# In[77]:


# 统计哪个品牌的平均车型投诉最多

# 提取data的brand和car_model列
temp = data.iloc[:,1:3]
# 去掉车型故障的重复项，计算一个品牌下车型的个数
def apply_count(df):
    return df.iloc[-1, :]
result_temp = temp.groupby(['brand','car_model']).apply(apply_count)
result_temp.reset_index(drop=True, inplace=True)
result_temp = result_temp.groupby('brand').agg('count')
# 将结果合并到result4中
result4 = result_temp.merge(result, how='inner', on='brand')
# 将故障总数列除以车型列，得到最终结果
def apply_div(Serie):
    return Serie['count']/Serie['car_model']
result4['avg'] = result4[['car_model','count']].apply(apply_div, axis=1)
# 对结果排序
result4.sort_values('avg', ascending=False)


# In[ ]:




