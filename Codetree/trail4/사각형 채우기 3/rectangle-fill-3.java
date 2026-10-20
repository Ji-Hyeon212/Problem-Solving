import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;
public class Main {
    static long[][] dp;
    static final long MOD = 1000000007L;

    public static void main(String[] args) throws IOException {
        
        // Please write your code here.
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        dp = new long [N+1][3];
        dp[0][0] = 1;
        if (N>=1){
            dp[1][0] = 2;
            dp[1][1] = 1;
            dp[1][2] = 1;
        }
        for(int n = 2; n <= N; n++){
            dp[n][0] = (2 * dp[n-1][0] + dp[n-2][0] + dp[n-1][1] + dp[n-1][2])%MOD;
            dp[n][1] = (dp[n-1][0] + dp[n-1][2])%MOD;
            dp[n][2] = (dp[n-1][0] + dp[n-1][1])%MOD;
        }
        long answer = dp[N][0]%MOD;
        System.out.println(answer);
    }
}