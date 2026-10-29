import java.io.*;
import java.util.*;

public class Main {
    static int N, M;
    static int[][] grid;

    static int[] dr = {-1, 1, 0, 0};
    static int[] dc = {0, 0, -1, 1};

    static class Module {
        int mask;
        int score;

        Module(int mask, int score) {
            this.mask = mask;
            this.score = score;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(
                new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        grid = new int[N][M];

        for (int r = 0; r < N; r++) {
            st = new StringTokenizer(br.readLine());
            for (int c = 0; c < M; c++) {
                grid[r][c] = Integer.parseInt(st.nextToken());
            }
        }

        // 1. 가능한 모듈 모두 생성
        ArrayList<Module> modules = generateModules();

        // 2. 두 모듈을 선택해 최댓값 탐색
        int answer = findMaxEfficiency(modules);

        System.out.println(answer);
    }

    // 1. 펜타 모듈
    static ArrayList<Module> generateModules() {
        ArrayList<Module> modules = new ArrayList<>();
        int size = N * M;

        for (int mask = 0; mask < (1 << size); mask++) {

            // 5칸 선택했는지 검사
            if (Integer.bitCount(mask) != 5) {
                continue;
            }

            // 5칸이 모두 연결되어 있는지 검사
            if (!isConnected(mask)) {
                continue;
            }

            int score = calculateScore(mask);
            modules.add(new Module(mask, score));
        }

        return modules;
    }

    // 2. BFS로 연결 여부 확인
    static boolean isConnected(int mask) {
        Queue<Integer> queue = new ArrayDeque<>();

        int start = Integer.numberOfTrailingZeros(mask);

        int visitedMask = (1 << start);
        queue.offer(start);

        while (!queue.isEmpty()) {
            int cur = queue.poll();

            int r = cur / M;
            int c = cur % M;

            for (int d = 0; d < 4; d++) {
                int nr = r + dr[d];
                int nc = c + dc[d];

                int next = nr * M + nc;
                int bit = (1 << next);

                if(nr < 0 || nr >= N || nc < 0 || nc >= M){
                    continue;
                }
                if ((mask & bit) == 0) {
                    continue;
                }

                if ((visitedMask & bit) != 0) {
                    continue;
                }

                visitedMask |= bit;
                queue.offer(next);
            }
        }

        return visitedMask == mask;
    }

    // 3. 모듈의 에너지 합 계산
    static int calculateScore(int mask) {
        int sum = 0;

        for (int i = 0; i < N * M; i++) {
            if ((mask & (1 << i)) != 0) {
                int r = i / M;
                int c = i % M;

                sum += grid[r][c];
            }
        }

        return sum;
    }

    // 4. 두 모듈의 조합으로 최대 효율 계산
    static int findMaxEfficiency(ArrayList<Module> modules) {
        int answer = Integer.MIN_VALUE;

        for (int i = 0; i < modules.size(); i++) {
            Module a = modules.get(i);

            for (int j = i + 1; j < modules.size(); j++) {
                Module b = modules.get(j);

                // 두 모듈이 겹치는 칸
                int overlap = a.mask & b.mask;

                // 2칸 겹쳐야 함
                if (Integer.bitCount(overlap) != 2) {
                    continue;
                }

                // 겹치는 칸은 2번 더하기
                int total = a.score + b.score;
                answer = Math.max(answer, total);
            }
        }

        return answer;
    }
}

