#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: list
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *fast, *slow;

	if (!list || !list->next)
		return (0);
	slow = list->next;
	fast = list->next->next;
	while (fast && slow && fast->next)
	{
		if (slow == fast)
			return (1);
		slow = slow->next;
		fast = fast->next->next;
	}
	return (0);
}
