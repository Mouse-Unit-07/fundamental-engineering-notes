# IO

- IO libraries notes

## Index

- [Index](#index)
- [Overview](#overview)
- [Example Usage](#example-usage)

## Overview

- Standard IO library headers in C++ include:
- `<iostream>`
  - Console IO (`std::cin`, `std::cout`, `std::cerr`, `std::clog`)
- `<istream>`, `<ostream>`
  - Base classes for IO streams
- `<iomanip>`
  - Manipulators (`std::setw`, `std::setprecision`)
- `<fstream>`
  - File IO (`std::ifstream`, `std::ofstream`, `std::fstream`)
- `<sstream>`
  - String-based IO (`std::istringstream`, `std::ostringstream`, `std::stringstream`)
- `<cstdio>`
  - Legacy
- Best practices include:
  - Checking stream state after input
    - Methods to `cin` include `good()`, `fail()`, `bad()`, `eof()`
  - Use `std::ostringstream` for safe string building
  - Prefer `\n` to `std:endl` unless you need a flush
    - Endl is slower due to including the flush

## Example Usage

```
#include <iostream>
#include <iomanip>
#include <fstream>
#include <sstream>
#include <string>

int main() {
    // -------- Console Output --------
    std::cout << "Enter a number: " << std::flush;

    // -------- Console Input w/ Validation --------
    int x;
    if (!(std::cin >> x)) {
        std::cerr << "Invalid input!\n";
        return 1;
    }

    // -------- Formatting Output --------
    std::cout << std::hex << std::showbase
              << "Hex value: " << x << "\n";

    std::cout << std::dec << std::setw(10) << std::setfill('*')
              << "Padded: " << x << "\n";

    std::cout << std::boolalpha << "x > 10? " << (x > 10) << "\n";

    // -------- File Output (RAII) --------
    std::ofstream fout("output.txt");
    if (!fout) {
        std::cerr << "Failed to open file\n";
        return 1;
    }
    fout << "You entered: " << x << "\n";
    // auto-closed on scope exit

    // -------- File Input --------
    std::ifstream fin("output.txt");
    std::string line;
    while (std::getline(fin, line)) {
        std::cout << "From file: " << line << "\n";
    }

    // -------- String Streams --------
    std::ostringstream oss;
    oss << "Value doubled = " << (x * 2);

    std::string built = oss.str();  // build a string safely
    std::cout << built << "\n";

    // Parsing with istringstream
    std::istringstream iss("100 200");
    int a, b;
    iss >> a >> b;
    std::cout << "Parsed: " << a << ", " << b << "\n";

    return 0;
}
```
