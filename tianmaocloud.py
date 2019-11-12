import data_clear
from wordcloud import WordCloud
import matplotlib.pyplot as plt
plt.figure(figsize=(20,10))

wc = WordCloud(background_color="white", max_words=2000, scale=4,
                   max_font_size=50, random_state=42, font_path=r'simkai.ttf')
w_c = wc.fit_words({x[0]:x[1] for x in data_clear.word_count.head(100).values})
plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
plt.figure()
plt.show()