/**
 * @param {string[]} words
 * @param {string} chars
 * @return {number}
 */
var countCharacters = function(words, chars) {
    const charCount = {};
    let result = 0;
    
    for (let char of chars){
        if (charCount[char]){
            charCount[char] += 1;
        }
        else {
            charCount[char] = 1;
        }
    }
    
    for (let word of words){
        if (formWord(word, charCount)){
            result += word.length;
        }
    }
    
    return result;
};

function formWord(word, charCount){
    const wordCount = {};
    wordLength = word.length
    
    for (let i = 0; i < wordLength; i++){
        if (wordCount[word[i]]){
            wordCount[word[i]] += 1;
        }
        else {
            wordCount[word[i]] = 1;
        }
        
        if (!charCount[word[i]] || wordCount[word[i]] > charCount[word[i]]){
            return false;
        }
    }
    
    return true;
}
    
    
    
    
    
    
    