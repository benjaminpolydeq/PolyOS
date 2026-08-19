# Contributing to PolyOS

Thank you for your interest in contributing to PolyOS! This document provides guidelines and instructions for contributing to the project.

## Code of Conduct

We are committed to providing a welcoming and inclusive environment for all contributors. Please be respectful and constructive in all interactions.

## How Can I Contribute?

### Reporting Bugs

Before creating a bug report, please check the [issue list](https://github.com/benjaminpolydeq/PolyOS/issues) to avoid duplicates.

When creating a bug report, include:
- **Title**: Clear and descriptive
- **Description**: What you expected vs. what actually happened
- **Steps to reproduce**: Detailed steps to reproduce the issue
- **Environment**: Python version, OS, relevant dependencies
- **Logs**: Any relevant error messages or logs

### Suggesting Enhancements

Enhancement suggestions are tracked as [GitHub issues](https://github.com/benjaminpolydeq/PolyOS/issues).

When suggesting an enhancement:
- Use a clear and descriptive title
- Provide a detailed description of the enhancement
- List some examples of how this would be used
- Explain why this enhancement would be useful

### Pull Requests

Follow these steps to submit a pull request:

1. **Fork the repository** and create a new branch from `develop`
2. **Clone your fork**:
   ```bash
   git clone https://github.com/YOUR_USERNAME/PolyOS.git
   cd PolyOS
   ```

3. **Create a feature branch**:
   ```bash
   git checkout -b feature/your-feature-name
   # or
   git checkout -b fix/your-bug-fix
   ```

4. **Install development dependencies**:
   ```bash
   make dev-install
   ```

5. **Make your changes** and commit them:
   ```bash
   git add .
   git commit -m "feat: add your feature description"
   ```

6. **Run tests and linting**:
   ```bash
   make lint
   make format
   make test
   ```

7. **Push to your fork**:
   ```bash
   git push origin feature/your-feature-name
   ```

8. **Create a Pull Request** on GitHub with:
   - Clear title describing the changes
   - Detailed description of what the PR does
   - Reference to any related issues (e.g., "Fixes #123")
   - Confirmation that tests pass

## Development Workflow

### Setting Up Your Development Environment

1. Clone the repository:
   ```bash
   git clone https://github.com/benjaminpolydeq/PolyOS.git
   cd PolyOS
   ```

2. Install dependencies:
   ```bash
   make dev-install
   ```

3. Verify installation:
   ```bash
   make test
   make lint
   ```

### Making Changes

#### Code Style

- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) for Python code
- Use meaningful variable and function names
- Add docstrings to functions and classes
- Keep functions small and focused

#### File Organization

```
PolyOS/
├── user/              # User-space modules
│   └── ars_core.py   # ARSKernel implementation
├── exemple/           # Example implementations
│   └── filesystem.py # Virtual filesystem
├── tests/            # Test modules
├── kernel/           # Rust kernel
├── docs/             # Documentation
└── tools/            # Build and utility scripts
```

#### Adding Tests

When adding new features, please include tests:

1. Create test functions in appropriate test file:
   ```python
   def test_new_feature():
       # Arrange
       setup_data = prepare_test_data()
       
       # Act
       result = function_under_test(setup_data)
       
       # Assert
       assert result == expected_value
   ```

2. Run tests to ensure they pass:
   ```bash
   make test
   ```

3. Check coverage:
   ```bash
   pytest tests/ --cov=user --cov=exemple --cov-report=html
   ```

### Commit Messages

Write clear, concise commit messages:

```
feat: add new feature description
^--- Type

fix: resolve issue description
^--- Type

docs: update documentation
^--- Type

Detailed explanation of the change if needed.
Reference any related issues: Fixes #123, Related to #456
```

**Types**:
- `feat`: A new feature
- `fix`: A bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, etc.)
- `refactor`: Code refactoring
- `test`: Adding or updating tests
- `chore`: Build, dependencies, or tooling changes
- `ci`: CI/CD pipeline changes

### Running Tests Locally

```bash
# Run all tests
make test

# Run specific test file
pytest tests/test_ars_core.py -v

# Run with coverage
pytest tests/ --cov=user --cov=exemple --cov-report=term-missing

# Run tests for specific Python version (if available)
tox
```

### Code Quality Checks

```bash
# Run linter
make lint

# Format code
make format

# Clean artifacts
make clean
```

## Pull Request Process

1. **Ensure all tests pass**: `make test`
2. **Ensure code quality**: `make lint` and `make format`
3. **Update documentation** if needed
4. **Add/update tests** for new functionality
5. **Write descriptive commit messages**
6. **Wait for review** from project maintainers

### PR Review Checklist

Your PR should:
- ✅ Have a clear title and description
- ✅ Reference any related issues
- ✅ Pass all CI/CD checks (lint, tests)
- ✅ Include tests for new functionality
- ✅ Update documentation if needed
- ✅ Follow code style guidelines
- ✅ Have no merge conflicts

## Documentation

When contributing code:

1. **Add docstrings** to functions and classes:
   ```python
   def schedule(self, task: Task) -> None:
       """
       Schedule a task for execution.
       
       Args:
           task (Task): The task to schedule
           
       Raises:
           ValueError: If task is invalid
       """
   ```

2. **Update README.md** if adding features
3. **Update ARCHITECTURE.md** if changing system design
4. **Add inline comments** for complex logic

## Testing Requirements

- **Minimum coverage**: 80%
- **All new features** must include tests
- **Bug fixes** should include regression tests
- **Tests must pass** on Python 3.8, 3.9, 3.10, 3.11

## Release Process

Releases are managed by project maintainers:

1. Update version in `pyproject.toml`
2. Update CHANGELOG.md
3. Create a release tag: `v1.0.0`
4. GitHub Actions automatically publishes the release

## Questions or Need Help?

- 📖 Check the [documentation](docs/)
- 🐛 Search [existing issues](https://github.com/benjaminpolydeq/PolyOS/issues)
- 💬 Create a [discussion](https://github.com/benjaminpolydeq/PolyOS/discussions)
- 📧 Contact the maintainers

## Additional Resources

- [Python Style Guide (PEP 8)](https://www.python.org/dev/peps/pep-0008/)
- [Git Documentation](https://git-scm.com/doc)
- [GitHub Flow Guide](https://guides.github.com/introduction/flow/)
- [Writing Good Commit Messages](https://chris.beams.io/posts/git-commit/)

---

**Thank you for contributing to PolyOS!** 🙏

Your contributions make this project better for everyone.
