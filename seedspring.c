#include <stdio.h>
#include <time.h>
#include <stdlib.h>

int main(int argc, char const *argv[]) {
  time_t i = time(0);
  srand(i);
  for (int j = 0; j < 31; j++) {
    printf("%d\n", rand() & 0xf);
  }
  return 0;
}
