import java.util.*;

class Solution {
    public int solution(String[] spell, String[] dic) {
        char[] arr = String.join("", spell).toCharArray();
        Arrays.sort(arr);
        String target = new String(arr);
        
        for (String word : dic) {
            char[] dicarr = word.toCharArray();
            Arrays.sort(dicarr);
            if (target.equals(new String(dicarr))){
                return 1;
            }
        }
        return 2;
    }
}