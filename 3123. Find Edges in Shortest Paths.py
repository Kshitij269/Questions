class Solution:
    def findAnswer(self, n: int, edges: List[List[int]]) -> List[bool]:
        graph = [[] for i in range(n)]
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))

        def dijkstra(source):
            distance = [float("inf") for _ in range(n)]
            distance[source] = 0
            pq = [(0, source)]

            while pq:
                w1, u1 = heappop(pq)
                if distance[u1] != w1:
                    continue
                for u2, w2 in graph[u1]:
                    if w1 + w2 < distance[u2]:
                        distance[u2] = w1 + w2
                        heappush(pq, (w1 + w2, u2))

            return distance

        distance_0 = dijkstra(0)
        distance_n_1 = dijkstra(n - 1)
        if distance_0[n - 1] == float("inf"):
            return [False for _ in range(len(edges))]

        res = []
        for u, v, w in edges:
            res.append(
                distance_0[u] + w + distance_n_1[v] == distance_0[n - 1] or \
                distance_0[v] + w + distance_n_1[u] == distance_0[n - 1]
            )
        return res

