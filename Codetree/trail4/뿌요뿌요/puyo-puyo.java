import java.util.ArrayDeque;
import java.util.Queue;
import java.util.Scanner;

public class Main {
    static int n;
    static int[][] grid;
    static boolean[][] visited;
    static int maxSize = 0;
    static int boomBlock = 0;

    static int[] dc = new int [] {0, 1, 0, -1};
    static int[] dr = new int [] {-1, 0, 1, 0};

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        grid = new int[n][n];
        visited = new boolean[n][n];
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                grid[i][j] = sc.nextInt();

        // Please write your code here.

        for(int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++){
                if (!visited[i][j]){
                    int blockSize = bfs(i, j);
                    if (blockSize >= 4) {
                        boomBlock++;
                    }
                    maxSize = Math.max(maxSize, blockSize);
                }
            }
        }

        System.out.print(boomBlock + " " + maxSize);
    }

    static int bfs(int r, int c){
        Queue<int[]> q= new ArrayDeque<>();
        q.offer(new int[]{r, c});
        visited[r][c] = true;

        int blockSize = 1;

        while(!q.isEmpty()){
            int[] curr = q.poll();

            for (int i = 0; i < 4; i++){
                int nr = curr[0] + dr[i];
                int nc = curr[1] + dc[i];
                if (nr<0 || nr>=n || nc < 0 || nc >= n) continue;
                if (visited[nr][nc]) continue;
                if (grid[r][c] != grid[nr][nc]) continue;

                visited[nr][nc] = true;
                q.offer(new int[]{nr, nc});
                blockSize++;
            }
        }

        return blockSize;
    }
}

/*
터지게 되는 블럭 개수, 가장 큰 블럭의 크기
*/