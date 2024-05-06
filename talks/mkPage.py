#!/usr/bin/env python3

import glob, time, os

def addText ( f ):
    if os.path.exists ( "text" ):
        g = open ( "text", "rt" )
        f.write ( g.read() )
        f.write ( "\n" )
        g.close()

def main():
    with open("README.md","wt") as f:
        f.write ( "# collection of talks\n" )
        f.write ( "%s\n\n" % time.asctime() )
        addText ( f )
        files = glob.glob("./*" )
        def getAnaid ( x ):
            x = x.replace("bestSR_","").replace("combo_","").replace("ratios_","").replace("-scalar","").replace("-ma5","")
            x = x.replace ("pDatabase","")
            x = x.replace("./","")
            print ( "x", x )
            return str(x)
        def getType ( x ):
            ## sort by type
            return str(x)
        files.sort ( key = getType )
        print ( "files", files )
        t = time.time()
        ncols = 2
        f.write ( "|                    |                  |\n" )
        f.write ( "|:------------------:|:----------------:|\n" )
        col = 0
        for F in files:
            if F.endswith ( ".py" ) or F.endswith ( ".md" ) or F.endswith( ".sh" ) or F.endswith("old") or F.endswith("Makefile") or F.endswith(".pdo") or F.endswith ( "text" ):
                continue
            f.write ( "| " )
            # f.write ( f'<img src="{F}?{t}" />\n' )
            # [SModelS version 2.0.0](https://github.com/SModelS/smodels/releases) 
            name = F.replace(".png","").replace("combo_","").replace("bestSR_","")
            name = name.replace("./","")
            f.write ( f' {name} [{F}]({F}?{t}) ' )
            if col == 1:
                f.write ( "|\n" )
                col = 0
            else:
                col = 1

main()
