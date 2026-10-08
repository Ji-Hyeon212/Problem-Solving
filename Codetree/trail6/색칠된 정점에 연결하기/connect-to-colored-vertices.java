import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.PriorityQueue;
import java.util.Scanner;
import java.util.StringTokenizer;
public class Main {
    static int N; // 정점
    static int M; // 간선
    static int K; // 색칠된 정점 수
    static int[] colored;
    static ArrayList<Edge>[] graph;
    static boolean[] visited;

    static class Edge implements Comparable<Edge>{
        int to;
        int weight;
        
        Edge (int to, int weight){
            this.to = to;
            this.weight = weight;
        }

        public int compareTo(Edge e){
            return Integer.compare(this.weight, e.weight);
        }
    }

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine());
        
        PriorityQueue<Edge> pq = new PriorityQueue<>();
        colored = new int[K];
        for(int i=0; i < K; i++){
            colored[i] = Integer.parseInt(st.nextToken());
            pq.offer(new Edge(colored[i], 0));
        }
        //그래프 초기화
        graph = new ArrayList[N+1];
        for (int i=1; i<=N; i++){
            graph[i] = new ArrayList<Edge>();
        }
        
        for(int i=0; i<M; i++){
            st = new StringTokenizer(br.readLine());

            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int w = Integer.parseInt(st.nextToken());

            graph[a].add(new Edge(b, w));
            graph[b].add(new Edge(a, w));
        }

        visited = new boolean[N+1];
        
        int total = 0;
        int cnt = 0;

        while(!pq.isEmpty()){
            Edge cur = pq.poll();
            int now = cur.to;
            int weight = cur.weight;

            if(visited[now]) continue;
            if(cnt == N) break;

            visited[now] = true;
            total += weight;
            cnt ++;

            for(Edge next: graph[now]){
                if(!visited[next.to]){
                    pq.offer(new Edge(next.to, next.weight));
                }
            }
        }
        System.out.print(total);
    }
}