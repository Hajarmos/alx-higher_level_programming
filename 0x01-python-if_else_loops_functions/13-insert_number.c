#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/**
 * insert_node - Inserts a number into a sorted singly linked list
 * @head: list head
 * @number: data
 * Return: node address
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp, *temp2, *node;

	node = malloc(sizeof(listint_t));
	if (node)
	{
		node->n = number;
		node->next = NULL;
		if (!*head)
		{
			*head = node;
			return (node);
		}
		temp = *head;
		temp2 = temp->next;
		if (temp->n >= node->n)
		{
			node->next = temp;
			*head = node;
			return (node);
		}
		while (temp2)
		{
			if (temp2->n >= node->n)
			{
				node->next = temp2;
				temp->next = node;
				return (node);
			}
			temp = temp->next;
			temp2 = temp2->next;
		}
		temp->next = node;
		return (node);
	}
	else
		return (NULL);
}
