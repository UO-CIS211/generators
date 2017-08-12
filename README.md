# Generators

A generator is like an expression or function that returns (yields) a sequence of values instead of a single value.  In Python, the most familiar use of generators is in iteration, e.g., *range* is a generator in 
``for i in range(7):``

They are used in many other contexts in Python 3, much more so than in Python 2.x.  

A Java iterator is a kind of generator, but much more limited.  A Java iterator must make an explicit record of its state in an object, so the saved state is limited to things that can be named and saved in variables.  A Python generator *implicitly* saves state by doing a *yield* rather than a *return*.  That allows it save state that can't be named.  In particular, it can save the call stack and all variables in scope.  

To get the full power of saving the call stack, we need generators that call generators. This is done with *yield from*.  



