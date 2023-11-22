/**
 * @param {number[][]} nums
 * @return {number[]}
 */
var findDiagonalOrder = function(nums) {
    let result = [];
    let groups = {};
    
    for (let row = nums.length - 1; row > -1; row--){
        for (let column = nums[row].length - 1; column > -1; column--){
            let diagonal = row + column;
            if (diagonal in groups){
                groups[diagonal].push(nums[row][column]);
            }
            else {
                groups[diagonal] = [nums[row][column]];
            }
        }
    }
    
    let curr = 0;
    
    while (curr in groups){
        result.push(...groups[curr]);
        curr += 1;
    }
    
    return result;
};