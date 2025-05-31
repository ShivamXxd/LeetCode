class Solution {
    public int[] getConcatenation(int[] nums) {
        int[] result = new int[2 * nums.length];
        int end = 2 * nums.length;
        for(int i = 0; i < end / 2; i++){
            // if(i < end / 2)
            //     result[i] = nums[i];
            // else if (i >= end / 2) 
            //     result[i] = nums[i - nums.length];
            result[i] = nums[i];
            result[i + nums.length] = nums[i];
        }
        return result;
    }
}