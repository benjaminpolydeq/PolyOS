#!/usr/bin/env bash
set -e
OUT=initramfs/initramfs.cpio
pushd initramfs
find . | cpio -o -H newc > ../${OUT}
popd
echo "Wrote ${OUT}"