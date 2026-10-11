

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    static int parent[];
    public static void main(String[] args) throws IOException {
        // TODO Auto-generated method stub
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        
        parent = new int[N+1];
        Arrays.fill(parent, -1);
        
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            String opp = st.nextToken();
            int a = Integer.parseInt(st.nextToken());
            
            if (opp.equals("x")) {
                int b = Integer.parseInt(st.nextToken());
                union(a, b);
            } else if(opp.equals("y")) {
                System.out.println(-parent[find(a)]);
            }
        }
    }
    
    static void union(int a, int b) {
        int rootA = find(a);
        int rootB = find(b);
        
        if (rootA == rootB) return;
        
        if(parent[rootA] > parent[rootB]) {
            int temp = rootA;
            rootA = rootB;
            rootB = temp;
        }
        
        parent[rootA] += parent[rootB];
        parent[rootB] = rootA;
    }

    static int find(int x) {
        if (parent[x] < 0) {
            return x;
        }
        return parent[x] = find(parent[x]);
    }
}