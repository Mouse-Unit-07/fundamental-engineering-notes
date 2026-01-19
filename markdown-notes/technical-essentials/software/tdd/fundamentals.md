# TDD Fundamentals

- Test-driven development fundamentals notes

## Index

- [Index](#index)
- [Overview](#overview)
- [3 TDD Rules](#3-tdd-rules)
- [Bad Test Spiral](#bad-test-spiral)
- [Classic vs Hamcrest Assertions](#classic-vs-hamcrest-assertions)
- [Cleaning Up](#cleaning-up)
- [Code Coverage](#code-coverage)
- [Collection of Related Test Cases](#collection-of-related-test-cases)
- [Concurrency](#concurrency)
- [Defects](#defects)
- [Development Cycle](#development-cycle)
- [Disabling Tests](#disabling-tests)
- [Do The Simplest Thing That Could Possibly Work](#do-the-simplest-thing-that-could-possibly-work)
- [DRY](#dry)
- [Dual Targeting](#dual-targeting)
- [Extreme Programming](#extreme-programming)
- [File Organization](#file-organization)
- [FIRST](#first)
- [Interaction/State-Based Testing](#interactionstate-based-testing)
- [Intermittent Passes](#intermittent-passes)
- [Katas, Dojos](#katas-dojos)
- [Mikado Method](#mikado-method)
- [Parameterized Tests](#parameterized-tests)
- [Precondition/NULL Checking](#preconditionnull-checking)
- [Production Code Guidelines](#production-code-guidelines)
- [Red-Green Refactor](#red-green-refactor)
- [Running Tests](#running-tests)
- [Simple vs Classical Design Concepts](#simple-vs-classical-design-concepts)
- [Tell-Don't-Ask](#tell-dont-ask)
- [Ten Minute Limit](#ten-minute-limit)
- [Triangulation](#triangulation)
- [Unit Tests vs Integration/Acceptance Tests](#unit-tests-vs-integrationacceptance-tests)
- [Violating Encapsulation](#violating-encapsulation)
- [Writing Tests](#writing-tests)

## Overview

> Write a test, get it to pass, clean up the design. That's all there is to TDD
>
> - Jeff Langr in _Modern C++ Programming with Test-Driven Development_

- TDD ("test-driven development") is a method of incrementally writing code as a by-product of failing unit tests, so that your software is documented/verified and can be reverified for whether it behaves as desired
  - It's the solution to counter the lack of linear progress software engineers make due to troubleshooting uncertainty, scaling issues, illegible code, etc
- TDD is the solution if you're troubled w/:
  - Monstrous source files w/ thousands of lines
  - Member functions w/ hundreds/thousands of lines of inscrutable code
  - Volumes of dead code
  - Build times extending into several hours
  - High numbers of defects
  - Logic too convoluted by quick fixes to be safely managed
  - Code duplication across files/classes/modules
  - Code riddled w/ long-obsolete coding practices
- “-ilities” Reinforced by TDD/DevOps/Agile
  - Maintainability
  - Manageability
  - Scalability
  - Reliability
  - Testability
  - Deployability
  - Security

## 3 TDD Rules

- By Robert C Martin (Uncle Bob):
  - 1: Production code may only be written in response to a failing test
  - 2: Don’t write more tests than needed to create a single failure (build failures are failures)
    - ...Sometimes it's necessary to write multiple tests, but follow this whenever possible
  - 3: Don’t write code ahead of tests
- Benefits:
  - This way you guarantee a test for all production code behaviors
  - Write/modify test cases until you see the need for production code to upgrade to resolve a way for production code to fail

## Bad Test Spiral

- Bad engineering practices and spirals are noted in DevOps notes, but a bad TDD spiral could look like:
  - Teams writing mostly integration tests
  - Growing body of tests begin to pass the pain threshold
  - Developers run the test suite less frequently, or run a subset of tests
  - Developers delete tests
  - Defects begin to increase
  - Team/management questions the value of TDD
  - Team abandons TDD

## Classic vs Hamcrest Assertions

- Classic assertions are simple value-based comparisons
- Hamcrest assertions are further bare-bones assertions that increase test expressiveness
- Whatever you use, if the test is simple and easy to understand we're good to go

```
// Classic
assertEquals(expected, actual);
assertTrue(condition);
assertFalse(condition);
assertNull(obj);
assertNotEquals(a, b);

// Hamcrest- relies on a library, but more expressive:
assertThat(actual, is(expected));
assertThat(value, greaterThan(10));
assertThat(list, hasItem("apple"));
assertThat(name, both(startsWith("J")).and(containsString("hn")));
```

## Cleaning Up

- Refactor/simplify tests and production code in response to every successful cycle of writing a test and updating production code
- TDD generates rot-free (not bug-free) interfaces thanks to you handling all code smells on the spot
- **Don’t cut- copy, build, then delete**
  - Don’t ever cut when refactoring- create a new bridge, verify bridge, then burn old bridge to maintain steady development
- **Critical refactoring skills**
  - Identify bad code
    - Don’t categorize just based on your code vs others’ code
    - Identify what’s wrong w/ both your own and others’ code
  - Envision better code
    - Envision a better solution following SOLID principles
  - Transform the code
    - Slowly change the code- write new code without deleting old code, confirm that the new code works, then delete old code
- **Ugly complex code arises from**:
  - Time pressure
    - Fighting deadlines and bureaucracy
  - Lack of education
    - You need to confront and know what you don't know
  - Existing complexity
    - Fighting legacy code
  - Fear of changing code
    - "If it ain't broke, don't fix it"
    - Fear prevents refactoring and tests
  - Speculation
    - Premature implementations/design decisions close doors for solutions that allow for easy change
- **Refactoring inhibitors**:
  - Insufficient tests
  - Long-lived branches
  - Implementation-specific tests
  - Crushing technical debt
  - No know-how
  - Premature performance obsession
  - Management metric mandates
    - ...Good luck convincing management that duplication is bad when performance is measured by lines of code
  - Short-sighted infatuation w/ speed
    - As in, from a development stand point ("just ship it!")

## Code Coverage

- Code coverage tools help you when code often gets ahead of tests- the tools will give you feedback
- These tools aren't perfect, so you'll never have 100%
- Heuristics:
  - < 90% means TDD isn't how the codebase was born
  - \> 90% usually means a codebase was written w/ TDD (but a nasty integration test can plow through code too)
- High coverage doesn't mean tests are simple and maintainable

## Collection of Related Test Cases

- Create tests in order of 0-1-N when there’s a collection of related cases to test

## Concurrency

- Working on a concurrent project is involved, but gateway tips before incorporating TDD include:
  - Separate threading logic from application logic
  - Don't call `sleep()`
  - Throttle down to single-threaded for application specific tests
  - Observe concurrency issues before introducing synchronization

## Defects

- TDD doesn't prevent all defects
  - Production code, test code, etc can all still be defective
  - The tests generated w/ TDD together help tackle uncertainty in development/troubleshooting
- Most dumb defects will be prevented, leaving:
  - Conditions no one ever expected
  - External things out of sync (config files, etc)
  - Curious combinations of behavior involving multiple methods/classes
  - Specification problems (inadvertent omissions/misunderstandings between developers and customers)

## Development Cycle

- ![tdd-state-machine](_images/tdd/tdd-state-machine.png)
- Write list of test cases ->
- Begin cycle of writing tests and production code ->
  - Write minimal test code ->
    - New test case->
    - See compilation failure from reference to non-existent test macro ->
    - Define test macro ->
    - See linking failure from call to non-existent production code ->
    - Implement empty production code function ->
    - See failing test ->
  - Write minimal production code (bare minimum, including hard coded solutions) ->
  - Note weaknesses realized from hard coded solutions (add to test list) ->
  - Refactor test fixture and production code if test cases are passing ->
    - Test fixture:
      - Add helper test macros to factor out repeated behavior
  - Production code:
    - Static global variables to represent and factor out fake hardware registers
    - Static helper functions to factor out repeated/complex/difficult to read behavior
    - Static enumerations for masks, constants, etc
  - Repeat until all test cases are exhausted ->

## Disabling Tests

- You can disable tests for when you're getting more than one test failure in response to a new feature you added
  - This way you can resolve each failure one by one
- Disabled tests aren't to be ignored forever, and code w/ tests disabled shouldn't be checked in to version control

## Do The Simplest Thing That Could Possibly Work

- Production code should be written in stages
  - You want to start w/ wrong hardcoded solutions, to up to how a chip vendor might implement something if they had factored and decoupled everything possible
- The collection of tests created through this process will all be correct and useful to verify software behavior

## DRY

- “Don’t repeat yourself”
- Minimize duplicate code (in both tests and production code)

## Dual Targeting

- When the target environment and the testing environment are different, you write portable and platform-agnostic code

## Extreme Programming

- 4 rules for simple design
  - Runs all tests
  - Expresses every idea needed to be expressed
    - Code should be self-documenting- clearly show the intention of the programmer
    - Don’t write comment blocks
  - Says everything once and only once
    - Eliminate all duplication
  - Has no superfluous parts
    - Don’t add in things that aren’t yet needed
- The "make it xxx" motto
  - Make it work
  - Make it right
  - Make it fast

## File Organization

- Header files for test implementation files are useless
- You can have multiple test files per class, but related concepts should be close together
- There's no harm in having test implementations and test doubles in the files where production code lies too
  - Once multiple fixtures need access to test implementations, then tests/doubles need to be isolated into their own files

## FIRST

- Tests come FIRST:
  - Fast
    - Run tests with every small change
  - Isolated
    - Tests shouldn’t set anything up for other tests
    - Isolates all failures
  - Repeatable
    - Should be able to run in a loop, and perform the same test every time
  - Self-verifying
    - Provide OK for pass, concise details in response to failures
  - Timely
    - Write every test right before the production code

## Interaction/State-Based Testing

- Interaction-based
  - When you use test doubles to spy on how a collaborator was interfaced w/, it's called interaction-based testing
- State-based
  - When you use data publicly available for you to verify that behavior is correct
  - ...There shouldn't be much public data if you're dealing w/ an encapsulated class, but if there is then this is what testing w/ it is called

## Intermittent Passes

- Sometimes you get tests to pass, by then they fail intermittently
- Potential causes:
  - Static data
    - Don't let your tests depend on side effects of other tests, or leave any remnants causing problems in other tests
  - Volatility of external services
    - Don't let tests depend on external forces out of your control (current time, file system. databases, API calls, etc)
    - Write test doubles as needed
  - Concurrency
    - Threaded/multiprocessing execution isn't deterministic
    - ...Incorporating TDD in a concurrent system is worth chapters and books (writing concurrent code in and of itself is already worth books)

## Katas, Dojos

- "katas" refer to choreographed patterns of movement
  - In software, there are katas that incorporate TDD for you to develop effectively
- You can run katas in teams called "dojos" (lol)

## Mikado Method

- There's a lot of friction against making large-scale changes to a codebase
- The "Mikado method" is a cycle that tries to work w/ that friction:
  - 1: Draw the "Mikado goal"- an end state you want to reach
  - 2: Implement the goal in a naive manner
  - 3: Find any errors
  - 4: Derive immediate solutions to the errors
  - 5: Draw the immediate solutions as new prerequisites
  - 6: Revert code to its initial state if there were errors
  - 7: Repeat steps 2-6 for each immediate solution
  - 8: Check in code if there were no errors: mark the prerequisite goal complete
  - 9: If the Mikado Goal is met, you're done
- This method allows you to develop without understanding/probing the entire system
  - It's a DFS method to find all the prerequisite goals to accomplish the larger goal, and fight each goal deepest first

## Parameterized Tests

- You can write tests that take in input/output arguments, but they make convoluted/complex tests
- If you have a spreadsheet w/ a whole collection of exceptional test cases, then it might be a good reason to write a complex test to encapsulate your repetitive test
  - ...Doing this is also beyond TDD- your test is turning into an integration test

## Precondition/NULL Checking

- If you define your system to behave in a certain way in response to violated preconditions (passing null, argument is over a limit, called a function before calling an initialization function, etc), then a test can be written to handle each of those cases
  - Developers need to do a careful job of defining the way the layer behaves in response to precondition violations, and write tests that verify said behavior
- It's not the job of mocks or unit tests to check whether a layer is violating another interface's preconditions
  - ...There's no way for a layer to communicate the precondition checks needed in the mocks written in another layer
- On the contrary, each post condition behavior is verified by their respective unit test
  - This means you shouldn't be writing redundant checks for whether a function returns null if there's a test for it already

## Production Code Guidelines

- Implementations are never objectively correct, but they can have objectively desirable characteristics:
  - Does what the customer asked for
    - If it doesn't, then it's a bad solution regardless of tests or elegance
    - TDD helps clarify requirements and exhaust all corner/exceptional cases
  - Works
    - If there are defects, it's a bad solution
    - TDD aids creating solutions that work
  - Readily understood
    - Time taken to decrypt bad code is wasted time
    - TDD documents what works, and forces you to write legible code
  - It's easily changed
    - When behavior can be reverified and work is legible, it can be easily changed

## Red-Green Refactor

- You can only refactor on green (passing tests)- don't start clean up on red (failing tests)
  - The terminology stems from SUnit (the first unit testing tools supporting TDD- written for Smalltalk in the 1990s)
- Factor out and simplify tests/production code only when all tests are passing, and when everything is compiling
- Doing more than one thing at a time (refactoring, adding behavior, writing tests, etc) is a waste of time- you need to handle one variable at a time

## Running Tests

- You want to run all your tests each time you run your tests
  - There's no behavior you can be sure of won't be affected- that's why you're writing tests to begin with
- Tests should run quickly
  - You could make them run in response to every file save
  - If they're not fast, you won't run them
  - You always want rapid feedback so you can fix your mistakes right when you make them, as opposed to after you have a large pool of potential causes for each issue
  - Slow tests causes developers to start writing integration tests labeled as "unit tests"

## Simple vs Classical Design Concepts

- Accessibility
  - Class members (whether it's an OOP class or a class created by an implementation file + header pair) should be kept private whenever possible
  - You can fully test an interface while having a collection of private helper functions
  - In tests, private vs public is irrelevant- just make everything public
- Timeliness
  - You can't implement a perfect design all in one go and expect it to work
  - The idea now is to incrementally implement following your best-effort project requirements, and refactor/optimize your code & update/clarify your requirements as you go

## Tell-Don't-Ask

- As in, tell an object to do something and don't ask how it's doing
- Refers to how you shouldn't be asking an object how it's behaving
- If you request an object to do something, it should just do it (no reporting statuses, checking the guts of the object, etc)
- When writing tests to ensure that your layer isn't violating any collaborator preconditions (passing null, etc), you use mocks and test doubles

## Ten Minute Limit

- Sometimes you can:
  - Struggle to get a test to pass
  - Attempt to clean up and break a few tests in the process
  - Feel the need to get a debugger to know what's happening
- Because TDD isn't a silver bullet, troubleshooting is inevitable
- A time limit should be set when you get stuck- just revert back and try again
- Don't get attached to small snippets of code that you're struggling w/- throw it away

## Triangulation

- Refers to the process of incrementally generalizing your software w/ tests
- Process could be:
  - First test hardcodes a solution
  - Second test breaks the solution and forces a bit more generalization
  - Third, fourth, etc test forces the "final" correct general behavior

## Unit Tests vs Integration/Acceptance Tests

- Unit tests verify individual behaviors of production code
  - By definition, unit tests are inadequate of validating whether an entire product (w/ multiple layers and pieces) does what it's supposed to do
  - Unit tests just verify that software behaves as desired
- Integration tests
  - Aka, acceptance tests, design verification tests, customer tests, system tests, load tests, performance tests, usability tests, functional tests, scalability tests, etc
  - These are all tests that verify integrated system behavior- when all parts are integrated together and the end product behavior is tested
  - Integration tests are needed alongside unit tests to verify a system/product
- Minimize integration tests
  - You want your set of integration tests to be the minimal set you need
  - Don't write integration tests that unit tests already cover
  - Integration tests aren't meant to run through every possible permutation/combination of possible uses- that's more for unit tests (though unit tests aren't for exhausting all possible conditions either)

## Violating Encapsulation

- In C, you don't have to worry about TDD breaking encapsulation
  - This is because static functions should be a by-product of refactoring your public interfaces- as in, they shouldn't add any new behavior to be tested
- In C++, classes can have private elements that add behavior
  - ...Even then, private elements should still consist of just be helpers
  - The problem is when a codebase isn't implemented w/ TDD to start w/- then all logic is in question
  - To cover all behavior, sometimes private elements should be made public to verify behavior
  - If doing so adds risk, then first reconsider the design and then figure out how to accept/manage the risk if there's no alternative

## Writing Tests

> A mantra surfaced in the early TDD days that says, “Test everything that can possibly break.” This is a glib response to the oft-asked question, “What do I have to test?” (...)
>
> A counterargument is that you can break just about anything, no matter how simple (and I’ve done it). As the tedium of entering repetitive data increases, so does our likelihood to make a mistake and not even notice it. Having tests would decrease the chance that we create a defect. (...)
>
> What’s the right answer? Maybe the most important consideration is that we are test-driving, not testing. “Is there a difference?” you ask. Yes. Using a testing technique, you would seek to exhaustively analyze the specification in question (and possibly the code) and devise tests that exhaustively cover the behavior. TDD is instead a technique for driving the design of the code. Your tests primarily serve the purpose of specifying the behavior of what you will build. The tests in TDD are almost a by-product of the process. They provide you with the necessary confidence to make subsequent changes to the code.
>
> The distinction between test-driving and testing may seem subtle. The important aspect is that TDD represents more of a sufficiency mentality. You write as many tests as you need to drive in the code necessary and no more. You write tests to describe the next behavior needed. If you know that the logic won’t need to change any further, you stop writing tests.
>
> Of course, real experience provides the best determinant. Test-driving for confidence works great until you ship a defect. When you do, remind yourself to take smaller, safer steps.
>
> - Jeff Langr in _Modern C++ Programming with Test-Driven Development_

- Every new test should test the behavior of the next smallest behavioral increment in production code
- **Test cases**
  - There's no need to cover everything- just cover the important cases:
  - Zero, one, many, boundary, and exceptional cases
- **Naming a test**
  - Just like naming everywhere else in code, naming is important and difficult
  - Follow single responsibility principle so the test verifies a single behavior, and make sure the test is named to encapsulate that tested behavior
  - A collection of tests replaces any comments/documentation questioning/clarifying code behavior
    - This also means don't write comments- your tests should be simple enough to explain themselves
- **One assert per test**
  - If possible, you want to have a single assert per test that verifies whatever behavior is being tested
  - You can have additional asserts to clarify the intent of the one assert that matters if needed
    - Use precondition assertions sparingly
    - Depending on the scenario, you could also add a constant or local variable instead
  - If you're tempted to add a post-condition test as opposed to a precondition test, it's a sign that you need another test
- **Test format: 4-Phase Test Pattern**
  - Aka, the "given-when-then" or "arrange-act-assert" test pattern
  - Setup
    - Establish preconditions to the test
  - Exercise
    - Do something to the system
  - Verify
    - Check the expected outcome
  - Cleanup
    - Return system under test to initial state after the test
- **A new test passes w/o any changes to code**
  - Each test you write should fail at least once- then your production code is a by-product of your tests
  - ...Sometimes a new test passes due to a new atomic behavioral change you added in response to an older failing test- then your tests become a by-product of your production code
  - Potential causes (silly mistakes included):
    - Running the wrong tests
      - Forgetting to add the test, filters, didn't compile/link new test, disabled tests, etc
    - Testing the wrong code
      - Forgetting to save/build, flawed build script, etc
    - Unfortunate test specification
      - Bad assert statement- bugs in tests
    - Invalid assumptions about the system
      - Bugs in the system/tests or both
    - Suboptimal test order
    - Linked production code
    - Over-coding
      - By restraining yourself from writing the most optimal solution and incrementally writing just what you need instead, you'll prevent suboptimal solutions from slipping in
    - Testing for confidence
  - If a bunch of new tests start to pass w/o new production code changes, try to revert your effort- you could:
    - Break down the changes you make, and change the order in which you add changes to as many tests fail before you add changes as possible
    - The cycle is one failing test -> one new behavior -> repeat- you can't write a whole wave of tests and then add a wave of behavior
- **A List of Tests**
  - What's important is that there's a test that verifies each behavior that's implemented, so you can progress w/ confidence
  - Preparing a list
    - You're never going to know every behavior your project needs to implement
      - ...This also means your planning documents are never going to be correct, and they'll forever need maintenance (just like comments in code)
      - Documentation that mirrors the actual work (software/hardware) should exist just when absolutely needed- otherwise the work should speak for itself
    - You can start w/ some list, and add as you go
      - Each time you encounter a new test case that questions behavior in a way you haven't anticipated, you need to make a decision about how your software needs to behave
      - This helps clarify the project requirements and closes doors for conflicts between customers and developers
