#include "lists.h"

/**
 * check_cycle - used to detect an edles loop presence
 * @list: to be checked list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *yoseph = list;
	listint_t *ambo = list;

	if (list == NULL)
		return (0);
	while (yoseph && yoseph->next)
	{
		ambo = ambo->next;
		yoseph = yoseph->next->next;

		if (ambo == yoseph)
			return (1);
	}
	return (0);
}
