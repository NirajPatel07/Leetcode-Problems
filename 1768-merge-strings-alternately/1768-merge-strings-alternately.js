/**
 * @param {string} word1
 * @param {string} word2
 * @return {string}
 */
var mergeAlternately = function(word1, word2) {
    let index = 0;
    let result = "";
    
    while (index < word1.length && index < word2.length){
        result += word1[index];
        result += word2[index];
        index += 1;
    }
    
    if (index < word1.length){
        result += word1.slice(index);
    }
    
    if (index < word2.length){
        result += word2.slice(index);
    }
    
    return result;
};