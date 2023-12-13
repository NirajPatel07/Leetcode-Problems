/**
 * @param {number[][]} mat
 * @return {number}
 */
var numSpecial = function(mat) {
    let count = 0;
    
    for (let row = 0; row < mat.length; row++){
        for (let column = 0; column < mat[0].length; column++){
            if (mat[row][column] == 1 && isSpecial(mat, row, column)){
                count += 1;
            }
        }
    }
    
    return count;
};


function isSpecial(mat, row, column){
    const rowData = mat[row];
    if (rowData.filter(val => val == 1).length > 1){
        return false;
    }
    
    let upRow = row;
    let downRow = row;

    while (upRow - 1 >= 0) {
        upRow--;
        if (mat[upRow][column] !== 0) {
            return false;
        }
    }

    while (downRow + 1 < mat.length) {
        downRow++;
        if (mat[downRow][column] !== 0) {
            return false;
        }
    }
    
    return true;
}