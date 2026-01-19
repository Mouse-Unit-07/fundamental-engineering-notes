# C++ Parenthesis Overloading

- C++ parenthesis tokens overloading notes

## Index

- [Index](#index)
- [Overview](#overview)
- [`noexcept` operator](#noexcept-operator)
- [Default Constructor](#default-constructor)
- [Exception Specifications](#exception-specifications)
- [Function-Style Cast](#function-style-cast)
- [Initialization](#initialization)
- [Lambda Invocation](#lambda-invocation)
- [Parameter Packs / Variadic Templates](#parameter-packs--variadic-templates)
- [Parentheses in `decltype` and `typeid`](#parentheses-in-decltype-and-typeid)
- [Placement New](#placement-new)
- [Structured Bindings](#structured-bindings)
- [User-Defined Overload: Function Call](#user-defined-overload-function-call)

## Overview

- In C, `()` are used for:
  - Function call
  - Function declaration
  - Casting
  - Expressions for `return`, `if`, `while`, `for`, `switch`
  - Specifying precedence
  - Function pointer declarators
  - Macro argument lists
  - Attributes
- C++ adds more meaning- below list helps sanity check what the tokens mean
- CAUTION- many of below uses are obsolete starting C++11

## `noexcept` operator

- Ok- required and good to use

```
/* Specifier on functions */
// Used to declare that a function does not throw
void f() noexcept;                 // no parenthesis needed for usual simple case
void g() noexcept(noexcept(f()));  // needed if the specifier takes an expression- second noexcept is the operator

/* noexcept operator */
// Used for checking whether an expression can throw at compile time
noexcept(expr)   // parentheses required
```

## Default Constructor

- Obsolete, but legal
- Also a vexing parse
- Use `{}` for constructor calls instead

```
T obj{arg1, arg2};   // avoids narrowing, no vexing parse
```

## Exception Specifications

- Obsolete- `thow()` is reserved for old C++ altogether
- `noexcept` is the only exception specifier in modern C++

```
void f() throw(int);      // parentheses are part of the grammar
```

## Function-Style Cast

- Obsolete, but legal
- Casting should be avoided, or made explicit w/ C++'s new set of casting semantics

```
float x = 1.9;
int y = int(x);
```

## Initialization

- Overall all obsolete- use `{}` instead

```
//------------------------------------------------------------------------------
/* Function-Style Initialization */
// Known as the "most vexing parse"
// ...Famous default constructor vs function call confusion
// Answer is that it's a function call, but that's not the point
// Use `{}` for initialization instead

int x();   // “most vexing parse”

//------------------------------------------------------------------------------
/* Aggregate Initialization */
// Use `{}` for initialization instead

S s(1, 2);      // allowed for aggregates before C++20 only sometimes
S s{1, 2};      // ✓ correct, modern
```

## Lambda Invocation

- Ok- required and good to use

```
auto f = [](int x) { return x+1; };
```

## Parameter Packs / Variadic Templates

- Ok- required and good to use

```
template<typename... Args>
void foo(Args... args) { bar(args...); }
```

## Parentheses in `decltype` and `typeid`

- Ok- required and good to use

```
int x;
decltype(x) a;     // int
decltype((x)) b;   // int&   <-- parentheses change meaning!
```

## Placement New

- Ok- the parenthesis after the `new` is required and good to use
- Constructors should be called w/ `{}`

```
void* p = ...;
T* t = new(p) T();    // don't do this- parentheses here call a constructor
T* t = new(p) T{};    // do this instead- uniform initialization
```

## Structured Bindings

- NOT needed- just a note that lvalues don't use parenthesis

```
auto [a, b] = some_pair(); // legal
auto (a, b) = some_pair(); // NOT illegal
```

## User-Defined Overload: Function Call

- Ok- required and good to use

```
struct F { int operator()(int); };
F f;
f(42);
```
