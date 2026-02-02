// HolyC Hello World
// Run in TempleOS: #include "hello.hc"

U0 Main() {
    "Hello from HolyC!\n";
    "Welcome to TempleOS!\n";
    
    I64 i;
    for (i = 0; i < 10; i++) {
        "Count: %d\n", i;
    }
}

Main;
