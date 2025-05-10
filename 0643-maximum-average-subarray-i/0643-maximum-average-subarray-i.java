import java.util.Arrays;

class Solution {
    public double findMaxAverage(int[] nums, int k) {
        int window_sum = 0;
        int i = 0;
        while(i < k){
            window_sum += nums[i];
            i++;
        }
        double max_average = window_sum / (double) k;
        for(int j = k; j < nums.length; j++){
            window_sum += nums[j] - nums[j - k];
            max_average = Math.max(max_average, window_sum / (double) k);
        }
        return max_average;
    }
}