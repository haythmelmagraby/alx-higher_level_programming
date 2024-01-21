#include <object.h>
#include <stdlib.h>
#include <stdio.h>
#include <listobject.h>
#include <Python.h>
/**
 *print_python_list_info- print info list for python object
 *@p: python object pointer
 *
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t size = Py_SIZE(p);
	Py_ssize_t allocations = ((PyListObject *)p)->allocated;
	int i = 0;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", allocations);

	while (i < size)
	{
		printf("Element %d: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
		i++;
	}
}
