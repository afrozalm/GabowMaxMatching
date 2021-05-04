from MaxMatching import MaxMatching


def solution(bananas):
    nodes = len(bananas)
    maxMatching = MaxMatching(nodes)
    for i in range(nodes):
        for j in range(i+1, nodes):
            if valid(bananas[i], bananas[j]):
                maxMatching.addEdge(i+1, j+1)

    maxMatching.E()
    return nodes - maxMatching.getMatchingSize()


def valid(n, m):
    s = n+m
    return s & (s-1) != 0


if __name__ == "__main__":
    print(solution([1, 1]))
    print(solution([1, 7, 3, 21, 13, 19]))
