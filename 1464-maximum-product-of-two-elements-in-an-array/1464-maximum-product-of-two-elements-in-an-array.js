/**
 * @param {number[]} nums
 * @return {number}
 */
var maxProduct = function(nums) {
    let n = nums.length;
    let largest = nums[0];
    let secondLargest;
    
    for (let i = 1; i < n; i++){
        if (nums[i] > largest){
            secondLargest = largest;
            largest = nums[i];
        }
        else if (!secondLargest || nums[i] > secondLargest){
            secondLargest = nums[i];
        }
    }
    
    return (largest - 1) * (secondLargest - 1);
};