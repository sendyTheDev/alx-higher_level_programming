#include "lists.h"
#include <stddef.h>
/*
 * insert_node - insert node into sorted singly linked list
 * @head: pointer to head of linked list
 * @number: data for new node
 * Return:  the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	 listint_t *san = NULL;
	 listint_t *new = NULL;

	 if (!head)
		 return (NULL);

	 if (*head == NULL)
	 {
		 *head = new;
		 (*head)->next = NULL;
		 new->n = number;
		 return (new);
	 }

	 san = *head;
	 while (san->next != NULL)
	 {
		 if (new->n < san->n)
		 {
			 new->next = san;
			 *head = new;
			 return (new);
		 }
		 if (((new->n > san->n) && (new->n < (san->next)->n)) || (new->n == san->n))
		 {
			 new->next = san->next;
			 san->next = new;
			  return (new);
		 }
		 san = san->next;
	 }
	 san->next = new;
	 return (new);
}
