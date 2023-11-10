import re
import pandas as pd
from collections import Counter
from nltk.probability import FreqDist
import matplotlib.pyplot as plt
import seaborn as sns
import nltk
from wordcloud import WordCloud

def taskOneA(chunkIterator):
    res = []
    count = 0
    for chunk in chunkIterator:
        for row in chunk["text"]:
            row = row.split()
        if count % 100000 == 0:
            print(count)
        count = count + 1
    for word in row:
        res.append(word)
    # calculate number of words in whole text in the data
    res = list(set(res))
    print(len(res))

    # create wordcloud
    unique_string = (" ").join(res)
    wordcloud = WordCloud(width=1000, height=500).generate(unique_string)
    plt.figure(figsize=(15, 8))
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()
    plt.close()


def taskOneB(chunkIterator):
    words = []
    i = 0
    for chunk in chunkIterator:
        if i % 1000 == 0:
            print(i)
        for text in chunk["passage"]:   
            words += text.split()
            i+=1
    print(words)
    frequencyDistribution = FreqDist(words)

    # Build plot to visualize word frequency distribution. Only look for the top 30 words.
    plt.figure(figsize=(12, 6))
    plt.title('Top 20 Most Frequent Words')
    frequencyDistribution.plot(30, cumulative=False)
    plt.show()


def taskOneC(chunkIterator):
    res = []
    count = 0
    for chunk in chunkIterator:
        for row in chunk["text"]:
            if count % 100000 == 0:
                print(count)
            count = count + 1
            res.append(row)
    bigrams = [x for l in res for x in zip(
        l.split(" ")[:-1], l.split(" ")[1:])]
    # print(bigrams)
    bigramsCounter = Counter(bigrams)
    # Only the 10 most common words.
    top_bigrams = bigramsCounter.most_common(20)
    x, y = [], []
    for word, count in top_bigrams:
        x.append(word)
        y.append(count)
    list = []
    [list.append(k+" "+v) for k, v in x]
    # Plotte die Daten
    plt.figure(figsize=(10, 6))
    plt.barh(list, y, color='skyblue')
    plt.xlabel('Häufigkeit')
    plt.ylabel('Bigrams')
    plt.title(
        'Top 20 Meist Verwendete Bigrams aus dem Datensatz in diesem geilen Modul')
    plt.show()


def taskOneD(chunkIterator):
    lengths = []
    i = 0
    for chunk in chunkIterator:
        if i % 10000 == 0:
            print(i/8000000)

        for text in chunk["passage"]:   
            lengths.append(len(text))
            i+=1
    # Create a density plot
    sns.set(style="whitegrid")
    plt.figure(figsize=(10, 6))
    sns.kdeplot(lengths, shade=True, color="skyblue")
    plt.title("Text Length Distribution")
    plt.xlabel("Text Length (Number of Words)")
    plt.ylabel("Density")
    plt.show()

def taskOneE(chunkIterator):
    words = []
    i = 0
    for chunk in chunkIterator:
        if i % 9000000 == 0:
            print(i)
        for text in chunk["passage"]:   
            words += text.split()
            i+=1
    pos_tags = nltk.pos_tag(words)

    #Build distribution empty lists.
    noun_freq = FreqDist()
    verb_freq = FreqDist()
    adj_freq = FreqDist()

    #Put words into their classes.
    for word, pos in pos_tags:
        if pos.startswith('N'):  # Noun
            noun_freq[word] += 1
        elif pos.startswith('V'):  # Verb
            verb_freq[word] += 1
        elif pos.startswith('J'):  # Adjective
            adj_freq[word] += 1
    
    zipfPlot(noun_freq, 'Noun')
    zipfPlot(verb_freq, 'Verb')
    zipfPlot(adj_freq, 'Adjective')

# Generate separate Zipfian plots for each category
def zipfPlot(freq_dist, category):
    plt.figure(figsize=(10, 6))
    plt.xscale('log')
    plt.yscale('log')
    plt.title(f'Zipfian Plot for {category}s')
    plt.xlabel('Word Rank (log)')
    plt.ylabel('Frequency (log)')
    freq_dist.plot(30, cumulative=False)
    plt.show()

def main() -> None:
    FILEPATH = "collection.tsv"
    chunkIterator = pd.read_csv(FILEPATH, sep='\t', chunksize=100, names = ["pid", "passage"])

    # taskOneA(chunkIterator)
    # taskOneB(chunkIterator)
    # taskOneC(chunkIterator)
    # taskOneD(chunkIterator)
    # taskOneE(chunkIterator)
    
main()