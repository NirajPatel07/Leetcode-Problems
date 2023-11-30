/**
 * @param {string} str1
 * @param {string} str2
 * @return {string}
 */
var gcdOfStrings = function(str1, str2) {
    if (str1.length < str2.length){
        let temp = str1;
        str1 = str2;
        str2 = temp;
    }
    
    if (str1 == str2){
        return str1;
    }
    
    if (str1.slice(0, str2.length) != str2){
        return "";
    }
    
    return gcdOfStrings(str1.slice(str2.length, str1.length), str2)
};