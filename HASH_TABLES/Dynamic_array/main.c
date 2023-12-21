#include "main.h"

person_t **hash_table;
/**
 * main - main function
 * Return: 0 on success else failure
 */
int main(void)
{
    char *name = "John";
    int age = 30;
    int status = 0;

    hash_table = init_hash();
    if (!hash_table)
    {
        safe_free();
        return (-1);
    }
    printf("Successfully initialized hash table\n");
    printf("---------------------------------------------\n");
    person_t *hash_ptr = hash_keeper(name, age);
    printf("Allocated pointer: %p\n", (void *)hash_ptr);
    printf("---------------------------------------------\n");
    hash_ptr = hash_keeper(name, age);
    printf("Allocated pointer: %p\n", (void *)hash_ptr);
    printf("---------------------------------------------\n");
    hash_ptr = hash_keeper("James", 56);
    printf("Allocated pointer: %p\n", (void *)hash_ptr);
    printf("---------------------------------------------\n");
    hash_ptr = hash_keeper("Tom", 79);
    printf("Allocated pointer: %p\n", (void *)hash_ptr);
    printf("---------------------------------------------\n");
    hash_ptr = hash_keeper("zebedy", 19);
    printf("Allocated pointer: %p\n", (void *)hash_ptr);
    printf("---------------------------------------------\n");
    hash_ptr = hash_keeper("Trokr", 45);
    printf("Allocated pointer: %p\n", (void *)hash_ptr);
    printf("---------------------------------------------\n");
    hash_ptr = hash_keeper("Tristan", 25);
    printf("Allocated pointer: %p\n", (void *)hash_ptr);
    printf("---------------------------------------------\n");
    hash_ptr = hash_keeper("Ian", 23);
    printf("Allocated pointer: %p\n", (void *)hash_ptr);
    printf("---------------------------------------------\n");
    hash_ptr = hash_keeper("Franko", 78);
    printf("Allocated pointer: %p\n", (void *)hash_ptr);
    printf("---------------------------------------------\n");
    hash_ptr = hash_keeper("Boyle", 56);
    printf("Allocated pointer: %p\n", (void *)hash_ptr);
    printf("---------------------------------------------\n");
    hash_ptr = hash_keeper("Barry", 78);
    printf("Allocated pointer: %p\n", (void *)hash_ptr);
    printf("---------------------------------------------\n");
    hash_ptr = hash_keeper("Dwight", 48);
    printf("Allocated pointer: %p\n", (void *)hash_ptr);
    printf("---------------------------------------------\n");
    hash_ptr = hash_keeper("Choko Dodo", 18);
    printf("Allocated pointer: %p\n", (void *)hash_ptr);
    printf("---------------------------------------------\n");

    print();
    safe_free();

    return(status);
}