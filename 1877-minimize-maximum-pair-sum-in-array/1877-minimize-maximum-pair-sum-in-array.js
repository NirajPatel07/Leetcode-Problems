/**
 * @param {number[]} nums
 * @return {number}
 */
var minPairSum = function(nums) {
    nums.sort((a, b) => a - b);
    let n = nums.length;
    const pairs = [];
    
    for (let i = 0; i < Math.floor(nums.length/2); i++){
        pairs.push(nums[i] + nums[n-i-1]);
    }
    
    return Math.max(...pairs);
};