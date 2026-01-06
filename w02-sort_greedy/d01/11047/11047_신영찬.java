import java.io.*;
import java.util.*;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());

        //TODO : 데이터 파싱
        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        List<Integer> coins = new ArrayList<>();

        for (int i = 0; i < N; i++) {
            coins.add(Integer.parseInt(br.readLine()));
        }

        //TODO : 내림차순 정렬
        Collections.reverse(coins);

        //TODO : 가치 계산
        int currentValue = 0;
        int i = 0;
        int answer = 0;
        while (currentValue != K) {
            if (currentValue + coins.get(i) > K) {
                i++;
            } else {
                currentValue += coins.get(i);
                answer += 1;
            }
        }
        bw.write(String.valueOf(answer));
        bw.flush();
        br.close();
    }
}