#include "lists.h"
#include <stdio.h>
/*
 * check_cycle - checks if the singly linked list is a cycle
 * Return: 0 otherwise 1 if yes
 */
int check_cycle(listint_t *list)
{
	listint_t *f_ward = list;
	listint_t *b_ward = list;

	if (f_ward->next != NULL && f_ward->next->next != NULL)
	{
		f_ward = f_ward->next->next;
		b_ward = b_ward->next;

		if (f_ward == b_ward)
			return (1);
	}
	else 
		return (0);
}
