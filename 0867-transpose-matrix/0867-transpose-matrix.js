/**
 * @param {number[][]} matrix
 * @return {number[][]}
 */
var transpose = function(matrix) {
    let rows = matrix.length;
    let cols = matrix[0].length;
    const result = Array.from({length: cols}, () => Array(rows).fill(0));
    
    for (let r = 0; r < rows; r++){
        for (let c = 0; c < cols; c++){
            result[c][r] = matrix[r][c];
        }
    }
    
    return result;
};