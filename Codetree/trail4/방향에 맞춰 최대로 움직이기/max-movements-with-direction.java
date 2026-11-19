import java.util.Scanner;
public class Main {
    static int n, r, c;
    static int[][] num;
    static int[][] moveDir;
    static int[] dx = new int[] {0, 0, 1, 1, 1, 0, -1, -1, -1};
    static int[] dy = new int[] {0, -1, -1, 0, 1, 1, 1, 0, -1};

    static int count = 0;
    static int answer = 0;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt(); // 격자의 크기
        num = new int[n+1][n+1]; // 격자
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n; j++) {
                num[i][j] = sc.nextInt();
            }
        }
        moveDir = new int[n+1][n+1];
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n; j++) {
                moveDir[i][j] = sc.nextInt();
            }
        }
        r = sc.nextInt(); // 시작지점
        c = sc.nextInt(); // 시작지점
        // Please write your code here.
        dfs(r, c, 0);
        System.out.println(answer);
    }
    static void dfs(int r, int c, int count){
        answer = Math.max(answer, count);

        int nextR = r + dy[moveDir[r][c]]; 
        int nextC = c + dx[moveDir[r][c]];

        while(nextR >= 1  && nextR <= n && nextC >= 1 && nextC <= n ){
            // 지금 값보다 큰수이면?
            if (num[nextR][nextC] > num[r][c]){
                dfs(nextR, nextC, count+1);
            }
            // 작은 수가 나오면 그 다음
            nextR += dy[moveDir[r][c]];
            nextC += dx[moveDir[r][c]];
        }
    }
}


/*
방향에 맞으면서 지금 값보다 큰수로만 이동
이 방향 숫자 중에 가장 큰 걸 구할 필요는 있나
N이 작음
moveDir[r][c] 방향으로 
dx[moveDir[r][c]], dy[moveDir[r][c]]로 계속 이동
이동할 수 있는 최대 횟수 구하기
r, c 인덱스 1부터 N
*/