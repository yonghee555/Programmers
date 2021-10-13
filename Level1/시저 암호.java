class Solution {
    public String solution(String s, int n) {
        char[] sarr = s.toCharArray();
        for (int i = 0; i < sarr.length; i++) {
            char c = sarr[i];
            if (c >= 'A' && c <= 'Z') {
                sarr[i] = (char)('A' + ((int)(c - 'A') + n) % 26);
            }
            else if (c >= 'a' && c <= 'z') {
                sarr[i] = (char)('a' + ((int)(c - 'a') + n) % 26);
            }
        }
        String answer = new String(sarr);
        return answer;
    }
}