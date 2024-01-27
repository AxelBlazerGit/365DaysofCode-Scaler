public class Solution {
    public ArrayList<Integer> getRow(int A) {
        ArrayList<Integer> row=new ArrayList<>();
        if(A<0) return row;
        row.add(1);
        for(int i=1;i<=A;i++){
            ArrayList<Integer> curr=new ArrayList<>();
            curr.add(1);
            for(int j=1;j<i;j++){
                curr.add(row.get(j-1)+row.get(j));
            }
            curr.add(1);
            row=curr;
        }
        return row;
    }
}
