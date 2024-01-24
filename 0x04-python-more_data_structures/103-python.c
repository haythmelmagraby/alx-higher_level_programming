#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
/**
 *print_python_list_info- print info list for python object
 *@p: python object pointer
 *
 */
void print_python_list(PyObject *p)
{
	int i = 0;
	PyObject *item;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", ((PyVarObject *)p)->ob_size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
	while (i < Py_SIZE(p))
	{
		item = ((PyListObject *)p)->ob_item[i];
		printf("Element %d: %s\n", i, (item)->ob_type->tp_name);
		i++;
		if (strcmp((item)->ob_type->tp_name, "bytes") == 0)
			print_python_bytes(item);
	}
}
/**
 *print_python_bytes- print first 10 bytes python object
 *@p: python object pointer
 *
 */
void print_python_bytes(PyObject *p)
{
	int i = 0;
	unsigned char size;
	PyBytesObject *b = (PyBytesObject *)p;

	printf("[.] bytes object info\n");
	if (strcmp((p)->ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	printf("  size: %ld\n", ((PyVarObject *)p)->ob_size);
	printf("  trying string: %s\n", b->ob_sval);

	if (((PyVarObject *)p)->ob_size > 10)
		size = 10;
	else
		size = ((PyVarObject *)p)->ob_size + 1;

	printf("first %d bytes: ", size);

	while (i < size)
	{
		printf("%02hhx", b->ob_sval[i]);
		if (i != size - 1)
			printf(" ");
		else
			printf("\n");
		i++;
	}
}
