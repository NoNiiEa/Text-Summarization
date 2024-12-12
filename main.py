import json 
from text_preprocessing import *
from triGraph import *
from pageRank_fun import *
from trustRank_fun import trustRank

def read_json(dir):
    with open(dir, 'r') as file:
        data = json.load(file)
    return data

def dump_json(dir, data):
    with open(dir, 'w') as file:
        json.dump(data, file, indent=4)

def main():
    data = read_json('./data/Itaewon_tragedy.json')
    tweets = text_processing(data)
    graph = create_trigramGraph(tweets)
    pageRanks = pageRank(graph.reverse(copy=True))
    pageRanks = dict(sorted(pageRanks.items(), key=lambda item: item[1], reverse=True))
    dump_json("./cache/score_pageRank.json", pageRanks)

    trustRanks = trustRank(graph)
    trustRanks = dict(sorted(trustRanks.items(), key=lambda item: item[1], reverse=True))
    dump_json("./cache/score_trustRank.json", trustRanks)
    # rank_test = nx.pagerank(t_graph)
    # rank_test = dict(sorted(rank_test.items(), key=lambda item: item[1], reverse=True))
    # dump_json("./cache/score_real.json", rank_test)
    # print(graph.number_of_nodes())
    # print(graph.number_of_edges())
    # pr = nx.pagerank(graph, alpha=0.85)
    # pr = sorted(pr, key=lambda x : x[1])
    # print(pr)
    

if __name__ == "__main__":
    main()