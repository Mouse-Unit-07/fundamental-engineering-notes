# Naming

- Naming things in code notes
- Primarily from Robert C Martin's _Clean Code_

## Index

- [Index](#index)
- [Add Meaningful Context](#add-meaningful-context)
- [Avoid Disinformation](#avoid-disinformation)
- [Avoid Mental Mapping](#avoid-mental-mapping)
- [Blocks and Indenting](#blocks-and-indenting)
- [Class Names (structs for C)](#class-names-structs-for-c)
- [Command Query Separation](#command-query-separation)
- [Do One Thing](#do-one-thing)
- [Don’t Be Cute](#dont-be-cute)
- [Don’t Repeat Yourself](#dont-repeat-yourself)
- [Eliminate "Hungarian Notation"](#eliminate-hungarian-notation)
- [Error Handling](#error-handling)
- [Function Arguments](#function-arguments)
- [Intention Revealing Names](#intention-revealing-names)
- [Interfaces and Implementations](#interfaces-and-implementations)
- [Make Meaningful Distinctions](#make-meaningful-distinctions)
- [Method Names](#method-names)
- [One Level of Abstraction Per Function](#one-level-of-abstraction-per-function)
- [Pick One Word Per Concept](#pick-one-word-per-concept)
- [Problem Domain Names](#problem-domain-names)
- [Reading Code from Top to Bottom: The Stepdown Rule](#reading-code-from-top-to-bottom-the-stepdown-rule)
- [Side Effects](#side-effects)
- [Small Functions](#small-functions)
- [Solution Domain Names](#solution-domain-names)
- [Structured Programming](#structured-programming)
- [Switch Statements](#switch-statements)
- [Use Descriptive Names](#use-descriptive-names)

## Add Meaningful Context

- Some words are descriptive and indicate context on their own, but most aren’t
- If you have a class or struct storing physical user addresses, then “state” can be used together w/ “zipcode” or “streetNumber”, but “state” on its own isn’t descriptive
- Don’t make users ever have to infer the concept based on a vague name

## Avoid Disinformation

- Don’t leave misleading hints for programmers
  - If a variable is an array and not a list, don’t name it accountList
- Don’t accumulate a collection of identifiers that differ in small ways
  - `thisIsAReallyLongVariableName`
  - `thisIsAPrettyLongVariableName`
- Lower case l’s and O’s
  - Hard to distinguish between 1/0 and the conventional i/j

## Avoid Mental Mapping

- Readers shouldn’t have to map your identifiers to concepts or other names to understand your code
- Chugging out a function w/ 10 different single letter variables doesn’t make you smart- it’s ugly code

## Blocks and Indenting

- The contents of a compound statement created by an “if”, “while”, “else” statement should ideally consist of just a single statement- that statement should be a function call
- The indent level of a function should not be greater than 1 or 2
- This adds readability, because it forces writers to choose descriptive and concise identifiers for helper functions as well

## Class Names (structs for C)

- Should be noun or noun phrases
- Avoid generic terms like “manager”, “processor”, “data”, etc

## Command Query Separation

- Functions should either do something or answer something, not both
- Aka, don’t return status
- A function should either modify the state of an object, or return information about an object- doing both leads to confusion, and goes against single responsibility principle
- If (set(“username”, “john doe”))
  - Does this set something and return status, or check whether something is just set?
  - Can’t tell

## Do One Thing

- > functions should do one thing. They should do it well. They should do it only.
- Single responsibility principle

## Don’t Be Cute

- You’re asking for people to be confused when you add inside jokes or references that only certain people will understand to identifier names

## Don’t Repeat Yourself

- DRY
- As mentioned before in TDD book

## Eliminate "Hungarian Notation"

- It’s an outdated concept from when programming languages limited identifier name lengths
- Don’t add to identifier names to indicate scope, class association, etc
- P* for pointers, g* for globals, m\_ for class fields, etc

## Error Handling

- Error handling is one thing
- Functions should do one thing- create an independent function for error handling
- Use exceptions instead of returning error codes if applicable to programming language- lets you follow single responsibility principle
- Enumeration of error codes
  - It’s a dependency magnet
  - Other files need to be aware of the error codes, forcing coupling between files far and wide
  - Goes against open-close principle- users can’t add error codes without rebuilding an entire project

## Function Arguments

- Functions should take inputs, and return outputs- output arguments are hard to understand, and add unnecessary clutter when we can divide the work to more helper functions instead
- Functions shouldn’t take Boolean/flag arguments- the function signature confesses that it does multiple things (one thing if flag, another if !flag)
- Write a unit test for a triadic is already impossible- try to minimize the number of arguments into a function everywhere
- Ideally, functions have niladic (zero) arguments
- Then what’s tolerable is:
  - Monadic (1 argument)
  - Dyadic (2 arguments)
  - Triadic (3 arguments) on special cases
  - There needs to be an outlier justification for anything more than that (and then that outlier function shouldn’t ever be used…)
- Monadic
  - Monadic functions that don’t classify as one of the below can be collapsed to niladic form:
    - Asking a question about an argument
    - Operating on an argument / transforming it, and returning it
    - Event- take in a particular event as an argument and modify the state of the system
- Dyadic
  - Used when there are two components to a single conceptual input
    - Point p = new Point(0, 1)
  - Come up w/ ways to reduce dyadic to monadic
    - WriteField(output-stream, name) ->
      - Make writeField a member function of output-stream class
      - Make output-stream a member variable of the class
      - Extract a new class to take output-stream in a constructor
  - Dyadic functions are hard to interpret
    - Ordering of arguments
    - Comprehending argument purpose
    - May cause readers to ignore arguments
- Triadic
  - Problems of a dyadic are scaled more than double when you have a triadic
  - There needs to be an exceptional reason to generate a triadic…
  - If there needs to be that many arguments to encapsulate a single conceptual input, then generate a new class or struct and take that as an input instead
    - This isn’t cheating- testability is maintained while enhancing readability
- Ellipsis and argument lists
  - A list of arguments (a collection of arguments passed to a print function) can be considered a single argument
- Descriptive function names continued
  - Function names can be made descriptive to specify how arguments are being used, and to indicate whether order matters
  - `Write(name)`
    - Writing “name” to what? What’s “writing”?
    - `writeField(name)` is better
  - `assert(expected, actual)`
    - Does order matter? What’s being compared to what?
    - `assertExpectedEqualsActual(expected, actual)` is better

## Intention Revealing Names

- Take time to choose an identifier name (function, variables, classes, etc) that reveal the single purpose of the thing you’re creating
- Long identifiers are perfectly fine if it’s necessary
- Short identifiers are even better if they do just as well to pinpoint exactly what the identifier is for

## Interfaces and Implementations

- If there’s an interface / abstract class / abstract data type, and it’s difficult to come up w/ a name to differentiate the interface and implementation, give the implementation the additional encoding/extension

## Make Meaningful Distinctions

- Meaningless names
  - Arguments a1, a2, etc for a function signature don’t tell you anything
  - Don’t just satisfy the compiler
- Noise words
  - Noise words are words that programmers will ignore- eliminate them
  - “variable”/”var” in a variable name is redundant
  - “data”/”info” in a class or struct don’t mean anything, and fail to distinguish one another
  - “string” for a string or “int” for an integer doesn’t add any meaning- focus on conveying the logical sequence and purpose of operations instead of implementation details
  - “ethernet” in front of all fields/attributes/methods in an “ethernet” class/struct doesn’t add any meaning, and it’s a lazy way of adding a distinguisher to your interface
- Pronounceable names
  - We can’t physically talk about code if things aren’t pronounceable
- Searchable names
  - Use single-letter names only for local variables inside short functions
  - Take time to come up w/ a unique identifier to avoid any overlap
- Encodings
  - If it needs extra explanation because only you or a set of individuals know what a set of letters mean, then it’s encoded- unravel the encoding

## Method Names

- Should have verb/verb phrase names
- Accessors, mutators, and predicates should be prefixed w/ “get”, “set”, “is” following the javabean standard

## One Level of Abstraction Per Function

- A function shouldn’t both perform a bitwise operation on a variable and perform a high-level send function- the bitwise operation should be abstracted into a helper function to match levels of abstraction
- This aids readability, and enforces additional modularity

## Pick One Word Per Concept

- “fetch”, “retrieve”, and “get” in the same codebase or file or class is confusing-choose a verb/noun for a particular concept and stick w/ it
- Be descriptive enough to be distinguishable in a codebase, and unique and concise enough to be distinguishable in an implementation file
- Don’t rely on IDE provided hints for function signatures- name items to be descriptive enough on their own
- Don’t hide differences- if a codebase has an “add” function for adding/concatenating two values, don’t create an “add” function that appends an item to an array

## Problem Domain Names

- If there’s no generic or “programmer-eese” lingo to describe a concept, choose a problem specific name- it’s better than a naked noise word

## Reading Code from Top to Bottom: The Stepdown Rule

- Code should read like a narrative- top level of abstraction down to all of its sub abstractions down to lowest level operations

## Side Effects

- Side effects are lies
- Your function promises to do one thing as per function name, but it does other hidden things
- Refactor and rename to follow single responsibility principle

## Small Functions

- > The first rule of functions is that they should be small. The second rule of functions is that they should be smaller than that
- This is for readability, testing, scalability, modularity
  - Short functions w/ consistent level of abstraction across the function is easy to read and build upon
  - It’s impossible to write a test for long functions- there are too many states and paths engraved into it
  - It’s easy to add features when implementation details are abstracted atomically by purpose
  - Short functions divided by purpose (writing modular code) allows for easy modification, replacement, and addition

## Solution Domain Names

- Programmers read code, so we’re free to use CS terms, algorithm names, pattern names, math terms, etc as need be
- Remember that we also want to convey purpose and functionality over implementation details

## Structured Programming

- "structured programming" is designing w/ clear logical structures as opposed to jumps/returns everywhere
- Concept introduced in 1960s
- Dijkstra says that “every function, and every block within a function, should have one entry and one exit”
  - This implies one return, no break or continue statements in loops, no goto statements
  - These rules provide benefit for larger functions- there’s less merit from following these rules for small functions
  - Jump statements are horrible on all fronts, but if there needs to be a break, continue, or multiple returns then go ahead

## Switch Statements

- Switch statements and long if-else chains are used to do more than 1 thing- this goes against single responsibility principle, as well as open-close principle if the set of processes needs be added to when adding additional features
- Collapse the operation down to smaller functions if applicable
- If you’re really dealing w/ a single static operation describable and controlled best by a single switch statement, then all is good

## Use Descriptive Names

- > you know you are working on clean code when each routine turns out to be pretty much what you expected
- The function name needs to encapsulate the entirety of the one thing it does- there shouldn’t be undescribed side effects or processing- don’t hesitate to make the function name longer to describe the one thing that the function does concisely
