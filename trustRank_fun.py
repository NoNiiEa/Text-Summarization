import json 
import numpy as np
from text_preprocessing import *
from triGraph import *
import json
import os

def read_json(dir):
    with open(dir, 'r') as file:
        data = json.load(file)
    return data

def dump_json(dir, data):
    with open(dir, 'w') as file:
        json.dump(data, file, indent=4)

def is_file_empty(file_path):
    if os.path.exists(file_path):
        if os.stat(file_path).st_size == 0:
            return True 
        return False
    else:
        raise FileNotFoundError(f"The file '{file_path}' does not exist.")

def trustRank(graph, alpha = 0.85, times = 20):
    pageRank = {}
    try :
        if not is_file_empty('./cache/score_pageRank.json'):
            with open('./cache/score_pageRank.json', 'r') as file:
                pageRank = json.load(file)
        else :
            print("File score_pageRank.json is empty!")
    except FileNotFoundError as e:
        print(e)

    seeds = {list(pageRank.keys())[0] : 1}

    nodes = list(graph.nodes())
    num_nodes = len(nodes)

    # Transition matrix T (row-normalized adjacency matrix)
    T = nx.to_numpy_array(graph, nodelist=nodes, weight='weight')
    row_sums = T.sum(axis=1)
    T = np.divide(T, row_sums[:, np.newaxis], where=row_sums[:, np.newaxis] != 0)

    # Initialize seed vector d
    d = np.zeros(num_nodes)
    if seeds is None:
        raise ValueError("Seeds must be provided as a dictionary of {node: score}.")

    for node, score in seeds.items():
        d[nodes.index(node)] = score

    # Normalize seed vector
    d = d / d.sum()

    # Initialize TrustRank vector t* with the seed vector
    trust_rank = np.copy(d)

    # Perform iterations of biased PageRank
    for _ in range(times):
        trust_rank = alpha * np.dot(T.T, trust_rank) + (1 - alpha) * d

    # Map TrustRank scores back to node labels
    trust_rank_dict = {nodes[i]: trust_rank[i] for i in range(num_nodes)}

    return trust_rank_dict

def main():
    data = read_json('./data/Itaewon_tragedy.json')
    tweets = text_processing(data)
    graph = create_trigramGraph(tweets)
    trustRanks = trustRank(graph)
    trustRanks = dict(sorted(trustRanks.items(), key=lambda item: item[1], reverse=True))
    dump_json("./cache/score_trustRank.json", trustRanks)
    return 0

if __name__ == '__main__':
    main()