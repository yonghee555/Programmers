class Solution {
    public double solution(int[] arr) {
        int size = arr.length;
        double answer = 0;
        for (int i = 0; i < size; i++) {
            answer += arr[i];
        }
        answer /= size;
        return answer;
    }
}