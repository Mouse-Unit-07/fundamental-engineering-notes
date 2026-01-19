# TDD Jargon

- TDD jargon notes

## Index

- [Index](#index)
- [Abstract Data Type](#abstract-data-type)
- [Multiple-Instance Module](#multiple-instance-module)
- [Single-Instance Module](#single-instance-module)
- [Test Case](#test-case)
- [Test Code](#test-code)
- [Test Double, Stub, Dummies, Spy, Mock, Fake](#test-double-stub-dummies-spy-mock-fake)
- [Test Fixture](#test-fixture)
- [Test Harness](#test-harness)
- [Unit Test](#unit-test)

## Abstract Data Type

- A module who’s data is private, and defined by the operations that may be performed on it
- Ex: a circular buffer struct type might be defined in a header using a forward struct declaration- user can’t see how it’s implemented, but it’s tossed around by functions in the circular buffer interface

## Multiple-Instance Module

- A module that a user can create multiple instances of
- Must pass in abstract data type (the particular instance) to functions
- Ex: a circular buffer module

## Single-Instance Module

- A module that has a single collection of data to manage
- No need for tossing around an instance of an abstract data type into functions
- Ex: an LED interface responsible for a particular set of LED’s on a board

## Test Case

- Code that describes/tests a particular behavior of the code under test

## Test Code

- Code written to test a particular interface

## Test Double, Stub, Dummies, Spy, Mock, Fake

- Test double
  - An impersonation of some function/data/module/library
  - Includes stubs, dummies, spies, mocks, fakes
  - Use-cases:
    - Hardware independence
    - Inject difficult to produce input(s)
    - Speed up a slow collaborator (dependency)
    - Dependency on something volatile
      - Time/clock, etc
    - Dependency on something under development
    - Dependency on something difficult to configure a database, etc
  - When you're forced to use a mock, recommendations include:
    - Reconsider the design
      - You shouldn't be mocking the same thing multiple times
      - Reduce all duplication to avoid redundant mocks
    - Recognize the concession to unit testing coverage
      - Mocks indicate holes that your tests don't cover
      - Make sure the stuff that's being mocked has their own separate tests
    - Refactor your tests
      - Prevent dependencies on a libraries from causing tests to look like a mess w/ mocks
      - Refactor, isolate dependencies, and try to minimize mock use
    - Question overly complex use of test doubles
      - Multiple levels of mocks should be avoided- refactor/reconsider the design
    - Choose expressiveness over power
      - Use clever/esoteric features just when you have to
      - Don't use mocks to do weird complicated things
- Stub
  - A double that returns hardcoded values
- Dummy
  - Empty stub to prevent a linker from rejecting a build
  - Used when replacing an entire DOC, and when you have functions in the DOC that aren’t called in your interface
- Spy
  - A double that captures information sent to it for later verification
- Fake
  - A double that provides a light-weight implementation of a production class
  - Partial implementation for a replaced component
  - Usually provides specific values/implementations just like mock objects
  - Exploding fake
    - Causes test to fail if called
  - Often the root cause of trouble, bc fakes need a lot of implementing- avoid whenever possible
    - When they're necessary, write tests for the fakes too
- Mock
  - A double that self-verifies based on expectations sent to it
    - In detail: an object that verifies the functions called, call order, and parameters passed from the code under test to depended on component
  - Programmed to return a specific value to the code under test
  - Used when a function in a depended on component is called multiple times, and each call/response is potentially different

## Test Fixture

- Set of tests and the source file compiled together with the tests written for a particular interface

## Test Harness

- Set of libraries and an environment for a user to begin writing tests for an interface
- Includes Unity and CppUTest

## Unit Test

- A test written to verify the behavior of a particular unit of code (a behavior in an interface)
