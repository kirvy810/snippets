#include <unistd.h>

const char text[] = "Hello World!";

void __libc_start_main() {
    write(1, text, sizeof text);
    _exit(0);
}

int main() {
    return 0;
}
