#include "lists.h"

/**
 *check_cycle- check cycle in linked list
 *@list: head of the linked list
 *Return: 1 if have cycle or 0 if not
 */

int check_cycle(listint_t *list)
{
	listint_t *ls1 = list;
	listint_t *ls2 = list;

	while (ls1 != NULL && ls1->next != NULL)
	{
		ls1 = ls1->next;
		ls2 = ls2->next->next;
		if (ls1 == ls2)
			return (1);
	}
	return (0);
}
