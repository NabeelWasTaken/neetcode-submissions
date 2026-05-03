class Solution {
    public boolean hasDuplicate(int[] nums) {

        HashSet<Integer> list2 = new HashSet<>();
        for(int num : nums){
            if (list2.contains(num)){
                return true;
            }

            list2.add(num);
        }

        return false;
        
    }
}