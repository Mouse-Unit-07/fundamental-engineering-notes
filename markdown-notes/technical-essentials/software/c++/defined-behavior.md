# C++ Defined Behavior

- Defined behavior in C++ notes

## Index

- [Index](#index)
- [Overview](#overview)
- [`const`, `constexpr`](#const-constexpr)
- [`enum class`](#enum-class)
- [`initializer_list`](#initializerlist)
- [`new` and `delete`](#new-and-delete)
- [`nullptr`](#nullptr)
- [Default Arguments](#default-arguments)
- [Explicit Casting](#explicit-casting)
- [Initialization](#initialization)
- [lvalue Reference](#lvalue-reference)
- [Macros](#macros)
- [Ranged-`for` Loop](#ranged-for-loop)
- [rvalue Reference](#rvalue-reference)
- [Scope Resolution Operator](#scope-resolution-operator)
- [Suffix Return Type](#suffix-return-type)
- [Traits](#traits)
- [Unique, Shared Pointers](#unique-shared-pointers)

## Overview

- C++ is a superset of C, so for the most part defined behavior in C applies for C++ too
- There are new semantics/features that are safer than C though

## `const`, `constexpr`

- Adds to C's incomplete implementation of constants w/ powered up `const` and new `constexpr` keywords
- `const`
  - Specifies that an assignment operation can't be used w/ the lvalue (just like C)
  - Primarily used to specify that data passed to the function isn't to be modified
- `constexpr`
  - A constant that's evaluated at compile time
  - Introduced in C++11
  - Can be applied to variables, functions, constructors, etc (it's a type qualifier)
  - Primarily for specifying constants for placement in data memory and for performance
  - Replaces macros, and serves in addition to enumerations

```
const int dmv = 17;                      // dmv is a named constant
int var = 17;                            // var is not a constant
constexpr double max1 = 1.4∗square(dmv); // OK if square(17) is a constant expression
constexpr double max2 = 1.4∗square(var); // error : var is not a constant expression
const double max3 = 1.4∗square(var);     // OK, may be evaluated at run time
double sum(const vector<double>&);       // sum will not modify its argument (§2.2.5)
vector<double> v {1.2, 3.4, 4.5};        // v is not a constant
const double s1 = sum(v);                // OK: evaluated at run time
constexpr double s2 = sum(v);            // error : sum(v) not constant expression
```

## `enum class`

- Regular C `enum`s exist, but there are `enum class`es too
- Enumerations w/in an `enum class` is restricted to use for that class name, and can't be mixed w/ other `enum class`es or integers
- You can also specify an underlying type in which to store each enum value (as opposed to a regular enum where all values are ints)

```
enum class Color { red, blue , green };
enum class Traffic_light { green, yellow, red };
enum class Flag : char{X, Y, Z}

Color col = Color::red;
Traffic_light light = Traffic_light::red;

Color x = red; // error : which red?
Color y = Traffic_light::red; // error : that red is not a Color
Color z = Color::red; // OK
```

## `initializer_list`

- `std::initializer_list` is a lightweight, compiler-generated object that allows functions and constructors to receive a list of values provided in `{}`
- It's read-only, has a size and pointer to the first element
- Used by constructor definitions of `vector`, `array`, etc

## `new` and `delete`

- Operators that replace `malloc()` and `free()` function calls
- Safer alternative, but better is to avoid them altogether and rely on RAII objects implemented in the standard library

## `nullptr`

- C++'s version of `NULL` is `nullptr`
- This is done to allow for type safe assignments
  - `NULL` in C is `(void*)0`
  - `nullptr` in C++ is `0` or `0L`

## Default Arguments

- Just like in Python, it's a way to give a function parameter a value if the caller doesn't supply one
  - Callers can go ahead and omit the argument
- `void log(const std::string& msg, int level = 1);`
- It's an implementation for clean optional parameters, but they're implicit and confusing so best to avoid

## Explicit Casting

- C++ provides explicit "named conversions" for when you need to perform dangerous type conversions:
  - `const_cast<>`
    - Getting write access to something declared `const`, or casting a `volatile` object
  - `static_cast<>`
    - Reversing a well-defined implicit conversion
    - Good for casting between:
      - Related pointer types in the same class hierarchy
      - Integral type to enumeration
      - Floating-point to integral type
  - `reinterpret_cast<>`
    - Changing the meaning of bit patterns
    - Used for unrelated types like:
      - Integer to pointer
      - Pointer to unrelated pointer type
  - `dynamic_cast<>`
    - For dynamically running type checking across pointers/references in class hierarchies

## Initialization

- In C++, you can initialize w/ below:

```
X a1 {v};
X a2 = {v};
X a3 = v;
X a4(v);

// extra:
char* my_string {new char[1024]{}} // all elements are 0
```

- The first one is from C++11 and best practice- it's called "list initialization" or "universal/uniform initialization"
- It's great because the compiler won't allow narrowing- no implicit casting
- `auto`
  - The exception is when you're using `auto`- you don't want the type deduced to something weird from the curly-brace tokens
  - Use `=` when using `auto`
- Copy vs direct initialization
  - Using the `=` is called "copy initialization (implicit conversions allowed)
  - Using `()` or `{}` is called direct initialization

## lvalue Reference

- "References" were introduced to get rid of C's default call-by-value behavior
- A reference is a non-owning alias to an existing object
- ...when you add the `const` qualifier to a variable, it's called a "const lvalue"
- Quirks include:
  - Must be initialized
  - Can't be null
  - Can't be reseated
  - No pointer arithmetic
  - No dereference operator needed
- Allows for:
  - Passing of objects by reference instead of by value
  - Space efficient passing of large objects (containers, structs, etc)
  - Cleaner object passing by avoiding pointer semantics

```
// r is x in every meaningful sense
// There is no "referenced object" separate from x, in contrast to pointers
// You cannot reseat a reference; it must bind to a valid object at initialization and stay bound forever
int x = 10;
int& r = x;  // r references x
```

## Macros

- Predefined macros in C++ include:
  - `__cplusplus`
  - `__DATE__`
  - `__TIME__`
  - `__FILE__`
  - `__LINE__`
  - `__FUNC__`
  - `__STDC_HOSTED__`

## Ranged-`for` Loop

- Aka, enhanced for loops
- Good for most collections of items:
  - `std::vector`
  - `std::array` (built-in arrays)
  - `std::deque`
  - `std::list`
  - `std::forward_list`
  - `std::set` / std`::multiset`
  - `std::map` / `std::multimap`
  - `std::unordered_set` / `unordered_map`
  - `std::string`
  - `std::string_view`
  - `std::filesystem::path` (iterates components)
  - All container adaptors if you expose `begin()`/`end()` manually (not by default)
- Use `auto` keyword for container types to avoid unnecessary copying, and to avoid typing out long types
- Use `const` reference as the iterator to improve efficiency
  - Not applicable for iteration through simple primitive types- go ahead and just iterate

```
// typical use
for (int x : vec) {
    std::cout << x;
}

//  iterating through keys
std::pair<const std::string, int>
for (std::pair<std::string, int> p : m)    // WRONG
for (auto& p : m)                          // correct; deduces std::pair<const std::string, int>&

// efficiency comparison
for (auto x : container)        // x is fully copied each time, which is expensive
for (auto& x : container)       // no copying, so efficient
for (const auto& x : container) // prevents modification and efficient- good practice
```

## rvalue Reference

- `int&& r = 5; // rvalue reference to a temporary integer`
- Refers to a reference that can bind to an rvalue (a temporary object) instead of a named variable (an lvalue)
- ...Introduced in C++11, and allows for move semantics and perfect forwarding
  - W/ this, you can move resources (memory, file handles) without copying
  - You can also combine w/ templates to allow functions to forward arguments preserving lvalue/rvalue nature

## Scope Resolution Operator

- The `::` used to:
  - Define methods of classes outside class definitions
  - Accessing names inside a namespace
  - Accessing static class members
  - Calling base-class method hidden by derived class
  - Specifying enum class values
  - Referring to type aliases or nested types inside classes
  - Accessing enclosed class members from a nested class
  - Qualification in templates
  - Accessing overloaded operators declared in a namespace
  - Disambiguate function template specializations

```
#include <iostream>

// 1. Global identifiers
int value = 100;   // global

// 2. Namespace members
namespace util {
    int value = 200;
    struct X { int n; };
    X operator+(const X& a, const X& b) { return {a.n + b.n}; }
}

// 3. Base class + method definition outside class
class Base {
public:
    void f() const { std::cout << "Base::f\n"; }
};

class Derived : public Base {
public:
    void f() const { std::cout << "Derived::f\n"; }
    void callBase() const { Base::f(); }
};

// 4. Static members, nested types
class Foo {
public:
    static int count;
    using value_type = int;
    void print();
};

int Foo::count = 300;     // definition uses ::

void Foo::print() {       // method definition uses ::
    std::cout << Foo::count << "\n";
}

// 5. enum class
enum class Color { Red, Blue };

// 6. Template-dependent names
template<typename T>
struct Wrapper : util::X {
    T get() const { return Base::f, (T)this->n; }
    // Base::f referenced only to show qualification in template context
};

int main() {
        // Local shadows global
        int value = 10;
    std::cout << ::value << "\n";      // global: 100

        // Namespace access
        std::cout << util::value << "\n";  // namespace: 200

        // Class static member & nested type
        Foo::value_type x = 42;
    std::cout << x << "\n";
    Foo f;
    f.print();                         // prints 300

        // Base vs derived + overriding
        Derived d;
    d.f();                             // Derived::f
    d.callBase();                      // Base::f

        // Enum class requires ::
        Color c = Color::Red;
    (void)c;

        // Operator from namespace
        util::X a{1}, b{2};
    util::X sum = util::operator+(a, b);
    std::cout << sum.n << "\n";        // 3

        // Template name qualification
        Wrapper<int> w;
    w.n = 7;
    std::cout << w.get() << "\n";      // 7

    return 0;
}
```

## Suffix Return Type

- A function declaration can have the return type specified at the end instead of at the beginning w/ the `->` token
- This is primarily for template declarations where the return type depends on the type of the arguments
- `auto to_string(int a) -> string;`

## Traits

- Traits are template-based structures that provide compile-time information about types or customize behavior based on type
- ...Used for generic programming, templates, and metaprogramming, and serves as the foundation of the standard library

## Unique, Shared Pointers

- Unique and shared pointers (`std::unique_ptr`, `std::shared_ptr`) are smart pointers that are RAII classes
- Unique pointer
  - Pointer that exclusively owns a heap-allocated object
  - Properties include:
    - Can't be copied
    - Can be moved
    - Fastest smart pointer
- Shared pointer
  - Copyable- each copy increments a reference count
  - Deleted just when the last shared pointer is destroyed
