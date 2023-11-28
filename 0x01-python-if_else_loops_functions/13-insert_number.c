#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - Inserts a number into a sorted singly linked list
 * @head: Pointer to the pointer of the head of the list
 * @number: The number to be inserted
 *
 * Return: The address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *current, *prev;

	/* Allocate memory for the new node */
	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);

	/* Initialize the new node */
	new_node->n = number;
	new_node->next = NULL;

	/* If the list is empty or the number is less than the first node */
	if (*head == NULL || number < (*head)->n)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}

	/* Traverse the list to find the correct position to insert the new node */
	current = *head;
	prev = NULL;
	while (current != NULL && number >= current->n)
	{
		prev = current;
		current = current->next;
	}

	/* Insert the new node at the correct position */
	prev->next = new_node;
	new_node->next = current;

	return (new_node);
}
