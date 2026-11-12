import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Map;
import java.util.TreeMap;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        TreeMap<String, Integer> counts = new TreeMap<>();

        for (int i = 0; i < n; i++) {
            String word = br.readLine();
            counts.put(word, counts.getOrDefault(word, 0) + 1);
        }

        StringBuilder sb = new StringBuilder();

        for (Map.Entry<String, Integer> entry : counts.entrySet()) {
            sb.append(entry.getKey())
              .append(' ')
              .append(entry.getValue())
              .append('\n');
        }

        System.out.print(sb);
    }
}