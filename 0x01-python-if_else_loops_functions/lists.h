#ifndef _LISTS_H_
#define _LISTS_H_
#include <stdlib.h>
#include <stddef.h>

/**
 * struct listint_s - singly linked list
 * @n: integer
 * @next: pts to next node
 * Description: singly-linked list node struct
 */
typedef struct listint_s
{
	int n;
	struct listint_s *next;
} listint_t;

listint_t *insert_node(listint_t **head, int number);

#endif
