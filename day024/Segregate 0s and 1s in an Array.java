public class Solution {
    public int[] solve(int[] A) {
        int left = 0;
        int right = A.length - 1;
        
        while (left < right) {
            //check sorted from left
            while (A[left] == 0 && left < right) {
                left++;
            }
            //check sorted from right
            while (A[right] == 1 && left < right) {
                right--;
            }

            if (left < right) {
                int temp = A[left];
                A[left] = A[right];
                A[right] = temp;

                left++;
                right--;
            }
        }

        return A;
    }
}
