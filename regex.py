import re

cnt = 0
newsList = []
output = open(r"news.txt", "a", encoding='utf8')
for line in open(r"net_news_data.txt", encoding='utf8'):
    news = re.sub("http.*title,|</content,,", "", line)
    if news == "":
        continue
    newsList.append(news)
    cnt += 1
    if cnt % 10000 == 0:
        print(cnt)
        output.writelines(newsList)
        newsList.clear()
output.writelines(newsList)
