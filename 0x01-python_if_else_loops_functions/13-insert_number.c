#include "lists.h"

/**
 * insert_node - insert num to singly-linked list
 * @head: list head
 * @number: index to insert
 * Return: addr or NULL
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp, *h;
	int key;

	h = malloc(sizeof(listint_t));
	h->n = number;
	h->next = NULL;
	key = number;

	if (*head == NULL || key < (*head)->n)
	{
		h->next = *head;
		*head = h;
	}
	else
	{
		temp = *head;
		while (temp->next != NULL && temp->next->n < key)
			temp = temp->next;

		h->next = temp->next;
		temp->next = h;
	}

	return (*head);
}
