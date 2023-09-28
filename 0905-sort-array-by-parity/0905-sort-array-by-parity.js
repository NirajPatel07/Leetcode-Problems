/**
 * @param {number[]} nums
 * @return {number[]}
 */
var sortArrayByParity = function(nums) {
    var left = 0;
    var right = nums.length - 1;
    
    while (left < right){
        
        while (left < nums.length && nums[left] % 2 == 0){
            left++;
        }
        
        while (right >= 0 && nums[right] % 2 == 1){
            right--;
        }
        
        if (left < right){
            [nums[left], nums[right]] = [nums[right], nums[left]];
        }
        
        left++;
        right--;
    }
    
    return nums;
};