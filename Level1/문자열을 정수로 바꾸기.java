class Solution {
    public int solution(String s) {
        int answer = 0;
        boolean isMinus = false;
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (i == 0) {
                if (c == '-') {
                    isMinus = true;
                    continue;
                }
                else if (c == '+') {
                    continue;
                }
            }
            answer *= 10;
            answer += (c - '0');
        }
        if (isMinus)
            answer *= -1;
        return answer;
    }
}