# Clean Code Fundamentals

- Clean code fundamentals notes
- Primarily from Robert C Martin's _Clean Code_

## Index

- [Index](#index)
- [Bean, Javabean](#bean-javabean)
- [Boundaries](#boundaries)
- [Boy Scout Rule](#boy-scout-rule)
- [Casing Style Names](#casing-style-names)
- [Comparing Variables to Constants](#comparing-variables-to-constants)
- [Dependency Injection](#dependency-injection)
- [Error handling](#error-handling)
- [NASA: The Power of 10](#nasa-the-power-of-10)
- [Objects and Data Structures](#objects-and-data-structures)
- [SOLID Principles](#solid-principles)

## Bean, Javabean

- Bean/Javabean
  - Link here: https://www.oracle.com/java/technologies/javase/javabeans-spec.html?
  - A reusable software component in Java following specific conventions for defining objects
  - POJO (“plain old java object”) that adheres to a strict set of rules:
    - Must have a public no-argument constructor
      - Allows frameworks to instantiate objects dynamically
    - Must provide public getter and setter methods
      - Encapsulates fields while allowing controlled access
    - Must be serializable
      - Enables object persistence and transfer
    - Etc

## Boundaries

- There’s an inherit tension between the provider of an interface and the user of an interface
- Minimize the work for the users of an interface- if you define an abstract interface / template, then the concrete implementations that inherit the interface should define functions that cast abstract types to the appropriate types
- Third party code
  - Learn the third party code by writing tests one by one and verifying behavior
- Using code that doesn’t exist yet
  - Write provided what you wish you had

## Boy Scout Rule

- Leave the campground cleaner than you found it
- Code rots when you don't consciously think about maintenance
- To prevent code from degrading over time, it’s our duty to make code cleaner than the way we found it

## Casing Style Names

- ...There are names for the casing styles we see everywhere:
  - Camel case
    - `myVariableName`
    - JavaScript variables, Java methods
  - Pascal case
    - `MyVariableName`
    - Originates from use in the Pascal programming language
    - C# classes, Java classes, TypeScript types
  - Snake case
    - `my_variable_name`
    - Python, C variables/functions
  - Screaming snake case
    - `MAX_BUFFER_SIZE`
    - Constants/macros in C/C++
  - Kebab case
    - `some-branch-name`
    - URLs, CSS, filenames
  - Train-Case
    - Rarely in docs or CLI flags
    - `My-Variable-Name`
- We see and generate camel and snake case the most- Pascal case for classes/functions
- Kebab case for non-source file folder names, git branch names, and git repo names
- Dunder case
  - "double underscore"
  - Used in Python for constructors, making objects callable, and module metadata
  - `__init__`, `__call__`, `__name__`/`__file__`

## Comparing Variables to Constants

- Injecting the constant first in the expression for a conditional statement:
- `if (0 != someVar)` , `if (0 == someVar)` , etc
- If the equality operator is mistyped and you have just a single equal sign in the expression, the compiler will throw an error if and only if you have the constant first
- Is a decent idea, but we don’t want to do this- unit tests should check code behavior, and readability always has priority

## Dependency Injection

- Forcing external sources to provide external dependencies as arguments instead of generating the dependencies internally
- Allows for loose coupling

## Error handling

- Refer to TDD section for more on error handling in C
- Java
  - The objective is to separate error handling from business logic:
  - Use exceptions rather than return codes
    - Removes clutter by removing need for caller to check for errors after a function call
  - Write try-catch-finally statement first
    - The first try-catch-finally block defines the scopes for you to work in- write this try-catch-finally block first in response to each exception w/ TDD, and then you can work your way down
  - Use unchecked exceptions
    - This allows you to follow open-close principle
    - You don’t want a low level change to cause changes all the way up where errors are handled
- Define the normal flow
  - You can bypass the need for an exception / error by using the “special case pattern”
    - If you have a function that would return an error code in response to a particular situation, you can define an output for such special cases instead of spitting out an error
- Don’t return null
  - Horrible- generates work for callers
- Don’t pass null
  - Horrible (as in, functions shouldn't be checking for null everywhere)- generates work for callees
- Error handling styles
  - ...error handling should be done case-by-case after defining how a system needs to address each error
  - ...but there are names for some attempts to generalize error handling:
  - Unix-style
    - In the context of Unix system calls (1970-1980s)
    - Checking for `-1` return value from system call, and `errno` global variable for error code
    - Cons:
      - `errno` thread safety issues
      - Easy to skip checking return codes
  - POSIX-style
    - In context of POSIX standardization (1980-90s)
    - Functions returning error codes directly
    - Cons:
      - Causes deep nesting from numerous error code checks
  - GAI-style
    - In context of `getaddrinfo()` and networking APIs introduced w/ IPv6 support
    - `getaddrinfo()` and related functions return error codes, and `gai_strerror()` used to convert to human-readable messages
    - Cons:
      - Involved method of error checking, not any better than POSIX style

## NASA: The Power of 10

1. Avoid complex flow constructs, such as goto and recursion.
2. All loops must have fixed bounds. This prevents runaway code.
3. Avoid heap memory allocation.
4. ~~Restrict functions to a single printed page.~~
   - Outdated- it should be “to a single concept that easily fits in your head”
5. ~~Use a minimum of two runtime assertions per function.~~
   - Outdated- we need a single assertion per unit test
6. Restrict the scope of data to the smallest possible.
7. Check the return value of all non-void functions, or cast to void to indicate the return value is useless.
8. Use the preprocessor sparingly.
9. Limit pointer use to a single dereference, and do not use function pointers.
   - Function pointers are good for abstractions, but otherwise no reason to use
10. Compile with all possible warnings active; all warnings should then be addressed before release of the software.

## Objects and Data Structures

- **Data abstraction**
  - Don’t expose details of abstract data types and interfaces through committed setter and getter names
- **Data/object anti-symmetry**
  - Objects and data structures are opposites- don’t mix and match
  - It’s a myth that everything is an object- sometimes you do want simple data structures w/ procedures operating on them
  - Objects
    - Objects hide their data behind abstractions and expose functions that operate on that data (functions are generic, and written w/ signatures to allow subclasses to be written to inherit templates)
    - OO code makes it easy to add new classes without changing existing functions
    - OO code makes it hard to add new functions because all the classes must change
  - Data structures
    - Data structures expose their data and have no meaningful functions (if there are functions, the data structure’s attributes are baked into the operations rather than performing abstract operations to follow and allow for polymorphism)
    - Procedural code makes it easy to add new functions without changing the existing data structures
    - Procedural code makes it hard to add new data structures since all functions must change
- **The law of Demeter**
  - A module should not know about the innards of the object it manipulates
  - Aka, object shouldn’t expose its internal structure through accessors because doing so would be to expose internal structure
  - This means that a method f of class C should only call methods of these:
    - C
    - An object created by f
    - An object passed as an argument of f
    - An object held in an instance variable of C
  - A method of a class shouldn’t call the method of an object generated by the object passed as an argument to it, or the method of the instance variable of an instance variable of it
  - Following this rule maintains modularity and boundaries between modules- otherwise it’s no longer a “module”
  - This rule doesn’t apply to data structures- only objects/modules have the intent of hiding their innards
- **Train wrecks**
  - Single line chains of calls sloppy
  - Store the return value of calls into variables instead
    - This doesn’t bypass law of Demeter- decoupling train wrecks aren’t an excuse to let modules manipulate and expose the innards of other modules
- **Hybrids**
  - Don’t create object / data structure hybrids
  - The purpose of creating an abstract module/object is defeated if there are public accessor functions that expose the innards of the object, making it look like a data structure that has abstract functions
- **Data transfer objects**
  - An ideal data structure just has public variables and no functions- these are called DTOs (“data transfer objects”)
  - Used for communicating w/ databases, parsing messages from sockets, etc
  - An object w/ a collection of private variables and accessors/setters to all of them is a data structure- just expose the member variables
  - Active record
    - A DTO w/ navigational methods like “save” and “find” are active records
    - Don’t add business rule methods- this creates hybrids

## SOLID Principles

- Single responsibility principle
  - Every module should only have one reason to change
- Open-closed principle
  - Code should be open for extension, but not modification
  - Changes to software should be made by adding new code, not by changing existing code
- Liskov substitution principle
  - Subtypes of an abstract type or concept should be interchangeable- write software to adhere to contracts to allow for easy substitution
- Interface segregation principle
  - Avoid depending on things that aren’t used
- Dependency inversion principle
  - High level application should not depend on low-level implementation details
  - Create modules wrapping low level details that are dependent on middle hardware interfaces instead
