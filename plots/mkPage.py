#!/usr/bin/env python3

import glob, time

def main():
    with open("README.md","wt") as f:
        f.write ( "# collection of plots\n" )
        f.write ( "%s\n\n" % time.asctime() )
        files = glob.glob("./*" )
        t = time.time()
        ncols = 2
        f.write ( "|                    |                  |\n" )
        f.write ( "|--------------------|------------------|\n" )
        col = 0
        for F in files:
            if F.endswith ( ".py" ) or F.endswith ( ".md" ):
                continue
            f.write ( "| " )
            # f.write ( f'<img src="{F}?{t}" />\n' )
            # [SModelS version 2.0.0](https://github.com/SModelS/smodels/releases) 
            f.write ( f'![{F}]({F}?{t}) ' )
            if col == 1:
                f.write ( "|\n" )
                col = 0
            else:
                col = 1

main()
