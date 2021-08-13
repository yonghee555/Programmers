class Solution {
    public long solution(long n) {
        long i = 1;
        while (true) {
            long a = i * i;
            if (a == n)
                return (i + 1) * (i + 1);
            else if (a > n)
                return -1;
            i++;
        }
    }
}