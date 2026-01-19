# C++ Angle Brackets Overloading

- C++ angle bracket tokens overloading notes

## Index

- [Index](#index)
- [Overview](#overview)
- [`decltype`, `auto`, Trailing Return Types](#decltype-auto-trailing-return-types)
- [Concepts](#concepts)
- [Structured Bindings](#structured-bindings)
- [Templates](#templates)
- [User-Defined Overload: Relational, Shifting](#user-defined-overload-relational-shifting)

## Overview

- In C, `<>` are used for:
  - Relational, equality, shift operators
  - Including headers
- C++ adds more meaning- below list helps sanity check what the tokens mean

## `decltype`, `auto`, Trailing Return Types

```
auto x = std::vector<int>{};

decltype(foo<int>()) val;
```

## Concepts

```
// concept definition
template <typename T>
concept Number = requires (T x) {
    { x + x } -> std::same_as<T>;
};

// constrained template using angle brackets
template <Number T>
void foo(T);
```

## Structured Bindings

```
auto [a, b] = pair<int, int>{1,2};
```

## Templates

```
//------------------------------------------------------------------------------
/* Basics */
// Template parameter list
template <typename T, int N>
struct Array { };

// Template argument list
Array<int, 10> arr;
foo<Bar>();

// Empty angle brackets <> meaning “use template argument deduction”
make_unique<Foo>();
std::vector<int> v;

//------------------------------------------------------------------------------
/* Template disambiguation rules (C++11+) */
T::template foo<U>();     // `template` keyword required sometimes

//...and then when parsing:
a < b, c > d // compiler needs to guess whether the angle bracket is a relational operator or template bracket

//------------------------------------------------------------------------------
/* Nested templates and >> fix (C++11) */
std::vector<std::vector<int> >   // before C++11, MUST have space between >>

std::vector<std::vector<int>>    // after C++11

//------------------------------------------------------------------------------
/* Less-than/greater-than in type traits and metaprogramming */
std::is_same<T, U>::value
std::enable_if<(N < 10), int>::type

```

## User-Defined Overload: Relational, Shifting

```
T operator<(const T&, const T&);
T operator>(const T&, const T&);
T operator<<(const T&, const T&);
T operator>>(const T&, const T&);
```
