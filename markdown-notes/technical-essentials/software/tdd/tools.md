# TDD Tools

- TDD tools notes

## Index

- [Index](#index)
- [CppUTest](#cpputest)
- [Google Mock/Test](#google-mocktest)
- [Mocking Tools](#mocking-tools)
- [Test Coverage Tools](#test-coverage-tools)

## CppUTest

- Test harness to test both C++ and C interfaces
- Written in C++
- Automatically adds test cases to the runner, in contrast to Unity

## Google Mock/Test

- A modern C++ testing framework
- Heavier compared to CppUTest and has longer compile time, but has rich formatting, advanced reporting, etc
- Great for desktop/server C++ applications
- CppUTest is the better alternative for embedded applications

## Mocking Tools

- Writing mocks gets repetitive- they all manage expectations and values to return
- You can use Google Mock, CppUMock, Hippo Mock, etc to factor out mock redundancy

## Test Coverage Tools

- Gcov (“GNU coverage”) & lcov (“LTP Gcov”, “Linux test project”) come together w/ gcc, and works w/ CppUTest
- Gcov is the command line interface, lcov provides HTML output
