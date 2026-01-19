# Map

- Map library notes

## Index

- [Index](#index)
- [Overview](#overview)
- [Example Usage](#example-usage)

## Overview

- Maps are associative containers that store key-value pairs using balanced binary search trees (usually red-black tree)
- Properties include:
  - Sorted by key
  - O(logn) lookup, insertion, and deletion
  - Keys are unique
  - Stable references- inserting doesn't invalidate interators except the inserted one
- Don't use when:
  - Order doesn't matter
  - Average-case performance is important
  - Keys are very frequently accessed

## Example Usage

```
#include <iostream>
#include <map>
#include <string>

int main() {
    // ---- Creating and initializing a map ----
    std::map<std::string, int> ages {
        {"Alice", 30},
        {"Bob", 25},
        {"Charlie", 35}
    };

    // ---- Insertion ----
    ages.insert({"David", 40});
    ages.emplace("Eve", 28);

    // operator[] inserts default value if not present
    ages["Frank"] = 50;

    // ---- Accessing values ----
    std::cout << "Alice: " << ages["Alice"] << "\n";

    // at() throws on missing key
    try {
        std::cout << ages.at("Unknown") << "\n";
    } catch (const std::out_of_range&) {
        std::cout << "Key not found\n";
    }

    // ---- Searching ----
    if (auto it = ages.find("Bob"); it != ages.end()) {
        std::cout << "Found Bob, age = " << it->second << "\n";
    }

    // ---- Check if key exists (count) ----
    if (ages.count("Charlie")) {
        std::cout << "Charlie exists\n";
    }

    // ---- Iterating (in sorted order) ----
    for (const auto& [name, age] : ages) {
        std::cout << name << ": " << age << "\n";
    }

    // ---- Erasing ----
    ages.erase("Alice");                // by key
    ages.erase(ages.find("Bob"));       // by iterator

    // ---- Lower and upper bounds ----
    auto lb = ages.lower_bound("C");    // first key >= "C"
    auto ub = ages.upper_bound("C");    // first key > "C"

    // ---- Size / empty ----
    std::cout << "Size: " << ages.size() << "\n";

    return 0;
}
```
