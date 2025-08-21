import java.util.*;

class Solution {
    public int solution(String numbers) {
        char[] digits = numbers.toCharArray();
        boolean[] used = new boolean[digits.length];
        Set<Integer> made = new HashSet<>();
        
        dfs(digits, used, new StringBuilder(), made);
        
        int count = 0;
        for (int x : made) {
            if (isPrime(x)) count++;
        }
        return count;
    }
    
    private void dfs(char[] digits, boolean[] used, StringBuilder cur, Set<Integer> made){
        if (cur.length() > 0) {
            made.add(Integer.parseInt(cur.toString()));
        }
        
        if (cur.length() == digits.length) return;
        
        for (int i = 0; i < digits.length; i++) {
            if (used[i]) continue;
            used[i] = true;
            cur.append(digits[i]);
            dfs(digits, used, cur, made);
            cur.deleteCharAt(cur.length() -1);
            used[i] = false;
        }
    }
    private boolean isPrime(int n) {
        if (n < 2) return false;
        if (n % 2 == 0) return n == 2;
        for (int d = 3; d * d <= n; d += 2) {
            if (n % d == 0) return false;
        }
        return true;
    }
}