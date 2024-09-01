# ☁️ Wordcloud

WordCloud is a data visualization technique used for representing text data in which the size of each word indicates its frequency or importance. Significant textual data points can be highlighted using a word cloud. Word clouds are widely used for analyzing data from social network websites.

To use WordCloud in Jupyter Notebook, you first need to install the wordcloud library. You can do this with pip:

```cmd
!pip install wordcloud
```

Here's an example of how to generate a word cloud in Jupyter Notebook:

```python
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Create a list of word
text=("Python Python Python Matplotlib Matplotlib Seaborn Network Plot Violin Chart Pandas Datascience Wordcloud Spider Radar Parrallel Alpha Color Brewer Density Scatter Barplot Barplot Boxplot Violinplot Treemap Stacked Area Chart Chart Visualization Dataviz Donut Pie Time-Series Wordcloud Wordcloud Sankey Bubble")

# Create the wordcloud object
wordcloud = WordCloud(width=480, height=480, margin=0).generate(text)

# Display the generated image:
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.margins(x=0, y=0)
plt.show()
```

In this example, we first import the necessary libraries. We then create a string of words, where the frequency of each word is proportional to how often it appears. The WordCloud function is then used to generate the word cloud, and the resulting image is displayed with matplotlib.

---

### Customizing cloud (parameters)

WordCloud in Python allows a variety of customizations to make the word cloud more informative and visually appealing. Here are some of them:

- **Size**: You can specify the size of the word cloud using the `width` and `height` parameters.
- **Background Color**: You can change the background color of the word cloud using the `background_color` parameter.
- **Maximum Words**: You can limit the number of words in the word cloud using the `max_words` parameter.
- **Stopwords**: You can remove certain words (like common English words "the", "is", etc.) from the word cloud using the `stopwords` parameter.
- **Color of Words**: You can set the color of words in the word cloud using the `color_func` parameter.
- **Mask**: You can shape your wordcloud in any form using the `mask` parameter.
- **Contour Width and Color**: You can set the width of the contour and its color using `contour_width` and `contour_color`.
- **Maximum and Minimum Font Size**: You can set the maximum and minimum font sizes for the words in the cloud using `max_font_size` and `min_font_size`.
- **Colormap**: You can change the colormap of the word cloud using the `colormap` parameter.

Here's an example of how you might use some of these parameters:

```python
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

text = 'Python python python matplotlib seaborn'

stopwords = set(STOPWORDS)
wordcloud = WordCloud(stopwords=stopwords, max_words=10, background_color="white").generate(text)

plt.figure(figsize=(8, 8), facecolor=None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad=0)
  
plt.show()
```

In this example, we've limited the word cloud to 10 words, set the background color to white, and removed common English words.