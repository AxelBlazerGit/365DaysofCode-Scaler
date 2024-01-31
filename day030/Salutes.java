public class Solution {
    public long countSalutes(String A) {
        long result = 0 ,count = 0;
        int n = A.length();
        for(int i = 0; i <n; i++){
            if(A.charAt(i) == '>')
                count++;
            else{
                result += count;
                }
        }
        return result;
    }
}
