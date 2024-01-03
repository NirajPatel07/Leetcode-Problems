/**
 * @param {string[]} bank
 * @return {number}
 */
var numberOfBeams = function(bank) {
    let prev = bank[0].split("").filter((char) => char == "1").length;
    let res = 0;
    
    for (let i = 1; i < bank.length; i++){
        let curr = bank[i].split("").filter((char) => char == "1").length;
        if (curr){
            res += (prev * curr);
            prev = curr;
        }
    }
    
    return res;
};