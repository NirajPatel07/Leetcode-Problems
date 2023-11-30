var gcdOfStrings = function(str1, str2) {
    if(str1 + str2 != str2 + str1) {
        return ""
    }
    let x = str1.length
    let y = str2.length
    function gcd(m, n) {
        if(!n) return m
        return gcd (n, m % n)

    }
    let div = gcd(x, y)
    return  str1.slice(0, div)
    
};