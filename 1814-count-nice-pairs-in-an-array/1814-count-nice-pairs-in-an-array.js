/**
 * @param {number[]} nums
 * @return {number}
 */
var countNicePairs = function(nums) {
    let count = 0;
    const counter = {};
    const mod = 10 ** 9 + 7;
    
    for (let num of nums){
        let curr = num - reverse(num);
        counter[curr] = (counter[curr] || 0) + 1;
    }
    
    for (let n in counter){
        count += Math.floor((counter[n] * (counter[n] - 1)) / 2);
    }
    
    return count % mod;
};

function reverse(num){
    let reversed_num = 0;
    
    while (num > 0){
        let remainder = num % 10;
        num = Math.floor(num / 10);
        reversed_num = reversed_num * 10 + remainder;
    }
    
    return reversed_num;
}