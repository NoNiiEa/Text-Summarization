import json 
import re
import string
import math
import networkx as nx
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import matplotlib.pyplot as plt

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

def read_json(dir):
    with open(dir, 'r') as file:
        data = json.load(file)
    return data

def clean_data(data):
    texts = []
    for msg in data:
        texts.append(msg["full_text"])
    return texts

def text_processing(texts):
    result = []

    emoj = re.compile("["
        u"\U0001F600-\U0001F64F"  
        u"\U0001F300-\U0001F5FF" 
        u"\U0001F680-\U0001F6FF" 
        u"\U0001F1E0-\U0001F1FF"  
        u"\U00002500-\U00002BEF"
        u"\U00002702-\U000027B0"
        u"\U000024C2-\U0001F251"
        u"\U0001f926-\U0001f937"
        u"\U00010000-\U0010ffff"
        u"\u2640-\u2642" 
        u"\u2600-\u2B55"
        u"\u200d"
        u"\u23cf"
        u"\u23e9"
        u"\u231a"
        u"\ufe0f"
        u"\u3030"
                      "]+", re.UNICODE)
    translator = str.maketrans('', '', string.punctuation)
    lemmatizer = WordNetLemmatizer()
    stop_words = set(stopwords.words("english"))

    for text in texts:
        text = text.lower()
        text = re.sub(r'(https|http)?:\/\/(\w|\.|\/|\?|\=|\&|\%)*\b', '', text, flags=re.MULTILINE)
        text = re.sub(emoj, '', text)
        text = text.translate(translator)
        tokens = word_tokenize(text)
        tokens = [word for word in tokens if word.isalpha() and word not in stop_words]
        lemmas = [lemmatizer.lemmatize(word) for word in tokens]
        result.append(lemmas)
    return result

def create_trigramGraph(texts):
    graph = nx.DiGraph()
    for post in texts:
        for i in range(len(post) - 2):
            bigram1 = post[i] + "-" + post[i+1]
            bigram2 = post[i+1] + "-" + post[i+2]

            if not graph.has_edge(bigram1, bigram2):
                graph.add_edge(bigram1, bigram2, weight = 1)
                continue
            
            graph[bigram1][bigram2]["weight"] += 1
            
    return graph

def visualize_graph(graph):
    plt.figure(figsize=(10, 8))
    pos = nx.spring_layout(graph)
    nx.draw(graph, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=500, font_size=8)
    plt.title("Trigram Graph")
    plt.show()

def pageRank(graph, alpha = 0.85):
    nodes = list(graph.nodes())
    numNodes = len(nodes)

    ranks = {node: 1/numNodes for node in nodes}

    base_rank = (1 - alpha)/numNodes

    for _ in range(100):
        new_rank = {}
        for node in nodes:
            sum_rank = sum(ranks[nieghbor] * graph[nieghbor][node].get('weight') / graph.out_degree[nieghbor] for nieghbor in graph.predecessors(node))
            rank = base_rank + alpha*sum_rank

            new_rank[node] = rank

        rank = new_rank

    
    return rank

def main():
    data = read_json('./data/Itaewon_tragedy.json')
    tweets = clean_data(data)
    tweets = text_processing(tweets)
    graph = create_trigramGraph(tweets)
    t_graph = graph.reverse(copy=True)
    rank = pageRank(t_graph)
    # rank_test = nx.pagerank(t_graph)
    # rank_test = dict(sorted(rank_test.items(), key=lambda item: item[1]))
    rank = dict(sorted(rank.items(), key=lambda item: item[1]))
    print(rank)

    # print(graph.number_of_nodes())
    # print(graph.number_of_edges())
    # pr = nx.pagerank(graph, alpha=0.85)
    # pr = sorted(pr, key=lambda x : x[1])
    # print(pr)
    

if __name__ == "__main__":
    main()
