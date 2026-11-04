import java.util.*;
import java.io.*;

public class Main {

    static class Point{
        int r, c;
        public Point(int r, int c){
            this.r = r;
            this.c = c;
        }
    }
    static int[] dr = {-1, 1, 0, 0};
    static int[] dc = {0, 0, -1, 1};

    static int N, M;
    static int[][] map;
    static boolean[][] visited;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        map = new int[N][M];
        int totalIce = 0;

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());

            for (int j = 0; j < M; j++) {
                map[i][j] = Integer.parseInt(st.nextToken());

                if (map[i][j] == 1) {
                    totalIce++;
                }
            }
        }

        int time = 0;
        int lastMelt = 0;

        while (totalIce > 0) {
            int melted = melt();

            totalIce -= melted;
            lastMelt = melted;
            time++;
        }

        System.out.println(time + " " + lastMelt);
    }

    static int melt() {
        visited = new boolean[N][M];

        Queue<Point> q = new ArrayDeque<>();
        ArrayList<Point> meltList = new ArrayList<>();

        q.offer(new Point(0, 0));
        visited[0][0] = true;

        while (!q.isEmpty()) {
            Point cur = q.poll();

            for (int d = 0; d < 4; d++) {
                int nr = cur.r + dr[d];
                int nc = cur.c + dc[d];

                if (nr < 0 || nr >= N ||
                    nc < 0 || nc >= M) {
                    continue;
                }

                if (visited[nr][nc]) {
                    continue;
                }

                visited[nr][nc] = true;

                if (map[nr][nc] == 1) {
                    meltList.add(new Point(nr, nc));
                } else {
                    q.offer(new Point(nr, nc));
                }
            }
        }

        for (Point p : meltList) {
            map[p.r][p.c] = 0;
        }

        return meltList.size();
    }
}