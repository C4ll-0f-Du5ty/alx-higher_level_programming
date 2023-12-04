#include "lists.h"

/**
 * is_palindrome - check if a linked list is a palindrome
 * @head: pointer to the head of the list
 * Return: 1 if palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	if (head == NULL || *head == NULL)
		return (1);

	return aux_palind(*head, *head);
}

/**
 * aux_palind - recursive helper function to check palindrome
 * @left: pointer to the left side of the sublist
 * @right: pointer to the right side of the sublist
 * Return: 1 if palindrome, 0 otherwise
 */
int aux_palind(listint_t *left, listint_t *right)
{
	if (right == NULL)
		return (1);

	if (aux_palind(left, right->next) && left->n == right->n)
		return (1);

	return (0);
}
