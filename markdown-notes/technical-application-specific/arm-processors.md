# ARM Processors

- ARM processor notes

## Index

- [Index](#index)
- [Overview](#overview)
- [3 Different Architecture Profiles for ARM Processors](#3-different-architecture-profiles-for-arm-processors)
- [ARM Architecture](#arm-architecture)
- [Bit-Banding](#bit-banding)
- [Bus Interface Unit](#bus-interface-unit)
- [GCC Tools](#gcc-tools)
- [Interrupt Requirements](#interrupt-requirements)
- [Links for ARM Processors](#links-for-arm-processors)
- [Main vs Process Stack Pointer](#main-vs-process-stack-pointer)
- [Redlib](#redlib)
- [Status Register](#status-register)
- [Thumb Mode](#thumb-mode)

## Overview

- Popular architecture for power efficiency, scalability, widespread support, and customizable licensing model
- Companies are able to purchase licenses to use ARM architecture cores in their custom chips

## 3 Different Architecture Profiles for ARM Processors

- A profile
  - “Applications” profile
  - High performance
  - Designed to run complex operating systems like Linux or Windows
  - Japan’s Fugaku supercomputer uses ARM A profile
- R profile
  - “real-time” profile
  - Designed for systems w/ real-time requirements
  - Found in networking and embedded control equipment
  - Made for those that demanded more from Cortex-M and wanted something closer to Cortex-A to manage real-time requirements
- M profile
  - “microcontroller” profile
  - Small and power efficient
  - Found in many IoT devices
  - Microchip’s SAM controllers and NXP’s controllers all use Arm Cortex-Mxx processor cores
  - Cortex-M3 was where assembly requirement was dropped
  - Interrupt priority
    - Different MCU’s using ARM Cortex-M profile processors allow different number of interrupt priority levels, but Cortex-M MCU’s designate lower numbers for higher priority and higher numbers for lower priority
    - Explained here:
      - Https://www.freertos.org/RTOS-Cortex-M3-M4.html
  - Chips select whichever processor is applicable to their function

## ARM Architecture

- ARM stands for “Advanced RISC Machines”
  - … but ARM makes it confusing and makes new acronyms using ARM in their documentation here and there…
- RISC (“reduced instruction set computer”) architecture relative to CISC (“complex instruction set computer”) for fast/robust computation on MCU & MPUs
- ARMv9 builds on a bunch of functionality on top of Armv8
  - SVE2- “scalable vector extension”
  - TME- “Transactional memory extension”
  - BRBE- “branch record buffer extension”
  - ETE- “embedded trace extension”
  - TRBE- “Trace buffer extension”
  - Realm management extension
- ARMv7 is 32 bit
  - Thumb & Thumb-2 instruction set
    - Reduced code size and power efficient
  - TrustZone technology
    - Isolates secure and non-secure software execution
- ARMv8 is 64 bit
  - Can use both 64- and 32-bit execution states
    - Called AArm64 and AArm32 execution environments
  - Holds addresses in 64 bit registers
  - AA64 instruction set offers more address space, larger registers, and improved performance for certain workloads
  - Allows multiple VMs to run on a single physical processor
  - Adds to Advanced SIMD (NEON) instruction set and cryptographic extensions
  - Increased scalability for various embedded systems
- NXP MCU called LPC54628 uses “ARM Cortex-M4” processor, which is under ARMv7
  - NXP stands for “next experience”- semiconductor design company

## Bit-Banding

- ARM Cortex-M feature to map each individual bit in a memory region to a 32-bit word in a special alias region
- ...So allows read/write from the alias word to directly set/clear the original memory location
- No need for weird Union data structures w/ bit fields each memory mapped to bits on memory

## Bus Interface Unit

- Units that handle all instruction and data transfers between CPU core and system buses
- All peripherals go through BIU's before they interface w/ the processor cores

## GCC Tools

- `arm-none-eabi` tools are tools made for ARM Cortex-M and other ARM-based MCU’s that don’t need OS’s
  - Arm- ARM architecture
  - None- for “no OS”, bare metal only
  - `eabi`
    - “embedded application binary interface”
    - Standard for embedded systems defining conventions for data types, function calls, etc to ensure consistency across tools

## Interrupt Requirements

- ...ARM processors have a bunch of enable/disable interrupt functions that all look like they do the same thing
- For an interrupt to be serviced:
  - Interrupts must be enabled at global and NVIC level
  - Interrupt flag must be set (interrupt must be "armed")
  - Interrupt must not be masked (if CPU is in the middle of servicing a higher priority interrupt, interrupt will be masked)

## Links for ARM Processors

- [A-Profile Architecture (arm.com)](https://developer.arm.com/Architectures/A-Profile%Architecture)
- [Documentation – Arm Developer](https://developer.arm.com/documentation/#cf[navigationhierarchiesproducts]=Architectures,Learn%20the%20architecture)
- ARM is also the company name…. They make arm processors

## Main vs Process Stack Pointer

- Main stack pointer
  - The primary stack pointer
- Process stack pointer
  - An optional stack pointer that can be used for an operating system
  - Allows a user program using the main stack pointer to crash without disturbing the OS

## Redlib

- C standard library
- Exclusive to NXP and MCUXpresso
- Includes things like assert.c, etc

## Status Register

- ARM's "program status register" consists of bit:
  - N for negative result
  - Z for result is zero
  - C for carry
  - V for signed overflow
  - Q for saturation
- There're two more called APSR ("application program status register") and EPSR ("execution program status register"), which are both accessible via the "program status register"

## Thumb Mode

- ARM mode
  - 32-bit instructions, and full set of instructions
- Thumb mode
  - 16-bit instructions for Thumb-1
  - Some 32-bit instructions for Thumb-2
  - Compact instruction encoding scheme for smaller code size in exchange for limited capability
- Modern Cortex-M processors don't even have an "ARM mode"- it's always in Thumb mode for efficiency
