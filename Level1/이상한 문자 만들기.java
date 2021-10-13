class Solution {
    public String solution(String s) {
        char[] sarr = s.toCharArray();
        int idx = 0;
        for (int i = 0; i < sarr.length; i++) {
            if (sarr[i] == ' ') {
                idx = 0;
                continue;
            }
            if (idx % 2 == 0) {
                sarr[i] = Character.toUpperCase(sarr[i]);
            }
            else {
                sarr[i] = Character.toLowerCase(sarr[i]);
            }
            idx += 1;
        }
        String answer = new String(sarr);
        return answer;
    }
}