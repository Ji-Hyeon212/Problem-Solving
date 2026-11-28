import java.io.*;
import java.util.*;
public class Main {

    static class Point {
        int r, c;
        Point (int r, int c){
            this.r = r;
            this.c = c;
        }
    }

    static int N, K, M;
    static int[][] grid;
    static int[][] removed_grid;
    static Point[] startPoints;
    static ArrayList<Point> stones; // 입력 받은 돌
    static Point[] selected; // 선택된 돌
    static int stoneCount; // 입력 받은 돌 개수
    static int answer;
    static int[] dr = {-1, 0, 1, 0};
    static int[] dc = {0, 1, 0, -1};

    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        // Please write your code here.
        N = Integer.parseInt(st.nextToken()); // 격자 크기
        K = Integer.parseInt(st.nextToken()); // 시작점 개수
        M = Integer.parseInt(st.nextToken()); // 치울 돌 개수

        grid = new int[N+1][N+1];
        removed_grid = new int[N+1][N+1];
        startPoints = new Point[K];
        stones = new ArrayList<>();
        selected = new Point[M];
        answer = 0;
        
        for (int r = 1; r <= N; r++){
            st = new StringTokenizer(br.readLine());
            for (int c = 1; c <= N; c++){
                grid[r][c] = Integer.parseInt(st.nextToken());
                removed_grid[r][c] = grid[r][c];
                if(grid[r][c] == 1) {
                    stoneCount++;
                    stones.add(new Point(r, c));
                }
            }
        }
        for (int i = 0; i < K; i++){
            st = new StringTokenizer(br.readLine());
            int r = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());
            startPoints[i] = new Point(r, c);
        }
        select(0, 0);
        System.out.println(answer);
    }

    static void select(int idxStone, int depth){ // 치울 돌 고르기. 돌 고를 때는 stones[idxStone].r, c
        if (depth == M){
            //선택한 돌 칸은 0으로 만들고 해당 격자로 bfs
            for(int i = 0; i < depth; i++){
                removed_grid[selected[i].r][selected[i].c] = 0;
            }
            int count = bfs();
            answer = Math.max(answer, count);

            for(int i = 0; i < depth; i++){
                removed_grid[selected[i].r][selected[i].c] = 1;
            }
            return;
        }
        for (int i = idxStone; i < stoneCount; i++){
            selected[depth] = stones.get(i);
            select(i+1, depth+1);
        }
    }

    static int bfs(){
        boolean[][] visited = new boolean[N+1][N+1];
        Queue<Point> q = new ArrayDeque<>();
        int count = K;
        //시작점 모두 큐에 넣기
        for (int i = 0; i < K; i++){
            q.offer(startPoints[i]);
            visited[startPoints[i].r][startPoints[i].c] = true;
        }

        while(!q.isEmpty()){
            Point curr = q.poll();
            int r = curr.r;
            int c = curr.c;
            for(int i = 0; i < 4; i++){
                int nextR = curr.r + dr[i];
                int nextC = curr.c + dc[i];
                if (nextR <=0 || nextR > N || nextC <= 0 || nextC > N ) continue;
                if (visited[nextR][nextC]) continue;
                if (removed_grid[nextR][nextC] == 1) continue;

                q.offer(new Point(nextR, nextC));
                visited[nextR][nextC] = true;
                count++;
            }
        }
        return count;
    }
}

/*
격자 인덱스 1부터
자기자신도 포함
돌 최대 8개. 중 M개 선택
시작점을 모두 큐에 넣고 bfs
*/