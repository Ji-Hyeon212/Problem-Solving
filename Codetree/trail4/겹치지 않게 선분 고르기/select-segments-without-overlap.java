import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Scanner;
import java.util.StringTokenizer;

public class Main {

    static class Line {
        int left, right;
        Line(int left, int right){
            this.left = left;
            this.right = right;
        }
    }

    static int N;
    static int answer;
    static int L, R;
    static Line[] lines;
    static boolean[] selected;

    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine()); //선분 개수
        answer = 0; //뽑을 수 있는 최대 선분 수
        lines = new Line[N];
        selected = new boolean[N];

        for (int i = 0; i < N; i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            L = Integer.parseInt(st.nextToken());
            R = Integer.parseInt(st.nextToken());
            lines[i] = new Line(L, R);
        }
        dfs(0, 0);
        System.out.println(answer);
    }

    static void dfs(int start, int count){
        answer = Math.max(answer, count);
        
        for (int i = start; i < N; i++){
            if(!canSelect(i)) continue;

            selected[i] = true;
            dfs(i+1, count +1);
            selected[i] = false;
        }
    }

    static boolean canSelect(int idx) {
        Line current = lines[idx];
        for (int i = 0; i < N; i++){
            if(!selected[i]) continue;

            Line prev = lines[i];

            if(current.right < prev.left || current.left > prev.right) continue;

            return false;
        }
        return true;
    }
}

/*
최대 N 개까지 고를 수 있음. 
경우의 수: nC1 + nC2 + ... + nCn n이 15니까 ...될듯? 시그마 조합 모든 경우 -> 2^N
선분 인덱스로 모든 조합 구성
선분 조합 중에 겹치는 게 생기면 가지치기
최대 선분 개수 갱신
[시간 복잡도]
조합 탐색: O(2^N)
겹침 검사: O(N)
전체: O(N * 2^N)
*/