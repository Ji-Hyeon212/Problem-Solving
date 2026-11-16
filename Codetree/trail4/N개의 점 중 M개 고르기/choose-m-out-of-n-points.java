import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Scanner;
import java.util.StringTokenizer;

public class Main {
    static int N, M;
    static int[][] points;
    static int[][] dist;
    static int[] selected;
    static int answer = Integer.MAX_VALUE;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        points = new int[N][2];
        dist = new int[N][N];
        selected = new int[M];

        for (int i = 0; i < N; i++){
            st = new StringTokenizer(br.readLine());
            points[i][0] = Integer.parseInt(st.nextToken());
            points[i][1] = Integer.parseInt(st.nextToken());
        }

        //모든 점 사이의 거리 계산
        for (int i = 0; i < N; i++){
            for (int j = i+1; j < N; j++){
                int dx = points[i][0] - points[j][0];
                int dy = points[i][1] - points[j][1];

                dist[i][j] = dx*dx + dy*dy;
                dist[j][i] = dist[i][j];
            }
        }
        dfs(0, 0, 0);
        System.out.println(answer);
    }

    static void dfs(int start, int depth, int maxDist){
        if(depth==M){
            answer = Math.min(answer, maxDist);
            return;
        }
        for (int i = start; i <= N - (M - depth); i++){
            int nextMax = maxDist;
            for (int j = 0; j < depth; j++){
                nextMax = Math.max(nextMax, dist[i][selected[j]]);
            }
            if(nextMax >= answer) continue;

            selected[depth] = i;
            dfs(i+1, depth + 1, nextMax);
        }
    }
}
