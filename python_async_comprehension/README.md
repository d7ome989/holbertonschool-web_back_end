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

### 1. Async Comprehensions
**File:** `1-async_comprehension.py`

A coroutine `async_comprehension` that collects 10 random numbers from `async_generator` using an async comprehension and returns them.

### 2. Run time for four parallel comprehensions
**File:** `2-measure_runtime.py`

A coroutine `measure_runtime` that runs `async_comprehension` four times in parallel with `asyncio.gather`, measures the total runtime, and returns it (roughly 10 seconds).

**Usage:**
```bash
$ ./0-main.py
[4.403136952967102, 6.9092712604587465, 6.293445466782645, ...]
```

## Author
Abdulrhman Saleh Alduqil (d7ome989)
