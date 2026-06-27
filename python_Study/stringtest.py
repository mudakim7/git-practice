import string
import wikipedia
import matplotlib.pyplot as plt
from wordcloud import WordCloud

#print(string.ascii_lowercase)

wiki = wikipedia.page('Artificial intelligence')
text = wiki.content
#print(text)
words = WordCloud(width=2000, height=1500).generate(text)
plt.figure(figsize=(40,30))
plt.imshow(words)
plt.show()
