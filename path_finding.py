from triGraph import read_graph_json
from json_handler import *
import networkx as nx

def path_finding(graph, pageRanks, trustRanks):
    summarize = []
    return 0

def main():
    pageRanks = read_json('./cache/score_pageRank.json')
    trustRanks = read_json('./cache/score_trustRank.json')
    return 0

if __name__ == "__main__":
    main()