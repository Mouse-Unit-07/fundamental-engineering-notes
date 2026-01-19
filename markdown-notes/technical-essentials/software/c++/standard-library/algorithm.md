# Algorithm

- Algorithm library notes

## Index

- [Index](#index)
- [Overview](#overview)
- [Example Usage](#example-usage)

## Overview

- Provides generic utilities for min/max, find, count, copy, move, replace, swap ranges, sort, etc

## Example Usage

```
#include <iostream>
#include <vector>
#include <algorithm> // core algorithms

int main() {
    std::vector<int> v = {3, 1, 4, 1, 5, 9, 2, 6};

    // --- sort ---
    std::sort(v.begin(), v.end());

    // --- find ---
    auto it = std::find(v.begin(), v.end(), 5);
    if (it != v.end()) std::cout << "Found 5 at index " << std::distance(v.begin(), it) << "\n";

    // --- count_if ---
    int evens = std::count_if(v.begin(), v.end(), [](int x){ return x % 2 == 0; });
    std::cout << "Number of even elements: " << evens << "\n";

    // --- transform (modify) ---
    std::transform(v.begin(), v.end(), v.begin(), [](int x){ return x*x; }); // square each element

    // --- min/max ---
    auto [min_it, max_it] = std::minmax_element(v.begin(), v.end());
    std::cout << "Min: " << *min_it << ", Max: " << *max_it << "\n";

    // --- accumulate (sum) ---
    int sum = std::accumulate(v.begin(), v.end(), 0);
    std::cout << "Sum of squares: " << sum << "\n";

    // --- all_of ---
    if (std::all_of(v.begin(), v.end(), [](int x){ return x >= 0; }))
        std::cout << "All elements are non-negative\n";

    return 0;
}
```
