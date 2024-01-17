#include "lists.h"
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp = *head;
	listint_t *node;
	while (temp != NULL && temp->next != NULL){
	
			printf("%d >= %d && %d < %d = %d\n",temp->n,number,(temp->next)->n,number,(temp->n <= number && (temp->next)->n > number));

		if (temp->n <= number && (temp->next)->n > number)
		{
			printf("i am here");
			node = malloc(sizeof(listint_t));
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
