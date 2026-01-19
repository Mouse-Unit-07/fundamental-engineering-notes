# cstddef

- cstddef library notes

## Index

- [Index](#index)
- [Overview](#overview)
- [Example Usage](#example-usage)

## Overview

- Provides `size_t` lol
- Also provides a safe byte type to use

## Example Usage

```
#include <iostream>
#include <cstddef>   // <--- this header

struct Point {
    int x;
    int y;
};

void accepts_nullptr(std::nullptr_t) {
    std::cout << "Got nullptr\n";
}

int main() {
    // --- size_t ---
    std::size_t count = 5;

    // --- ptrdiff_t ---
    int arr[10];
    int* p1 = &arr[2];
    int* p2 = &arr[7];
    std::ptrdiff_t diff = p2 - p1;   // = 5

    // --- nullptr_t ---
    accepts_nullptr(nullptr);

    // --- byte ---
    std::byte b = std::byte{0b00001111};
    b <<= 1;  // shift
    std::cout << std::to_integer<int>(b) << "\n";

    // --- offsetof ---
    std::cout << "Offset of y is: "
              << offsetof(Point, y) << " bytes\n";

    // --- max_align_t ---
    alignas(std::max_align_t) char storage[64];

    return 0;
}
```
