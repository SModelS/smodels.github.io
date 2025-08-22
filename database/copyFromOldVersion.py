#!/usr/bin/env python3

""" very simple script that copies the json files from the latest
    version tag to the one requested """
    
import glob

def guessLatestVersion():
    files = glob.glob ( "official*" )
    nrs = []
    for f in files:
        if "fastlim" in f or "superseded" in f or "beta" in f:
            continue
        f = f.replace( "official","" )
        nr = int ( f[:3] )
        nrs.append ( nr )
    maxnr = str( max ( nrs ) )
    return f"{maxnr[0]}.{maxnr[1]}.{maxnr[2]}"

def copyFromOldVersion( newversion, oldversion ):
    """ copy the json files from oldversion to newversion """
    if oldversion == None:
        oldversion = guessLatestVersion()
    print ( f"[copyFromOldVersion] {oldversion} -> {newversion}" )
    dotlessv = oldversion.replace('.','')
    files = glob.glob ( f"*{dotlessv}" )
    newversion = newversion.replace(".","")
    import shutil
    for f in files:
        newf = f.replace(dotlessv,newversion)
        print ( f"[copyFromOldVersion] {f} -> {newf}" )
        try:
            shutil.copyfile ( f, newf )
        except shutil.SameFileError as e:
            pass
    import subprocess
    subprocess.getoutput ( "./createREADME.py" )

if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser(description="very simple script that copies the json files from the latest version tag to the one requested")
    ap.add_argument('-n', '--newversion', help='new version tag [3.0.0]',
        default = '3.0.0', type = str )
    ap.add_argument('-o', '--oldversion', help='old version tag. if None, then  try to guess [None]',
        default = None, type = str )
    args = ap.parse_args()
    copyFromOldVersion ( args.newversion, args.oldversion )
