# String

- String library notes

## Index

- [Index](#index)
- [Overview](#overview)
- [Example Usage](#example-usage)

## Overview

- When working w/ C++, string (the C++ class) use is standard over classic C style strings
- C++ strings allow for:
  - Memory management
  - Size
  - Overflow safety
  - Concatenation
  - Copying
  - STL Compatibility
  - Flexibility (conversion helpers, etc)

## Example Usage

```
#include <iostream>
#include <string>
#include <algorithm> // for sort, transform

int main() {
    // 1. Declaration
    std::string s1;                       // empty string
    std::string s2 = "Hello";             // initialization
    std::string s3("World");              // constructor
    std::string s4(5, '!');               // "!!!!!" repeated character

    // 2. Accessing characters
    s2[0] = 'h';                          // no bounds checking
    std::cout << s2.at(1) << "\n";        // bounds-checked

    // 3. Concatenation
    std::string s5 = s2 + " " + s3;       // using +
    s5.append("!!!");                      // append method

    std::cout << s5 << "\n";              // Output: "hello World!!!"

    // 4. Size and capacity
    std::cout << "Length: " << s5.size() << "\n";
    std::cout << "Capacity: " << s5.capacity() << "\n";

    // 5. Searching
    size_t pos = s5.find("World");
    if (pos != std::string::npos)
        std::cout << "'World' found at position " << pos << "\n";

    // 6. Substring
    std::string s6 = s5.substr(pos, 5);   // "World"

    // 7. Removing / replacing
    s5.replace(0, 5, "Hi");               // replace first 5 characters
    s5.erase(2, 7);                        // remove 7 characters starting at index 2

    // 8. Iteration
    for (char c : s6) std::cout << c << " ";
    std::cout << "\n";

    // 9. Conversion
    std::string numStr = "123";
    int num = std::stoi(numStr);           // string to int
    double d = std::stod("3.14");          // string to double

    // 10. STL algorithms
    std::transform(s6.begin(), s6.end(), s6.begin(), ::toupper); // to uppercase
    std::cout << s6 << "\n";              // Output: "WORLD"

    return 0;
}
```
