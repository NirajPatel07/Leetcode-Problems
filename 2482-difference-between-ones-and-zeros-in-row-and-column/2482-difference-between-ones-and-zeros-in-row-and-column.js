/**
 * @param {number[][]} grid
 * @return {number[][]}
 */
var onesMinusZeros = function(grid) {
    const matrix = Array.from({ length: grid.length }, () => Array(grid[0].length).fill(0));

        const { rowZeros, columnZeros, rowOnes, columnOnes } = gridDifference(grid);

        for (let row = 0; row < grid.length; row++) {
            for (let column = 0; column < grid[0].length; column++) {
                matrix[row][column] = rowOnes[row] + columnOnes[column] - rowZeros[row] - columnZeros[column];
            }
        }

        return matrix;
};

function gridDifference(grid) {
        const rowZeros = [];
        const columnZeros = [];
        const rowOnes = [];
        const columnOnes = [];

        for (let row = 0; row < grid.length; row++) {
            rowZeros.push(grid[row].filter(num => num === 0).length);
            rowOnes.push(grid[row].filter(num => num === 1).length);
        }

        for (let column = 0; column < grid[0].length; column++) {
            let zeroCount = 0;
            let oneCount = 0;
            for (let row = 0; row < grid.length; row++) {
                if (grid[row][column] === 1) {
                    oneCount++;
                } else {
                    zeroCount++;
                }
            }
            columnZeros.push(zeroCount);
            columnOnes.push(oneCount);
        }

        return { rowZeros, columnZeros, rowOnes, columnOnes };
    }