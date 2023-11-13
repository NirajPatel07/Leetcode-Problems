/**
 * @param {string} s
 * @return {string}
 */
var sortVowels = function(s) {
    let vowels = ['a','e','i','o','u','A','E','I','O','U'];
    let sv = [];
    
    for(let i = 0; i < s.length; i++){
        if(vowels.includes(s[i])){
            sv.push(s[i]);
        }
    }
    
    sv.sort();
    let result = "";
    let idx = 0;
    
    for(let i = 0; i < s.length; i++){
        if(vowels.includes(s[i])){
            result += sv[idx];
            idx += 1;
        }
        else{
            result += s[i];
        }
    }
    
    return result;
};