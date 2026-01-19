# Array

- Array library notes

## Index

- [Index](#index)
- [Overview](#overview)
- [Example Usage](#example-usage)

## Overview

- When working w/ C++, vector / C++ array use is standard over classic C style arrays
- Arrays implemented in the standard library in C++ are to be used if you know the size of the array at compile time
- Provides type safety and helper functions that vectors provide, while being a bit more time/space efficient
- Array quirks:
  - Fixed size
  - No heap allocation (vectors have heap allocation)
  - Better cache locality due to being stored contiguously in memory
  - Better odds for compiler optimization

## Example Usage

```
#include <array>
#include <iostream>
#include <algorithm>

int main() {
    // 1. Declaration
    std::array<int, 5> arr = {1, 2, 3, 4, 5};

    // 2. Access
    std::cout << arr[0] << "\n";      // fast, unchecked
    std::cout << arr.at(1) << "\n";   // bounds-checked

    // 3. Size & properties
    std::cout << arr.size() << "\n";
    std::cout << std::boolalpha << arr.empty() << "\n";

    // 4. Iteration
    for (int x : arr) {
        std::cout << x << " ";
    }
    std::cout << "\n";

    // 5. Fill entire array
    arr.fill(7);

    // 6. Using STL algorithms
    std::sort(arr.begin(), arr.end());

    // std::array supports all STL algorithms because it has iterators
    int sum = std::accumulate(arr.begin(), arr.end(), 0);

    std::cout << "Sum: " << sum << "\n";

    // 7. Tuple-like features
    auto& first = std::get<0>(arr);   // compile-time index
    std::cout << "First: " << first << "\n";

    // 8. Comparison
    std::array<int, 3> a = {1, 2, 3};
    std::array<int, 3> b = {1, 2, 4};

    std::cout << (a < b) << "\n"; // lexicographical compare

    // 9. Structured bindings (C++17)
    std::array<int, 3> coords = {10, 20, 30};
    auto [x, y, z] = coords;
    std::cout << x << ", " << y << ", " << z << "\n";

    return 0;
}
```
