#include "lists.h"

/**
* print_dlistint - Prints all the elements of a dlistint_t list
* @h: A pointer to the head of the dlistint_t list
*
* Return: The number of nodes
*
*/

size_t print_dlistint(const dlistint_t *h)
{
size_t size = 0;

if (!h)
return (0);

while (h)
{
printf("%d\n", h->n);
h = h->next;
size++;
}

return (size);
}