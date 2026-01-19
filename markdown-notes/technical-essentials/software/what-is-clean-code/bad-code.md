# Bad Code

- Bad code notes, primarily from _Test-Driven Development for Embedded C_

## Index

- [Index](#index)
- [Abstraction Distraction](#abstraction-distraction)
- [Bad Names](#bad-names)
- [Bad Pasta](#bad-pasta)
- [Bewildering Boolean](#bewildering-boolean)
- [Comments](#comments)
- [Conditional Compilation](#conditional-compilation)
- [Copy-Paste-Tweak-Repeat](#copy-paste-tweak-repeat)
- [Duplicate Code](#duplicate-code)
- [Duplicate Switch Case](#duplicate-switch-case)
- [Feature Envy](#feature-envy)
- [Global Free-For-All](#global-free-for-all)
- [Long Functions](#long-functions)
- [Long Parameter List](#long-parameter-list)
- [Nefarious Nesting](#nefarious-nesting)
- [Switch Case Disgrace](#switch-case-disgrace)
- [Willy-Nilly Initialization](#willy-nilly-initialization)

## Abstraction Distraction

- Don’t mix low level manipulation with function calls that abstract similar low level manipulation
- Add additional abstraction to keep the level of abstraction consistent in functions and in a particular scope

## Bad Names

- Don’t use acronyms that aren’t widely known
- Reveal the intended outcome through function identifiers, instead of writing out any internal details

## Bad Pasta

- Spaghetti
  - Dependencies left and right, layers and modules aren’t made clear
- Lasagna
  - Software in layered architecture, loosely coupled together
  - Lasagna invites spaghetti within each layer, but still better than just spaghetti
- Ravioli
  - Small self-contained packets, all loosely coupled w/ tomato sauce
  - Could lead to processing spread out too much across all the packets, but usually this isn’t a problem

## Bewildering Boolean

- Don’t write long boolean expressions- factor out the expression into a private function

## Comments

- Comments are used as deodorant to hide bad code
- Code should be simple enough to explain itself
- Use comments when code can’t be structured in a self-explanatory way (when necessary optimizations are in place, etc)
- Outdated comments turn into lies
- Don’t leave commented out code in a repository

## Conditional Compilation

- Hard to follow, and makes development impossible
- Use the linker and compiler instead- create new implementation source files instead

## Copy-Paste-Tweak-Repeat

- Especially prominent when writing tests
- Duplication occurs when you copy and paste w/ small modifications- make sure to add refactoring to the cycle

## Duplicate Code

- All program language evolutions can be summed up as efforts to eradicate duplicate code
- Don't misuse your tools

## Duplicate Switch Case

- If switch case logic is duplicated just w/ different actions, it’s time to think of an alternative- apply open-closed principle

## Feature Envy

- If objects/functions demand shared data/objects to be passed around and manipulated, there’s “feature envy”
- Isolate data manipulation for single instance modules, and follow data abstraction for multiple instance modules

## Global Free-For-All

- This includes file scope and completely global variables
- Horrible for testing, and for creating independent functions and modules
- If they need to exist, create functions to initialize and manipulate the globals
- If the global is a struct, create an abstract data type

## Long Functions

- It’s too long if it can’t quickly fit into your head
- A single switch statement with no nesting can fit into your head, but an ugly mess of nesting, long expressions, etc doesn’t fit int your head even if it’s less than a page or x number of lines specified in a company’s coding standards
- Factor out all individual concepts/processes to reduce a function to implement just a single high task declared by its function name, following single-responsibility principle

## Long Parameter List

- When a parameter list is copied across multiple functions, it’s time to write a new struct module and take that as a parameter instead
- We want to minimize struct use, since padding and memory allocation for structs are target dependent- use explicit data types as struct members

## Nefarious Nesting

- Again, minimize nesting
- Abstract out the contents inside of loops and conditional statements to maintain minimal layers to think about for both you and others

## Switch Case Disgrace

- Don’t nest things under switch case statements
- Try to reduce the number of cases too

## Willy-Nilly Initialization

- A lack of a distinct initialization function forces you to initialize structs and variables in tests for legacy code
- Add the initialization functions to the production code
