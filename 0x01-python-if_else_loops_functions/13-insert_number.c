#include "lists.h"

/**
 * insert_node - inserts a number
 * @head: pointer
 * @number: number
 * Return: address
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *current;

	current = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;

	if (*head == NULL)
		*head = new;
	else
	{
		while (current->next != NULL)
		{
			if (current->next->n > number)
				break;

			current = current->next;
		}
		new->next = current->next;
		current->next = new;
	}

	return (new);
}
