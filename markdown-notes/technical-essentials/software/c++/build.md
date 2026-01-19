# C++ Build

- C++ build notes

## Index

- [Index](#index)
- [Overview](#overview)
- [Compilation](#compilation)
- [Linkage](#linkage)
- [Preprocessing](#preprocessing)

## Overview

- C++ is a superset of C, and the build/compile/link process is mostly identical, but C++ has different symbol naming rules, type systems, and standard libraries
- But otherwise, the preprocess -> compile -> assemble -> link toolchain is identical

## Compilation

- Compared to C, C++ has different:
- Type systems
  - Forbids implicit `void*` to typed pointer casts
  - Treats `struct`s as full classes
  - Has references, classes, templates, overloads, constructors/destructors
  - Allows implicit function declarations
- Name mangling
  - Encodes below into each symbol name:
    - Function name
    - Namespace
    - Class
    - Parameter types
    - Overloads
    - Templates

## Linkage

- `extern "C"` exists for C++ due to symbol name differences between C and C++
- C
  - Generates "unmangled symbols", so each symbol has no excessive information tied to each
- C++
  - Generates "mangled symbols", where types, namespaces, overloads, and templates are encoded in each symbol
  - Expect other metadata like
    - Constructor/destructor registration
    - Exception-handling tables
    - RTTI metadata
    - Static initialization code
  - Need support for
    - `.ctors` / `.dctors` lists
    - `.eh_frame` or `.gcc_except_table`
    - "vtable" layout symbols
- This difference causes undefined reference errors when C code in C++ source files aren't specified to be C code

## Preprocessing

- Compared to C, C++ has different:
  - Rules for macro expansion w/ templates
  - Built-in macros (like `__cplusplus`)
  - Behavior for keywords (`new`, `class`, `this`)
  - Header inclusion semantics
