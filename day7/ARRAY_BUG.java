public class Solution {
	public ArrayList<Integer> rotateArray(ArrayList<Integer> A, int B) {
		ArrayList<Integer> ret = new ArrayList<Integer>();
        int N = A.size();

        for (int i = 0; i < N; i++) {
            int newIndex = (i + B) % N;
            ret.add(A.get(newIndex));
        }

        return ret;
	}
}
