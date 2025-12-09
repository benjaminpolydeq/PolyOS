.PHONY: all build-kernel build-initramfs run

all: build-kernel build-initramfs

build-kernel:
	cd kernel && cargo build

build-initramfs:
	tools/build_initramfs.sh

run: all
	tools/qemu_run.sh