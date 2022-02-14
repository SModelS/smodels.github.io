#!/usr/bin/env python3

import glob, time, os

valdir = "~/git/smodels-database/13TeV/CMS/CMS-SUS-19-006-agg"
valdir = os.path.expanduser ( valdir )

def getNumbers():
    """ get a list of # of SRs """
    dirs = glob.glob ( valdir + "/validation?*/" )
    ret = set()
    for d in dirs:
        p = d.find( "validation" )
        nr = int ( d[p+10:-1] )
        ret.add ( nr )
    ret = list ( ret )
    ret.sort()
    return tuple ( ret )

def getTopos():
    """ get a list of # of SRs """
    dirs = glob.glob ( valdir + "/validation?*/T*combined.png" )
    ret = set()
    for d in dirs:
        p = d.find( "validation" )
        tname = d[p+1:]
        p1 = tname.find("T")
        p2 = tname.find("_")
        tname = tname[p1:p2]
        ret.add ( tname )
    ret = list ( ret )
    ret.sort()
    return tuple ( ret )

def header ( numbers, topos ):
    with open("README.md","wt") as f:
        f.write ( "# comparison of aggregations\n" )
        f.write ( "%s\n\n" % time.asctime() )
        f.write ( f"| topology " )
        for nr in numbers:
            f.write ( f"|        {nr:2d}        " )
        f.write ( "|\n|:--------:" )
        for nr in numbers:
            f.write ( "|:----------------:" )
        f.write ( "|\n" )
        f.close()

def footer ( numbers, topos ):
    with open("README.md","at") as f:
        f.write ( "\n" )
        f.close()

def main():
    numbers = getNumbers()[:]
    print ( numbers )
    topos = getTopos()[:]
    print ( topos )
    header ( numbers, topos )
    t = time.time()
    with open("README.md","at") as f:
        for topo in topos:
            f.write ( f"| {topo:8s} " )
            for nr in numbers:
                base = "https://smodels.github.io/validation/210adl/"
                url  = f"{base}/13TeV/CMS/CMS-SUS-19-006-agg/"
                vdir = f"{url}/validation{nr}/"
                name = f"{vdir}{topo}_2EqMassAx_EqMassBy_combined.png"
                f.write ( f"| ![{name}]({name}?{t}) " )
            f.write ( "|\n" )
    footer ( numbers, topos )

main()
