#include <iostream>
#include <string>
#include <pthread.h>

#define NUM_THREADS 50
#define WAIT_TIME 1


struct thread_data {
    int thread_id;
    std::string message;
    int* counter;
};

static pthread_mutex_t mutex = PTHREAD_MUTEX_INITIALIZER;

void* thread_function(void* arg) {
    thread_data* data = (thread_data*) arg;
    std::cout << "Thread " << data->thread_id << " started - " << data->message << std::endl;
    for(int i = 0; i < 10; i++) {
        int counterValue = *data->counter;
        std::cout << "Thread ID: " << data->thread_id << " -- counter:" << counterValue << std::endl;
        for(int j = 0; j < WAIT_TIME; j++);
        pthread_mutex_lock(&mutex);
        (*data->counter)++;
        pthread_mutex_unlock(&mutex);
    }
    return NULL;
}

int main() {
    int counter = 0;
    pthread_t thread[NUM_THREADS];
    thread_data data[NUM_THREADS];

    for(int i = 0; i < NUM_THREADS; i++) {
        data[i].thread_id = i;
        data[i].message = "Hello ";
        data[i].message += std::to_string(i);
        data[i].counter = &counter;
        pthread_create(&thread[i], NULL, thread_function, (void*) &data[i]);
    }

    for(int i = 0; i < 10; i++) {
        std::cout << "main" << std::endl;
        for(int j = 0; j < WAIT_TIME; j++);
    }
    for(int i = 0; i < NUM_THREADS; i++) {
        pthread_join(thread[i], NULL);
    }

    return 0;
}

// to run:
// g++ -o bin/thread.exe src/thread_test.cpp -lpthread; bin/thread.exe

// to debug:
// g++ -g -o bin/thread.exe src/thread_test.cpp -lpthread; gdb bin/thread.exe