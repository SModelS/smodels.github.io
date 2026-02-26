#!/usr/bin/env python

""" create the html table that lists all subdirs """

import glob, os

def header ( f ):
    f.write ( "<table>\n" )
    # f.write ( "<caption>High Score Models</caption>\n" )
    f.write ( "<thead>\n" )
    f.write ( "  <tr>\n" )
    f.write ( "    <th scope='col'>Name</th>\n" )
    f.write ( "    <th scope='col'>Link</th>\n" )
    f.write ( "    <th scope='col'>Description</th>\n" )
    f.write ( "  </tr>\n" )
    f.write ( "</thead>\n" )

def getContent ( subdir : os.PathLike, what : str = "explanation" ):
    explfile = f"{subdir}/{what}"
    if not os.path.exists ( explfile ):
        return "no explanation found"
    with open  ( explfile, "rt" ) as f:
        return f.read()

def body ( f ):
    f.write ( "<tbody>\n" )
    files = glob.glob ( "./*" )
    for subdir in files:
        if subdir.endswith(".html"):
            continue
        if not os.path.isdir ( subdir ):
            continue
        expl = getContent ( subdir, "explanation" )
        label = getContent ( subdir, "name" )
        link = "<a href={subdir}>link</a>"
        f.write ( "  <tr>\n" )
        f.write ( f"    <td>{label}</td>\n" )
        f.write ( f"    <td>{link}</td>\n" )
        f.write ( f"    <td>{expl}</td>\n" )
        f.write ( "  </tr>\n" )

    f.write ( "</tbody>\n" )

def footer ( f ):
    f.write ( "</table>\n" )

def create():
    with open ( "table.html", "wt" ) as f:
        header ( f )
        body ( f )
        footer ( f )

if __name__ == "__main__":
    create()
