# Fibonaccier

## Task

### Read positive (>0) number n (from stdin or cmdline)

Make 2 asynchronous/concurrent calls to a function fib(...) which

1. includes a random delay of up to 1 second
2. calculates and returns the fibonacci number calculated using the following recursive formula:

```python
Fib(0) = 0
Fib(1) = 1
Fib(n) = Fib(n-1) + Fib(n-2)
```

Wait until both of the asynchronous calls finish.

Print out the resulting Fibonacci number Fib(n), and which one of
the two calls finished out first.

If you are unsure how to go about it, consider implementing
the solution incrementally e.g. as follows:

1. Implement a synchronous Fibonacci function without
   the random delay. Verify it produces the correct result.
2. Change it into an async function. Verify it still works.
3. Add the random delay into the function.
4. Implement the 2 concurrent async calls to this function

## Instruction for use

Use Fibonaccier script to find out fibonacci value for a number and which of two created async functions complete first.
The script is run with the number as a command line argument. Code tested to work with Python 3.11.4.

```sh
python fibonaccier.py <positive integer number>
```
