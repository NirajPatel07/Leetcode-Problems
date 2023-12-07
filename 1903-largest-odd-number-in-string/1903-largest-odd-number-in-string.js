/**
 * @param {string} num
 * @return {string}
 */
var largestOddNumber = function(num) {
    const oddNumbers = ["1", "3", "5", "7", "9"];
    
    for (let i = num.length - 1; i > -1; i--){
        if (oddNumbers.includes(num[i])){
            return num.slice(0, i+1);
        }
    }
    
    return "";
};