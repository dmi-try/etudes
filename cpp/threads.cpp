#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

#define NUMBER_OF_THREADS 10
void *print_hello_world(void *tid) {
  int delay = rand() % 4;
  sleep(delay);
  printf("Hello world from thread N%d that slept for %d seconds\n", tid, delay);
  pthread_exit(NULL);
}

int main(int argc, char *argv[]) {
  pthread_t threads[NUMBER_OF_THREADS];
  int status, i;

  srand(time(0));
  for(i=0; i < NUMBER_OF_THREADS; i++) {
    printf("Main process. Creating thread N%d\n", i);
    status = pthread_create(&threads[i], NULL, print_hello_world, (void *)i);

    if (status != 0) {
      printf("pthread_create failed with code %d\n", status);
      exit(-1);
    }
  }
  for(i=0; i < NUMBER_OF_THREADS; i++) {
    pthread_join(threads[i], NULL);
  }
  exit(NULL);
}
