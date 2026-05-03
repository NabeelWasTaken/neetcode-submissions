class Solution {
    public boolean hasDuplicate(int[] nums) {

        HashSet<Integer> look = new HashSet();

        for(int i = 0;i < nums.length;i++){
            if(look.contains(nums[i])){
                return true;
            }
            look.add(nums[i]);
        }
        return false;

    }
}
