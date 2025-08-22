import java.util.*;

class Solution {
    public long solution(int n, int[] times) {
        long left = 1L;
        long right = (long) Arrays.stream(times).max().getAsInt() * n;
        long ans = right;
        
        while (left <= right){
            long mid = (left + right) / 2;
            
            long done = 0L;
            for (int t : times) {
                done += mid / t;
                if (done >= n) break; 
            }
            
            if (done >= n) {
                ans = mid;
                right = mid -1;
            } else {
                left = mid + 1;
            }
        }
        return ans;
    }
}