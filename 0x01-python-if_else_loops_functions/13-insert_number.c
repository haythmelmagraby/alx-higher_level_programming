#include "lists.h"
/**
 *insert_node- insert node in order of sorted linked list
 *@head: linkedlist array of pointers
 *@number: the value to be added
 *Return: the adree if SUCCESS and NULL if faild
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp = *head;
	listint_t *node = malloc(sizeof(listint_t));

	if(temp == NULL)
		return (NULL);


	while (temp != NULL && temp->next != NULL)
	{
		if (temp->n <= number && (temp->next)->n > number)
		{
			if (node == NULL)
				return (NULL);
			node->n = number;
			node->next = temp->next;
			temp->next = node;
			return (node);
		}
		temp = temp->next;
	}
	return (NULL);
}
