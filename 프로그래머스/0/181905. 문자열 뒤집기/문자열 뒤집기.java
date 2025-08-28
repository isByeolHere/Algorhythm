class Solution {
    public String solution(String my_string, int s, int e) {
        char[] arr = my_string.toCharArray();
        while (s < e) {
            char tmp = arr[s];
            arr[s] = arr[e];
            arr[e] = tmp;
            s++;
            e--;
        }
        return new String(arr);
    }
}



// class Solution {
//     public String solution(String my_string, int s, int e) {
//         StringBuilder sb = new StringBuilder();
//         sb.append(my_string.substring(0, s));           // 앞부분
//         sb.append(new StringBuilder(my_string.substring(s, e+1)).reverse()); // 뒤집을 부분
//         sb.append(my_string.substring(e+1));            // 뒷부분
//         return sb.toString();
//     }
// }