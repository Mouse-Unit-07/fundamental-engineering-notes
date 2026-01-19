# Interrupt

- Interrupt notes

## Index

- [Index](#index)
- [Don't We Need Synchronization?](#dont-we-need-synchronization)
- [Latency](#latency)
- [Nested Interrupts](#nested-interrupts)
- [NVIC](#nvic)
- [Polled vs Vectored Interrupts](#polled-vs-vectored-interrupts)
- [Software vs Hardware Interrupt](#software-vs-hardware-interrupt)
- [To-Do List](#to-do-list)

## Don't We Need Synchronization?

- When you have ISRs updating global variables and a main program behaving w/ respect to the globals, you're essentially multithreading
- ...W/o an OS, you don't have access to synchronization primitives to protect accesses/modifications to globals
- The solution is:
  - To keep flag updates, count updates, etc as minimal as possible so the operations are as close to atomic as possible
  - Accesses to the globals as minimal as possible in main program
  - Make the globals `atomic_t` so operations on them are atomic
  - ...Disable interrupts when accessing the globals in the main program if absolutely necessary

## Latency

- C doesn't provide a native way for firmware to be aware of interrupt execution time between lines of code at runtime
- The strat is to toggle a pin and put hardware on a scope

## Nested Interrupts

- When an interrupt is triggered and serviced while the program is servicing some other ISR, it's called a "nested interrupt"
- Can occur when an interrupt that's higher or equal priority is called while the program is in an ISR
- Tail chaining
  - One ISR executing immediately after another is called "tail chaining"

## NVIC

- “nested vector interrupt control”
- System to prioritize interrupts and reduce interrupt latency
- This is a block that communicates w/ core processor (CPU) to prioritize certain interrupts over others

## Polled vs Vectored Interrupts

- Polled interrupt
  - When one ore more triggers share the same interrupt vector
- Vectored interrupt
  - When the ISR knows what event triggered the interrupt

## Software vs Hardware Interrupt

- Software interrupt
  - Triggered by software instructions
  - Relies on OS to pause tasks to service the interrupt
- Hardware interrupt
  - Triggered by hardware changes detected
  - Relies on external hardware and software associated w/ detected hardware changes

## To-Do List

- The interrupt servicing todo list:
- Interrupt request (IRQ) happens inside the processor
  - Triggered by external component, software, or fault in the system
- Processor saves the context
  - Where the program counter was and local variables
- Processor finds the function associated w/ the interrupt in the vector table
- Callback function (aka ISR or interrupt handler) runs
- Processor restores the saved context and returns to the point before the interrupt occurred, and the program continues to run
