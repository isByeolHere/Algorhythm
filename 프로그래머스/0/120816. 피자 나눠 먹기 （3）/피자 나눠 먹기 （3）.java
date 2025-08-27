class Solution {
    public int solution(int slice, int n) {
        int num = 0;
        while(slice * num < n) {
            num += 1;
        }
        return num;
    }
}