from json_handler import *
from text_preprocessing import *
from triGraph import *
from pageRank_fun import *
from trustRank_fun import trustRank

def main():
    data = read_json('./data/Itaewon_tragedy.json')
    tweets = text_processing(data)

    graph = create_trigramGraph(tweets)
    dump_graph_json('./cache/TriGraph.json', graph)

    pageRanks = pageRank(graph.reverse(copy=True))
    dump_json("./cache/score_pageRank.json", pageRanks)

    trustRanks = trustRank(graph)
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