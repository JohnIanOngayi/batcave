#ifndef __MAIN_H__
#define __MAIN_H__

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stddef.h>
#include <stdbool.h>

/**
 * MAX_NAME = A macro to define max characters for name
*/
#define MAX_NAME 256


/**
 * person_t - a struct defininga person's info
 * @name: the name of the person
 * @age: the age of the person
 * 
 * Description: each struct for a person
 */
typedef struct person
{
    char name[MAX_NAME];
    int age;
} person_t;


/**
 * hash_table - global variable that is a pointer to the hash table memblk
 */
extern person_t **hash_table;


/**
 * TABLE_SIZE - global variable that defines the size of the table
 */
extern int TABLE_SIZE;

person_t **init_hash(void);
person_t *hash_keeper(char *name, int age);
void print(void);
void _free(void *ptr);
void safe_free(void);

#endif /* __MAIN_H__ */