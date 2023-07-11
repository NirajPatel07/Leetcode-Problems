/**
 * @param {string} s
 * @return {number}
 */
var romanToInt = function(s) {
    const lookup = {
            "I":            1,
            "V":            5,
            "X":             10,
            "L":             50,
            "C":             100,
            "D":             500,
            "M":             1000
        };
    
    let res = 0;
    
    for(let i = 0; i < s.length; i++){
        if (lookup[s[i+1]] > lookup[s[i]]){
            res -= lookup[s[i]];
        } else {
            res += lookup[s[i]];
        }
    }
    
    return res;
    
};