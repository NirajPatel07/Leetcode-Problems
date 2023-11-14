/**
 * @param {string} s
 * @return {number}
 */
var countPalindromicSubsequence = function(s) {
    let position = new Map();
    for (let i = 0; i < s.length; i++){
        if (position.has(s[i])){
            position.get(s[i])[1] = i;
        }
        else{
            position.set(s[i], [i, i]);
        }
    }
    
    let result = 0;
    for (let [left, right] of position.values()){
        let count = new Set();
        for (let i = left+1; i < right; i++){
            count.add(s[i]);
        }
        result += count.size;
    }
    
    return result;
};