class Solution {
    public int solution(int[] numbers) {
        int answer = numbers[0]*numbers[1];
        int temp = 0;
        for (int i = 0; i < numbers.length; i++) {
            for (int j = i+1; j < numbers.length; j++) {
                temp = numbers[i] * numbers[j];
                if (answer < temp) {
                    answer = temp;
                }
            }
            }
        return answer;
    }
}