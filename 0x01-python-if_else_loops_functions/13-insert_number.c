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

	if (node == NULL)
	{
		free(node);
		return (NULL);
	}
	if (*head == NULL)
	{
		node->n = number;
		node->next = NULL;
		*head = node;
		return (*head);
	}

	while (temp != NULL)
	{
		if (temp->next == NULL)
		{
			if (temp->n <= number)
			{
				temp->next = node;
				node->n = number;
				node->next  = NULL;
			}
			else
			{
				node->next = temp;
				node->n = number;
			}
			return (node);
		}
		else if (temp->n <= number && (temp->next)->n > number)
		{
			node->n = number;
			node->next = temp->next;
			temp->next = node;
			return (node);
		}
		else if (number < temp->n)
		{
			node->n = temp->n;
			node->next = temp->next;
			temp->n = number;
			temp->next = node;
			return (temp);
		}
		temp = temp->next;
	}
	free(node);
	return (NULL);
}
