import java.util.*;

class Solution {
    public int solution(int[] scoville, int K) {
    int cnt = 0;
        
    PriorityQueue<Long> pq = new PriorityQueue<>();
    for (int i : scoville) {
         pq.offer((long) i);
    }
       
    while (!pq.isEmpty() && pq.peek() < K){
        if (pq.size() < 2) return -1;
        
        long tmp = pq.poll() + (pq.poll()) * 2;
        pq.offer(tmp);
        cnt++;
       }
        return cnt;
    }
}