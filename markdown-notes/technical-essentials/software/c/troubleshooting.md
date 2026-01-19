# Troubleshooting

- Troubleshooting in C notes

## Index

- [Index](#index)
- [Breakpoint Issues](#breakpoint-issues)
- [Build System Error](#build-system-error)
- [Bus Error](#bus-error)
- [Common Memory Related Bugs](#common-memory-related-bugs)
- [Compiler Error](#compiler-error)
- [Debugger Intrusiveness](#debugger-intrusiveness)
- [Debugging Hard Faults](#debugging-hard-faults)
- [Disabled Interrupts Behavior](#disabled-interrupts-behavior)
- [Dynamic Memory Allocation](#dynamic-memory-allocation)
- [Linker Error](#linker-error)
- [Logical Error](#logical-error)
- [Preprocessor Error](#preprocessor-error)
- [Runtime Error](#runtime-error)
- [Segmentation Fault](#segmentation-fault)
- [Warnings](#warnings)

## Breakpoint Issues

- If you can't place a breakpoint w/ an IDE, it could be because:
  - Breakpoint placed on code that's not loaded
    - Optimization might've inlined or removed functions
  - Breakpoint in flash vs RAM mismatch
    - If a debugger is trying to inject a software breakpoint w/ an explicit instruction, and gets the assumption wrong about the kind of memory it's interfacing w/ (RAM vs flash), there'll be issues
  - Debug info / binary mismatch
    - If source code on the IDE isn't what was compiled and flashed to the hardware, there'll be issues
  - Hardware breakpoint exhaustion
    - Could have exhausted the number of breakpoints available
  - Address isn't executable
    - If your breakpoint happens to be associated w/ .data, .bss sections instead of .text, there will be issues
    - Can't place a breakpoint on a function pointer that doesn't point to valid code
    - Can't place a breakpoint on a stub function that's not linked in either

## Build System Error

- No rule to make target
  - Missing dependency file
- Missing separator
  - Makefile syntax error
- Undefined CMake command
  - Invalid or unknown command
- Cannot open source file
  - File path wrong or missing
- Cannot find compiler
  - Misconfigured toolchain

## Bus Error

- Refers to misaligned or impossible hardware access
- The address exists, but hardware can't fetch the data properly
- Not a seg fault, which is when the address doesn't exist
- The two have separate signals- `SIGBUS` and `SIGSEGV`

## Common Memory Related Bugs

- Dereferencing bad pointers
- Reading uninitialized memory
- Allowing stack buffer overflows
- Assuming that pointers and the objects they point to are the same
  - Dynamically allocating memory for pointers instead of objects they need to point to
- Off-by-one errors
- Referencing a pointer instead of the object it points to
- Misunderstanding pointer arithmetic
  - Pointer arithmetic is done relative to the size of the object that a pointer points to- not the size of the pointer
- Referencing nonexistent variables
- Referencing data in free heap blocks
- Introducing memory leaks

## Compiler Error

- Expected ‘;’ before
  - Missing semicolon
- Undeclared identifier
  - Variable or function not defined
- Incompatible types
  - Assignment of wrong type
- Redefinition
  - Variable or function defined more than once
- Conflicting types
  - Function prototype doesn’t match implementation
- Invalid operands
  - Performing an operation on incompatible types
- Non-void function should return a value
  - Return missing in non-void function
- Array subscript is not an integer
  - Using a non-integer index
- Initializer element is not constant
  - Invalid static/global variable initialization
- Storage size of ‘X’ isn’t known
  - Incomplete type used
- Too few/many arguments to function
  - Function call mismatch
- Dereferencing pointer to incomplete type
  - Missing struct/typedef definition

## Debugger Intrusiveness

- Print statements, breakpoints, single-stepping, etc are all intrusive debugging methods
- If a debugger adds negligible time to perform its debugging tasks, it's a nonintrusive method

## Debugging Hard Faults

- Steps:
  - Find information from processor about what went wrong
  - Find stack and look to see where you were and what you were doing
  - Store the information somewhere in RAM to be able to log the info on reboot

## Disabled Interrupts Behavior

- When you disable interrupts w/ software, and then the hardware encounter an interrupt event (whether intended or not), you'll see that the program services the interrupt
- This is because the interrupt flag associated w/ the pin or whatever hardware peripheral is still set, and the MCU services it after interrupts are enabled again
- This means an MCU can "buffer" up to a single interrupt event on the particular peripheral, and the rest will be missed

## Dynamic Memory Allocation

- Be careful not to touch memory outside of what's allocated- causes segmentation fault
- Don't free the same memory region twice- also causes segmentation fault
- Don't pass a pointer that wasn't used to call `malloc()` to `free()`
- ...Ensure that all `malloc()`'s have an associated `free()`

## Linker Error

- Undefined reference to ‘function’
  - Function declared but not defined
- Multiple definition of
  - Function or variable defined in multiple source files
- Cannot find -l<libname>
  - Missing library during linking
- Unresolved external symbol
  - Object file references missing symbol
- Symbol already defined in object
  - Conflicting symbol definitions
- Duplicate symbol
  - Identical symbols in separate files

## Logical Error

- Wrong condition in if/while
  - = instead of ==, etc
- Infinite loop
  - Missing exit condition
- Incorrect algorithm
  - Wrong output due to logic flaw
- Off-by-one error
  - Accessing one element too many/few
- Misuse of operators
  - Misuse of operators

## Preprocessor Error

- #include file not found
  - Missing or misspelled header
- #ifdeef/#ifndef mismatch
  - Conditional compilation issues
- Macro redefined
  - Duplicate macro definitions
- Unterminated #if
  - Mismatched #if/#endif
- #error directive
  - Manual compile-time error trigger

## Runtime Error

- Segmentation fault (SIGSEGV)
  - Invalid memory access
- Bus error
  - Misaligned memory access
- Stack overflow
  - Infinite recursion or large stack allocation
- Division by zero
  - Dividing integer or float by 0
- Null pointer dereference
  - Dereferencing a NULL pointer
- Use-after-free
  - Accessing freed memory
- Memory leak
  - Allocated memory not freed
- Buffer overflow
  - Writing past array boundaries
- Double free
  - Freeing already freed memory
- Undefined behavior
  - From violating C spec (signed overflow, assigning a enumerated variable something that’s not enumerated, etc)

## Segmentation Fault

- Common causes include:
- Bad pointer value errors
  - Null pointer, bad pointer value, etc
- Overwriting errors
  - Writing before/after an array, past allocated memory, past a management structure, etc
- Freeing errors
  - Excessive freeing

## Warnings

- Unused variable/function
  - Unused declaration
- Comparison between signed and unsigned
  - Type mismatch
- Control reaches end of non-void function
  - Missing return
- Uninitialized variable
  - Variable used without initialization
- Implicit declaration
  - Function used without a prototype
- Cast from pointer to integer of different size
  - Unsafe cast
- Ignoring return value
  - Return value not used
