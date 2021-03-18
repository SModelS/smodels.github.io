#!/usr/bin/python3

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
f.write ( "|        **label**        |         **mtime**         | **size** | **server** |\n" )
f.write ( "|-------------------------|---------------------------|----------|------------|\n" )
for F in files:
    if F.endswith(".py") or F.endswith(".md") or F.endswith(".html"):
        continue
    if F in  [ "obsolete" ]:
        continue
    with open(F,"rt") as g:
        d = json.load( g )
        mtime = "???"
        if "mtime" in d:
            mtime = d["mtime" ]
        size = sizeof_fmt ( d["size"] )
        #server = "SModelS"
        server = '<img height=30 src="https://smodels.github.io/pics/banner.png" alt="SModelS">'
        if "zenodo" in d["url"]:
            # server = "zenodo"
            server = '<img height=30 src="https://smodels.github.io/logos/zenodo_small.png" alt="SModelS">'
        line = f'| {F:23.23} | {mtime:25.25} | {size:>8.8} | {server:>40.40} |\n'
        f.write ( line )

f.write ( f"\nPage created {time.asctime()}.\n" )

f.close()
