#ifndef _LISTS_H_
#define _LISTS_H_

/**
 * struct listint_s - list
 * @n: int
 * @next: ptr
 * Description: singly-linked list node struct
 */

typedef struct listint_s
{
    int n;
    struct listint_s *next;
} listint_t;

size_t print_listint(const listint_t *h);
listint_t *add_nodeint_end(listint_t **head, const int n);
void free_listint(listint_t *head);

int is_palindrome(listint_t **head);
listint_t *reverse_listint(listint_t **head);

#endif
