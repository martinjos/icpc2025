#include <inttypes.h>
#include <stdio.h>
#include <stdlib.h>
#include "bridge.h"

int main(int argc, char** argv) {
    int n = argc-1;
    int64_t a[n];
    int64_t b[n][2];
    for (int i = 0; i < n; i++) {
        a[i] = atoi(argv[i+1]);
    }
    fprintf(stderr, "Calling A_insert()...\n");
    if (-1 == PyImport_AppendInittab("bridge", PyInit_bridge)) {
        fprintf(stderr, "Failed to prepare bridge module for import.\n");
    }
    Py_Initialize();
    PyObject *path = PySys_GetObject("path");
    if (path != NULL) {
        // This will only work from top dir of repository
        PyList_Insert(path, 0, Py_BuildValue("s", "."));
    }
    int rv = 0;
    if (! PyImport_ImportModule("bridge")) {
        PyErr_Print();
        rv = 2;
    } else {
        A_insert(a, n, (int64_t*)b);
        fprintf(stderr, "Returned from A_insert.\n");
        for (int i = 0; i < n; i++) {
            printf("%" PRId64 "\t%" PRId64 "\n",
                   b[i][0], b[i][1]);
        }
    }
    Py_Finalize();
    return rv;
}