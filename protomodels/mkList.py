#!/usr/bin/env python3

def mkList():
    import glob
    outfile = "list.md"
    outfile = "4lucas.md"
    f = open ( outfile, "wt" )
    f.write ( "# List of protomodel pages\n\n" )
    f.write ( "|     **label**     |     **url**     |\n" )
    f.write ( "|-------------------|-----------------|\n" )
    files_glob = "*"
    files_glob = "rundir*_320"
    files = glob.glob ( files_glob )
    for g in files:
        if g.endswith ( ".html" ):
            continue
        if g in [ "plots", "videos", "list.md", "mkList.py", "logos" ]:
            continue
        f.write ( f"| {g} | [https://smodels.github.io/protomodels/{g}](https://smodels.github.io/protomodels/{g}) |\n" )
    f.close()



if __name__ == "__main__":
    mkList()
