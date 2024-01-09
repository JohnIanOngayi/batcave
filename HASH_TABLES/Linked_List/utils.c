#include "main.h"

person_t **hash_table;
unsigned int TABLE_SIZE;

/**
 * init_hash - Initialises the hash table main 'branch' array
 * Return: a pointer to the hash table memblk
 */
person_t **init_hash(void)
{
	person_t **hash_space = NULL;
	int i = 0;

	TABLE_SIZE = 10;
	hash_space = (person_t **)malloc(sizeof(person_t *) * TABLE_SIZE);
	if(hash_space == NULL)
	{
		perror("init malloc error");
		return(NULL);
	}

	for(i = 0; i < TABLE_SIZE; i++)
	{
		hash_space[i] = NULL;
	}
	printf("Initialised hash main branch\n");
	return(hash_space);
}


/**
 * hash_insert - inserts data into the hash table
 * @name: the name of the person, can be reused as the key
 * @phone: the person's phone number
 * @state: the person's nationality
 * @age: the person's age in years
 * Return: 0 on success, -1 on failure
 */
unsigned int hash_insert(char *name, char *phone, char *state, int age)
{
	unsigned index = 0;
	person_t *ptr = NULL;
	person_t *new = NULL;
	char *str;
	int i = 0;

	/*Using ASCII character decimal values to choose index on main*/
	for(i = 0; name[i] != '\0'; i++)
	{
		index += name[i];
		index %= TABLE_SIZE;
	}
	index %= TABLE_SIZE;

	new = (person_t *)malloc(sizeof(person_t));
	if(new == NULL)
	{
		perror("hash_insert malloc error");
		return(-1);
	}

	/*Inserting name into member node*/
	new->name = malloc(sizeof(char) * (strlen(name) + 1));
	if((new->name) == NULL)
	{
		perror("hash_insert malloc error");
		return(-1);
	}
	strcpy(new->name, name);

	/*Inserting phone into member node*/
	new->phone = malloc(sizeof(char) * (strlen(phone) + 1));
	if((new->phone) == NULL)
	{
		perror("hash_insert malloc error");
		return(-1);
	}
	strcpy(new->phone, phone);

	/*Inserting state into member node*/
	new->state = malloc(sizeof(char) * (strlen(state) + 1));
	if((new->state) == NULL)
	{
		perror("hash_insert malloc error");
		return(-1);
	}
	strcpy(new->state, state);

	new->age = age;
	new->chain_next = NULL;

	/*Adding node to list*/
	if(hash_table[index])
	{
		printf("Index %d on main already assigned\n", index);
		if(hash_table[index]->chain_next == NULL)
		{
			printf("First chain element\n");
			hash_table[index]->chain_next = new;
			return(0);
		}
		ptr = hash_table[index]->chain_next;
		while(ptr->chain_next)
		{
			ptr = ptr->chain_next;
		}
		ptr->chain_next = new;
		return(0);
	}
	hash_table[index] = new;
	printf("Assigned index: %d\n", index);
	printf("Assigned at location: %p on main\n", hash_table[index]);
	printf("Assigned at location on chain: %p on chain\n", new);
	return(0);
}


/**
 * hash_lookup - looks up values for a certain name
 */
void hash_lookup(const char *key)
{
	int value = 0;
	int index = 0;
	int i = 0, *ptr = NULL;
	int entry = 0;
	person_t *ptr = NULL;

	for(i = 0; key[i] != '\0'; i++)
	{
		value += key[i];
		value = value % 10;
	}
	index = value;
	ptr = hash_table[index];
	while(ptr)
	{
		if (strncmp(key, ptr->name, strlen(key)) == 0)
		{
			entry++;
			printf("----------------------\n");
			printf("----------------------\n");
			printf("Data for %s\n", key);
			printf("Occurence %d\n", entry);
			printf("----------------------\n");
			printf("Full Names        : %s\n", ptr->name);
			printf("Mobile Number     : %s\n", ptr->phone);
			printf("State/ Nationality: %s\n", ptr->state);
			printf("Age in Years      : %d\n", ptr->age);
			printf("----------------------\n");
		}
		ptr = ptr->chain_next;
		if (entry == 0)
		{
			printf("Invalid Key.No records of %s\n", key);
		}
	}
	if (entry == 0)
	{
		printf("Invalid Key.\nNo records of %s\n", key);
	}
}


/**
 * hash_delete - deletes a node in the hash table
 * @key: the name of the info to be purged
 */
 void hash_delete(char *key)
 {
    int value = 0;
	int index = 0;
	int i = 0;
	int entry = 0;
	person_t *head = NULL;
	person_t *iter = NULL;
	person_t *stiff = NULL;

	for(i = 0; key[i] != '\0'; i++)
	{
		value += key[i];
		value = value % 10;
	}
    index = value;
    head = hash_table[index];
	if(hash_table[i]->chain_next)
	{
		iter = hash_table[i]->chain_next;
	}
 }