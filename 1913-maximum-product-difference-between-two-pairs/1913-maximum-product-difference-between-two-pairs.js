/**
 * @param {number[]} nums
 * @return {number}
 */
var maxProductDifference = function(nums) {
    let [min1, min2, max1, max2] = [Infinity, Infinity, 0, 0];
    
    for (let n of nums){
        
        if (n > max1){
            max2 = max1;
            max1 = n;
        } else if (n > max2){
            max2 = n;
        }
        
        if (n < min1){
            min2 = min1;
            min1 = n;
        } else if (n < min2){
            min2 = n;
        }
        
    }
    
    return (max2 * max1) - (min1 * min2);
};