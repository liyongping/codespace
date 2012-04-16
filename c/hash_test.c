#include <stdio.h>
#include <stdint.h>

#include "hash.h"

/**
 * gcc hash.c hash_test.c
 */
int main(int argc, char *argv[])
{
    char *key = "testkey";
    printf ("key:%s,length:%d,hash value:%d\n", key, strlen(key), hash(key,strlen(key),0));
    return 0;
}

