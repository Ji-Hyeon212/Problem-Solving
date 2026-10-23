import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Queue;
import java.util.Scanner;
import java.util.StringTokenizer;
public class Main {
    static int N, M, K;
    static ArrayList<Integer>[] graph;
    static int[] maxDist;
    static int[] reachCount;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        N = Integer.parseInt(st.nextToken()); // 노드수
        M = Integer.parseInt(st.nextToken()); // 간선수
        K = Integer.parseInt(st.nextToken()); // 사람수
        graph = new ArrayList[N+1];
        maxDist = new int[N+1];
        reachCount = new int[N+1];
        //그래프 초기화
        for(int i = 1; i <= N; i++){
            graph[i] = new ArrayList<>();
        }
        // 그래프 생성
        for(int i = 0; i < M; i++){
            st = new StringTokenizer(br.readLine());
            int from = Integer.parseInt(st.nextToken());
            int to = Integer.parseInt(st.nextToken());
            graph[from].add(to);
        }
        // 사람 입력
        st = new StringTokenizer(br.readLine());
        for(int i = 0; i < K; i++){
            int start = Integer.parseInt(st.nextToken());
            bfs(start);
        }
        int answer = Integer.MAX_VALUE;

        for(int i = 1; i <= N; i++){
            if(reachCount[i] == K){
                answer = Math.min(answer, maxDist[i]);
            }
        }
        System.out.println(answer == Integer.MAX_VALUE ? -1: answer);
    }

    static void bfs(int start) {
        int[] dist = new int[N + 1];
        Arrays.fill(dist, -1);

        Queue<Integer> queue = new ArrayDeque<>();
        queue.offer(start);
        dist[start] = 0;

        while (!queue.isEmpty()) {
            int cur = queue.poll();

            // 현재 사람이 도달한 노드 정보 갱신
            reachCount[cur]++;
            maxDist[cur] = Math.max(maxDist[cur], dist[cur]);

            for (int next : graph[cur]) {
                if (dist[next] != -1) continue;

                dist[next] = dist[cur] + 1;
                queue.offer(next);
            }
        }
    }
}

// 모든 사람들이 지날 수 있는 노드 중 생각