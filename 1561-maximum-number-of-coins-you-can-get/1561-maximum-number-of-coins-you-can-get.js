/**
 * @param {number[]} piles
 * @return {number}
 */
var maxCoins = function(piles) {
    piles.sort((a, b) => a - b);
    let totalCoins = 0;
    let rounds = Math.floor(piles.length / 3);
    let idx = rounds;
    
    for (let i = 0; i < rounds; i += 1){
        totalCoins += piles[idx];
        idx += 2;
    }
    
    return totalCoins;
};