# C++ Dot Overloading

- C++ dot token overloading notes

## Index

- [Index](#index)
- [Overview](#overview)
- [Calling Overloaded Operators](#calling-overloaded-operators)
- [Dependent `template` Disambiguator](#dependent-template-disambiguator)
- [Member Access](#member-access)
- [Member Pointers](#member-pointers)
- [Smart Pointer Member Access](#smart-pointer-member-access)

## Overview

- In C, `.` is used for:
  - Member/attribute access for structs/unions
  - Designated initializers in C99+ (not recommended or portable)
    - `struct S s = { .x = 10, .y = 20 };`
  - Decimal point
- C++ adds more meaning- below list helps sanity check what the tokens mean

## Calling Overloaded Operators

- ...Weird and discouraged, but legal

```
obj.operator+(5);
obj.operator;
```

## Dependent `template` Disambiguator

- Needed when calling a templated member function on a dependent type

```
// in the format obj.template foo<T>()
obj.template method<int>();
```

## Member Access

- Same as C, but additionally applies to members in classes
- Good for:
  - Reference members
  - Inherited members
  - Static data members
  - Static member functions
  - Overloaded members
  - Dependent members (templates)

```
obj.x;
obj.func();
```

## Member Pointers

- If a member is a pointer and you need to dereference it, you use the `.*` operator
- Confusing to look at, so avoid if possible

```
(obj.*pmf)(5);
obj.*pmd = 10;
```

## Smart Pointer Member Access

- The `->` operator is overloaded for smart pointers, so `.` operator is the way to go

```
std::unique_ptr<Foo> p;
p.get();       // using . on smart pointer object
```
