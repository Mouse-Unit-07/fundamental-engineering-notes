# Comments

- Clean comments notes
- Primarily from Robert C Martin's _Clean Code_

## Index

- [Index](#index)
- [Overview](#overview)
- [Bad Comments](#bad-comments)
- [Good Comments](#good-comments)

## Overview

- > The proper use of comments is to compensate for our failure to express ourself in code. Note that I used the word failure. I meant it.
  - Robert C. Martin in _Clean Code_
  - Comments (including obligatory Javadoc comments) demand maintaining, become lies when they’re not maintained, and invite doubt to begin with
  - Explain yourself through concise and descriptive source code instead

## Bad Comments

- **Mumbling**
  - Don’t talk to yourself through comments
  - If only you can interpret it, remove it or rewrite it
- **Redundant comments**
  - Don’t rewrite what the code already explains on its own
- **Misleading comments**
  - Comments that explain what’s being done tend to be wrong and misleading in subtle ways- don’t write them, just write why things are done if need be
- **Mandated comments**
  - Javadocs are silly if they’re mandated for no reason
  - They clutter code, and create potential for lies and misdirection
- **Journal comments**
  - Revision history, log messages, etc
  - That’s what version control is for- don’t add them
- **Noise comments**
  - Don’t state the obvious
  - Most common for mandated javadocs
  - Noise turns into scary noise when you accidentally write in lies
- **Add variables and functions instead of comments**
  - Variables encapsulate expressions into concepts, and functions encapsulate a series of processes into concepts
- **Position markers**
  - Comments that are used to mark a particular position in a source file are fine, but they should be used sparingly
  - The less there are, the more they stand out, and the less users will ignore them and consider them noise
  - When there are too many, they’re all translated to noise
- **Closing brace comments**
  - Often used to indicate what each closing brace is for
  - Write shorter functions instead
- **Attributions and bylines**
  - Authors, etc
  - That’s what version control is for- don’t add them
- **Commented-out code**
  - Horrible- they exist to rot, never to be uncommented
  - Delete them all- they’ll be saved in source control
- **HTML and multiple languages**
  - Minimize the number of languages in a single source file- we’re already working w/ English + source code language by default
  - Don’t force unnecessary context switching on the reader
- **Nonlocal information**
  - If a comment must be written, don’t add information about code elsewhere- comments are associated w/ where they’re written
- **Too much information**
  - Don’t add unnecessary background information
- **Unobvious connection**
  - Readers shouldn’t have to think about how your comments map to the code- make the connection as obvious as possible
- **Function headers**
  - Functions should describe themselves- this eliminates the need for both function headers and javadocs

## Good Comments

- **Legal comments**
  - Copyrights, etc- no way around it
- **Informative comments**
  - Do this if there’s absolutely no way for the code itself to explain the context- so when there’s a need to explain why something exists
  - Providing basic information with a comment (kept concise and descriptive as possible) is fine, provided above
- **Explanation of intent**
  - If there’s a design decision that can only be explained by elaborating on a piece of code (abstractions and descriptive names aren’t enough), then comments are valid
- **Clarification**
  - Obscure arguments and return values can be clarified if need be (a function name can beautifully describe the one thing it does, but fail to describe what it returns or takes in without the full function signature)
  - The issue again is that clarifications can lie or mislead- minimize at all costs and be concise
- **Warning of consequences**
  - Consequences of changing an implementation to something that would appear to be more efficient but not, a warning that a function takes a long time to run, etc
- **Todo comments**
  - TODOs are jobs that the programmer thinks should be done, but for some reason can’t do at the moment- it’s not an excuse to leave bad code in the system
- **Amplification**
  - If there are processes or decisions that seem inconsequential, a comment can be written to highlight it
- **Javadocs**
  - Write them if you absolutely have to- so if you’re writing a public API
  - Otherwise the maintenance isn’t worth it for the little benefit of having a bunch of documentation that should otherwise be inherit in your code that should already be explaining itself
