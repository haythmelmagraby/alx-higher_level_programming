#include <stdio.h>
#include <Python.h>
/**
 *print_python_list_info- print info list for python object
 *@p: python object pointer
 *
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t size = PyList_Size(p);
	Py_ssize_t allocations = ((PyListObject *)p)->allocated;
	int i = 0;
	PyObject *p2;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %ld\n", allocations);

	while (i < size)
	{
		p2 = PyList_GetItem(p, i);
		printf("Element %d: %s\n", i, Py_TYPE(p2->ob_item[i])->tp_name);
		i++;
	}
}
