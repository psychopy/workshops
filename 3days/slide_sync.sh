#!/bin/bash

#get to right directory
# P=$PWD
# cd /Users/lpzjwp/Dropbox/P4N/materials

# make slides pdf
# cp -r build/slides build/html/
# cp build/epub/P4N2014.epub build/html/
# -a means keep file times etc
# -u means updated files only
# -n means dry-run
# -v verbos
input Have you connected VPN?

cp build/latex/3days.pdf build/slides/psychopy3days.pdf

echo synchronising...
rsync -auv build/slides/* lpzjwp@psychopy.org:/var/www/psychopy/3days
# rsync -auv build/latex/3days.pdf lpzjwp@psychopy.org:/var/www/psychopy/psychopy3days.pdf

#back to orig directory
# cd $P

echo done
