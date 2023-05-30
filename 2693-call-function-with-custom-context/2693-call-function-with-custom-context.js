/**
 * @param {Object} context
 * @param {any[]} args
 * @return {any}
 */
Function.prototype.callPolyfill = function(context, ...args) {

    f = this
    sym = Symbol()
    context[sym] = f
    ans = context[sym](...args)
    delete context[sym]
    return ans

}

/**
 * function increment() { this.count++; return this.count; }
 * increment.callPolyfill({count: 1}); // 2
 */