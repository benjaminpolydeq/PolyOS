#![no_std]
#![no_main]

use core::panic::PanicInfo;

#[no_mangle]
pub extern "C" fn _start() -> ! {
    // Write to serial port (0x3f8) for QEMU serial console
    unsafe {
        const COM1: u16 = 0x3f8;
        let s = b"PolyOS kernel: hello from no_std kernel!\n";
        for &b in s {
            core::ptr::write_volatile((COM1 as *mut u8), b);
        }
    }

    loop {}
}

#[panic_handler]
fn panic(_info: &PanicInfo) -> ! {
    loop {}
}