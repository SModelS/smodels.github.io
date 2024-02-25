#!/usr/bin/env python3

def fetch():
    import glob, shutil
    dbpath = "../../smodels-database"
    files = glob.glob ( f"{dbpath}/**/*_prettyZ.png", recursive=True )
    for f in files:
        fn = f.replace( dbpath+"/", "" )
        tokens = fn.split("/")
        name = tokens[2]+"_"+tokens[4]
        # print ( tokens, "->", name )
        print ( f"fetching {name}" )
        shutil.copy ( f, name )

if __name__ == "__main__":
    fetch()
