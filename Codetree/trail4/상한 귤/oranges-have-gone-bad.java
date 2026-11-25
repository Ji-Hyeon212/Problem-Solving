import java.io.*;
import java.util.*;

class Point {
    int r, c;
    Point (int r, int c){
        this.r = r;
        this.c = c;
    }
}

public class Main {
    static int N, K;
    static int[][] tans;
    static Queue<Point> rottens;
    static boolean[][] visited;
    static int[] dr = {-1,0,1,0};
    static int[] dc = {0,1,0,-1};
    
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken()); //
        K = Integer.parseInt(st.nextToken()); //썩은 개수
        tans = new int[N][N];
        rottens = new ArrayDeque<>();        
        visited = new boolean[N][N];

        for (int r = 0; r < N; r++){
            st = new StringTokenizer(br.readLine());
            for (int c = 0; c < N; c++){
                tans[r][c] = Integer.parseInt(st.nextToken());
                if(tans[r][c]==2){
                    rottens.offer(new Point(r, c));
                    visited[r][c] = true;
                    tans[r][c] = 0;
                }
            }
        }
        while(!rottens.isEmpty()){
            Point curr = rottens.poll();

            for (int i = 0; i < 4; i++){
                int nr = curr.r + dr[i];
                int nc = curr.c + dc[i];

                if(nr<0 || nr>=N || nc<0 || nc>=N) continue;
                if(visited[nr][nc]) continue;
                if(tans[nr][nc]==0){
                    tans[nr][nc]=-1;
                    visited[nr][nc] = true;
                    continue;
                }
                tans[nr][nc] = tans[curr.r][curr.c] + 1;
                visited[nr][nc] = true;
                rottens.offer(new Point(nr, nc));
            }
        }
        //끝까지 visited 아니면 -2
        for (int r = 0; r<N; r++){
            for (int c = 0; c<N; c++){
                if(!visited[r][c] ){
                    if(tans[r][c]==0){
                        tans[r][c] = -1;
                    } else{
                        tans[r][c] = -2;
                    }
                }

                System.out.print(tans[r][c]+ " ");
            }
            System.out.println();
        }

    }
}