from collections import deque
from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []
            
        ROWS, COLS = len(heights), len(heights[0])
        p_queue = deque()
        a_queue = deque()
        p_reached = set()
        a_reached = set()
        
        # 1. Initialize queues with border cells
        for c in range(COLS):
            p_queue.append((0, c))
            p_reached.add((0, c))
            
            a_queue.append((ROWS - 1, c))
            a_reached.add((ROWS - 1, c))
            
        for r in range(ROWS):
            p_queue.append((r, 0))
            p_reached.add((r, 0))
            
            a_queue.append((r, COLS - 1))
            a_reached.add((r, COLS - 1))
            
        # 2. Reusable BFS function to expand from the queue
        def bfs(queue, ocean_reached):
            dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
            while queue:
                r, c = queue.popleft()
                
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    
                    # Boundary check
                    if nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS:
                        continue
                    # Visited check
                    if (nr, nc) in ocean_reached:
                        continue
                    # Uphill validation (since we flow backward from ocean to mountain)
                    if heights[nr][nc] < heights[r][c]:
                        continue
                        
                    ocean_reached.add((nr, nc))
                    queue.append((nr, nc))
                    
        # 3. Process both oceans
        bfs(p_queue, p_reached)
        bfs(a_queue, a_reached)
        
        # 4. Return coordinates that can reach both
        return [list(cell) for cell in (p_reached & a_reached)]
