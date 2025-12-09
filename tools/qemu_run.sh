#!/usr/bin/env bash
set -e
KERNEL="kernel/target/debug/bootimage-kernel"
INITRAMFS="initramfs/initramfs.cpio"
qemu-system-x86_64 -machine q35 -m 1024 \
  -kernel ${KERNEL} \
  -initrd ${INITRAMFS} \
  -serial mon:stdio -nographic