#!/usr/bin/env python3

import glob, time

def main():
    with open("README.md","wt") as f:
        f.write ( "# collection of plots\n" )
        f.write ( "%s\n\n" % time.asctime() )
        files = glob.glob("./*" )
        t = time.time()
        for F in files:
            if F.endswith ( ".py" ) or F.endswith ( ".md" ):
                continue
            f.write ( f'<img src="{F}?{t}" />\n' )
        

main()
