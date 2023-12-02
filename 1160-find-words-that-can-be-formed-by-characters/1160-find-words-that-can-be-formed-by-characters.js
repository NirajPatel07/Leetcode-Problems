/**
 * @param {string[]} words
 * @param {string} chars
 * @return {number}
 */
var countCharacters = function(words, chars) {
    const charCount = new Map();
    let result = 0;
    
    for (let char of chars){
        charCount.set(char, (charCount.get(char) || 0) + 1);
    }
    
    for (let word of words){
        if (formWord(word, charCount)){
            result += word.length;
        }
    }
    
    return result;
};

function formWord(word, charCount){
    const wordCount = new Map();
    const wordLength = word.length;
    
    for (let i = 0; i < wordLength; i++){
        const currentCount = (wordCount.get(word[i]) || 0) + 1;
        wordCount.set(word[i], currentCount);
        
        if (!charCount.has(word[i]) || currentCount > charCount.get(word[i])){
            return false;
        }
    }
    
    return true;
}
