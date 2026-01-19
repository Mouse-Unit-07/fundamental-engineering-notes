# C++ Asterisk Overloading

- C++ asterisk token overloading notes

## Index

- [Index](#index)
- [Overview](#overview)
- [Fold Expressions](#fold-expressions)
- [Overloaded `operator*()` for Iterators/Smart Pointers](#overloaded-operator-for-iteratorssmart-pointers)
- [Pointer-to-Member Declarator/Dereference](#pointer-to-member-declaratordereference)
- [User-Defined Overload: Dereference](#user-defined-overload-dereference)
- [User-Defined Overload: Multiplication](#user-defined-overload-multiplication)

## Overview

- In C, `*` is used for:
  - Multiplication operator, multiply assignment
  - Pointer declarator
  - Pointer dereference (optionally for function pointers too)
- C++ adds more meaning- below list helps sanity check what the tokens mean

## Fold Expressions

- Ok- good to use

```
(auto product = ... * args);
```

## Overloaded `operator*()` for Iterators/Smart Pointers

- Ok- iterators and smart pointers are defined this way

```
auto it = vec.begin();
int x = *it;

std::unique_ptr<Foo> p;
(*p).bar(); // ugly, but legal
p->bar();   // that's the whole point of why -> is overloaded
```

## Pointer-to-Member Declarator/Dereference

- ...awkward, but ok
- Not many practical use cases

```
// declarator
struct A { int x; };
int A::* p = &A::x;

// dereference
A a;
int A::* pm = &A::x;
a.*pm = 10;   // object pointer-to-member access
A* pa = &a;
pa->*pm = 10; // pointer pointer-to-member access
```

## User-Defined Overload: Dereference

- ...You could use smart pointers or iterators instead, but legal

```
T& operator*() { return value; }
```

## User-Defined Overload: Multiplication

- Ok- good to use

```
Vector operator*(double scalar);
Vector operator*(const Matrix&, const Vector&);
```
