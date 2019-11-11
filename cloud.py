#coding:utf-8
import matplotlib.pyplot as plt
import jieba
from wordcloud import WordCloud,STOPWORDS
COMMENT_FILE_PATH='D:\project\pacong\jd_an3+_comment.txt'
def cut_word():
    with open(COMMENT_FILE_PATH,'r',encoding='utf-8') as file:
        comment_txt = file.read()
        wordlist = jieba.cut(comment_txt, cut_all=True)
        wl = " ".join(wordlist)
        # print(wl)
        return wl
def create_word_cloud():
    wc = WordCloud(background_color="white", max_words=2000, scale=4,
                   max_font_size=50, random_state=42, font_path=r'simkai.ttf')
    wc.generate(cut_word())
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    plt.figure()
    plt.show()
if __name__ == '__main__':
    create_word_cloud()
