# C++ Square Brackets Overloading

- C++ square bracket tokens overloading notes

## Index

- [Index](#index)
- [Overview](#overview)
- [Array New/Delete](#array-newdelete)
- [Attribute Syntax](#attribute-syntax)
- [GNU or MSVC Extensions](#gnu-or-msvc-extensions)
- [Lambda Capture Lists](#lambda-capture-lists)
- [User-Defined Overload: Subscript](#user-defined-overload-subscript)

## Overview

- In C, `[]` are used for:
  - Array subscripting and declaration
  - Designated initialization
- C++ adds more meaning- below list helps sanity check what the tokens mean

## Array New/Delete

```
int* p = new int[10]; // this is the same as C
delete[] p;           // ...but this isn't
```

## Attribute Syntax

```
[[nodiscard]]
```

## GNU or MSVC Extensions

```
int a[10] __attribute__((aligned(16)));
```

## Lambda Capture Lists

```
[x, &y]() { return x + y; }
```

## User-Defined Overload: Subscript

- Overloading the `[]` operator allows for:
  - Smart pointers
  - Containers
  - Proxy objects
  - Custom string classes

```
class Vec {
public:
    int operator[](int i) const { return data[i]; }
private:
    int data[10];
};
```
