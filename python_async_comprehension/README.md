# Python - Async Comprehension

## Description
This project covers asynchronous generators and async comprehensions in Python 3.8. It shows how to write an async generator, how to use `async for`, and how to type-annotate generators with `AsyncGenerator`.

## Learning Objectives
- How to write an asynchronous generator
- How to use async comprehensions
- How to type-annotate generators

## Requirements
- Ubuntu 20.04 LTS
- Python 3.8 (`python3`)
- Code style: `pycodestyle` (version 2.5.x)
- All files start with `#!/usr/bin/env python3` and end with a new line
- All modules and functions are documented
- All functions and coroutines are type-annotated

## Tasks

### 0. Async Generator
**File:** `0-async_generator.py`

A coroutine called `async_generator` that takes no arguments. It loops 10 times, waits 1 second asynchronously each time, then yields a random number between 0 and 10.

**Usage:**
```bash
$ ./0-main.py
[4.403136952967102, 6.9092712604587465, 6.293445466782645, ...]
```

## Author
Abdulrhman Saleh Alduqil (d7ome989)
