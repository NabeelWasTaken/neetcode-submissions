class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        
        if(matrix.length == 0 || matrix[0].length == 0 || matrix == null){
            return false;
        }
        int ROWS = matrix.length;
        int COLUMNS = matrix[0].length;

        int top = 0;
        int bot = ROWS - 1;
        
        while(top <= bot){
            int row = (top + bot)/2;
            if (target < matrix[row][0]){
                bot = row - 1;
            }
            else if(target > matrix[row][COLUMNS - 1]){
                top = row + 1;
            }
            else{
                break;
            }
        }
        // if (!(top <= bot)) {
        //     return false;
        // }
        

        int l = 0;
        int r = COLUMNS - 1;
        int row = (top + bot)/2;
        while(l <= r){
            int mid = (l + r)/2;
            if(target < matrix[row][mid]){
                r = mid - 1;
            }
            else if(target > matrix[row][mid]){
                l = mid + 1;
            }
            else {
                return true;
            }
        }

        return false;
    }
}
