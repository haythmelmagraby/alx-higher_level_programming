#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
/**
 *print_python_list_info- print info list for python object
 *@p: python object pointer
 *
 */
void print_python_list(PyObject *p){
	int i = 0;
	PyObject *item;

	printf("[*] Size of the Python List = %ld\n", Py_SIZE(p));
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
	while (i < Py_SIZE(p))
	{
		item = PyList_GET_ITEM(p, i);
		printf("Element %d: %s\n", i, Py_TYPE(item)->tp_name);
		i++;
		if(strcmp(Py_TYPE(item)->tp_name, "bytes") == 0)
			print_python_bytes(item);
	}
}
void print_python_bytes(PyObject *p){
	int i = 0, size;
	PyBytesObject *b = (PyBytesObject *)p;

	printf("[.] bytes object info\n");
	if (strcmp(Py_TYPE(p)->tp_name, "bytes") != 0)
	{
		printf("[ERROR] Invalid Bytes Object\n");
		return;
	}

	printf("  size: %ld\n",Py_SIZE(p));
	printf("  trying string: %s\n",b->ob_sval);

	if (Py_SIZE(p) < 10 )
		size = Py_SIZE(p) + 1;
	else
		size = Py_SIZE(p);

	printf("first %d bytes: ", size);

	while (i < size)
	{
		printf("%02hhx",b->ob_sval[i]);
		if (i != size - 1)
			printf(" ");
		else
			printf("\n");
		i++;
	}
}
