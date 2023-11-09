/**
 * @param {string} s
 * @return {number}
 */
var countHomogenous = function(s) {
    let result = 0;
    let count = 0;
    let mod = 10 ** 9 + 7
    
    for(let i = 0; i < s.length; i++){
        
        if(i == 0 || s.charAt(i) == s.charAt(i-1)){
            count += 1;
        }
        else{
            count = 1;
        }
        
        result += count;
    }
    
    return result % mod;
};