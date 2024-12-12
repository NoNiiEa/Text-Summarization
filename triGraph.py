import networkx as nx
import matplotlib.pyplot as plt

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