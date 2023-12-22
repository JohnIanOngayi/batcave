#ifndef __MAIN_H__
#define __MAIN_H__

/*Standard Libraries*/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <time.h>
#include <unistd.h>
#include <stddef.h>
#include <stdbool.h>

/**
 * TABLE_SIZE - defines the size of the hash table arrray
 */
extern unsigned int TABLE_SIZE;

/**
 * person_t - a struct that holds user's information
 * @name: the person's name
 * @phone: the person's phone number
 * @state: the person's nationality
 * @age: the person's age in years
 * 
 * Description: This is the structure of the nodes of the linked list that
 *      form the hash table. Both the main array and the chain members use this.
 */
typedef struct member
{
	char *name;
	char *phone;
	char *state;
	int age;
	struct member *chain_next;
} person_t;


/**
 * hash_table - a global variable pointer to the  hash table memblk
 */
extern person_t **hash_table;

/*Hash Table Functionalities*/
person_t **init_hash(void);
unsigned int hash_insert(char *name, char *phone, char *state, int age);
void hash_lookup(const char *key);

/*Memory Handlers*/
void safe_free(void);
void _free(void *ptr);
void free_node(person_t *ptr);

#endif /*__MAIN_H__*/
