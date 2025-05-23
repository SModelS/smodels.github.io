#!/usr/bin/python3

""" simple script that creates the list of databases in markdown format,
    see https://smodels.github.io/database/ """

def sizeof_fmt(num, suffix='B'):
    for unit in ['','Ki','Mi','Gi','Ti','Pi','Ei','Zi']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Yi', suffix)

import glob, os, pickle, time, sys, json
files = glob.glob("*" )
files.sort()

f=open("README.md","w")
##f.write ( '<p align="center"><img src="https://smodels.github.io/pics/banner.png" alt="banner"></p>\n\n' )
f.write ( "# SModelS Databases\n\n" )
f.write ( "|         **label**         |         **mtime**         | **size** | **server** |\n" )
f.write ( "|---------------------------|---------------------------|----------|------------|\n" )
for F in files:
    if F.endswith(".py") or F.endswith(".md") or F.endswith(".html"):
        continue
    if F in  [ "obsolete" ]:
        continue
    with open(F,"rt") as g:
        # print ( "loading as json", F )
        try:
            d = json.load( g )
        except json.decoder.JSONDecodeError as e:
            print ( f"cannot read {F}: {e}" )
            continue
        mtime = "???"
        if "mtime" in d:
            tokens = d["mtime" ].split(" ")
            mtime = " ".join ( ( tokens[0], tokens[1], tokens[2], tokens[4] ) )
        size = sizeof_fmt ( d["size"] )
        #server = "SModelS"
        server = '<img height=20 src="https://smodels.github.io/pics/banner.png" alt="SModelS">'
        if "zenodo" in d["url"]:
            # server = "zenodo"
            server = '<img height=20 src="https://smodels.github.io/logos/zenodo_small.png" alt="zenodo">'
        line = f'| {F:25.25} | {mtime:25.25} | {size:>8.8} | {server} |\n'
        f.write ( line )

f.write ( f"\nPage created {time.asctime()}.\n" )

f.close()
