import java.util.Scanner;

public class Main {
    static int[] parent;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();

        parent = new int[n+1];
        for(int j=0; j<=n; j++){
            parent[j] = j;
        }

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
        int rootA = find(a);
        int rootB = find(b);

        if(rootA != rootB) parent[rootB] = rootA;
    }
    static int find(int x){
        if (parent[x] == x){
            return x;
        }
        return parent[x] = find(parent[x]);
    }
}