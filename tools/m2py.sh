#!/bin/bash
sed -i 's/%/#/' "$@"
sed -Ei 's/;($| *#)/\1/' "$@"
gawk -i inplace '
    /^ *(if|else|while|for|function)\>([^#]*[^:# ])? *(#|$)/ {
        sub(/$| *#/, ":&")
    }
    /^ *end *$/ {
        sub(/end/, "# &")
    }
    { print }
' "$@"
