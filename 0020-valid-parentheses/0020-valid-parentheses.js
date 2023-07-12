/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    var lookup = {")": "(", "]": "[", "}": "{"};
    var stack = [];
    const open_paren = "([{"
    
    for(let i=0; i<s.length; i++){
        if(open_paren.includes(s[i])){
            stack.push(s[i]);
        }
        else{
            if(stack.length != 0 && stack[stack.length - 1] == lookup[s[i]]){
                stack.pop();
            }
            else{
                return false;
            }
        }
    }
    
    if(stack.length==0){
        return true;
    }
    return false;
    
};