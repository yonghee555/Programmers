import java.util.Arrays;
import java.util.Collections;

class Solution {
    public long solution(long n) {
        String[] array = String.valueOf(n).split("");
        Arrays.sort(array, Collections.reverseOrder());

        StringBuilder sb = new StringBuilder();
        for (String a: array) {
            sb.append(a);
        }
        long answer = Long.parseLong(sb.toString());
        return answer;
    }
}