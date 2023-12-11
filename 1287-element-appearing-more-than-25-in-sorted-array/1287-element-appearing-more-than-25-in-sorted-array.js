/**
 * @param {number[]} arr
 * @return {number}
 */
var findSpecialInteger = function(arr) {
    let currNum = arr[0];
    let count = 1;
    const arrLength = arr.length;
    const threshold = Math.floor(arrLength/4);
    
    for (let i = 1; i < arrLength; i++){
        if (arr[i] == currNum){
            count += 1;
        }
        else {
            currNum = arr[i];
            count = 1;
        }
        
        if (count > threshold){
            return arr[i];
        }
    }
    
    return currNum;
};