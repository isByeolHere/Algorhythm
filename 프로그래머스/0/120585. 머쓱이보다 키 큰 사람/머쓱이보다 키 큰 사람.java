class Solution {
    public int solution(int[] array, int height) {
        int num = 0;
        for (int x : array) {
            if (x > height) num++;
        }
        return num;
    }
}