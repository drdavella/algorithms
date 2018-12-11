#include <stdlib.h>
#include <stdio.h>


typedef struct _node node_t;


struct _node
{
    node_t *next;
    int val;
};


void create_list(node_t **list, size_t n)
{
    size_t i = 0;
    node_t *this;


    if (n == 0)
    {
        return;
    }

    /* This will leak when the list is reversed. Oops. */
    *list = malloc(n * sizeof(node_t));
    this = *list;

    while (i < n)
    {
        this->val = i++;
        this->next = this + sizeof(node_t);
        this = this->next;
    }

    this->val = i;
    this->next = NULL;
}


void reverse_list(node_t **list)
{
    node_t *head = *list;
    node_t *old_next = NULL;
    node_t *new_next = NULL;

    for (;; head = old_next)
    {
        old_next = head->next;
        head->next = new_next;
        new_next = head;
        if (old_next == NULL)
        {
            break;
        }
    }

    *list = head;
}


void traverse_and_print(node_t *list)
{
    node_t *this = list;


    while (this != NULL)
    {
        printf("%d\n", this->val);
        this = this->next;
    }
}


int main()
{
    node_t *head = NULL;


    create_list(&head, 10);
    printf("forward:\n");
    traverse_and_print(head);

    reverse_list(&head);
    printf("reverse:\n");
    traverse_and_print(head);
}
