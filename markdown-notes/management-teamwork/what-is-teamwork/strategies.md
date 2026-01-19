# Teamwork Strategies

- Teamwork strategies notes

## Index

- [Index](#index)
- [Create a Single, Shared Source Code Repository](#create-a-single-shared-source-code-repository)
- [Pair Programming](#pair-programming)
- [Two-Pizza Team Rule](#two-pizza-team-rule)

## Create a Single, Shared Source Code Repository

- Integrating local discoveries across an entire organization is done best by having a single shared repo
- Includes:
  - Source code
  - Configuration standards for libraries, infrastructure, and environments (Chef, Puppet, Ansible scripts)
  - Deployment tools
  - Testing standards and tools, including security
  - Deployment pipeline tools
  - Monitoring and analysis tools
  - Tutorials and standards
- "repository" doesn't need to mean a single git repo (that's not possible)- it just means keep all technical knowledge in one place
  - No passing around files on local drives, multiple shared drives, depending on chats for critical documentation, etc

## Pair Programming

- Two engineers working together at the same workstation, to divide “driver” role and “navigator/observer/pointer” role
- Coined by Extreme Programming and Agile in early 2000s
- Allows one to focus on technical aspects, and the other to serve as a safety net
- Reinforces TDD, if one engineer focuses on automated tests, and the other engineer implements the code
- Allows for spread of knowledge
- The pair should frequently swap (90 min? some arbitrary/reasonable time) to allow diffusion of knowledge

## Two-Pizza Team Rule

- A team should only be as small as can be fed w/ two pizzas (5-10 people)
- Pros include:
  - Team has a clear, shared understanding of the system
  - Limits growth rate of product or service being worked on (to allow organization to maintain a shared understanding)
  - Decentralizes power and enables autonomy
  - Allows for employees to gain some leadership experience
