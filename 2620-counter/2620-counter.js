/**
 * @param {number} n
 * @return {Function} counter
 */
var createCounter = function(n) {
    let ans = n - 1
    return function() {
        ans += 1;
        return ans;
    };
};

/** 
 * const counter = createCounter(10)
 * counter() // 10
 * counter() // 11
 * counter() // 12
 */