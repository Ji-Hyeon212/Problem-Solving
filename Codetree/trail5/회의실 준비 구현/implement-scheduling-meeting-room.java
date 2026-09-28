import java.io.*;
import java.util.*;

public class Main {

    static class Meeting {
        int start;
        int end;

        Meeting(int start, int end) {
            this.start = start;
            this.end = end;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());

        Meeting[] meetings = new Meeting[N];

        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());

            int start = Integer.parseInt(st.nextToken());
            int end = Integer.parseInt(st.nextToken());

            meetings[i] = new Meeting(start, end);
        }

        // 종료 시간이 빠른 순
        // 종료 시간이 같으면 시작 시간이 빠른 순
        Arrays.sort(meetings, (a, b) -> {
            if (a.end == b.end) {
                return Integer.compare(a.start, b.start);
            }
            return Integer.compare(a.end, b.end);
        });

        int count = 0;
        int endTime = 0;

        for (Meeting meeting : meetings) {
            if (meeting.start >= endTime) {
                count++;
                endTime = meeting.end;
            }
        }

        System.out.println(count);
    }
}