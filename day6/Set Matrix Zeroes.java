import java.util.ArrayList;
public class Solution{
    public void setZeroes(ArrayList<ArrayList<Integer>> a){
        if(a.size()==0) return;
        int rows=a.size(),cols=a.get(0).size();
        boolean[] zRows=new boolean[rows];
        boolean[] zCols=new boolean[cols];
        for(int i=0; i<rows; i++){
            for(int j=0; j<cols; j++){
                if(a.get(i).get(j)==0){
                    zRows[i]=zCols[j]=true;
                }
            }
        }
        for(int i=0; i<rows; i++){
            if(zRows[i]){
                for(int j=0; j<cols; j++) a.get(i).set(j, 0);
            }
        }
        for(int j=0; j<cols; j++){
            if(zCols[j]){
                for(int i=0; i<rows; i++) a.get(i).set(j, 0);
            }
        }
    }
}
