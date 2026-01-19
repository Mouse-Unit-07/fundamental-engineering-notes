# High Level Software

- High level software notes
- List of niche/application specific high level software notes
- Concepts encountered when working w/ high level software- not about high-level languages or coding semantics

## Index

- [Index](#index)
- [DSN file](#dsn-file)
- [gRPC](#grpc)
- [JSON](#json)
- [Node.js](#nodejs)
- [npm](#npm)
- [Relational vs Document-Based Databases](#relational-vs-document-based-databases)
- [REST API](#rest-api)
- [Saas](#saas)
- [Trie](#trie)
- [WPF](#wpf)

## DSN file

- “data source name” file
- Contains information for applications to connect to a database

## gRPC

- ~~“google remote procedure call”~~
  - `gRPC` has Google origins, but it's now open source and the stance now is that the acronym doesn't stand for anything
- Framework by google to let services communicate w/ each other over a network
- Uses “protobufs” (protocol buffers) for serialization instead of JSON/XML
- Good to be used by microservices in distributed systems

## JSON

- “java script object notation”
- Used for things like data storage, data exchange between systems, configuration files, etc
- Databases often store data in JSON-like or in JSON format, so JSON files serve as a bridge between applications and databases

## Node.js

- A runtime environment for running JavaScript outside a web browser
- Built on Google's V8 JavaScript engine

## npm

- "node package manager"
- Default package manager for Node.js

## Relational vs Document-Based Databases

- Relational
  - Data stored in rows and columns
  - Tables accessed via keys
  - SQL (“structured query language”) used to query and manipulate data
  - Examples include MySQL, Microsoft SQL, etc
  - Good for enforcing rigid and consistent data
  - Bad for storing hierarchical/nested data
- Document-based
  - Data stored in documents (JSON/BSON) without predefined scheme
  - Good for dynamic data storage
  - Disadvantage is that querying data can get complex
  - Examples include MongoDB, Amazon DynamoDB, etc

## REST API

- "representational state transfer"
  - An architectural style introduced in 2000 to suggest an architecture where web services are:
    - Stateless
      - Server doesn't store any sessions
    - Cacheable
      - Responses can be cached for better performance
    - Uniform in interface
      - Standard HTTP verbs and predictable URLs
    - Client-server separated
      - UI/client logic separate from data/server logic
    - Layered
    - ...and optionally code-on-demand
- So a REST API is a web service interface that follows the REST style

## Saas

- “software as a service”
- Cloud-based software delivery model where apps are hosted by a provider and made available to users over the internet
- Users can subscribe to a service and access it online as opposed to installing software on local machines
- Ex: Word, excel, teams, github, emails, docs, etc

## Trie

- Special type of tree used to store associative data structures (typically strings)
- Every edge represents a character, and each node represents a sequence of characters

## WPF

- “Windows presentation format”
