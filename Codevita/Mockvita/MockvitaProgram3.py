def max_light_loop(M, N, grid):
    # Directions: 0=Up, 1=Down, 2=Left, 3=Right
    directions = [(-1,0),(1,0),(0,-1),(0,1)]

    def change_direction(mirror, d):
        if mirror == '/':
            return [3,2,1,0][d]  # Up->Right, Down->Left, Left->Down, Right->Up
        if mirror == '\\':
            return [2,3,0,1][d]  # Up->Left, Down->Right, Left->Up, Right->Down
        return d

    max_loop_length = 0

    # Start from each mirror
    for i in range(M):
        for j in range(N):
            if grid[i][j] == '0':
                continue
            for d in range(4):  # Try all 4 directions
                visited_list = []
                visited_set = set()
                x, y, dir = i, j, d

                while True:
                    state = (x, y, dir)
                    if state in visited_set:
                        # Loop detected
                        idx = visited_list.index(state)
                        loop_length = len(visited_list) - idx
                        max_loop_length = max(max_loop_length, loop_length)
                        break

                    visited_list.append(state)
                    visited_set.add(state)

                    # Move one step in current direction
                    dx, dy = directions[dir]
                    x, y = x + dx, y + dy

                    # Check grid boundaries
                    if not (0 <= x < M and 0 <= y < N):
                        break
                    # Change direction if hitting a mirror
                    if grid[x][y] != '0':
                        dir = change_direction(grid[x][y], dir)

    return max_loop_length


if __name__ == "__main__":
    M, N = map(int, input().split())
    grid = [input().split() for _ in range(M)]
    print(max_light_loop(M, N, grid))
