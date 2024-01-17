#include "lists.h"

/**
 *check_cycle- check cycle in linked list
 *@list: head of the linked list
 *Return: 1 if have cycle or 0 if not
 */

int check_cycle(listint_t *list)
{
	listint_t *list_o = list;
	listint_t *list_c = list;

	while (list_o && list_c)
	{
		list_o = list_o->next;
		list_c = list_c->next->next;
		if (list_o == list_c)
			return (1);
	}
	return (0);
}
