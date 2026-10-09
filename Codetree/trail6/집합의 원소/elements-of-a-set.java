import java.util.Arrays;
import java.util.Scanner;

public class Main {
    static int[] parent;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();

        parent = new int[n+1];
        Arrays.fill(parent, -1);

        for (int i = 0; i < m; i++) {
            int qType = sc.nextInt();
            int a = sc.nextInt();
            int b = sc.nextInt();
            // Please write your code here.

            if (qType == 0){
                union(a, b);
            } else if (qType == 1){
                if (find(a) == find(b)){
                    System.out.println(1);
                } else {
                    System.out.println(0);
                }
            }
        }
    }
    static void union(int a, int b){
        int rootA = find(a); // 대표노드
        int rootB = find(b); // 대표노드

        if (rootA == rootB) return; // 이미 같은 집합이면 패스

        if (parent[rootA] > parent[rootB]){ 
            int temp = rootA;
            rootA = rootB;
            rootB = temp;
        }

        parent[rootA] += parent[rootB]; // 다른 집합의 모든 원소를 끌어모음
        parent[rootB] = rootA;
    }
    static int find(int x){
        if (parent[x] < 0){
            return x;
        }
        return parent[x] = find(parent[x]);
    }
}