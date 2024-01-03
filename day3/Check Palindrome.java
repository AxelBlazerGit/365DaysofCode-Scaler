public class Solution {
    public int solve(String A) {
        int l=A.length(),odds=0;
        int[] freq=new int[26];
        for(char ele : A.toCharArray()){
            freq[ele-'a']++;
        }
        
        for(int ele:freq){
            if(ele%2!=0) odds++;
        }
        return odds<2? 1:0;
    }
}
