/**
 * @param {string[]} bank
 * @return {number}
 */
var numberOfBeams = function(bank) {
    let prev = bank[0].split('1').length - 1;
    console.log(bank[0].split('1'));
        let res = 0;

        for (let i = 1; i < bank.length; i++) {
            let curr = bank[i].split('1').length - 1;
            if (curr) {
                res += prev * curr;
                prev = curr;
            }
        }

        return res;
};