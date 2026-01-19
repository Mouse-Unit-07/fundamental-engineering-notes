# UML

- UML notes
- Primarily from _UML Distilled_

## Index

- [Index](#index)
- [Overview](#overview)
- [Activity Diagram](#activity-diagram)
- [Class Diagram](#class-diagram)
- [Communication Diagram](#communication-diagram)
- [Component Diagram](#component-diagram)
- [Composite Structure Diagram](#composite-structure-diagram)
- [Deployment Diagram](#deployment-diagram)
- [Interaction Overview Diagram](#interaction-overview-diagram)
- [Object Diagram](#object-diagram)
- [Organigram](#organigram)
- [Package Diagram](#package-diagram)
- [Sequence Diagram](#sequence-diagram)
- [State Machine diagram](#state-machine-diagram)
- [Timing Diagram](#timing-diagram)
- [UML Jargon](#uml-jargon)
- [Use Case Diagram](#use-case-diagram)
- [Uses of UML](#uses-of-uml)
- [What UML Diagrams to Use?](#what-uml-diagrams-to-use)

## Overview

- “unified modeling language”
- > A family of graphical notations, backed by single meta-model, that help in describing and designing software systems, particularly software systems built using the object-oriented style
  - Martin Fowler in _UML Distilled_
- > Question: What is the difference between a methodologist and a terrorist? Answer: You can negotiate with a terrorist
  - Martin Fowler in _UML Distilled_
- The biggest risk w/ using UML in analysis is when there are diagrams that domain experts don’t understand- the diagrams are worse than useless. They breed a false sense of confidence in the development team
- UML and adhering to strict rules
  - Prescriptive rules
    - A language w/ prescriptive rules is controlled by an official body that states what is or isn’t legal in the language and what meaning you give to utterances in that language
    - Aka, programming languages
  - Descriptive rules
    - A language w/ descriptive rules is one which you understand its rules by looking at how people use the language in practice
    - English, etc
  - UML is a mix of both- the objective is to communicate and establish a common understanding- not to be caught up and slowed by semantics
- Notation
  - Graphical syntax of the modeling language
  - Aka, the nitty gritty
- Meta-model
  - A diagram (usually a class diagram) that define the concepts of a language

## Activity Diagram

- Procedural and parallel behavior
- Aka, flow charts formalized, w/ an extension to describe parallel behavior
- ![activity-diagram](_images/uml/activity-diagram.png)

## Class Diagram

- Class, features, and relationships
- Describes the types of objects in the system and the various kinds of static relationships that exist among them
- Great for showing objects in detail, illustrating dependencies, etc
- Key concepts
  - Properties
- Structural features of a class
- Include attributes and associations
  - Attributes
    - Describes a property as a line of text w/in the class box itself
    - What you usually see when you have a condensed set of classes on a single page
  - Associations
    - Solid line between two classes, directed from source class to target class
    - Breaking down a class into parts w/ arrows and smaller boxes
    - Multiplicity
- Indication of the number of objects that may fill the property
  - Operations
- The actions that a class knows to carry out
- Operation
  - Something invoked on an object- the procedure declaration
- Method
  - Body of a procedure
- ![class-diagram](_images/uml/class-diagram.png)

## Communication Diagram

- Interaction between objects, emphasis on links
- Interaction diagram that emphasize the data links between various participants in an interaction
- ![communications-diagram](_images/uml/communications-diagram.png)

## Component Diagram

- Structure and connections of components
- The box w/ two pins on it you see sometimes is there to indicate that something is a component
- There’s an endless debate about what a class is vs a component, but usually it refers to a software entity that a customer can buy and worry about
- ![component-diagram](_images/uml/component-diagram.png)

## Composite Structure Diagram

- Runtime decomposition of a class
- New to UML 2

## Deployment Diagram

- Deployment of artifacts to nodes
- Shows a system’s physical layout revealing which pieces of software run on which pieces of hardware
- A “node” is something that can host some software
  - Nodes contain artifacts to run
- A “device” is hardware
- An “execution environment” is software that itself hosts/contains other software (ie, an OS or container process)
- ![deployment-diagram](_images/uml/deployment-diagram.png)

## Interaction Overview Diagram

- Mix of sequence and activity diagram

## Object Diagram

- Example configurations of instances
- A snapshot of objects in a system at a particular point in time
- Good for illustrating examples of objects connected together
- ![object-diagram](_images/uml/object-diagram.png)

## Organigram

- Software architecture diagram mentioned in _Making Embedded Systems_ along w/ context & block diagrams
- An org chart for software components
- ![organizational-diagram](_images/uml/organizational-diagram.png)
- > Keep your sketches messy enough that if you have to do it all over again, it doesn't make you want to give up.
  - Elicia White in _Making Embedded Systems_

## Package Diagram

- Compile-time hierarchic structure
- Package
  - Grouping construct to take any construct in UML and group them together into higher-level units- most common to group together classes, but can be applied to group together anything
- A package diagram shows packages and their dependencies
- ![package-diagram](_images/uml/package-diagram.png)

## Sequence Diagram

- Interaction between objects; emphasis on sequence
- Captures the behavior of a single scenario- where a number of example objects and messages are passed between each other in the particular use case
- ![sequence-diagram](_images/uml/sequence-diagram.png)

## State Machine diagram

- How events change an object over its life
- Describes the behavior of a system
- Used to describe the behavior of a system across multiple use cases

## Timing Diagram

- Interaction between objects; emphasis on timing
- Show timing constraints between state changes on different objects
- The usual waveform diagrams

## UML Jargon

- MDA
  - “model driven architecture”
- CRC cards
  - “class-responsibility-collaboration”
  - When you have a meeting w/ colleagues to simulate various scenarios w/ cards describing each class, their responsibilities, and their collaborators
- OMG
  - “object management group”
  - An open consortium of companies formed to build standards that support interoperability of OO systems
  - Known for COBRA (“common object request broker architecture”) standards
- Interaction diagram
  - Describe how groups of objects collaborate in some behavior
  - The most common interaction diagram is the sequence diagram

## Use Case Diagram

- How users interact w/ a system
- A “scenario” is a sequence of steps that describe an interaction between a user and a system
- A “use case” is a set of scenarios tied together by a common user goal
- Used to understand the functional requirements of a system
- ![use-case-diagram](_images/uml/use-case-diagram.png)

## Uses of UML

- UML as a sketch
  - When developers use UML to communicate some aspects of a system
  - Informal and dynamic- to be done quickly and collaboratively to talk about just the items worth talking about
  - Forward engineering
    - Drawing UML diagrams before coding
    - Objective is to discuss ideas, alternatives, and potential issues
    - Short 10 min sessions to talk w/ colleagues w/ UML visuals as an aid
  - Reverse engineering
    - Drawing UML diagrams after coding (to better understand existing code)
    - Using UML as an aid to talk about a part of a system
- UML as a blueprint
  - A detailed design for engineers to use to code up
  - Issues w/ using UML as a blueprint:
    - Fine details tie a diagram to a particular language and application
    - W/ too many details, it becomes a hassle to change the diagram in response to each software design change
    - The value of an abstract visual diminishes when a diagram is daunting to look at (pages and pages of diagrams)
  - To thoroughly describe an entire system w/ UML, a user might use CASE (“computer-aided software engineering”) tools to store and generate UML diagrams
  - Round-trip tools
    - CASE tools that can be used for both forward engineering (allow engineers to create and store UML diagrams on their own) and reverse engineering (generate UML diagrams from existing source code)
- UML as a programming language
  - Aka, MDA
  - When a CASE tool can generate source code

## What UML Diagrams to Use?

- The most useful are class diagrams, and after that it’s dependent on your particular project
