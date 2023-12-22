#include "main.h"

/**
 * main - this is the entry point
 */
int main(void)
{
	char *name = "John Smith";
	char *phone = "123-456-7890";
	char *state = "USA";
	int age = 25;
	int status = 0;

	hash_table = init_hash();
	status = hash_insert(name, phone, state, age);
	printf("----------------------------------------\n");
	status = hash_insert(name, phone, state, age);
	printf("----------------------------------------\n");
	status = hash_insert(name, phone, state, age);
	printf("----------------------------------------\n");
	status = hash_insert(name, phone, state, age);
	printf("----------------------------------------\n");
	status = hash_insert(name, phone, state, age);
	printf("----------------------------------------\n");
	status = hash_insert(name, phone, state, age);
	printf("----------------------------------------\n");
	status = hash_insert("Kai Havertz", "2929-2929-2929", "GERMANY", 24);
	printf("----------------------------------------\n");
	status = hash_insert("Declan Rice", "4141-4141-4141", "ENGLAND", 24);
	printf("----------------------------------------\n");
	status = hash_insert("Declan Rice", "4141-4141-4141", "ENGLAND", 24);
	printf("----------------------------------------\n");
	status = hash_insert("Declan Rice", "4141-4141-4141", "ENGLAND", 24);
	printf("----------------------------------------\n");
	status = hash_insert("Bukayo Saka", "0707-0707-0707", "ENGLAND", 22);
	printf("----------------------------------------\n");
	status = hash_insert("Gabriel Martinelli", "1111-1111-1111", "BRAZIL", 21);
	printf("----------------------------------------\n");
    hash_lookup(name);
    hash_lookup("Malala");

	return(status);
}
