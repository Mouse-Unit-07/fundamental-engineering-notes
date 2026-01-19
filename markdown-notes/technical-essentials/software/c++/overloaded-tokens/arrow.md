# C++ Arrow Overloading

- C++ Arrow token overloading notes

## Index

- [Index](#index)
- [Overview](#overview)
- [Call Overloaded Functions / Dependent Names](#call-overloaded-functions--dependent-names)
- [Pointer-to-Member Function/Data](#pointer-to-member-functiondata)
- [User-Defined Overload: Arrow](#user-defined-overload-arrow)

## Overview

- In C, `->` operator is used just for pointer-to-struct/union member access
  - This is to counter the way the member access operator has higher precedence than the dereference operator
- C++ adds more meaning- below list helps sanity check what the tokens mean

## Call Overloaded Functions / Dependent Names

- Just another instance of member access use of `->`

```
ptr->template method<T>();
```

## Pointer-to-Member Function/Data

- The ->\* token is used w/ pointer-to-member functions and data
- ...Niche- best to avoid if possible
- Use lambda functions instead

```
(obj->*pmf)(5);
```

## User-Defined Overload: Arrow

- Encountered if a library defines a class w/ an overloaded `->` operator, or if your new class needs it

```
class Ptr {
public:
    T* operator->();
};

Ptr p;
p->member;      // calls p.operator->(), then accesses that pointer

iter->member; // -> operator overloaded for iterators

```
