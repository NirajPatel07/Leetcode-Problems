/**
 * @param {string[][]} paths
 * @return {string}
 */
var destCity = function(paths) {
    const seen = new Set();
    
    for (const path of paths){
        seen.add(path[0]);
    }
    
    for (const path of paths){
        if (!seen.has(path[1])){
            return path[1];
        }
    }
};