import pandas as pd
import matplotlib.pyplot as plt
from nltk.tokenize import word_tokenize

# 数据加载
data = pd.read_csv('./Market_Basket_Optimisation.csv', header = None)
# 数据整理
transactions = []
item_count = {} 	# 使用字典计数
# 按行遍历数据
for i in range(0, data.shape[0]):
	# 按列遍历，相当于一行一行读取
	temp = []
	for j in range(0, data.shape[1]):
		item = str(data.values[i,j])
		if item != 'nan':
			temp.append(item)
			if item not in item_count:
				item_count[item] = 1
			else:
				item_count[item] += 1
	# print(temp)
	transactions.append(temp)
# print(item_count)
# print(transactions)

from wordcloud import WordCloud
def remove_stop_words(f):
	stop_words = []
	for stop_word in stop_words:
		f = f.replace(stop_word, '')
	return f

def create_word_cloud(f):
	f = remove_stop_words(f)
	cut_text = word_tokenize(f)
	cut_text = " ".join(cut_text)
	wc = WordCloud(
		max_words=100,
		width=2000,
		height=1200,
    )
	wordcloud = wc.generate(cut_text)
	wordcloud.to_file("wordcloud.jpg")

# 生成词云
all_word = ' '.join('%s' %item for item in transactions)
# print(all_word)
create_word_cloud(all_word)

# 绘制词汇频率top10 柱状图
s1 = pd.Series(item_count).sort_values(ascending=False)[:11]
plt.figure(figsize=(10,6))
s1.plot(kind = 'bar')
plt.title('Top10 Data of Wordcloud')
plt.show()