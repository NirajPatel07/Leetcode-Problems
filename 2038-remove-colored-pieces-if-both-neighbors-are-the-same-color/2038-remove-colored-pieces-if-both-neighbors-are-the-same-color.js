/**
 * @param {string} colors
 * @return {boolean}
 */
var winnerOfGame = function(colors) {
    let alice = 0;
    let bob = 0;
    const clength = colors.length - 1;
    
    for (let i = 1; i < clength; i++){
        if (colors[i-1] === colors[i] && colors[i] === colors[i+1]){
            if (colors[i] === 'A'){
                alice++;
            }
            else {
                bob++;
            }
        }
    }
    
    return alice > bob;
};