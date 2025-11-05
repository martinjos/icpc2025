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
sed -i '
    s/\<error(/raise RuntimeError(/
    s/~=/!=/g
    s/~/not /g
    s/\<length(/len(/g
    s/||/or/g
    s/&&/and/g
    s/\<disp(/print(/g
' "$@"
sed -Ei '
    s/\<np.([a-zA-Z_0-9]+)\(/np.NP\1(/g
    s/\<(all|sort|zeros|size)\(/np.\1(/g
    s/np.NP([a-zA-Z_0-9]+)/np.\1/g
' "$@"