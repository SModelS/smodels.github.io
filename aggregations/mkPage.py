#!/usr/bin/env python3

import glob, time, os

from covariances.computeTimes import computeTimes

#valdir = "~/git/smodels-database/13TeV/CMS/CMS-SUS-19-006-agg"
valdir = "~/git/smodels-database/13TeV/CMS/CMS-SUS-16-050-agg"
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

def getTimes( numbers, topos ):
    """ get the wall clock times """
    ret = {}
    for nr in numbers:
        ret[nr]={}
        for topo in topos:
            f = f"{valdir}/validation{nr}/{topo}_*_combined.py"
            files = glob.glob ( f )
            t = computeTimes ( files[0] )
            ret[nr][topo]=t
    return ret

def header ( numbers, topos ):
    with open("README.md","wt") as f:
        f.write ( "# comparison of aggregations\n" )
        f.write ( "%s\n\n" % time.asctime() )
        f.write ( f"|          " )
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
    times = getTimes ( numbers, topos )
    header ( numbers, topos )
    t = time.time()
    axes = { "TGQ": "EqMassAx_EqMassB695.0__EqmassAy_EqmassB695.0",
             "T5tctc": "2EqMassAx_EqMassBy+20_EqMassCy",
             "T3GQ": "EqMassAy_EqMassB695.0__EqmassAx_EqmassBy_EqmassC695.0",
             "T5GQ": "EqMassAx_EqMassBy_EqMassC695.0__EqmassAy_EqmassB695.0" }
    with open("README.md","at") as f:
        for topo in topos:
            f.write ( f"| {topo:8s} " )
            for nr in numbers:
                #base = "https://smodels.github.io/validation/210adl/"
                #url  = f"{base}/13TeV/CMS/CMS-SUS-19-006-agg/"
                base = "https://smodels.github.io/validation/220-ww/"
                url  = f"{base}/13TeV/CMS/CMS-SUS-16-050-agg/"
                vdir = f"{url}/validation{nr}/"
                axis = "2EqMassAx_EqMassBy"
                if topo in axes:
                    axis = axes[topo]
                name = f"{vdir}{topo}_{axis}_combined.png"
                f.write ( f"| ![{name}]({name}?{t} =300x) " )
                f.write ( f"{times[nr][topo][0]:.2f}s " )
            f.write ( "|\n" )
    footer ( numbers, topos )

main()
