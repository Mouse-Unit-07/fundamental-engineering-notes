# Code Smells

- Code smells notes (as in, indications of bad code)
- Primarily from Robert C Martin's _Clean Code_

## Index

- [Index](#index)
- [Avoid Negative Conditionals](#avoid-negative-conditionals)
- [Build Requires More Than One Step](#build-requires-more-than-one-step)
- [Dead Functions](#dead-functions)
- [Don’t Be Arbitrary](#dont-be-arbitrary)
- [Encapsulate Boundary Conditions](#encapsulate-boundary-conditions)
- [Follow Standard Conventions](#follow-standard-conventions)
- [Hidden Temporal Couplings](#hidden-temporal-couplings)
- [Incorrect Behavior at Boundaries](#incorrect-behavior-at-boundaries)
- [Keep Configurable Data at High Levels](#keep-configurable-data-at-high-levels)
- [Overridden Safeties](#overridden-safeties)
- [Structure Over Compliance](#structure-over-compliance)
- [Tests](#tests)
- [Tests Require More Than One Step](#tests-require-more-than-one-step)

## Avoid Negative Conditionals

- When encapsulating conditional expressions, it’s easier to read if the encapsulations aren’t negative
- Do this:
  - `if (buffer.shouldCompact())`
- Over this:
  - `if (!buffer.shouldNotCompact())`

## Build Requires More Than One Step

- Building a project should be a single operation
- Shouldn’t be checking out a bunch of little pieces from source code control, no sequence of arcane commands or context dependent scripts to build individual elements, no searching for JARs, XML files, or other artifacts

## Dead Functions

- Functions that aren’t ever called should be removed

## Don’t Be Arbitrary

- Have a reason for the way code is structured, and make sure the reason is communicated through the code
- If structure looks arbitrary, others will feel empowered to change it

## Encapsulate Boundary Conditions

- Adding a simple variable is enough to encapsulate +1s and -1s in conditional expressions

## Follow Standard Conventions

- Every team should follow a coding standard based on common industry norms
- There shouldn’t be a document- examples should speak for themselves
- Every team member must be mature enough to realize it doesn’t matter where you put your braces as long as you all agree on where to put them

## Hidden Temporal Couplings

- Structure functions to make it obvious the way in which functions need to be called
- By forcing functions to generate results required for other functions to run, it forces a particular function order
- Extra syntactic complexity is demanded in exchange for exposing true temporal complexity

## Incorrect Behavior at Boundaries

- Don’t rely on intuition
- Look for every boundary condition and write a test for it
- It’s how that iPod freeze issue could’ve been avoided
- And how all other software related RMAs could be avoided

## Keep Configurable Data at High Levels

- Constants like default or configuration values that are known and expected shouldn’t be buried in low-level functions
- Expose such data as arguments to the low-level functions from high-level functions

## Overridden Safeties

- Chernobyl melted down because the plant manager overrode each safety mechanism one by one- they were in the way of running an experiment
- Don’t turn off compiler warnings or failing tests

## Structure Over Compliance

- Enforce design decision w/ structure over convention
- Switch cases w/ nicely named enumerations are inferior to base classes w/ abstract methods, etc

## Tests

- Insufficient tests
  - A test suite should test everything that could possibly break
  - Tests are insufficient for as long as there are conditions that haven’t been explored by the tests
- Use a coverage tool
  - Tools like Clover (Java only) can report gaps in a testing strategy
- Don’t skip trivial tests
  - They’re easy to write- just write them
  - Documentary value is higher than cost to write them
- An ignored test is a question about an ambiguity
  - Readers question whether the ambiguity is about something that compiles or not
- Exhaustively test near bugs
  - If there’s one bug, there are likely more
- Tests should be fast
  - You won't run tests if they're slow
  - Do what you must to keep tests fast

## Tests Require More Than One Step

- Running all tests should be a single operation
