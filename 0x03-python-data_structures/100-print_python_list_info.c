#include <stdio.h>
#include <Python.h>
#include <time.h>
/**
 *print_python_list_info- print info list for python object
 *@p: python object pointer
 *
 */
void print_python_list_info(PyObject *p)
{
	int size = PY_SIZE(p);
	int allocate = ((PyListObject *)p)->allocated;
	int i = 0;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", allocate);

	while (i < size)
		printf("Element %d: %s\n", i, PY_TYPE(PyList_GetItem(p, i))->tp_name);
}
