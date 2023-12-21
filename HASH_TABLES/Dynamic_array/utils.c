#include "main.h"

int TABLE_SIZE;

/**
 * init_hash - initialises the hash table
 * Return: a pointer to the memblk or NULL
 */
person_t **init_hash(void)
{
	person_t **hash_space = NULL;
	int i = 0;

	TABLE_SIZE = 10;
	hash_space = (person_t **)malloc(sizeof(person_t *) * TABLE_SIZE);
	if (!hash_space)
		return (NULL);

	for (i = 0; i < TABLE_SIZE; i++)
	{
		hash_space[i] = NULL;
	}

	return(hash_space);
}


/**
 * hash_keeper - inserts a person into the hash table
 * @name: the person's name to insert
 * @age: the age's name to insert
 * Return: a pointer to the person's struct or NULL
 */
person_t *hash_keeper(char *name, int age)
{
	int index = 0;
	int i = 0;
	person_t *psn = NULL;

	(void)age;

	/*Randomise insertion using ASCII decimal values*/
	for (i = 0; name[i] != '\0'; i++)
	{
		index += name[i];
	}
	index = index % 10;

	if(hash_table[index])
	{
		printf("Index %d already occupied\n", index);
		for(i = 0; i < TABLE_SIZE; i++)
		{
			if (hash_table[i] == NULL)
			{
				index = i;
				break;
			}
			/*
			   else if (hash_table[i] && i == index)
			   {
			   index = (i + 1) % TABLE_SIZE;
			   break;
			   }
			 */
		}
		if (i == TABLE_SIZE)
		{
			hash_table = realloc(hash_table, (sizeof(person_t *) * (TABLE_SIZE + 1)));
			if (hash_table == NULL)
			{
				printf("hash table reallocation error");
				safe_free();
				return (NULL);
			}
			hash_table[TABLE_SIZE] = NULL;
			index = TABLE_SIZE;
			TABLE_SIZE++;
		}
	}
	printf("Assigned index: %d\n", index);

	psn = (person_t *)malloc(sizeof(person_t));
	if (!psn)
	{
		perror("malloc in hash_insert");
		safe_free();
		return (NULL);
	}
	printf("Person's pointer in table: %p\n", psn);
	strcpy(psn->name, name);
	printf("name inserted: %s\n", psn->name);
	psn->age = age;
	printf("age inserted: %d\n", psn->age);
	hash_table[index] = psn;

	return(hash_table[index]);
}


/**
 * safe_free - frees the hash table memblk
 */
void safe_free(void)
{
	int i = 0;
	for (i = 0; i < TABLE_SIZE; i++)
	{
		_free(hash_table[i]);
		hash_table[i] = NULL;
	}
	free(hash_table);
	hash_table = NULL;
}


/**
 * _free - safely frees a non-NULL pointer
 */
void _free(void *ptr)
{
	if (ptr)
		free(ptr);
	ptr = NULL;
}


/**
 * print - print contents of hash table
 */
void print(void)
{
	int i = 0;
	for (i = 0; i < TABLE_SIZE; i++)
	{
		if (hash_table[i]!= NULL)
		{
			printf("Index: %d\n", i);
			printf("Name: %s\n", hash_table[i]->name);
			printf("Age: %d\n", hash_table[i]->age);
			printf("-----><------\n");
		}
	}
}
