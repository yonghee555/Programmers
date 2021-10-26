class Solution {
    public int solution(int[][] sizes) {
        int small = 0;
        int big = 0;

        for (int i = 0; i < sizes.length; i++) {
            if (sizes[i][0] >= sizes[i][1]) {
                if (sizes[i][0] > big)
                    big = sizes[i][0];
                if (sizes[i][1] > small)
                    small = sizes[i][1];
            }
            else {
                if (sizes[i][1] > big)
                    big = sizes[i][1];
                if (sizes[i][0] > small)
                    small = sizes[i][0];
            }
        }
        return small * big;
    }
}