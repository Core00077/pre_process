import jieba
import jieba.analyse
import time

start = time.time()
jieba.analyse.set_idf_path("idf.txt")
jieba.analyse.set_stop_words("stopwords.txt")
# jieba.enable_parallel(8)

reducedList = []
cnt = 0
not_important = 0.2
very_important = 0.2
filename = "tfidf_seg_" + str(very_important) + "_" + \
           str(not_important) + ".txt"
for line in open("news.txt", encoding='utf8'):
    cnt += 1
    words = jieba.analyse.extract_tags(line, topK=0)
    x = int(len(words) - len(words) * not_important)
    y = int(len(words) * very_important)
    reducedWords = words[y:x]
    reducedList.append(" ".join(reducedWords) + "\n")

    if len(reducedList) >= 1000:
        with open(filename, 'a', encoding='utf8') as f:
            f.writelines(reducedList)
            reducedList.clear()
        print("已tfidf切词:" + str(cnt))
with open(filename, 'a', encoding='utf8') as f:
    f.writelines(reducedList)
    reducedList.clear()
end = time.time()
print("用时共计：" + str(end - start))
