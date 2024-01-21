#include "lists.h"
/**
 *is_palindrome- check palindrome in linkedlist
 *@head: linked list header pointer
 *
 *Return: 0 if not palindrome and 1 if palindrome
 */

int is_palindrome(listint_t **head)
{
	int counter = 0, i;
	listint_t *temp = *head, *copy = temp;

	if (*head == NULL)
		return (1);
	while (temp)
	{
		counter++;
		temp = temp->next;
	}

	counter--;
	while (head)
	{
		if (counter == 0)
			return (1);
		i = 0;
		temp = copy;
		counter--;
		while (i <= counter)
		{
			temp = temp->next;
			i++;
		}
		if ((*head)->n != temp->n)
			return (0);
		*head = (*head)->next;
	}
	return (1);
}
