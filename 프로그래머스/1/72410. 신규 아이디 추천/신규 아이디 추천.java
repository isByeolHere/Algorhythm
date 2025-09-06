class Solution {
    public String solution(String new_id) {
        String s = new_id.toLowerCase();

        // 2단계: 허용 문자만 남기기
        s = s.replaceAll("[^a-z0-9-_.]", "");

        // 3단계: 마침표 연속 제거
        s = s.replaceAll("\\.+", ".");
        
                // 4단계: 처음/끝 마침표 제거
        s = s.replaceAll("^\\.|\\.$", "");
        
        if (s.isEmpty()) s = "a";
        if (s.length() >= 16) {
            s = s.substring(0, 15).replaceAll("\\.$", "");
        }
            
        while (s.length() < 3) {
            s += s.charAt(s.length() - 1);
        }
        
        return s;
    }
}