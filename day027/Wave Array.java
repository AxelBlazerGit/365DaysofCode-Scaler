import java.util.Arrays;

public class Solution {
    public int[] wave(int[] A) {
        Arrays.sort(A);
        for (int i = 0; i < A.length - 1; i += 2) {
            swap(A, i, i + 1);
        }

        return A;
    }

    private void swap(int[] arr, int i, int j) {
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }
}
