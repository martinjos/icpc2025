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
gawk -i inplace '
    BEGIN { FS = "[ =]+" }
    /^function +[a-zA-Z_][a-zA-Z_0-9]* *= */ {
        retName = $2
        sub(/^[^=]*= */, "def ")
    }
    /^function\>[^=]*$/ {
        retName = "";
    }
    /^# end/ {
        if (retName != "") {
            print "    return " retName
        }
    }
    { print }
' "$@"
