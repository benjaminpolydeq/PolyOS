# PolyOS

PolyOS v1 — prototype OS skeleton: microkernel-friendly repo, ARS userspace daemon, Kivy mobile UI and QEMU test harness.

See `docs/ARCHITECTURE.md` for details.

## Quick start (dev)

Requirements: rustup, cargo, qemu-system-x86_64, python3

```bash
# Build kernel (stub)
cd kernel
cargo build
cd ..

# Build initramfs
tools/build_initramfs.sh

# Boot in QEMU
tools/qemu_run.sh