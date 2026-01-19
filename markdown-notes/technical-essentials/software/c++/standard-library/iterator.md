# Iterator

- Iterator library notes

## Index

- [Index](#index)
- [Overview](#overview)
- [Example Usage](#example-usage)

## Overview

- Provides a generic iterator utility in case you need sequential access through containers defined in the standard library

## Example Usage

```
#include <iostream>
#include <vector>
#include <list>
#include <iterator>
#include <algorithm>

int main() {
    std::vector<int> v = {1, 2, 3, 4, 5};
    std::list<int> l;

    // --- basic iterators ---
    for(auto it = std::begin(v); it != std::end(v); ++it) {
        std::cout << *it << " ";
    }
    std::cout << "\n";

    // --- reverse iterators ---
    for(auto rit = std::rbegin(v); rit != std::rend(v); ++rit) {
        std::cout << *rit << " ";
    }
    std::cout << "\n";

    // --- inserters ---
    std::copy(v.begin(), v.end(), std::back_inserter(l));

    // --- ostream iterator ---
    std::copy(l.begin(), l.end(), std::ostream_iterator<int>(std::cout, ", "));
    std::cout << "\n";

    // --- distance & advance ---
    auto it = l.begin();
    std::advance(it, 3);                  // move 3 steps forward
    std::cout << "4th element: " << *it << "\n";
    std::cout << "Distance from begin to it: " << std::distance(l.begin(), it) << "\n";

    // --- iterator traits ---
    using traits = std::iterator_traits<decltype(v.begin())>;
    static_assert(std::is_same<traits::value_type, int>::value, "value_type is int");

    return 0;
}
```
