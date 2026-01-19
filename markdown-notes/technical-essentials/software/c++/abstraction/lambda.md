# C++ Lambdas

- Lambdas in C++ notes

## Index

- [Index](#index)
- [Overview](#overview)
- [Example Usage](#example-usage)

## Overview

- "lambda expressions" are anonymous function objects that can:
  - Be defined inline without naming it
  - Capture variables from the surrounding scope
  - Be passed directly to algorithms, threads, callbacks, etc
- Syntax:
  - `[ captures ] ( parameters ) -> return_type { body }`
  - `[ captures ]`- local variables to capture (by value or reference)
  - `( parameters )`- function parameters (just like a regular function)
  - `-> return_type`- optional, inferred if not provided
  - `{ body }`- function body
- Good for:
  - STL algorithms like `sort`, `for_each`, `transform`
  - Callbacks (GUI events, async operations, threading, etc)
  - Small inline functions
  - Closures (capture variables to maintain state across calls)
- Best practices if in use:
  - Prefer `auto` for storing lambdas
  - Capture only what's needed
  - Keep lambdas short and readable- otherwise you'd rather define a named function

## Example Usage

```
#include <iostream>
#include <vector>
#include <algorithm>
#include <functional>

int main() {
    int a = 10, b = 20;

    // 1. Basic lambda, no capture
    auto add = [](int x, int y) { return x + y; };
    std::cout << "5 + 3 = " << add(5, 3) << "\n";

    // 2. Capture by value
    auto sumVal = [a, b]() { return a + b; };
    std::cout << "sumVal = " << sumVal() << "\n";

    // 3. Capture by reference
    auto sumRef = [&a, &b]() { return a + b; };
    a = 15;
    std::cout << "sumRef = " << sumRef() << "\n";

    // 4. Capture all by value / reference
    auto allByVal = [=]() { return a + b; }; // captures all local vars by value
    auto allByRef = [&]() { return a + b; }; // captures all local vars by reference

    // 5. Mutable lambda (modify captured by value)
    auto mutableLambda = [a]() mutable { a += 5; return a; };
    std::cout << "mutableLambda = " << mutableLambda() << "\n"; // modifies copy of a

    // 6. Lambda with explicit return type
    auto divide = [](double x, double y) -> double { return x / y; };
    std::cout << "10 / 2 = " << divide(10, 2) << "\n";

    // 7. Using lambdas with STL algorithms
    std::vector<int> vec = {1, 2, 3, 4, 5};
    std::for_each(vec.begin(), vec.end(), [](int &n){ n *= 2; }); // doubles all elements

    for (int n : vec) std::cout << n << " ";
    std::cout << "\n";

    // 8. Storing lambda in std::function
    std::function<int(int,int)> func = add;
    std::cout << "func(7,8) = " << func(7,8) << "\n";

    return 0;
}
```
