# File

- File notes

## Index

- [Index](#index)
- [File Definition](#file-definition)
- [MP3](#mp3)
- [PDF, PNG, JPEG](#pdf-png-jpeg)
- [Repository, Folder, Directory](#repository-folder-directory)
- [Root File System](#root-file-system)
- [Symbolic Link](#symbolic-link)

## File Definition

- A "file" is just a sequence of bytes
- All IO devices (disks, keyboards, displays, networks, etc) are modeled as files
- Possible IO operations consist of:
  - Opening files
  - Changing current file position
  - Reading and writing files
  - Closing files

## MP3

- Aka, MPEG
- "moving picture experts group"
- Lossy compression file type for audio files

## PDF, PNG, JPEG

- “portable document format”
- “portable network graphics”
- “joint photographics experts group”

## Repository, Folder, Directory

- “repository” vs “folder” vs “directory”
  - Repository
    - Refers to data structure to store a collection of files
    - Used in version control system context
  - Folder
    - Aka directory
    - Container to organize files and folders
    - Contains an array of links mapping filenames to files
  - Directory
    - Aka folder
- Directories/folders are special files that abstract tables fo filenames and their respective references to the files on memory
  - Filename + reference are together called a "link", or "hard link" as opposed to "symbolic link"

## Root File System

- Top level directory from which all other directories branch from
- For Linux, `/` is the root file system

## Symbolic Link

- A type of file that points to another file/directory
  - So a file that serves as a pointer to another file
- ...UNIX's implementation of shortcuts in Windows
- Good for abstracting files, convenience, etc
- Ex: `/usr/ibn/python` -> `/usr/bin/python3.11`
- Hard link
  - The full path from the root directory
- Soft link
  - A relative path from where the symbolic link file sits
- Dangling link
  - A symbolic link that doesn't point to anything
