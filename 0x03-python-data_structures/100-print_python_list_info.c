#include <stdio.h>
#include <stdlib.h>
#include <Python.h>

/**
 * print_python_list_info - prints basic information about py lists
 * @p: PyObject list
 * Return: no return statement
 */

void print_python_list_info(PyObject *p)
{
	int size, allctd, i;
	PyObject *obj;
	size = Py_SIZE(p);
	allctd = ((PyListObject *) p)->allocated;
	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", allctd);

	for (i = 0; i < size; i++)
	{
		printf("Element %d: ", i);
		obj = PyList_GetItem(p, i);
		printf("%s\n", Py_TYPE(obj)->tp_name);
	}
}
