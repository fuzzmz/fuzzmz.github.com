pelican -s /home/fuzzmz/pelican/qwerty/content/config/pelicanconf.py /home/fuzzmz/pelican/qwerty/content -o /home/fuzzmz/pelican/qwerty/fuzzmz.github.com -t /home/fuzzmz/pelican/src/pelican/pelican/themes/notmyidea
git log -1 --pretty=%B > commit.txt
python replace.py
chmod +x ./update.sh
#rm ./commit.txt
./update.sh
#rm ./update.sh

#test