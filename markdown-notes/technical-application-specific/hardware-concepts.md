# Hardware Concepts

- Miscellaneous hardware facts and convention notes
- List of niche/application specific hardware concepts

## Index

- [Index](#index)
- [Battery Management System](#battery-management-system)
- [DPA Countermeasures](#dpa-countermeasures)
- [LLC Isolator](#llc-isolator)
- [Nyquist Theorem](#nyquist-theorem)
- [PoE](#poe)

## Battery Management System

- System to monitor charging / discharging of rechargeable batteries
- Includes:
  - I & V monitoring
  - Cell balancing
  - Temperature monitoring
  - Over current protection
  - Short circuit protection
  - Etc
- SOH
  - “state of health”
  - Measure of battery performance relative to when it was new
- SOC
  - “state of charge”
  - Energy remaining in battery as a percent relative to max capacity
- Battery monitoring methods
  - Voltage measurement
    - Comparing battery voltage to voltage vs SOC curve
    - Requires battery to be temporarily isolated from system
    - Not the most accurate
  - Coulomb counting
    - Measuring charge entering/leaving battery
    - Most popular choice
    - Doesn’t require interruption and removal of battery
    - Requires complex algorithm to calculate SOC
  - Ohmic/impedance measurement
    - Measuring internal resistance of battery that changes as battery charges/discharges
- OCV
  - “open circuit voltage”
- LoRaWAN
  - “long range wide area network”
  - Networking protocol for IoT applications
  - Good for low power consumption

## DPA Countermeasures

- “differential power analysis countermeasures”
- Hot damn- so by analyzing power consumption of a device, a malicious user can infer secret information like encryption keys
  - The dedication is real
- Countermeasures include masking, noise injection, balancing power consumption, randomized execution, etc

## LLC Isolator

- A module that combines concepts of LLC resonant converters and electrical isolation to transfer power from one circuit to another while keeping the two circuits isolated
- “LL” comes from the two inductor windings of a transformer, and C from the capacitors used to switch and convert power to whatever desired
- Some other isolation done somehow? Otherwise inductor is an isolator in and of itself from lack of physical electrical connection from one winding to another?

## Nyquist Theorem

- Theorem that a system has to sample at a frequency at least double the highest frequency component of a continuous-time signal to avoid losing information
- Otherwise you get "aliasing"- where high-frequency components appear as lower frequencies
  - Just as you wouldn't be able to reconstruct a sine/cosine wave properly if you look at the signal at the end of each period

## PoE

- “power over ethernet out”
- Feature/capability of a network device or switch to provide power to another device over ethernet
- Special for the new IEEE PoE standard to deliver high power to devices over long distances
- Works w/ Cat5 cables and onward
