# C++ Curly Braces Overloading

- C++ curly brace tokens overloading notes

## Index

- [Index](#index)
- [Overview](#overview)
- [`new` Expressions w/ Braces](#new-expressions-w-braces)
- [`using` Declarations for Enum Classes](#using-declarations-for-enum-classes)
- [Braced Function Parameters- Lambda Captures](#braced-function-parameters--lambda-captures)
- [Initialization](#initialization)
- [Return-Braced-Value](#return-braced-value)
- [Structured Bindings](#structured-bindings)
- [Synthetic Uses in Templates](#synthetic-uses-in-templates)
- [Throwing Braced Value](#throwing-braced-value)

## Overview

- In C, `{}` are used for:
  - Compound statements
  - Initializer lists for aggregate types (structs, unions, enums)
  - Designated initializers
    - ...Method of explicitly initializing attributes in structs, introduced in C99
- The `{}` tokens are heavily overloaded in C++...
- Below list helps sanity check what the tokens mean

## `new` Expressions w/ Braces

```
auto p = new X{1, 2};
```

## `using` Declarations for Enum Classes

- Introduced in C++11
- Prevents polluting the namespace w/ enum names

```
enum class Color { Red, Blue };
Color c{Color::Red}; // in place of Color c = Red;
```

## Braced Function Parameters- Lambda Captures

- Introduced in C++14
- Used for lambda captures w/ brace initializers

```
auto f = [x{42}](){};
```

## Initialization

- When working w/ C++11, everything should be initialized w/ `{}`

```
//------------------------------------------------------------------------------
/* Uniform init */
// ...as this long list shows, everything can be initialized w/ braces
int x{5};
std::string s{"hello"};
std::vector<int> v{1,2,3};

struct S { int x, y; };
S s{1, 2};

//------------------------------------------------------------------------------
/* List init that suppresses narrowing */
// implicit casting cause compiler errors
int x{3.14};   // ERROR (narrowing)
int y = 3.14;  // OK (implicit conversion)

//------------------------------------------------------------------------------
/* Member init in constructors */
struct S {
    int x;
    S() : x{5} { /* constructor guts here */ }
};

//------------------------------------------------------------------------------
/* Value init */
int x{};     // zero-initialize
X obj{};     // value-initialize object (calls constructor or zero)

//------------------------------------------------------------------------------
/* Empty-brace zero init */
int x{};       // = 0
double d{};    // = 0.0
S s{};         // all members zero

//------------------------------------------------------------------------------
/* Cast-like list init */
X obj{1,2};         // initialization
X obj2 = X{1,2};    // functional cast-style list initialization
auto y = int{5.0};  // list-initialization cast (can forbid narrowing)

//------------------------------------------------------------------------------
/* Static data member init */
struct S {
    static inline std::vector<int> v{1,2,3};
};

//------------------------------------------------------------------------------
/* Base-class member subobject list init */
struct D : B {
    D() : B{1}, member{2,3} { /* constructor guts here */ }
};

//------------------------------------------------------------------------------
/* Brace-or-equal initializers in class definitions */
// Introduced in C++11
struct S {
    int x = 3; // allowed, but below preferred to suppress narrowing
    int y{4};  // nice
};

//------------------------------------------------------------------------------
/* Initializer-list for range-based for loops */
//Introduced in C++11
for (auto x : {1,2,3}) {
    ...
}

//------------------------------------------------------------------------------
/* Designated initializers */
// Introduced in C++20
Point p = {.x = 1, .y = 2};

//------------------------------------------------------------------------------
/* `std::initializer_list` temporary objects */
auto il = {1,2,3};  // creates std::initializer_list<int>

//------------------------------------------------------------------------------
/* Thread constructor init */
std::thread t{func, 1, 2, 3};
```

## Return-Braced-Value

- Valid if returning an aggregate type, or an initializer-list capable type

```
return {1, 2};
```

## Structured Bindings

- Introduced in C++17
- Used for decomposition declaration grammar

```
std::tuple<int, int> some_pair{1, 2};
auto [a, b] = some_pair;

//...under the hood, the above is equivalent to:
auto&& __tmp = t;
decltype(auto) a = std::get<0>(__tmp);
decltype(auto) b = std::get<1>(__tmp);
```

## Synthetic Uses in Templates

```
template <class T>
void foo(T);

foo({1,2,3});  // deduces initializer_list<int>
```

## Throwing Braced Value

```
throw MyError{42, "bad"};
```
