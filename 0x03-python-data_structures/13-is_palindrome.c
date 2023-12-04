#include "lists.h"
#include <stdlib.h>

/**
 * reverse - reverses a linked list
 * @head: double pointer to head node
 * Return: pointer to first node of reversed list
 */
listint_t *reverse(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *current = *head;
	listint_t *next;
	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	*head = prev;
	return (*head);
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: double pointer to head node
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head, *second_half, *prev_slow = *head;
	int res = 1; /* Initialize result */

	if (*head != NULL && (*head)->next != NULL)
	{
		/* Get the middle of the list */
		while (fast != NULL && fast->next != NULL)
		{
			fast = fast->next->next;
			prev_slow = slow;
			slow = slow->next;
		}

		/* fast would become NULL when there are even elements in list. */
		/* And not NULL for odd elements. We need to skip the middle node */
		/* for odd case and store it somewhere so that we can restore the */
		/* original list*/
		if (fast != NULL)
		{
			prev_slow = slow;
			slow = slow->next;
		}

		/* Now reverse the second half and compare it with first half */
		second_half = slow;
		prev_slow->next = NULL;					/* NULL terminate first half */
		reverse(&second_half);					/* Reverse the second half */
		res = compareLists(*head, second_half); /* compare */

		/* Construct the original list back */
		reverse(&second_half);			   /* Reverse the second half again */
		if (fast != NULL)				   /* If there was a mid node (odd size case) which */
			prev_slow->next = second_half; /* was not part of either first half or second half */
		else
			prev_slow->next = second_half;
	}
	return (res);
}

/**
 * compareLists - compares two linked lists
 * @head1: pointer to head of first list
 * @head2: pointer to head of second list
 * Return: 1 if lists are identical, 0 otherwise
 */
int compareLists(listint_t *head1, listint_t *head2)
{
	listint_t *temp1 = head1;
	listint_t *temp2 = head2;

	while (temp1 && temp2)
	{
		if (temp1->n == temp2->n)
		{
			temp1 = temp1->next;
			temp2 = temp2->next;
		}
		else
			return (0);
	}

	/* Both are empty reurn 1*/
	if (temp1 == NULL && temp2 == NULL)
		return (1);

	/* Will reach here when one is NULL and other is not */
	return (0);
}
