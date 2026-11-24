import java.io.*;
import java.util.*;

public class Main {
    static int[][] grid;
    static int N, K, U, D;
    static int[] selected;
    static boolean[][] visited;
    static int answer = 0;

    static int[] dr = {-1, 0, 1, 0};
    static int[] dc = {0, 1, 0, -1};

    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());
        U = Integer.parseInt(st.nextToken());
        D = Integer.parseInt(st.nextToken());

        grid = new int[N][N];
        selected = new int[K];

        for(int r = 0; r < N; r++){
            st = new StringTokenizer(br.readLine());
            for (int c = 0; c < N; c++){
                grid[r][c] = Integer.parseInt(st.nextToken());
            }
        }

        select(0, 0);
        System.out.print(answer);
    }

    static void select(int start, int depth){
        if (depth == K){
            int count = bfs();
            answer = Math.max(answer, count);
            return;    
        }
        for (int i=start; i <N*N; i++){
            selected[depth] = i;
            select(i+1, depth+1);
        }
    }
    
    static int bfs(){ //지금 selected 조합으로 이동가능한 횟수 계산
        Queue<int[]> q = new ArrayDeque<>();
        visited = new boolean[N][N];
        int count = 0;
        //시작 도시들 큐에 넣기
        for (int i = 0; i < K; i++){
            int r = selected[i]/N;
            int c = selected[i]%N;

            q.offer(new int[]{r, c});
            visited[r][c] = true;
            //시작도시 포함
            count++;
        }
        while(!q.isEmpty()){
            int[] curr = q.poll();
            for (int i = 0; i <4; i++){
                int nr = curr[0] + dr[i];
                int nc = curr[1] + dc[i];

                if(nr < 0 || nr >= N || nc < 0 || nc >= N) continue;
                if(visited[nr][nc]) continue;

                int diff = Math.abs(grid[curr[0]][curr[1]] - grid[nr][nc]);
                if(diff > D || diff < U) continue;

                visited[nr][nc] = true;
                count++;
                q.offer(new int[]{nr, nc});
            }
        }
        return count;
    }
}
/*
N*N개의 도시에서 K개를 고름.
각 경우마다 도시 K_i에서 이동할 수 있는 도시 계산 U<=|dh|<=D
K개의 도시를 큐에 넣음.
각 구성마다 visited 초기화 해서 이동 가능한 도시 카운트
도시 개수 최대값 갱신
*/