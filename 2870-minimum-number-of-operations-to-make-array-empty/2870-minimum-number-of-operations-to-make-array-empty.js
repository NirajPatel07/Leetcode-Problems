/**
 * @param {number[]} nums
 * @return {number}
 */
var minOperations = function(nums) {
    const count = {};
    for (let i = 0; i < nums.length; i++){
        if (count[nums[i]]){
            count[nums[i]]++;
        } else {
            count[nums[i]] = 1;
        }
    }
    
    let res = 0;
    const values = Object.values(count);
    
    for (let i = 0; i < values.length; i++){
        if (values[i] == 1){
            return -1;
        }
        else if (values[i] % 3 == 0){
            res += (values[i] / 3);
        }
        else {
            res += (Math.ceil(values[i]/3));
        }
    }
    
    return res;
};