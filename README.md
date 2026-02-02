# NullSec HolyC Research

Research and tools for HolyC programming language (TempleOS).

## About HolyC

HolyC is the programming language created by Terry A. Davis for TempleOS. It's a unique language that combines:

- C-like syntax with simplified semantics
- Built-in assembly support
- JIT compilation
- No memory protection (direct hardware access)
- 64-bit only, ring 0 execution

## Key HolyC Features

### Syntax
```holyc
// Variables (no type declaration needed)
I64 x = 10;
U8 *str = "Hello";

// Functions
U0 PrintHello() {
    "Hello from HolyC!\n";  // Print is automatic
}

// Inline assembly
asm {
    MOV RAX, 60
    XOR RDI, RDI
    SYSCALL
}
```

### Memory
- Direct memory access
- No virtual memory
- No memory protection
- Manual everything

### Unique Features
- Dollar sign `$` for special operations
- Auto-print for expressions
- Built-in graphics
- Sound support
- No network stack

## NullSec HolyC Tools

### holyc-to-c
Transpiler converting HolyC to C for analysis.

### holyc-lint
Static analyzer for HolyC code.

### holyc-doc
Documentation generator.

## TempleOS VM Setup

### Requirements
- QEMU, VirtualBox, or VMware
- 512MB RAM minimum
- 2GB disk space

### Quick Start
```bash
# Download TempleOS
wget https://templeos.org/Downloads/TempleOS.ISO

# Create disk image
qemu-img create -f qcow2 templeos.qcow2 2G

# Run
qemu-system-x86_64 \
    -m 512M \
    -hda templeos.qcow2 \
    -cdrom TempleOS.ISO \
    -boot d \
    -enable-kvm
```

### After Install
```bash
# Boot from disk
qemu-system-x86_64 \
    -m 512M \
    -hda templeos.qcow2 \
    -enable-kvm \
    -soundhw pcspk
```

## Research Goals

1. **Understand HolyC internals**
   - JIT compilation process
   - Memory model
   - Kernel integration

2. **Security analysis**
   - Exploit vectors in ring 0
   - Memory corruption implications
   - Novel attack surfaces

3. **Port concepts to NullSec**
   - JIT compilation
   - Simplified syntax
   - Direct hardware access (controlled)

## Example HolyC Programs

See `examples/` directory for sample programs.

## License

MIT License - NullSec Project
