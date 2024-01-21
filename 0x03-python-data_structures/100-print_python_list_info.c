#include <Python.h>
/**
 *print_python_list_info- print info list for python object
 *@p: python object pointer
 *
 */
void print_python_list_info(PyObject *p)
{
	int i = 0;
	PyObject *item;

	printf("[*] Size of the Python List = %ld\n", Py_SIZE(p));
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
	while (i < Py_SIZE(p))
	{
		item = PyList_GET_ITEM(p, i);
		printf("Element %d: %s\n", i, Py_TYPE(item)->tp_name);
		i++;
	}
}
