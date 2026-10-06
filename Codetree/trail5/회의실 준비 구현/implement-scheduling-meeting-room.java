
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    static class Meeting implements Comparable<Meeting> {
        int start;
        int end;
        
        Meeting (int start, int end){
            this.start = start;
            this.end = end;
        }
        
        public int compareTo (Meeting o) {
            if (this.end == o.end) {
                return Integer.compare(this.start, o.start);
            }
            return Integer.compare(this.end, o.end);
        }
    }
    
    public static void main(String[] args) throws IOException {
        // TODO Auto-generated method stub
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        Meeting[] meetings = new Meeting[N];
        
        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int start = Integer.parseInt(st.nextToken());
            int end = Integer.parseInt(st.nextToken());
            meetings[i] = new Meeting(start, end);
        }
        Arrays.sort(meetings);
        
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
