pelican -s /home/fuzzmz/pelican/qwerty/content/config/pelicanconf.py /home/fuzzmz/pelican/qwerty/content -o /home/fuzzmz/pelican/qwerty/fuzzmz.github.com -t /home/fuzzmz/pelican/src/pelican/pelican/themes/notmyidea
git --git-dir=/home/fuzzmz/pelican/qwerty/sources --work-tree=/home/fuzzmz/pelican/qwerty/sources log -1 --pretty=%B > commit.txt
python /home/fuzzmz/pelican/qwerty/content/config/scripts/replace.py
chmod +x /home/fuzzmz/pelican/qwerty/content/config/scripts/update.sh
#rm ./commit.txt
/home/fuzzmz/pelican/qwerty/content/config/scripts/update.sh
#rm ./update.sh

