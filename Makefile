.PHONY: help lint test format clean install dev-install all build-kernel build-initramfs run

help:
	@echo "PolyOS Development Commands"
	@echo "=============================="
	@echo "make lint          - Run ruff linter on all Python code"
	@echo "make test          - Run pytest with coverage report"
	@echo "make format        - Format code with ruff (fix style issues)"
	@echo "make clean         - Remove build artifacts and cache files"
	@echo "make install       - Install runtime dependencies"
	@echo "make dev-install   - Install runtime + development dependencies"
	@echo "make all           - Build kernel and initramfs"
	@echo "make build-kernel  - Build Rust kernel"
	@echo "make build-initramfs - Build initial ramdisk"
	@echo "make run           - Build and run with QEMU"

lint:
	@echo "Running ruff linter..."
	ruff check user/ exemple/ tests/ --show-source --statistics

test:
	@echo "Running pytest with coverage..."
	pytest tests/ -v --tb=short --cov=user --cov=exemple --cov-report=term-missing --cov-report=html
	@echo "Coverage report generated in htmlcov/index.html"

format:
	@echo "Formatting code with ruff..."
	ruff check user/ exemple/ tests/ --fix
	@echo "Code formatting complete"

clean:
	@echo "Cleaning build artifacts..."
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete
	find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".coverage" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name "htmlcov" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".ruff_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name "*.egg-info" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name "dist" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name "build" -exec rm -rf {} + 2>/dev/null || true
	@echo "Cleanup complete"

install:
	@echo "Installing runtime dependencies..."
	pip install -r requirements.txt

dev-install:
	@echo "Installing development dependencies..."
	pip install -r requirements.txt -r requirements-dev.txt

all: build-kernel build-initramfs

build-kernel:
	cd kernel && cargo build

build-initramfs:
	tools/build_initramfs.sh

run: all
	tools/qemu_run.sh

.DEFAULT_GOAL := help
