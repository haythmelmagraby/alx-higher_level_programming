#include "lists.h"
#include <stdio.h>
int is_palindrome(listint_t **head)
{
	int counter = 0;
	listint_t *temp = *head;
	if (*head == NULL)
		return (1)
	while (temp)
	{
		counter++;
		printf("counter : %d = %d\n",counter,temp->n);
		temp = temp->next;
	}
	temp = *head;
	while (head)
	{
		while (counter >= 0)
		{
			printf("*head = %d , temp[%d] = %d\n",(*head)->n,counter,temp[counter].n);
			if ((*head)->n != temp[counter].n)
				return (0);
			counter --;
		}
		*head = (*head)->next;
	}
	return (1);
}
