class Solution {
    public int[] solution(long n) {
        String s = Long.toString(n);
        StringBuffer sBuffer = new StringBuffer(s);
        String[] strings = sBuffer.reverse().toString().split("");
        int[] answer = new int[strings.length];
        for (int i = 0; i < strings.length; i++) {
            answer[i] = Integer.parseInt(strings[i]);
        }
        return answer;
    }
}