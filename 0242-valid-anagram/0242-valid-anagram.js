/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function(s, t) {
    if (s.length !== t.length) return false;
    
    const counter = new Map();
    for (let char of s){
        counter[char] = (counter[char] || 0) + 1;
    }
    
    for (let char of t){
        if (!counter[char]) return false;
        
        counter[char]--;
    }
    
    return true;
};