# answers.md

## 1a. Is 2^(n+1) in O(2^n)? Why or why not?

### Answer:
Yes, 2^(n+1) is in O(2^n).
We can rewrite 2^(n+1) as 2 * 2^n. This shows that 2^(n+1) grows at most twice as fast as 2^n. Therefore, it is in O(2^n).

---

## 1b. Is 2^(2^n) in O(2^n)? Why or why not?

### Answer:
No, 2^(2^n) is not in O(2^n).
The function 2^(2^n) grows much faster than 2^n. Therefore, it is not in O(2^n).

---

## 1c. Is n^1.01 in O(log(n)^2)?

### Answer:
No, n^1.01 is not in O(log(n)^2).
n^1.01 grows faster than log(n)^2. As n becomes large, log(n) grows much slower compared to n^1.01. Therefore, it is not in O(log(n)^2).

---

## 1d. Is n^1.01 in Omega(log(n)^2)?

### Answer:
Yes, n^1.01 is in Omega(log(n)^2).
As mentioned earlier, n^1.01 grows faster than log(n)^2. Therefore, it is in Omega(log(n)^2).

---

## 1e. Is sqrt(n) in O(log(n)^3)?

### Answer:
No, sqrt(n) is not in O(log(n)^3).
sqrt(n) grows faster than log(n)^3. Therefore, it is not in O(log(n)^3).

---

## 1f. Is sqrt(n) in Omega(log(n)^3)?

### Answer:
Yes, sqrt(n) is in Omega(log(n)^3).
As mentioned earlier, sqrt(n) grows faster than log(n)^3. Therefore, it is in Omega(log(n)^3).

---

## 1g. Proving that o(g(n)) intersection omega(g(n)) is the empty set

#### Proof by Contradiction

Let's assume that there exists some function f(n) that belongs to both o(g(n)) and omega(g(n)).

1. For o(g(n)): For every positive constant c1, there exists a constant n01 such that f(n) <= c1 * g(n) for all n >= n01.
  
2. For omega(g(n)): For every positive constant c2, there exists a constant n02 such that f(n) >= c2 * g(n) for all n >= n02.

Let c1 and c2 be any two positive constants.

Now, let n_max = max(n01, n02). For n >= n_max, both conditions must hold:

1. The first condition f(n) <= c1 * g(n) implies that f(n)/g(n) <= c1.
  
2. The second condition f(n) >= c2 * g(n) implies that f(n)/g(n) >= c2.

Since c1 and c2 are any two positive constants, this leads to a contradiction: f(n)/g(n) cannot be both less than any c1 and greater than any c2.

Therefore, our initial assumption is false, and we can conclude that o(g(n)) intersection omega(g(n)) must be the empty set.
---

## 2b. What does this function do?
The function `foo` calculates the n-th Fibonacci number using recursion. For inputs 0 and 1, it returns the value itself. Otherwise, it calculates the sum of the (x-1)-th and  (x-2)-th Fibonacci numbers by recursively calling itself.

---

## 3b. Work and Span of Iterative Implementation
- Work:  Since we explore each element of the array at least once, the work done by the algorithm is O(n), where n  is the length of the array. 
- Span:  It  implements in an iterative, sequential way, so its span is O(1)

## 3d. Work and Span of Recursive Algorithm
- Work:  O(n) 
- Span:  At each level of recursion, the algorithm splits the problem into two independent subproblems, so the depth of the recursion tree would be log n . Thus, the span of the algorithm is O(log n).

### 3e. Work and Span in Parallelized `longest_run_recursive`
- Work:In our recursive algorithm for finding the longest run, we divide the array into two halves in each recursive call until we reach arrays of size 1. Since we explore each element of the array at least once, the work done by the algorithm is O(n), where n  is the length of the array.
- Span: At each level of recursion, the algorithm splits the problem into two independent subproblems, so the depth of the recursion tree would be log n .And current result relies in its sub-result. Thus, the span of the algorithm is O(log n).



