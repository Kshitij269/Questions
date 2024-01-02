class Solution:

    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if not image:
            return 0

        initialColor = image[sr][sc]
        newColor = color
        rows = len(image)
        columns = len(image[0])
        visited = set()
        ans = image

        def bfs(sr, sc, ans, visited, image, initialColor, newColor):
            q = collections.deque()
            visited.add((sr, sc))
            q.append((sr, sc))

            while q:
                row, col = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                for dr, dc in directions:
                    if (
                            (row + dr) in range(rows)
                            and (col + dc) in range(columns)
                            and image[row + dr][col + dc] == initialColor
                            and ans[row + dr][col + dc] != newColor
                            and (row + dr, col + dc) not in visited
                    ):
                        ans[row + dr][col + dc] = newColor
                        q.append((row + dr, col + dc))
                        visited.add((row + dr, col + dc))

        if (sr, sc) not in visited:
            bfs(sr, sc, ans, visited, image, initialColor, newColor)
        ans[sr][sc] = newColor
        print(ans)
        return ans


class Solution:

    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if not image:
            return 0

        initialColor = image[sr][sc]
        newColor = color
        rows = len(image)
        columns = len(image[0])
        visited = set()
        ans = image

        def bfs(sr, sc, ans, visited, image, initialColor, newColor):
            q = collections.deque()
            visited.add((sr, sc))
            q.append((sr, sc))

            while q:
                row, col = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                for dr, dc in directions:
                    if (
                            (row + dr) in range(rows)
                            and (col + dc) in range(columns)
                            and image[row + dr][col + dc] == initialColor
                            and ans[row + dr][col + dc] != newColor
                            and (row + dr, col + dc) not in visited
                    ):
                        ans[row + dr][col + dc] = newColor
                        q.append((row + dr, col + dc))
                        visited.add((row + dr, col + dc))

        if (sr, sc) not in visited:
            bfs(sr, sc, ans, visited, image, initialColor, newColor)
        ans[sr][sc] = newColor
        print(ans)
        return ans
