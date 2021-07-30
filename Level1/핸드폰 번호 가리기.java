class Solution {
    public String solution(String phone_number) {
        int size = phone_number.length();
        String answer = "";
        for (int i = 0; i < size - 4; i++) {
            answer += "*";
        }
        answer += phone_number.substring(size - 4, size);
        return answer;
    }
}