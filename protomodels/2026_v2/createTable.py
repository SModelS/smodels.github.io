#!/usr/bin/env python

""" create the html table that lists all subdirs """

import glob, os
from typing import Union

def header ( f ):
    f.write ( "<table>\n" )
    # f.write ( "<caption>High Score Models</caption>\n" )
    f.write ( "<thead>\n" )
    f.write ( "  <tr>\n" )
    f.write ( "    <th scope='col'>Name</th>\n" )
    f.write ( "    <th scope='col'>Link</th>\n" )
    f.write ( "    <th scope='col'>Description</th>\n" )
    f.write ( "    <th scope='col'>K</th>\n" )
    f.write ( "    <th scope='col'>TL</th>\n" )
    f.write ( "  </tr>\n" )
    f.write ( "</thead>\n" )

def getContent ( subdir : os.PathLike, what : str = "explanation" ):
    explfile = f"{subdir}/{what}"
    if not os.path.exists ( explfile ):
        return f"no {what} found"
    with open  ( explfile, "rt" ) as f:
        return f.read()

def getTestStat ( webpage : str, teststat : str ) -> str:
    """ scrape the test statistic 'teststat' off the webpage """
    if not os.path.exists ( webpage ):
        return "n/a"
    with open ( webpage, "rt" ) as f:
        lines = f.readlines()
        for line in lines:
            if not "Current best" in line:
                continue
            p1 = line.find(f"<i>{teststat}</i>=")
            half = line[p1+8:p1+22]
            p1 = half.find("=")
            half = half[p1+1:]
            p2 = half.find(",")
            if p2 > 0:
                half = half[:p2]
            p2 = half.find("<")
            if p2 > 0:
                half = half[:p2]
            return half
    return "n/a"


def body ( f, globpattern : Union[list,str] ):
    """ the body of index.html
    :param globpattern:  e.g. 'fake*'
    """
    f.write ( "<tbody>\n" )
    files = globpattern
    if type ( globpattern ) == str:
        files = glob.glob ( f"./{globpattern}" )
    for subdir in files:
        if subdir.endswith(".html"):
            continue
        if not os.path.isdir ( subdir ):
            continue
        expl = getContent ( subdir, "explanation" )
        label = getContent ( subdir, "name" )
        indexpage = f"{subdir}/index.html"
        link = f'<a href="{indexpage}" target="_top">link</a>'
        f.write ( "  <tr>\n" )
        f.write ( f"    <td>{label}</td>\n" )
        f.write ( f"    <td>{link}</td>\n" )
        f.write ( f"    <td>{expl}</td>\n" )
        K = getTestStat ( indexpage, "K" )
        TL = getTestStat ( indexpage, "TL" )
        f.write ( f"    <td>{K}</td>\n" )
        f.write ( f"    <td>{TL}</td>\n" )
        f.write ( "  </tr>\n" )

    f.write ( "</tbody>\n" )

def footer ( f ):
    f.write ( "</table>\n" )

def create( globpattern : str, outfile : str ):
    with open ( outfile, "wt" ) as f:
        header ( f )
        body ( f, globpattern )
        footer ( f )

if __name__ == "__main__":
    create( [ "hiscore_20000", "hiscore", "hiscore_stops" ], "hiscore.html", )
    create( [ "fake_stops3", "fake_ewkoff3", "fake_ewk2" ], "closure.html" )
    create( "noX2Z*", "noX2Z.html" )
