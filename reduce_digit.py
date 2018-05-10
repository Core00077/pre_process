import re

filename = "tfidf_seg_0.1_0.2_full.txt"
with open(filename, encoding="utf8") as f:
    texts = f.readlines()

reduced_texts = []
cnt = 0
output = open(filename[:-4] + "_reduce_digit.txt", 'a', encoding="utf8")
for line in texts:
    reduced_texts.append(re.sub("\w*\d+\w*\.?\d*%?\w* |\w*\d+\w*\.?\d*%?\w*", "", line))
    cnt += 1
    if cnt % 10000 == 0:
        print(cnt)
        output.writelines(reduced_texts)
        reduced_texts.clear()

output.writelines(reduced_texts)
output.close()
