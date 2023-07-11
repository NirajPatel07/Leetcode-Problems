/**
 * @param {string[]} strs
 * @return {string}
 */
var longestCommonPrefix = function(strs) {
    var prefix = strs[0];
    
    for (let i = 1; i < strs.length; i++){
        while (strs[i].slice(0, prefix.length) != prefix){
            prefix = prefix.slice(0, prefix.length-1);
            
            if (! prefix) return "";
        }
    }
    
    return prefix;
};