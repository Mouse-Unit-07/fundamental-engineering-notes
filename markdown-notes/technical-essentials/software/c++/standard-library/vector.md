# Vector

- Vector library notes

## Index

- [Index](#index)
- [Overview](#overview)
- [Example Usage](#example-usage)

## Overview

- When working w/ C++, vector / C++ array use is standard over classic C style arrays
- Vectors allow for:
  - Size flexibility
  - Memory management
  - Bounds safety
  - Copy / assignment
  - Insertion / deletion
  - Iteration
  - Compatibility w/ STL

## Example Usage

```
#include <iostream>
#include <vector>
#include <algorithm>  // for sort, find

int main() {
    // 1. Declaration
    std::vector<int> v1;                // empty vector
    std::vector<int> v2 = {1, 2, 3, 4}; // initializer list
    std::vector<int> v3(5, 10);         // 5 elements, all 10

    // 2. Accessing elements
    v2[0] = 100;        // no bounds checking
    std::cout << v2.at(1) << "\n"; // bounds-checked

    // 3. Adding elements
    v1.push_back(42);   // append to end
    v1.emplace_back(99); // construct in place

    // 4. Removing elements
    v1.pop_back();      // remove last element
    v2.erase(v2.begin() + 1); // remove element at index 1
    v3.clear();         // remove all elements

    // 5. Iteration
    std::cout << "v2 elements: ";
    for (int x : v2) { // range-based for
        std::cout << x << " ";
    }
    std::cout << "\n";

    std::cout << "v1 elements using iterators: ";
    for (auto it = v1.begin(); it != v1.end(); ++it) {
        std::cout << *it << " ";
    }
    std::cout << "\n";

    // 6. Size and capacity
    std::cout << "v2 size: " << v2.size() << ", capacity: " << v2.capacity() << "\n";
    v2.reserve(20); // pre-allocate memory

    // 7. Searching & algorithms
    auto it = std::find(v2.begin(), v2.end(), 100);
    if (it != v2.end()) std::cout << "Found 100 at index " << std::distance(v2.begin(), it) << "\n";

    std::sort(v2.begin(), v2.end()); // sort vector

    return 0;
}
```
