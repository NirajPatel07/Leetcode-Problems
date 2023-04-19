import java.util.HashMap;
import java.util.Map;
 
class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> n = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            if (n.containsKey(target - nums[i])) {
                return new int[] {n.get(target - nums[i]), i};
            }
            n.put(nums[i], i);
        }
        return new int[] {};
    }
}