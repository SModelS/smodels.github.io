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
        f.write ( "# collection of videos\n" )
        f.write ( "%s\n\n" % time.asctime() )
        addText ( f )
        files = glob.glob("./*" )
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
            if F.endswith ( ".py" ) or F.endswith ( ".md" ) or F.endswith( ".sh" ) or F.endswith("old") or F.endswith("Makefile") or F.endswith(".pdf") or F.endswith ( "text" ):
                continue
            f.write ( "| " )
            # f.write ( f'<img src="{F}?{t}" />\n' )
            # [SModelS version 2.0.0](https://github.com/SModelS/smodels/releases) 
            name = F.replace(".mp4","")
            name = name.replace("./","")
            descriptions = { 
                "EvolutionSModelSDatabase": "evolution of SModelS database over time",
                "blendefast": "intro clip for lectures" }
            description = name
            if name in descriptions:
                description = descriptions[name]
            f.write ( f' {description} [{F}]({F}?{t}) ' )
            if col == 1:
                f.write ( "|\n" )
                col = 0
            else:
                col = 1

main()
