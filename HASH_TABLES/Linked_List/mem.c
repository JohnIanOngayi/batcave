#include "main.h"

/**
 * safe_free - frees the hash table memblk
 */
void safe_free(void)
{
	int i = 0;
	person_t *head = NULL;
	person_t *iter = NULL;
	person_t *stiff = NULL;

	for(i = 0; i < TABLE_SIZE; i++)
	{
		if(hash_table[i]->chain_next)
		{
			iter = hash_table[i]->chain_next;
			head = hash_table[i]->chain_next;
			stiff = hash_table[i]->chain_next;
			while(iter)
			{
				stiff = iter->chain_next;
				free_node(iter);
				iter = stiff;
			}
			_free(head);
		}
	}
	for(i = 0; i < TABLE_SIZE; i++)
	{
		free_node(hash_table[i]);
	}
	_free(hash_table);
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
 * free_node - frees a node in hash table list
 * @ptr: a pointer to the node
 */
void free_node(person_t *ptr)
{
	_free(name);
	_free(phone);
	_free(state);
	_free(ptr);
}
