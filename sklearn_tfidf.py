import time
import jieba
import numpy as np
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer

# jieba.enable_parallel(4)

# 简体可以使用encoding = 'utf-8',繁体需要使用encoding='gbk'
stopwords = [line.strip() for line in
             open('stopwords.txt', 'r', encoding='utf-8').readlines()]
X, Y = ['\u4e00', '\u9fa5']

# 2.用sklearn的tfidf提取关键词
# 2.1把文章全部合并再计算tfidf再提取关键词语
# 因为tfidf不止需要计算词频（tf）还需要求逆文档频率（idf），
# TF表示词条d在该文档中出现的频率。
# IDF的主要思想是：如果除去本文档包含词条t的文档越少，
# 也就是n越小，IDF越大，则说明词条t具有很好的类别区分能力。
# 具体计算公式见前一篇jieba分词博客的介绍部分。
# 那么我们把所有文档合并，即总文档数为1，这样计算出来IDF值会偏大，很可能失去意义。
# Running time1: 4.5165 Seconds (不开启并行)
# 此法提取一百个关键词的结果最终和jieba自带的分词结果重合度超过65%
content = open("net_news_data_test.txt",'r',encoding='utf-8').read()

tag = jieba.lcut(content.strip())
tag = [i for i in tag if len(i) >= 2 and X <= i <= Y and i not in stopwords]
tag_str = [' '.join(tag)]

vectorizer = CountVectorizer()
cif = vectorizer.fit_transform(tag_str)
transformer = TfidfTransformer()
tfidf = transformer.fit_transform(cif)
word = vectorizer.get_feature_names()  # 得到所有切词以后的去重结果列表
word = np.array(word)  # 把词语列表转化为array数组形式
weight = tfidf.toarray()  # 将tf-idf矩阵抽取出来
word_index = np.argsort(-weight)
word = word[word_index]  # 把word数组按照tfidf从大到小排序
tags = []
for i in range(100):
    tags.append(word[0][i])

##2.2分开所有文章做为语料，再计算总文章的tf-idf
# 这样计算就是原生tfidf值所表达的意义
#
# Running time1: 5.256 Seconds (不开启并行)
'''
tag = []
corpus_list = []
vectorizer = CountVectorizer()
transformer = TfidfTransformer()
for i in range(len(list_content)):
    each_tag = jieba.lcut(list_content[i].strip(),cut_all = False)
    each_tag = [ i for i in each_tag if len(i) >= 2 and X<=i<=Y and i not in stopwords ]
    tag.append(each_tag)
    corpus_list.append([' '.join(tag[i])])

alltag_str = [y for x in corpus_list for y in x]
Alltag_str = ''
for i in range(len(list_content)):
    Alltag_str = Alltag_str + ' ' + alltag_str[i]
alltag_str = [Alltag_str]
corpus_list.append(alltag_str)

corpus = []
for i in range(len(corpus_list)):
    each_content_str = ''.join(corpus_list[i])
    corpus.append(each_content_str)

tfidf=transformer.fit_transform(vectorizer.fit_transform(corpus))
word=vectorizer.get_feature_names()
weight=tfidf.toarray()
word = np.array(word) #把词语列表转化为array数组形式 
weight = tfidf.toarray()#将tf-idf矩阵抽取出来
word_index = np.argsort(-weight)
word = word[word_index]#把word数组按照tfidf从大到小排序
tags = []
for i in range(100):
    tags.append(word[len(word)-1][i])
'''
t3 = time.time()
print(t3 - t2)
