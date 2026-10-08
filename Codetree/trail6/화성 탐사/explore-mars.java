import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
    static int[][] grid;
    static int N;
    
    static ArrayList<Point> bases = new ArrayList<>();
    static ArrayList<Edge> edges = new ArrayList<>();
    
    static int[] parent;
    
    static int[] dr = {-1, 1, 0, 0};
    static int[] dc = {0, 0, -1, 1};
    
    static class Point {
        int r;
        int c;
        Point (int r, int c){
            this.r = r;
            this.c = c;
        }
    }
    
    static class Edge implements Comparable<Edge>{
        int from;
        int to;
        int weight;
        Edge (int from, int to, int weight) {
            this.from = from;
            this.to = to;
            this.weight = weight;
        }
        public int compareTo(Edge e) {
            return Integer.compare(this.weight, e.weight);
        }
    }
    
    public static void main(String[] args) throws NumberFormatException, IOException {
        // TODO Auto-generated method stub
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        grid = new int[N][N];
        
        // 격자 입력, 기지 그래프 생성
        for (int r = 0; r < N; r++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int c = 0; c < N; c++) {
                grid[r][c] = Integer.parseInt(st.nextToken());
                
                if(grid[r][c] == 1|| grid[r][c] == 2) {
                    bases.add(new Point(r, c));
                }
            }
        }
        int K = bases.size(); // 노드 개수
        
        // 기지 그래프에서 bfs로 거리 간선 생성
        for (int i = 0; i < K; i++) {
            Point start = bases.get(i);
            int[][] dist = bfs(start.r, start.c);
            for (int j = i+1; j<K; j++) {
                Point target = bases.get(j);
                int distance = dist[target.r][target.c];
                if (distance != -1) {
                    edges.add(new Edge(i, j, distance));
                }
            }
        }
        Collections.sort(edges);
        parent = new int[K];
        // parent 초기화
        for (int i = 0; i < K; i++) {
            parent[i] = i;
        }
        
        // 크루스칼
        int answer = 0;
        int cnt = 0;
        
        for (Edge edge : edges) {
            if (find(edge.from) != find(edge.to)) {

                union(edge.from, edge.to);

                answer += edge.weight;
                cnt++;

                if (cnt == K - 1) {
                    break;
                }
            }
        }
        
        // 결과 출력
        if (cnt == K - 1) {
            System.out.println(answer);
        } else {
            System.out.println(-1);
        }
    }
    
    // 시작 기지에서 모든 칸 까지의 최단 거리
    static int[][] bfs(int sr, int sc) {
        int[][] dist = new int[N][N];
        
        for (int i = 0; i < N; i++) {
            Arrays.fill(dist[i], -1);
        }
        
        Queue<Point> q = new ArrayDeque<>();
        
        q.offer(new Point(sr, sc));
        dist[sr][sc] = 0;
        
        while(!q.isEmpty()) {
            Point cur = q.poll();
            
            for (int i = 0; i < 4; i++) {
                int nr = cur.r + dr[i];
                int nc = cur.c + dc[i];
                
                if (nr < 0 || nr >= N || nc < 0 || nc >= N) {
                    continue;
                }
                
                if (grid[nr][nc] == -1) {
                    continue;
                }
                
                if (dist[nr][nc] != -1) {
                    continue;
                }
                
                dist[nr][nc] = dist[cur.r][cur.c] + 1;
                q.offer(new Point(nr, nc));
            }
        }
        
        return dist;
    }
    
    //union-find
    static int find(int x) {

        if (parent[x] != x) {
            parent[x] = find(parent[x]);
        }

        return parent[x];
    }

    // Union-Find
    static void union(int a, int b) {

        int rootA = find(a);
        int rootB = find(b);

        if (rootA != rootB) {
            parent[rootB] = rootA;
        }
    }
}
