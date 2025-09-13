import java.util.*;

public class MirrorMaze {

    static int[][] directions = {{-1,0},{1,0},{0,-1},{0,1}}; // Up, Down, Left, Right

    static int changeDirection(char mirror, int dir) {
        if (mirror == '/') {
            switch(dir) {
                case 0: return 3; // Up -> Right
                case 1: return 2; // Down -> Left
                case 2: return 1; // Left -> Down
                case 3: return 0; // Right -> Up
            }
        } else if (mirror == '\\') {
            switch(dir) {
                case 0: return 2; // Up -> Left
                case 1: return 3; // Down -> Right
                case 2: return 0; // Left -> Up
                case 3: return 1; // Right -> Down
            }
        }
        return dir;
    }

    public static int maxLightLoop(int M, int N, char[][] grid) {
        int maxLoopLength = 0;

        for (int i=0;i<M;i++) {
            for (int j=0;j<N;j++) {
                if (grid[i][j] == '0') continue;

                for (int d=0; d<4; d++) {
                    List<State> visitedList = new ArrayList<>();
                    Set<State> visitedSet = new HashSet<>();
                    int x=i, y=j, dir=d;

                    while (true) {
                        State state = new State(x, y, dir);
                        if (visitedSet.contains(state)) {
                            int idx = visitedList.indexOf(state);
                            int loopLength = visitedList.size() - idx;
                            maxLoopLength = Math.max(maxLoopLength, loopLength);
                            break;
                        }

                        visitedList.add(state);
                        visitedSet.add(state);

                        x += directions[dir][0];
                        y += directions[dir][1];

                        if (x<0 || x>=M || y<0 || y>=N) break;
                        if (grid[x][y] != '0') {
                            dir = changeDirection(grid[x][y], dir);
                        }
                    }
                }
            }
        }

        return maxLoopLength;
    }

    static class State {
        int x, y, dir;
        State(int x, int y, int dir) {
            this.x = x;
            this.y = y;
            this.dir = dir;
        }

        @Override
        public boolean equals(Object o) {
            if (this == o) return true;
            if (!(o instanceof State)) return false;
            State s = (State) o;
            return x == s.x && y == s.y && dir == s.dir;
        }

        @Override
        public int hashCode() {
            return Objects.hash(x, y, dir);
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int M = sc.nextInt();
        int N = sc.nextInt();
        sc.nextLine();

        char[][] grid = new char[M][N];
        for (int i=0;i<M;i++) {
            String[] parts = sc.nextLine().split(" ");
            for (int j=0;j<N;j++) {
                grid[i][j] = parts[j].charAt(0);
            }
        }

        System.out.println(maxLightLoop(M, N, grid));
    }
}
