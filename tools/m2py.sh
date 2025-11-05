#!/bin/bash
sed -i 's/%/#/' "$@"
sed -Ei 's/;($| *#)/\1/' "$@"
