#!/usr/bin/env python3

import glob

def main():
    with open("README.md","wt") as f:
        f.write ( "# collection of plots\n" )
        files = glob.glob("./*" )
        for F in files:
            if F.endswith ( ".py" ) or F.endswith ( ".md" ):
                continue
            f.write ( f'<img src="{F}" />\n' )
        

main()
