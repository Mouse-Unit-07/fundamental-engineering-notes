# C++ Ampersand Overloading

- C++ ampersand token overloading notes

## Index

- [Index](#index)
- [Overview](#overview)
- [Forwarding / Universal Reference](#forwarding--universal-reference)
- [Lambda Capture](#lambda-capture)
- [Lvalue Reference Declarator](#lvalue-reference-declarator)
- [Lvalue-Qualified Member Functions](#lvalue-qualified-member-functions)
- [Reference Collapsing](#reference-collapsing)
- [Rvalue Reference Declarator](#rvalue-reference-declarator)
- [Type Traits / `decltype`](#type-traits--decltype)
- [User-Defined Overload: Address-Of](#user-defined-overload-address-of)
- [User-Defined Overload: Bitwise AND](#user-defined-overload-bitwise-and)
- [User-Defined Overload: Casting](#user-defined-overload-casting)

## Overview

- In C, `&` is used for:
  - Unary address-of operator
  - Bitwise AND, equality operator w/ bitwise AND
- C++ adds more meaning- below list helps sanity check what the tokens mean

## Forwarding / Universal Reference

- Good for generic programming
- Bindings determined by template deduction rules

```
template<typename T>
void f(T&& x); // universal reference
```

## Lambda Capture

- Indicates capture by reference
- ...need to be careful to capture just what you need

```
int a = 3;
auto f = [&]() { a++; };
```

## Lvalue Reference Declarator

- Used for declaring references

```
int x = 10;
int& r = x;
```

## Lvalue-Qualified Member Functions

- Good for C++11+
- Limits a member function to lvalue objects only

```
struct X {
    void f() &;   // only callable on lvalues (named objects)
};

X x;
x.f();    // OK
X{}.f();  // ERROR — temporary (rvalue)
```

## Reference Collapsing

- References to references
  - ...ugh
- Enables safe reference composition in templates
- Rules:
  - T& & (collapses to)-> T&
  - T& && -> T&
  - T&& & -> T&
  - T&& && -> T&&

## Rvalue Reference Declarator

- Good for C++11+
- Allows for move semantics and perfect forwarding

```
std::string&& tmp = make_string();
```

## Type Traits / `decltype`

- Needed for template programming

```
std::remove_reference<T&>::type
```

## User-Defined Overload: Address-Of

- Strongly discouraged... a custom address-of operator is confusing

```
struct X {
    X* operator&();         // very rare, obscure, discouraged
};
```

## User-Defined Overload: Bitwise AND

- Ok if the use case makes sense (it's a binary AND)

```
X operator&(const X&, const X&);
```

## User-Defined Overload: Casting

- Rare, and smells like a mess waiting to happen
- C++20+

```
struct X {
    explicit operator int&();
};
```
