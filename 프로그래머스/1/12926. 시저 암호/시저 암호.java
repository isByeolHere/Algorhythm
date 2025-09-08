class Solution {
    public String solution(String s, int n) {
        StringBuilder sb = new StringBuilder();
        
        for (char c : s.toCharArray()) {
            if (c == ' '){
                sb.append(' ');
            } else if (c >= 'A' && c <= 'Z') {
                char shifted = (char) ((c - 'A' + n) % 26 + 'A');
                sb.append(shifted);
            } else if (c >= 'a' && c <= 'z') {
                char shifted = (char) ((c - 'a' + n) % 26 + 'a');
                sb.append(shifted);
            }
        }
        return sb.toString();
    }
}
