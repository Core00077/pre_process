import re
import time
import jieba
import math

# 非常不节省内存的使用方法
# import jieba.analyse

start = time.time()
# jieba.enable_parallel(4)
jieba.load_userdict(r"userwords.txt")
cnt = 0
newsList = []
newsSets = []
output = open("seg.txt", 'a', encoding="utf8")
inline = []
allWordsSet = set()
print("开始分词...分词同时记录所有词汇，根据数据集大小会占用较大内存")
for line in open(r"C:\news\OurNews\net_news_data.txt", encoding="utf8"):
    cnt += 1
    news = re.sub("http.*title,|</content,,", "", line)
    words = jieba.lcut(news)
    words_set = set(words)
    # 添加到list和set
    newsList.append(" ".join(words))
    newsSets.append(words_set)
    allWordsSet = words_set | allWordsSet

    if cnt % 1000 == 0:
        print(cnt)
        output.writelines(newsList)
        newsList.clear()
output.writelines(newsList)
print("分词结束，结果已写入本地。开始统计计算idf值...")
docs = len(newsList)
idf = {}
print("统计得共有" + str(len(allWordsSet)) + "个词语...")
cnt = 0
for word in allWordsSet:
    cnt += 1
    if cnt % 1000 == 0:
        print(cnt)
    wordCount = 0
    for newsSet in newsSets:
        if word in newsSet:
            wordCount += 1
    idf[word] = math.log(docs / wordCount + 1)
print("统计计算完成，开始写入本地...")
with open(r"idf.txt", "w", encoding="utf8")as f:
    idfList = []
    for key, value in idf.items():
        idfList.append(key + " " + str(value) + "\n")
    f.writelines(idfList)
print("写入成功！")
end = time.time()
print("分词+idf统计计算完成，用时：" + str(end - start) + "s")
