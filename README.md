# PolyOS - Advanced Resource Scheduling Architecture

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg)
![Tests](https://github.com/benjaminpolydeq/PolyOS/workflows/Tests%20and%20Coverage/badge.svg)
![Linting](https://github.com/benjaminpolydeq/PolyOS/workflows/Lint%20and%20Format%20Check/badge.svg)

PolyOS is an innovative operating system that combines modern kernel architecture with advanced resource scheduling capabilities. The system implements the **Advanced Resource Scheduling Architecture (ARSA)** to provide efficient multi-threaded resource management and virtual filesystem abstraction.

## 🎯 Features

- **Advanced Resource Scheduling (ARSA)**: Intelligent scheduling algorithm for optimal resource allocation
- **Virtual Filesystem**: In-memory filesystem abstraction with directory and file support
- **Multi-threaded Support**: Efficient handling of concurrent operations
- **Kernel Architecture**: Rust-based kernel with Python userland
- **Comprehensive Testing**: 64+ unit tests with high coverage
- **Development Tools**: Makefile, CI/CD pipelines, and development workflows

## 📋 Table of Contents

- [Quick Start](#quick-start)
- [Installation](#installation)
- [Usage](#usage)
- [Architecture](#architecture)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip/pip3
- Make
- Rust and Cargo (for kernel development)

### Installation

Clone the repository:
```bash
git clone https://github.com/benjaminpolydeq/PolyOS.git
cd PolyOS
```

Install dependencies:
```bash
make dev-install
```

### Basic Usage

```python
from user.ars_core import ARSKernel, Task
from exemple.filesystem import VirtualDirectory

# Initialize the kernel
kernel = ARSKernel()

# Create tasks
task1 = Task("process_1", priority=1, resource_requirement={"cpu": 2, "memory": 1024})
task2 = Task("process_2", priority=2, resource_requirement={"cpu": 1, "memory": 512})

# Schedule tasks
kernel.schedule(task1)
kernel.schedule(task2)

# Execute scheduled tasks
kernel.execute()

# Create virtual filesystem
root = VirtualDirectory("root")
root.add_dir("home")
root.add_file("config.txt", "System configuration")
```

## 🏗️ Architecture

PolyOS implements a hybrid architecture:

### Components

1. **ARSKernel (user/ars_core.py)**
   - Task scheduling and management
   - Resource allocation strategy
   - Multi-threading support
   - Task execution engine

2. **Virtual Filesystem (exemple/filesystem.py)**
   - In-memory file system
   - Directory and file abstractions
   - Content storage and retrieval

3. **Kernel (kernel/)**
   - Rust-based low-level operations
   - System-level resource management
   - Hardware abstraction

For detailed architecture documentation, see [ARCHITECTURE.md](docs/ARCHITECTURE.md).

## 🧪 Testing

Run the complete test suite:
```bash
make test
```

Run specific test modules:
```bash
pytest tests/test_ars_core.py -v
pytest tests/test_filesystem.py -v
```

Generate coverage report:
```bash
make test
# Coverage report available in htmlcov/index.html
```

### Test Coverage
- **ARSKernel**: 31 comprehensive tests
- **Virtual Filesystem**: 33 comprehensive tests
- **Total**: 64+ unit tests

## 🔧 Development

### Available Commands

```bash
make help           # Show all available commands
make lint           # Run ruff linter
make format         # Format code with ruff
make test           # Run tests with coverage
make clean          # Clean build artifacts
make install        # Install runtime dependencies
make dev-install    # Install all dependencies
```

### Code Quality

Code must pass linting checks before merging:
```bash
make lint
make format
```

### CI/CD Pipeline

The project includes automated workflows:
- **Lint Check** (`.github/workflows/lint.yml`): Validates code quality
- **Tests** (`.github/workflows/test.yml`): Runs full test suite

## 📚 Documentation

- [Architecture Guide](docs/ARCHITECTURE.md) - Detailed system architecture
- [Contributing Guide](CONTRIBUTING.md) - How to contribute
- [API Documentation](docs/API.md) - API reference

## 🤝 Contributing

We welcome contributions! Please read our [Contributing Guide](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👨‍💻 Author

**Benjamin Polydec** - [GitHub Profile](https://github.com/benjaminpolydeq)

## 🙏 Acknowledgments

- Python community for excellent libraries (kivy, pytest, ruff)
- Rust community for systems programming tools
- Contributors and testers

## 📞 Support

For support, please:
1. Check the [documentation](docs/)
2. Search [existing issues](https://github.com/benjaminpolydeq/PolyOS/issues)
3. Create a [new issue](https://github.com/benjaminpolydeq/PolyOS/issues/new) if needed

---

**Status**: Active Development 🚀

Last Updated: August 19, 2026
