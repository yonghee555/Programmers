class Solution {
    String[] weekday = {"SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"};
    int[] dayOfMonth = {31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
    public String solution(int a, int b) {
        int day = b;
        for (int i = 0; i < a - 1; i++) {
            day += dayOfMonth[i];
        }
        String answer = weekday[(day + 4) % 7];
        return answer;
    }
}