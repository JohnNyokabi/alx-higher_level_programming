#include "lists.h"

/**
 * check_cycle - checks whether singly-linked list contains a cycle
 * @list: A singly-linked list
 *
 * Return: 0 if no cycle and 1 if a cycle exists
 */
int check_cycle(listint_t *list)
{
	listint_t *fast = list, *slow = list;

	if (!list)
		return (0);
	while (1)
	{
		/* traverse through nodes as long as linked lists exists */
		if (fast->next != NULL && fast->next->next != NULL)
		{
			fast = fast->next->next;
			slow = slow->next;

			if (fast == slow)/* incase the nodes match, cycle found */
				return (1);
		}
		else
			return (0);
	}
}
