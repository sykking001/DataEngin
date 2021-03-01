from sklearn.cluster import KMeans
from sklearn import preprocessing
import pandas as pd
import numpy as np

'''数据导入'''
data = pd.read_csv('car_data.csv',encoding='gbk')
# 将城市列去除
data_train = data.iloc[:,1:]
print(data_train)

'''数据清洗, 均一化'''
min_max_scaler=preprocessing.MinMaxScaler()  #数值的特征化，默认区间为0到1
data_train = min_max_scaler.fit_transform(data_train)
print(data_train)

'''使用KMeans聚类'''
kmeans = KMeans(n_clusters=3)
kmeans.fit(data_train)
predict_y = kmeans.predict(data_train)

'''合并聚类结果，插入到原始数据中'''
result = pd.concat((data, pd.DataFrame(predict_y)), axis=1)
result.rename({0:u'聚类结果'},axis=1, inplace=True)
print(result)

'''结果导出csv'''
result.to_csv("car_data_result.csv",index=False)