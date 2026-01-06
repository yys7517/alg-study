import java.io.*;
import java.util.*;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        //TODO : 배열 만들어서 add
        int[] brr = new int[10001];
        String nextLine = br.readLine();
        while (nextLine != null) {
            brr[Integer.parseInt(nextLine)] += 1;
            nextLine = br.readLine();
        }

        //TODO : 배열 출력
        for (int i = 0; i < 10001; i++) {
            if (brr[i] != 0) {
                for (int j = 0; j < brr[i]; j++) {
                    bw.write(String.valueOf(i) + '\n');
                }
            }
        }
        bw.flush();
        br.close();
    }
}