def count_closed_shapes(segments):
    from collections import defaultdict, deque
    # 
    adj = defaultdict(list)
    for x1, y1, x2, y2 in segments:
        p1 = (x1, y1)
        p2 = (x2, y2)
        adj[p1].append(p2)
        adj[p2].append(p1)
    # 
    visited = set()
    count = 0
    # 
    def dfs(node, parent):
        visited.add(node)
        for neighbor in adj[node]:
            if neighbor not in visited:
                if dfs(neighbor, node):
                    return True
            elif neighbor != parent:
                # Found a cycle
                return True
        return False
    # 
    for node in adj:
        if node not in visited:
            # Check if this component has a cycle
            stack = [(node, None)]
            has_cycle = False
            while stack:
                curr, parent = stack.pop()
                if curr in visited:
                    continue
                visited.add(curr)
                for neighbor in adj[curr]:
                    if neighbor not in visited:
                        stack.append((neighbor, curr))
                    elif neighbor != parent:
                        has_cycle = True
            if has_cycle:
                count += 1
    # 
    return count

# Reading input
n = int(input())
segments = []
for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    segments.append((x1, y1, x2, y2))

print(count_closed_shapes(segments))

