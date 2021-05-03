#웹 크롤링을 위한 import
from bs4 import BeautifulSoup
from collections import Counter
import nltk
import requests

#wordcloud import
import re
from wordcloud import WordCloud, ImageColorGenerator
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

def text_convert(txt):
    return txt


def textfile_convert(txtfile):
    text = ""
    with open('test.txt', encoding='utf-8') as f:
        text = ''.join(f.readlines())
    return text


def url_convert(url):
    content = ""
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        script_tag = soup.find_all(['script', 'style', 'header', 'footer', 'form'])
        for item in script_tag:
            item.extract()
        content = soup.get_text()
        return content

def get_noun(text):
    cleaned_text = re.sub('[\{\}\[\]\/?.,;:|\)*~`!^\-_+<>@\#$%&\\\=\(\'\"]',
                          '', text)
    is_noun = lambda pos: pos[:2] == "NN"
    tokenized = nltk.word_tokenize(cleaned_text)

    nouns = [word for (word, pos) in nltk.pos_tag(tokenized) if is_noun(pos)]
    count = Counter(nouns)
    noun_list = count.most_common(100)
    return noun_list

def generation(request):
    converted_text = ""
    if request['sourceType'] == "T":
        converted_text = text_convert(request['source'])
    elif request['sourceType'] == "U":
        converted_text = url_convert(request['source'])


    noun_list = get_noun(converted_text)
    mask = np.array(Image.open('cloud.png'))
    wc = WordCloud(background_color="white", mask=mask, font_path='font/NanumGothic.ttf').generate_from_frequencies(dict(noun_list))
    filename = request['uid'] + '.png'

    wc.to_file('./media/' + filename)
    print("filename", filename)

    #plt.imshow(wc, interpolation='bilinear')
    #plt.axis("off")
    #plt.show()
    return filename

