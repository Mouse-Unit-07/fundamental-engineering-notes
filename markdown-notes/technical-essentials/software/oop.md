# OOP

- OOP notes
- All non-language specific but OOP specific notes

## Index

- [Index](#index)
- [5 Pillars of OOP](#5-pillars-of-oop)
- [Aggregation vs Composition](#aggregation-vs-composition)
- [Association vs Acquaintance](#association-vs-acquaintance)
- [Class Invariant](#class-invariant)
- [Class vs Type](#class-vs-type)
- [Concrete vs Abstract Class](#concrete-vs-abstract-class)
- [Mangling of Linker Symbols](#mangling-of-linker-symbols)
- [Mixin Class](#mixin-class)
- [Namespaces](#namespaces)
- [Principles of Reusable OO Design](#principles-of-reusable-oo-design)
- [Super vs Parent Class](#super-vs-parent-class)

## 5 Pillars of OOP

- Encapsulation
  - Bundling data/methods into classes to enforce modularity/security/portability
- Abstraction
  - Hiding complex implementation details and exposing just essential features via interfaces / abstract classes
- Inheritance
  - Allowing a class to inherit its properties and methods from another class allowing code reuse and hierarchical relationships
- Polymorphism
  - Allowing an interface to take various forms via overriding/interfaces
- Composition
  - ...Not purely OOP, but often included to remind developers that Occam's Razor always holds
  - Defining objects w/ other objects as their attributes to enforce modularity and organization

## Aggregation vs Composition

- Both are types of object relationships in OOP, but differ in ownership/semantics
- Composition
  - When an object includes another object as a field
  - Strong “has-a” relationship
  - Implies ownership- containing object is responsible for the lifetime of a contained object
  - A car has an engine (it needs an engine instance to exist)
- Aggregation
  - When an object includes a pointer to an object as a field
  - Weak “has-a” relationship
  - Implies shared ownership or no ownership
  - A school has students (also needs students to exist, but variable)

## Association vs Acquaintance

- Association
  - Aggregation/composition
  - When an object holds a reference to another as part of its state and can interact w/ it freely
- Acquaintance
  - When an object just knows about another object in a limited way
  - Knows enough to send it a message, but no heavy reliance for interface implementation or for the object instance's lifetime
  - Ex:
    - Class function is passed an object, which is then used to call its method
    - No pointer or hard instance of the object in the class definition

## Class Invariant

- Aka, "invariant"
- Condition or property of a class that has to always be true for any valid object of the class
  - ...except potentially during brief periods of mutation inside member functions
- Requirements include:
  - Maintenance by class functions only
  - Only temporarily violated internally by member functions
  - Used for correctness/safety

## Class vs Type

- Class
  - Defines how an object is implemented (internal state and implementation of its operations)
  - A user-defined type to represent a concept in the code of a program
- Type
  - Refers only to its interface (the set of requests to which an object responds to)
- Class vs interface inheritance
  - An object can have many types, and objects of the same class can have the same type

## Concrete vs Abstract Class

- Concrete class
  - Class that can be (and is meant to be) instantiated
  - Provides implementations for all member functions, included inherited virtual functions
- Abstract class
  - A class that can't be instantiated due to having at least one pure virtual function to be implemented by its subclass

## Mangling of Linker Symbols

- When the compiler encodes each unique method and parameter list combination into a unique name of the linker, it's called "mangling"
- ...the reverse is called "demangling"
- C++, Java, etc support overloading, so there needs to be some scheme to distinguish between identical identifiers w/ different parameter lists

## Mixin Class

- A class that's intended to be "mixed into" other classes to add extra behavior/functionality
- Not meant to be instantiated directly on its own

## Namespaces

- Container to organize code and prevent name conflicts by grouping related identifiers (variables, functions, classes)
- Supported in C++, C#, Java, Python, etc
- Allows grouping around related items for better readability and navigation
- Extensibility
  - Can safely modify and add features without conflicting w/ existing items
- “global namespace”
  - The default scope in C++ that encompasses all software

## Principles of Reusable OO Design

- > Program to an interface, not an implementation
  - Aka, dependency inversion
- > Favor object composition over class inheritance
  - Inheritance can be completely replaced by composition
  - Class hierarchies and relationships are conveyed well through inheritance, but disadvantages include:
    - Can't change implementations inherited from parent classes at run-time
    - Parent classes often define a part of their subclasses' physical representation- this exposure breaks encapsulation

## Super vs Parent Class

- Synonymous, where “super class” has some more technical nuances…
