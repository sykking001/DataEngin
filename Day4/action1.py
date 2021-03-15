import pandas as pd

# 数据加载
pd.set_option('max_columns', None)
data = pd.read_csv('./Market_Basket_Optimisation.csv', header = None)
print(data.shape) # 7501 * 20

transactions = []
# 按行遍历数据
for i in range(0, data.shape[0]):
	# 按列遍历，相当于一行一行读取
	temp = []
	for j in range(0, data.shape[1]):
		if str(data.values[i,j]) != 'nan':
			temp.append(data.values[i,j])
	# print(temp)
	transactions.append(temp)
# print(transactions)

'''使用efficient_apriori工具包'''
from efficient_apriori import apriori
itemsets, rules = apriori(transactions, min_support=0.05,  min_confidence=0.3)
print('频繁项集：', itemsets)
print('关联规则：', rules)

print('-'*100)

'''采用mlxtend.frequent_patterns工具包'''
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules
from mlxtend.preprocessing import TransactionEncoder
# 进行one-hot编码
te = TransactionEncoder()  # 套路，当作工具使用
data = te.fit_transform(transactions)  # 套路，当作工具使用
transactions = pd.DataFrame(data, columns=te.columns_)  # 使用原list里的数值作为columns，否则将会由数字进行代替
itemsets = apriori(transactions, use_colnames=1, min_support=0.05)
# 按照支持度从大到小进行排序
itemsets = itemsets.sort_values(by="support", ascending=False)
print('-' * 20, '频繁项集', '-' * 20)
print(itemsets)
# 根据频繁项集计算关联规则，设置最小提升度
rules = association_rules(itemsets, metric='lift', min_threshold=1.1)
# 按照提升度从大到小进行排序
rules = rules.sort_values(by="lift", ascending=False)
print('-' * 20, '关联规则', '-' * 20)
print(rules)





