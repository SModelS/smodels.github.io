#!/usr/bin/env python3

import glob
f=open("index.html","w")
f.write ( "<html>\n" )
f.write ( "<body>\n" )
f.write ( "<h1>Private downloads</h1>\n" )
f.write ( "<ul>\n" )
for g in glob.glob ( "./*" ):
    if g in [ "./index.html", "./update.py" ]:
        continue
    f.write ( "<li><a href=%s>%s</a>\n" % ( g, g ) )
f.write ( "</ul>\n" )
f.write ( "</body>\n" )
f.write ( "</html>\n" )
f.close()
