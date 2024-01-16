#include "lists.h"
/**
 *check_cycle - checks if a singly linked list has a cycle in it
 *@list : linked list
 *
 *Return : 0 if there is no cycle, 1 if there is a cycle
 * */

int check_cycle(listint_t *list){

	listint_t *l1 = list;
	listint_t *l2 = list;

	while (l1->next)
	{
		if(l1 != l2)
			{
			l1 = l1->next->next;
			l2 = l2->next;
			}
			else
			{
				return (1);
			}
	}
	return (0);
}
