import java.util.*;

class Solution {
    public int solution(String[] s1, String[] s2) {
        Set<String> set = new HashSet<>(Arrays.asList(s1));
        
        int cnt = 0;
        for (String i : s2){
                if (set.contains(i)) {
                    cnt++;
                }
            }
        return cnt;
    }
}