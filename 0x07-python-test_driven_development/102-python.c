#include "Python.h"

/**
 * print_python_string - Prints information about Python strings.
 * @p: A PyObject string object.
 */
void print_python_string(PyObject *p)
{
    Py_UNICODE *wide_str;
    Py_ssize_t length;

    fflush(stdout);

    printf("[.] string object info\n");

    // Check if p is a valid string object
    if (!PyUnicode_Check(p))
    {
        printf("  [ERROR] Invalid String Object\n");
        return;
    }

    // The following code to obtain the length and value of the string is correct:
    length = PyUnicode_GET_SIZE(p);

    printf("  type: compact unicode object\n");
    printf("  length: %ld\n", length);
    
    // Printing a Python string as a wide character string
    wide_str = PyUnicode_AsWideCharString(p, &length);
    if (wide_str)
    {
        printf("  value: %ls\n", wide_str);
        PyMem_Free(wide_str); // Free the allocated memory
    }
    else
    {
        printf("  [ERROR] Unable to retrieve the string value\n");
    }
}

