def pageRank(graph, alpha=0.85, tol=1e-5, max_iter=100):
    nodes = list(graph.nodes())
    numNodes = len(nodes)

    ranks = {node: 1 / numNodes for node in nodes}

    base_rank = (1 - alpha) / numNodes

    for _ in range(max_iter):
        new_ranks = {}
        for node in nodes:
            sum_rank = sum(
                ranks[neighbor] * graph[neighbor][node].get('weight', 1) /
                sum(graph[neighbor][nbr].get('weight', 1) for nbr in graph.successors(neighbor))
                for neighbor in graph.predecessors(node)
                if sum(graph[neighbor][nbr].get('weight', 1) for nbr in graph.successors(neighbor)) > 0
            )
            new_ranks[node] = base_rank + alpha * sum_rank

        if all(abs(new_ranks[node] - ranks[node]) < tol for node in nodes):
            break

        ranks = new_ranks

    return ranks