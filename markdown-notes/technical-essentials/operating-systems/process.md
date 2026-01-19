# Processes

- Processes notes

## Index

- [Index](#index)
- [CPU Affinity](#cpu-affinity)
- [Daemon](#daemon)
- [Deferred Processing](#deferred-processing)
- [Memory Layout](#memory-layout)
- [Privileged Process Precautions](#privileged-process-precautions)
- [Process](#process)
- [Program Termination](#program-termination)
- [Program vs Process](#program-vs-process)
- [Reaping Child Processes](#reaping-child-processes)
- [States](#states)
- [Task Scheduling Techniques](#task-scheduling-techniques)
- [Task-Level Parallelism](#task-level-parallelism)

## CPU Affinity

- Processes aren't guaranteed to run on the same CPU processor each time it gets CPU time
- Each context switch between processors causes an overhead due to invalidating caches
- Soft CPU affinity
  - When the kernel tries to have each processor be on the CPU processor that it was on last time whenever possible
- Hard CPU affinity
  - Making sure each process can only be run on the process it was originally running on
  - If multiple processes are operating on some shared data, picking a CPU to operate for all of them helps performance
  - It could also allocate a core to time-critical operations and another for non-time-critical operations

## Daemon

- No not Doraemon
- A computer program/process that runs without any interfacing/interaction
  - From "guiding spirit"/"attendant power" in Ancient Greece- supernatural being between gods and humans
- Features:
  - Long-lived- remains until system is shut down
  - Runs in the background w/ no terminal to read input or output anything

## Deferred Processing

- Selecting processes to be executed later
- Includes top-half/bottom-half concept and priority based scheduling via OS

## Memory Layout

- Just like your typical program:
  - `text` segment
    - Machine-language instructions of the program run by the process
    - Read-only for if other processes are running the same program
  - `data` segment
    - Global/static variables are initialized by the process (either explicitly, or implicitly to 0)
  - `heap`
    - For dynamic memory allocation
  - `stack`
    - Manages stack frames
  - Segments are divisions of virtual memory of a process- doesn't refer to hardware segmentation
- Memory allocation for the process is managed by the kernel

## Privileged Process Precautions

- File creations
  - Privileged processes create files w/ all permissions
  - Processes must be careful that such files have no way of being maliciously manipulated
- Inputs and environment list
  - Privileged processes shouldn't trust environment variables like PATH, or assume that inputs are correct
  - You don't want a privileged process running malicious programs w/ all permissions

## Process

- An instance of a program in execution
  - A program can generate a bunch of other processes
  - A bunch of processes can each be running the same program
- Executes abstract instructions, where some correspond to requests for the kernel to do work
- Each program in the system runs in the "context" of some process
  - Context consists of the state that the program needs to run correctly, including code/data stored in memory, stack, contents of general purpose registers, program counter, environment variables, set of open file descriptors
- Abstractions provided by a process:
  - Independent logical control flow that provides the illusion that a program has exclusive use of the processor
  - Private address space that provides the illusion that a program has exclusive use of the memory system
    - Space where other processes can't write/read to/from
- Pros and cons
  - Pros:
    - Clean model for sharing state information between parents and children- not possible for a process to overwrite virtual memory of another process
  - Cons:
    - Difficult to share state information
    - IPC mechanisms must be used

## Program Termination

- A C/C++ program can terminate by:
  - Returning from `main()`
  - Calling `exit()`
  - Calling `abort()`
  - Throwing an uncaught exception
  - Violating `noexcept`
  - Calling `quick_exit()`

## Program vs Process

- Program
  - A collection of code and data
  - Programs can exist as object files on disk or as segments in an address space
- Process
  - Specific instance of a program in execution
  - Always runs in the context of some process

## Reaping Child Processes

- Parent processes need to "reap" child processes that are terminated to remove it from a system
- A terminated child process that hasn't been reaped is called a "zombie"
- In contrast, a child process that's adopted by parent process due to termination of it's immediate parent is called an "orphan" child process

## States

- Running
  - Process is either executing on the CPU or waiting to be executed and will eventually be scheduled by the kernel
- Stopped
  - Execution of the process is suspended and will not be scheduled
  - Can stop as a result of a "signal" received
- Terminated
  - Process is stopped permanently
  - Could be because of:
    - Receiving a signal whose default action is to terminate the process
    - Returning to the main routine
    - `exit()` called

## Task Scheduling Techniques

- First-come, first-serve
  - Simple, but fails if there are many long tasks
- Earliest deadline first
  - Requires deadline and execution times
- Least slack time first
  - So the task w/ the least time to spare first
- Shortest job first
  - Requires required time for each job
- Rate monotonic scheduling
  - All tasks are periodic, and priority is inversely proportional to their service period times
  - Great if you know how long tasks need to run, and if all tasks can be periodic
- Round robin, priority based, etc
  - All thread scheduling schemes also fall under this larger umbrella of "task scheduling techniques", but not all task scheduling techniques qualify at the thread level due to the information they need like deadlines, job service time, etc

## Task-Level Parallelism

- Aka, "process-level" parallelism
- Using multiple processes to run independent programs simultaneously
