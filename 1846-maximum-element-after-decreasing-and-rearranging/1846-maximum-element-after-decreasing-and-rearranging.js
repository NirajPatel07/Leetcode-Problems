/**
 * @param {number[]} arr
 * @return {number}
 */
var maximumElementAfterDecrementingAndRearranging = function(arr) {
    arr.sort((a, b) => a-b);
    let prev = 0;
    
    for (let n of arr){
        prev = Math.min(prev + 1, n);
    }
    
    return prev;
};