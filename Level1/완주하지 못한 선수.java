import java.util.HashMap;

class Solution {
    public String solution(String[] participant, String[] completion) {
        String answer = "";
        HashMap<String, Integer> hashMap = new HashMap<>();
        for (String c: completion) {
            if (hashMap.get(c) == null) {
                hashMap.put(c, 1);
            }
            else {
                int i = hashMap.get(c) + 1;
                hashMap.put(c, i);
            }
        }

        for (String p: participant) {
            if (hashMap.get(p) == null ) {
                answer = p;
                break;
            }
            if (hashMap.get(p) == 0) {
                answer = p;
                break;
            }
            else {
                int i = hashMap.get(p) - 1;
                hashMap.put(p, i);
            }
        }
        return answer;
    }
}