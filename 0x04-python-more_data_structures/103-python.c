#include <Python.h>

/**
 * print_python_list - Prints basic info about Python lists.
 * @p: A PyObject list object.
 */
void print_python_list(PyObject *p)
{
    int size, i;
    const char *type;

    size = PyList_Size(p);

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %d\n", size);

    for (i = 0; i < size; i++)
    {
        type = Py_TYPE(PyList_GetItem(p, i))->tp_name;
        printf("Element %d: %s\n", i, type);
        if (strcmp(type, "bytes") == 0)
            print_python_bytes(PyList_GetItem(p, i));
    }
}

/**
 * print_python_bytes - Prints basic info about Python byte objects.
 * @p: A PyObject byte object.
 */
void print_python_bytes(PyObject *p)
{
    int size, i;
    PyBytesObject *bytes = (PyBytesObject *)p;

    printf("[.] bytes object info\n");
    if (!PyBytes_Check(p))
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    size = PyBytes_Size(p);
    printf("  size: %d\n", size);
    printf("  trying string: %s\n", PyBytes_AsString(p));

    printf("  first %d bytes: ", size);
    for (i = 0; i < size; i++)
    {
        printf("%02hhx", bytes->ob_sval[i]);
        if (i == (size - 1))
            printf("\n");
        else
            printf(" ");
    }
}
