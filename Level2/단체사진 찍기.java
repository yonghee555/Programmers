// 단체사진 찍기
// https://programmers.co.kr/learn/courses/30/lessons/1835

import java.util.HashMap;

class Solution {
    static boolean visited[];
    static HashMap<Character, Integer> friends;
    static int[] order;
    static int answer;

    public static int solution(int n, String[] data) {
        visited = new boolean[8];

        friends = new HashMap<>();
        friends.put('A', 0);
        friends.put('C', 1);
        friends.put('F', 2);
        friends.put('J', 3);
        friends.put('M', 4);
        friends.put('N', 5);
        friends.put('R', 6);
        friends.put('T', 7);
        
        order = new int[8];
        answer = 0;
        dfs(0, data);
        return answer;
    }

    public static void dfs (int i, String[] data) {
        if (i == 8) {
            if (check(data))
                answer++;
        }
        else {
            for (int j = 0; j < 8; j++) {
                if (visited[j] == false) {
                    visited[j] = true;
                    order[i] = j;
                    dfs(i + 1, data);
                    visited[j] = false;
                }
            }
        }
    }

    public static boolean check(String[] data) {
        int f1, f2, dist;
        char op;
        for (String d: data) {
            f1 = friends.get(d.charAt(0));
            f2 = friends.get(d.charAt(2));
            op = d.charAt(3);
            dist = d.charAt(4) - '0' + 1;
            if (op == '=' ) {
                if (Math.abs(order[f1] - order[f2]) != dist)
                    return false;
            }
            else if (op == '>') {
                if (Math.abs(order[f1] - order[f2]) <= dist)
                    return false;
            }
            else if (op == '<') {
                if (Math.abs(order[f1] - order[f2]) >= dist)
                    return false;
            }
        }
        return true;
    }
}