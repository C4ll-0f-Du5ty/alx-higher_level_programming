#include <Python.h>

void custom_print_python_list(PyObject *p);
void custom_print_python_bytes(PyObject *p);

/**
 * custom_print_python_list - Prints customized info about Python lists.
 * @p: A PyObject list object.
 */
void custom_print_python_list(PyObject *p)
{
    int size, alloc, i;
    const char *type;
    PyListObject *list = (PyListObject *)p;
    PyVarObject *var = (PyVarObject *)p;

    size = var->ob_size;
    alloc = list->allocated;

    printf("[*] Custom Python list info\n");
    printf("[*] Custom Size of the Python List = %d\n", size);
    printf("[*] Custom Allocated = %d\n", alloc);

    for (i = 0; i < size; i++)
    {
        type = list->ob_item[i]->ob_type->tp_name;
        printf("Custom Element %d: %s\n", i, type);
        if (strcmp(type, "bytes") == 0)
            custom_print_python_bytes(list->ob_item[i]);
    }
}

/**
 * custom_print_python_bytes - Prints customized info about Python byte objects.
 * @p: A PyObject byte object.
 */
void custom_print_python_bytes(PyObject *p)
{
    unsigned char i, size;
    PyBytesObject *bytes = (PyBytesObject *)p;

    printf("[.] Custom bytes object info\n");
    if (strcmp(p->ob_type->tp_name, "bytes") != 0)
    {
        printf("  [ERROR] Custom Invalid Bytes Object\n");
        return;
    }

    printf("  Custom size: %ld\n", ((PyVarObject *)p)->ob_size);
    printf("  Custom trying string: %s\n", bytes->ob_sval);

    if (((PyVarObject *)p)->ob_size > 10)
        size = 10;
    else
        size = ((PyVarObject *)p)->ob_size + 1;

    printf("  Custom first %d bytes: ", size);
    for (i = 0; i < size; i++)
    {
        printf("%02hhx", bytes->ob_sval[i]);
        if (i == (size - 1))
            printf("\n");
        else
            printf(" ");
    }
}
