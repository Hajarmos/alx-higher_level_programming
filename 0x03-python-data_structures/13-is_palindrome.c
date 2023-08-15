#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * is_palindrome - check if list is palindrome
 * @head: head list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *temp = *head, *temp_t;
	unsigned int len = 0, lent, lentt;

	if (!temp || !temp->next)
		return (1);
	while (temp)
	{
		len ++;
		temp = temp->next;
	}
	temp = *head;
	lent = len;
	while (lent >= len / 2)
	{
		temp_t = *head;
		lentt = lent;
		while (lentt - 1)
		{
			temp_t = temp_t->next;
			lentt--;
		}
		if (temp->n == temp_t->n)
		{
			temp = temp->next;
			lent--;
		}
		else
			return (0);
	}
	return (1);
}
