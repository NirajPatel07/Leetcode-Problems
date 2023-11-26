/**
 * @param {string} word1
 * @param {string} word2
 * @return {string}
 */
var mergeAlternately = function(word1, word2) {
    let index = 0;
    let result = "";
    let w1 = word1.length;
    let w2 = word2.length;
    
    while (index < w1 && index < w2){
        result += word1[index];
        result += word2[index];
        index += 1;
    }
    
    if (index < w1){
        result += word1.slice(index);
    }
    
    if (index < w2){
        result += word2.slice(index);
    }
    
    return result;
};