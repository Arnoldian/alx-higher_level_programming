#include <Python.h>
#include <stdio.h>

/**
 * print_python_list - prints pyton list
 * @p: ptr
 * Return: no return statement
 */

void print_python_list(PyObject *p)
{
	if (!PyList_Check(p))
	{
		printf("[*] Python list info\n  [ERROR] Invalid List Object\n");
		return;
	}

	Py_ssize_t size = PyList_Size(p);
	Py_ssize_t allocated = ((PyListObject *)p)->allocated;

	printf("[*] Python list info\n[*] Size of the Python List = %ld\n[*] Allocated = %ld\n", size, allocated);
	
	for (Py_ssize_t i = 0; i < size; i++)
	{
		PyObject *item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}

/**
 * print_python_bytes - Print information about a Python bytes object
 * @p: Pointer to a Py obj
 * Return: no return statement
 */

void print_python_bytes(PyObject *p)
{
	if (!PyBytes_Check(p))
	{
		printf("[.] bytes object info\n  [ERROR] Invalid Bytes Object\n");
		return;
	}

	Py_ssize_t size = PyBytes_Size(p);
	printf("[.] bytes object info\n  size: %ld\n", size);
	
	printf("  trying string: ");
	for (Py_ssize_t i = 0; i < size; i++)
	{
		printf("%c", PyBytes_AS_STRING(p)[i]);
	}
	printf("\n");
	
	printf("  first 10 bytes: ");
	for (Py_ssize_t i = 0; i < size && i < 10; i++)
	{
		printf("%02x ", (unsigned char)PyBytes_AS_STRING(p)[i]);
	}
	printf("\n");
}

/**
 * print_python_float - Print information about a Python float object
 * @p: Pointer to a Py obj
 * Return: no return statement
 */

void print_python_float(PyObject *p)
{
	if (!PyFloat_Check(p))
	{
		printf("[.] float object info\n  [ERROR] Invalid Float Object\n");
		return;
	}
	
	printf("[.] float object info\n  value: %f\n", PyFloat_AS_DOUBLE(p));
}
