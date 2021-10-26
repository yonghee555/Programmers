import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        ArrayList<Integer> new_arr = new ArrayList<Integer>();
        new_arr.add(arr[0]);
        for (int i = 1; i < arr.length; i++) {
            if (arr[i] != arr[i - 1])
                new_arr.add(arr[i]);
        }
        int[] answer = new int[new_arr.size()];
        for (int i = 0; i < answer.length; i++) {
            answer[i] = new_arr.get(i);
        }
        return answer;
    }
}