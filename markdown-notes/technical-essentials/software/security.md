# Software security

- Software security notes

## Index

- [Index](#index)
- [Buffer Overflow Attacks](#buffer-overflow-attacks)
- [DoS Attacks](#dos-attacks)
- [Hacker](#hacker)
- [Worm vs Virus](#worm-vs-virus)

## Buffer Overflow Attacks

- Malicious engineers can abuse buffer overflow conditions to write registers that move the processor to newly written malicious code
- In C, this means
  - `gets()` isn't safe
  - `scanf()`, `sprintf()`, `strcpy()`, `strcat()` should be used w/ caution
  - ...The takeaway is to be careful w/ extraneous reading and writing- don't leave room for overflow of reading or writing
- `gets()`
  - This is what let a worm through thousands of computers over the Internet in 1988
  - Bc `gets()` doesn't check the amount of memory available in the buffer that it's provided, stack can be corrupted
  - `fgets()` exists to counter this issue, but `gets()` still exists in the standard library

## DoS Attacks

- Attempts to make services unavailable to legitimate clients by sending server malformed data that causes crashes or overloading w/ random requests is called Dos ("denial of service") attacks
- This can happen locally too
  - A fork bomb is problematic, but can be found and prevented a lot easier than an external DoS attack

## Hacker

- Before "hacker" would refer to "evil genius", it would refer to "gifted programmer"

## Worm vs Virus

- Both are pieces of code that attempt to spread themselves among computers
- Worm
  - A program that can run by itself and can propagate a fully working version of itself to other machines
- Virus
  - A piece of code that adds itself to other programs, including OS's
  - Cannot run independently
