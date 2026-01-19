# Standard Library Fundamentals

- C++ standard library notes

## Index

- [Index](#index)
- [Overview](#overview)
- [1998, 2003: C++98, C++03](#1998-2003-c98-c03)
- [2011: C++11](#2011-c11)
- [2017: C++17](#2017-c17)
- [2020: C++20](#2020-c20)
- [2023: C++23](#2023-c23)

## Overview

- C++ headers available vary by C++ release, just like C
- What's worth noting:
  - Stdint and stdbool only made it in C++11...
  - `bool` w/ `true`/`false` is a fundamental type now
- An implementation is called "hosted" if it provides all standard libraries, and "freestanding" if it doesn't

## 1998, 2003: C++98, C++03

- C++ headers introduced:
  - `<algorithm>`
  - `<bitset>`
  - `<complex>`
  - `<deque>`
  - `<exception>`
  - `<fstream>`
  - `<functional>`
  - `<iomanip>`
  - `<ios>`
  - `<iosfwd>`
  - `<iostream>`
  - `<istream>`
  - `<iterator>`
  - `<limits>`
  - `<list>`
  - `<locale>`
  - `<map>`
  - `<memory>`
  - `<new>`
  - `<numeric>`
  - `<ostream>`
  - `<queue>`
  - `<set>`
  - `<sstream>`
  - `<stack>`
  - `<stdexcept>`
  - `<streambuf>`
  - `<string>`
  - `<valarray>`
  - `<vector>`
- C headers introduced (slightly modified C standard library headers):
  - `<cassert>`
  - `<cctype>`
  - `<cerrno>`
  - `<cfloat>`
  - `<climits>`
  - `<clocale>`
  - `<cmath>`
  - `<csetjmp>`
  - `<csignal>`
  - `<cstdarg>`
  - `<cstddef>`
  - `<cstdio>`
  - `<cstdlib>`
  - `<cstring>`
  - `<ctime>`
- Depracated C headers:
  - `<assert.h>`
  - `<ctype.h>`
  - `<errno.h>`
  - `<float.h>`
  - `<limits.h>`
  - `<locale.h>`
  - `<math.h>`
  - `<setjmp.h>`
  - `<signal.h>`
  - `<stdarg.h>`
  - `<stddef.h>`
  - `<stdio.h>`
  - `<stdlib.h>`
  - `<string.h>`
  - `<time.h>`

## 2011: C++11

- C++ headers introduced:
  - `<array>`
  - `<atomic>`
  - `<chrono>`
  - `<condition_variable>`
  - `<forward_list>`
  - `<future>`
  - `<initializer_list>`
  - `<mutex>`
  - `<random>`
  - `<ratio>`
  - `<regex>`
  - `<thread>`
  - `<tuple>`
  - `<type_traits>`
  - `<typeindex>`
  - `<unordered_map>`
  - `<unordered_set>`
- C headers introduced (slightly modified C standard library headers):
  - `<cstdint>`
  - `<stdbool.h>`

## 2017: C++17

- C++ headers introduced:
  - `<any>`
  - `<optional>`
  - `<variant>`
  - `<string_view>`
  - `<filesystem>`
  - `<shared_mutex>`

## 2020: C++20

- C++ headers introduced:
  - `<barrier>`
  - `<bit>`
  - `<compare>`
  - `<concepts>`
  - `<coroutine>`
  - `<format>`
  - `<latch>`
  - `<semaphore>`
  - `<source_location>`
  - `<stop_token>`
  - `<span>`
  - `<synchronization>`
  - `<version>`

## 2023: C++23

- C++ headers introduced:
  - `<expected>`
  - `<flat_map>`
  - `<flat_set>`
  - `<mdspan>`
  - `<stacktrace>`
