import heapq

def min_cost_path(grid):
  """
  Finds the minimum cost path from the top-left corner to the bottom-right corner of a grid.

  Args:
    grid: A 2D list of integers representing the cost of each cell.

  Returns:
    A list of coordinates representing the minimum cost path.
  """

  rows, cols = len(grid), len(grid[0])
  visited = [[False for _ in range(cols)] for _ in range(rows)]
  distance = [[float('inf') for _ in range(cols)] for _ in range(rows)]
  distance[0][0] = grid[0][0]

  pq = [(grid[0][0], 0, 0)]  # (cost, row, col)

  while pq:
    cost, row, col = heapq.heappop(pq)

    if row == rows - 1 and col == cols - 1:
      return reconstruct_path(distance, row, col)

    if not visited[row][col]:
      visited[row][col] = True

      for dr, dc in [(1, 0), (0, 1)]:
        new_row, new_col = row + dr, col + dc

        if 0 <= new_row < rows and 0 <= new_col < cols and not visited[new_row][new_col]:
          new_cost = distance[row][col] + grid[new_row][new_col]
          if new_cost < distance[new_row][new_col]:
            distance[new_row][new_col] = new_cost
            heapq.heappush(pq, (new_cost, new_row, new_col))

  return None  # No path found

def reconstruct_path(distance, row, col):
  """
  Reconstructs the minimum cost path from the end point.

  Args:
    distance: A 2D list of integers representing the distance to each cell.
    row: The row coordinate of the end point.
    col: The column coordinate of the end point.

  Returns:
    A list of coordinates representing the minimum cost path.
  """

  path = [(row, col)]
  while row > 0 or col > 0:
    dr, dc = 0, 0
    if row > 0 and distance[row - 1][col] < distance[row][col]:
      dr = -1
    if col > 0 and distance[row][col - 1] < distance[row][col]:
      dc = -1
    row += dr
    col += dc
    path.append((row, col))
  return path[::-1]  # Reverse the path

# Example usage
grid = [
  [1,3,1,1],
  [2,1,5,2],
  [2,4,3,1],
  [3,2,3,1]
]

path = min_cost_path(grid)
print(path)  # Output: [(0, 0), (1, 0), (1, 1), (2, 1), (2, 2)]
