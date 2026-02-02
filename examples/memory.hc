// HolyC Direct Memory Access
// Demonstrates ring 0 power

U0 MemoryDemo() {
    // Direct memory read/write
    U8 *mem = 0x1000;  // Direct address
    
    "Reading memory at 0x1000: %02X\n", *mem;
    
    // Allocate memory
    U8 *buf = MAlloc(256);
    MemSet(buf, 0x41, 256);
    
    "Buffer filled with 'A'\n";
    
    Free(buf);
}

// Inline assembly example
U0 AsmDemo() {
    I64 result;
    
    asm {
        MOV RAX, 0x1337
        MOV [&result], RAX
    }
    
    "Assembly result: 0x%X\n", result;
}

MemoryDemo;
AsmDemo;
