#ifndef _LISTS_H_
#define _LISTS_H_

#include <stdlib.h>

/**
 * struct listint_s - singly-linked list
 * @n: int
 * @next: points to next node
 * Description: singly-linked list node struct
 */

typedef struct listint_s
{
    int n;
    struct listint_s *next;
} listint_t;

int check_cycle(list_t *list);

#endif
