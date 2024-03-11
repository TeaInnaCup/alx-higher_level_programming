#include "lists.h"

/**
 * check_cycle - checks if linked list has
 * cycle in it
 * @list: a pointer to the list
 * Return: 0 if no cycle,
 * 1 if there is.
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	while (fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (slow == fast)
			return (1);
	}

	return (0);
}
