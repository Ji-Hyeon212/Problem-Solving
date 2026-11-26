import java.util.*;

public class Main {
    static int N;
    static int[] steps;
    static int answer;
    static int MAX;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        // Please write your code here.
        MAX = 2 * N;
        steps = new int[2*N+1];
        Arrays.fill(steps, -1);
        System.out.print(bfs(N));
    }

    static int bfs(int n){ // n은 현재 숫자
        Queue<Integer> q = new ArrayDeque<>();
        q.offer(n);
        steps[n] = 0; //출발점
        while(!q.isEmpty()){
            int curr = q.poll();
            if (curr == 1) return steps[curr]; // N이 1인 경우 처리ㅏ
            
            int[] nexts = {
                curr -1, curr+1, curr%2 == 0 ? curr/2 : curr, curr%3 == 0 ? curr/3 : curr
            };
            
            for(int next: nexts){
                if (next<1 || next> MAX) continue;
                if (steps[next] != -1) continue; // -1 이 아니면 이미 방문한 숫자.

                steps[next] = steps[curr]+ 1;

                q.offer(next);
            }
        }
        return -1;
    }
}

/*
    주어진 사칙 연산으로 bfs를 돌려서 가장 먼저 1이 나오는 경우의 연산 횟수 출력
    최대 범위가 어디까지지? +1 연산을 어디까지 가능? -> 2*N까지?
*/