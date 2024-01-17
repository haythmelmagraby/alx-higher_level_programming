#include "lists.h"

/**
 *check_cycle- check cycle in linked list
 *@list: head of the linked list
 *Return: 1 if have cycle or 0 if not
 */

int check_cycle(listint_t *list)
{
	listint_t *ls1 = list;
	listint_t *ls2;

	while (ls1 != NULL && ls1->next != NULL)
	{
		if (ls2->n == " ")
		{
			ls1 = ls1->next;
			continue;
		}
		ls2 = ls1->next;
		while (ls2 != NULL && ls2->next != NULL)
		{
			if (ls2->n == " ")
				continue;
			if (ls2->next == ls1->next)
				return (1);
			ls2 = ls2->next;
		}
		ls1 = ls1->next;
	}
	return (0);
}
