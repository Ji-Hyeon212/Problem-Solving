
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    static int[] parent;
    public static void main(String[] args) throws NumberFormatException, IOException {
        // TODO Auto-generated method stub
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        parent = new int[N+1];
        Arrays.fill(parent, -1);
        
        for (int i = 0; i < N-2; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());

            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            
            union(a, b);
        }
        // 사전순이므로 정점 하나는 1, 나머지 정점 중 1과 다른 집합에 든 정점 하나만 찾으면 됨.
        for (int i = 2; i < N+1; i++) {
            if (find(i)!=find(1)) {
                System.out.println(1 + " " + i);
                break;
            }
        }
    }

    static void union(int a, int b) {
        int rootA = find(a);
        int rootB = find(b);
        
        if (rootA == rootB) return;
        
        if (parent[rootA] > parent[rootB]) {
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
