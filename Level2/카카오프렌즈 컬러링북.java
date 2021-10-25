class Solution {
    int[] solution(int m, int n, int[][] picture) {
        int numberOfArea = 0;
        int maxSizeOfOneArea = 0;

        int[][] newPicture = new int[m][n];

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                newPicture[i][j] = picture[i][j];
            }
        }

        for (int i = 0; i < newPicture.length; i++) {
            for (int j = 0; j < newPicture[i].length; j++) {
                int count = CountArea(i, j, newPicture, newPicture[i][j]);
                if (count > 0)
                    numberOfArea++;
                if (count > maxSizeOfOneArea)
                    maxSizeOfOneArea = count;
            }
        }
        int[] answer = new int[2];
        answer[0] = numberOfArea;
        answer[1] = maxSizeOfOneArea;
        return answer;
    }

    public int CountArea(int x, int y, int[][] picture, int color) {
        if (x < 0 || y < 0 || x >= picture.length || y >= picture[x].length || picture[x][y] == 0 || picture[x][y] != color)
            return 0;
        else
            picture[x][y] = 0;
        return 1 + CountArea(x + 1, y, picture, color) + CountArea(x, y + 1, picture, color) 
                + CountArea(x - 1, y, picture, color) + CountArea(x, y - 1, picture, color);
    }
}