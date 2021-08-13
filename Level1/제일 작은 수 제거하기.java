class Solution {
    public int[] solution(int[] arr) {
        int j = arr.length;
        if (j == 1)
            return (new int[] {-1});
        int[] answer = new int[j - 1];
        int min = 0;
        for (int i = 0; i < j; i++) {
            if (arr[i] < arr[min])
                min = i;
        }
        for (int i = 0; i < j - 1; i++) {
            if (i >= min)
                answer[i] = arr[i + 1];
            else
                answer[i] = arr[i];
        }
        return answer;
    }
}