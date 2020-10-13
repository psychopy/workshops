#!/bin/bash

#get to right directory
# P=$PWD
# cd /Users/lpzjwp/Dropbox/P4N/materials

make slides pdf
# cp -r build/slides build/html/
# cp build/epub/P4N2014.epub build/html/
# -a means keep file times etc 
# -u means updated files only
# -n means dry-run
# -v verbos
input Have you connected VPN?

cp build/latex/builderWorkshop2019.pdf lpzjwp@psychopy.org:/var/www/psychopy/builderWorkshop2019.pdf
cp ../examples2019.zip lpzjwp@psychopy.org:/var/www/psychopy/PsychoPy_examples2019.zip

echo synchronising...
rsync -auv build/slides/* lpzjwp@psychopy.org:/var/www/psychopy/builderworkshop
rsync -auv build/latex/builderWorkshop2019.pdf lpzjwp@psychopy.org:/var/www/psychopy/builderWorkshop2019.pdf
rsync -auv build/latex/examples2019.zip lpzjwp@psychopy.org:/var/www/psychopy/PsychoPy_examples2019.zip

#back to orig directory
# cd $P

echo done
