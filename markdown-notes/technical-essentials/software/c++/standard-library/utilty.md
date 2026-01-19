# Utility

- Utility library notes

## Index

- [Index](#index)
- [Overview](#overview)
- [Example Usage](#example-usage)

## Overview

- Utility library in C++ provides moving, forwarding, pair, swapping, exchanging, declval, etc
- Primarily used for:
  - Move semantics
  - Forwarding in generic code
  - Returning two things
  - Swapping

## Example Usage

```
#include <iostream>
#include <string>
#include <utility>   // <--- the star

// Perfect-forwarding factory
template <class T, class... Args>
T make_obj(Args&&... args) {
    return T(std::forward<Args>(args)...);
}

class Person {
public:
    std::string name;

    Person(std::string n) : name(std::move(n)) {} // use move semantics
};

int main() {
    // --- move ---
    std::string s = "Alice";
    std::string s2 = std::move(s);   // s is now empty/moved-from

    // --- forward ---
    Person p = make_obj<Person>("Bob");

    // --- pair ---
    std::pair<int, std::string> pr(42, "hello");
    auto pr2 = std::make_pair(10, std::string("world"));

    // --- swap ---
    int a = 1, b = 2;
    std::swap(a, b);

    // --- exchange ---
    int old = std::exchange(a, 99); // a becomes 99, old=2

    // --- index sequence (small demo) ---
    auto tup = std::make_tuple(1, 2, 3);
    std::apply([](auto... xs){
        ((std::cout << xs << ' '), ...);
    }, tup);

    return 0;
}
```
