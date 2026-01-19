# C++ Namespace

- Namespaces in C++ notes

## Index

- [Index](#index)
- [Overview](#overview)
- [Example Usage](#example-usage)

## Overview

- Just like in C, namespaces are scopes that group identifiers (types, functions, variables) to avoid naming collisions and to organize code
- Best practices include:
  - Never add anything to the `std` namespace
  - Avoid `using namespace std` in headers
    - Causes pollution of the global namespace w/ everything in the standard library
- Namespaces are open
  - You can add names to a namespace from other namespaces
- A namespace should
  - Express a logically coherent set of features
  - Not give users access to unrelated features
  - Not impose a significant notational burden on users

## Example Usage

```
#include <iostream>
#include <vector>

// 1. Basic namespace
namespace math {
    int add(int a, int b) { return a + b; }
}

// 2. Nested namespace (C++17 compact syntax)
namespace company::utils {
    void log(const std::string& msg) {
        std::cout << "[LOG] " << msg << "\n";
    }
}

// 3. Namespace alias
namespace cu = company::utils;

// 4. Anonymous namespace (internal linkage)
namespace {
    int hiddenValue = 42;  // only visible within this translation unit
}

// 5. Extending a namespace across multiple blocks
namespace math {
    int multiply(int a, int b) { return a * b; }
}

// 6. Inline namespace (versioning)
namespace api {
    inline namespace v1 {   // default version
        void hello() { std::cout << "API v1\n"; }
    }
    namespace v2 {
        void hello() { std::cout << "API v2\n"; }
    }
}

int main() {

    // Basic namespace usage
    std::cout << math::add(2, 3) << "\n";
    std::cout << math::multiply(3, 4) << "\n";

    // Nested namespace usage
    company::utils::log("Hello from nested namespace");

    // Alias usage
    cu::log("Using namespace alias");

    // Accessing anonymous namespace variable
    std::cout << "hiddenValue = " << hiddenValue << "\n";

    // Inline namespace: v1 chosen by default
    api::hello();

    // Explicit call to v2
    api::v2::hello();

    // Standard namespace usage
    std::vector<int> v = {1, 2, 3};
    std::cout << "v size = " << v.size() << "\n";

    return 0;
}
```
