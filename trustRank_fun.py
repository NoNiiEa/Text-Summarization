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

    nodes = list(graph.nodes())

    ranks = {node: 0 for node in nodes}
    ranks[list(pageRank.keys())[0]] = 1

    seed = {node: 1 if ranks[node] == 1 else 0 for node in nodes}
    divider = sum(seed.values())
    seed = {node: value / divider for node, value in seed.items()}

    for _ in range(times):
        new_ranks = {}
        for node in nodes:
            base_rank = (1 - alpha) * seed[node]
            sum_rank = sum(
                ranks[neighbor] * graph[neighbor][node].get('weight', 1) /
                sum(graph[neighbor][nbr].get('weight', 1) for nbr in graph.successors(neighbor))
                for neighbor in graph.predecessors(node)
                if sum(graph[neighbor][nbr].get('weight', 1) for nbr in graph.successors(neighbor)) > 0
            )
            new_ranks[node] = base_rank + alpha * sum_rank
        ranks = new_ranks

    return ranks

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