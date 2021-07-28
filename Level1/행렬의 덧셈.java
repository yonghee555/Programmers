class Solution {
    public int[][] solution(int[][] arr1, int[][] arr2) {
        int a = arr1.length;
        int b = arr1[0].length;
        int[][] answer = new int[a][b];
        
        for (int i = 0; i < a; i++) {
            int[] temp = new int[b];
            for (int j = 0; j < b; j++) {
                temp[j] = arr1[i][j] + arr2[i][j];
            }
            answer[i] = temp;
        }
        return answer;
    }
}