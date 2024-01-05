#include "lists.h"

/*
 * check_cycle - inspects if singly-linked list has cycle
 * list - ptr to singly-linked list
 * Return: 0 no cycle 1 cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *current, *insp;

	if (list == NULL || list->next == NULL)
		return (0);

	current = list;
	insp = current->next;

	while (current != NULL && insp->next != NULL && insp->next->next != NULL)
	{
		if (current == insp)
			return (1);

		current = current->next;
		insp = insp->next->next;
	}

	return (0);
}
