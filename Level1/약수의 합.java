class Solution {
    public int solution(int n) {
        int answer = 0;
        int j = (int)Math.sqrt((double)n);
        for (int i = 1; i <= j; i++) {
            if (n % i == 0) {
                if (i * i == n) {
                    answer += i;
                    break;
                }
                answer += i + n / i;
            }
        }
        return answer;
    }
}