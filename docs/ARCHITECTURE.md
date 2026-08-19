# PolyOS Architecture Documentation

## Overview

PolyOS is a hybrid operating system combining a Rust-based kernel with Python userland. The system implements the **Advanced Resource Scheduling Architecture (ARSA)**, which provides intelligent task scheduling and resource allocation.

## System Architecture

```
┌─────────────────────────────────────────────────────┐
│               User Applications                      │
│         (Python Scripts, Services)                  │
└────────────────┬────────────────────────────────────┘
                 │
┌────────────────▼────────────────────────────────────┐
│         ARSKernel (user/ars_core.py)               │
│  ┌──────────────────────────────────────────────┐  │
│  │  Task Scheduling & Management                │  │
│  │  Resource Allocation Strategy                │  │
│  │  Multi-threading Support                     │  │
│  └──────────────────────────────────────────────┘  │
└────────────────┬────────────────────────────────────┘
                 │
┌────────────────▼────────────────────────────────────┐
│      Virtual Filesystem (exemple/filesystem.py)    │
│  ┌──────────────────────────────────────────────┐  │
│  │  In-Memory File System                       │  │
│  │  Directory & File Abstraction                │  │
│  │  Content Storage & Retrieval                 │  │
│  └──────────────────────────────────────────────┘  │
└────────────────┬────────────────────────────────────┘
                 │
┌────────────────▼────────────────────────────────────┐
│         Rust Kernel (kernel/)                       │
│  ┌──────────────────────────────────────────────┐  │
│  │  Low-Level Operations                        │  │
│  │  Hardware Abstraction                        │  │
│  │  System Resource Management                  │  │
│  └──────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────┘
```

## Core Components

### 1. ARSKernel (user/ars_core.py)

The **Advanced Resource Scheduling Kernel** is the heart of PolyOS. It manages task scheduling, resource allocation, and execution.

#### Key Classes

##### Task
```python
class Task:
    """
    Represents a schedulable unit of work.
    
    Attributes:
        name (str): Unique task identifier
        priority (int): Priority level (lower = higher priority)
        resource_requirement (dict): Required resources
        status (str): Current task status
    """
```

**Properties**:
- `name`: Unique identifier
- `priority`: Integer priority (0-10, lower = higher)
- `resource_requirement`: Dict with CPU, memory, etc.
- `status`: One of PENDING, RUNNING, COMPLETED, FAILED

##### ARSKernel
```python
class ARSKernel:
    """
    Main kernel managing task scheduling and execution.
    
    Methods:
        schedule(task): Add task to scheduling queue
        execute(): Run scheduled tasks
        get_status(): Get kernel status
    """
```

**Key Features**:
- Multi-threaded task execution
- Priority-based scheduling
- Resource-aware allocation
- Task dependency management

#### Scheduling Algorithm

The ARSKernel uses a **priority-based round-robin scheduling** algorithm:

1. **Priority Queue**: Tasks ordered by priority level
2. **Time Quantum**: Each task gets limited execution time
3. **Context Switching**: Switch between tasks based on time quantum
4. **Resource Awareness**: Consider available resources before scheduling

```
Scheduling Flow:
┌─────────────────┐
│  New Task       │
└────────┬────────┘
         │
         ▼
┌─────────────────────────┐
│ Priority Queue Sort     │
└────────┬────────────────┘
         │
         ▼
┌─────────────────────────┐
│ Resource Check          │
│ (CPU, Memory, etc.)     │
└────────┬────────────────┘
         │
    ┌────┴────┐
    │          │
    ▼          ▼
┌────────┐  ┌──────────┐
│Execute │  │Wait Queue│
└────────┘  └──────────┘
```

#### Thread Management

ARSKernel uses Python's `threading` module for concurrent task execution:

- **ThreadPool**: Manages worker threads
- **Locks**: Ensure thread-safe queue operations
- **Events**: Coordinate thread synchronization

### 2. Virtual Filesystem (exemple/filesystem.py)

Provides an in-memory filesystem abstraction for file and directory operations.

#### Key Classes

##### VirtualFile
```python
class VirtualFile:
    """
    Represents a file in virtual filesystem.
    
    Attributes:
        name (str): File name
        content (str): File content
        created_at (datetime): Creation timestamp
    """
```

##### VirtualDirectory
```python
class VirtualDirectory:
    """
    Represents a directory in virtual filesystem.
    
    Methods:
        add_file(name, content): Create file
        add_dir(name): Create subdirectory
        get_file(name): Retrieve file
        list_contents(): List directory contents
    """
```

#### Filesystem Operations

```
Directory Tree Example:
root/
├── home/
│   ├── user1/
│   │   └── config.txt
│   └── user2/
├── system/
│   └── kernel.log
└── var/
    └── cache/
```

**Supported Operations**:
- Create/delete files
- Create/delete directories
- Read/write content
- Navigate filesystem
- List directory contents

### 3. Rust Kernel (kernel/)

Low-level kernel operations implemented in Rust.

#### Responsibilities
- Hardware abstraction layer
- System call implementation
- Memory management
- Device drivers
- Interrupt handling

#### Build Process
```bash
cd kernel
cargo build
```

## Design Patterns

### 1. Singleton Pattern
ARSKernel implements singleton pattern:
```python
kernel = ARSKernel()
kernel.schedule(task)
```

### 2. Observer Pattern
Tasks notify kernel of status changes:
- Task completion
- Task failure
- Resource requirements change

### 3. Strategy Pattern
Different scheduling strategies can be implemented:
- Priority-based
- FIFO
- Round-robin
- Custom algorithms

## Data Flow

### Task Execution Flow

```
1. Task Creation
   └─→ Create Task object with requirements

2. Task Scheduling
   └─→ Add to ARSKernel queue
   └─→ Sort by priority

3. Resource Allocation
   └─→ Check available resources
   └─→ Allocate if sufficient

4. Task Execution
   └─→ Run in worker thread
   └─→ Update status

5. Task Completion
   └─→ Release resources
   └─→ Update completion time
```

### File Operation Flow

```
1. Filesystem Request
   └─→ File/Directory operation

2. Validation
   └─→ Check path validity
   └─→ Verify permissions

3. Execution
   └─→ Perform operation
   └─→ Update filesystem state

4. Response
   └─→ Return result/error
```

## Threading Model

PolyOS uses a **thread pool model** for concurrent task execution:

```
Main Thread
    │
    ├─→ Worker Thread 1 (Task execution)
    ├─→ Worker Thread 2 (Task execution)
    ├─→ Worker Thread 3 (Task execution)
    └─→ Worker Thread N (Task execution)
```

**Synchronization**:
- Thread-safe queues for task management
- Locks for shared resource access
- Events for thread coordination

## Performance Considerations

### 1. Task Scheduling
- **Time Complexity**: O(log n) priority queue operations
- **Space Complexity**: O(n) for task storage

### 2. Filesystem
- **File Lookup**: O(log n) with BST implementation
- **Directory Traversal**: O(n) for listing contents

### 3. Memory Management
- In-memory storage for filesystem
- Efficient task object recycling
- Resource pooling for threads

## Configuration

### Environment Variables
```bash
# Maximum worker threads
POLYOS_MAX_THREADS=4

# Default time quantum (ms)
POLYOS_TIME_QUANTUM=100

# Log level
POLYOS_LOG_LEVEL=INFO
```

### Runtime Settings
```python
kernel = ARSKernel(
    max_threads=4,
    time_quantum=100
)
```

## Testing Architecture

### Test Organization
```
tests/
├── test_ars_core.py       # ARSKernel tests
├── test_filesystem.py     # Filesystem tests
└── conftest.py           # Pytest configuration
```

### Test Coverage
- **ARSKernel**: 31+ unit tests
- **Filesystem**: 33+ unit tests
- **Total**: 64+ tests with 80%+ coverage

## Security Considerations

### Current Implementation
- Basic input validation
- No user isolation
- Single-user environment

### Future Enhancements
- User authentication
- Permission-based access control
- Resource quotas per user
- Audit logging

## Extensibility

### Adding New Features

1. **New Task Type**
   - Extend Task class
   - Implement in ARSKernel

2. **New Scheduling Algorithm**
   - Implement Strategy pattern
   - Register with kernel

3. **Filesystem Extensions**
   - Extend VirtualDirectory/VirtualFile
   - Implement new operations

## Performance Metrics

### Benchmark Results
- Task scheduling: ~0.1ms per task
- File creation: ~0.05ms per file
- Directory traversal: ~0.2ms per 100 items

## Deployment

### System Requirements
- Python 3.8+
- 4GB minimum RAM
- 2+ CPU cores recommended

### Installation
```bash
pip install -r requirements.txt
make dev-install
```

### Running
```bash
# Execute tasks
python -c "from user.ars_core import ARSKernel; kernel = ARSKernel(); ..."

# Or use QEMU for full system
tools/qemu_run.sh
```

## Future Roadmap

### Version 1.1
- [ ] Advanced scheduling algorithms
- [ ] Persistent filesystem support
- [ ] Network I/O support

### Version 1.2
- [ ] Multi-user support
- [ ] Permission system
- [ ] Process isolation

### Version 2.0
- [ ] Full POSIX compliance
- [ ] Real hardware support
- [ ] Production-ready kernel

## References

- [Python Threading Documentation](https://docs.python.org/3/library/threading.html)
- [Rust Book](https://doc.rust-lang.org/book/)
- [Operating Systems Concepts](http://www.os-book.com/)
- [Advanced Scheduling Algorithms](https://en.wikipedia.org/wiki/Scheduling_(computing))

---

**Last Updated**: August 19, 2026
**Maintainer**: Benjamin Polydec
