#ifndef __BINARY__
#define __BINARY__

#include <stdio.h>
#include <string.h>
#include <stddef.h>
#include <string.h>
#include <stdint.h>
#include <stdbool.h>

typedef struct bin_tree_node
{
        char *value;
        struct bin_tree_node *root;
        struct bin_tree_node *parent;
        struct bin_tree_node *right;
        struct bin_tree_node *left;
} node_t;

#endif /*__BINARY__*/
