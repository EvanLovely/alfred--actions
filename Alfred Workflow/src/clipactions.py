import re
from sys import argv, exit
from os import listdir, path, walk
import optparse
from xml.etree.ElementTree import Element, SubElement, tostring
 
 
class toXML():
 
    def __init__(self):
        self.toxml = Element('items')
 
    def __repr__(self):
        return tostring(self.toxml)
 
    def add_item(
            self,
            title,
            subtitle="",
            arg="",
            valid="YES",
            autocomplete="",
            icon="icon.png"):
        item = SubElement(self.toxml, 'item', {
            'uid': str(len(self.toxml)),
            'arg': arg,
            'valid': valid,
            'autocomplete': autocomplete
        })
 
        _title = SubElement(item, 'title')
        _title.text = title
 
        _subtitle = SubElement(item, 'subtitle')
        _subtitle.text = subtitle
 
        _icon = SubElement(item, 'icon')
        _icon.text = icon
 
    def display(self):
        print self
 
 
class SearchPages():
 
    def __init__(self, directory):
        query = argv[-1]
 
        self.script_list = self.traverse_directory(directory)
 
        script_name_args = [
            path.splitext(f) for f in self.script_list
            if not f.startswith(('.', '_'))
            and not path.isdir(path.join(directory, f))
        ]
 
        p = self.create_fuzzy_pattern(query)
        self.matched_args = [arg for arg in script_name_args if p.match(arg[0])]
        output = toXML()
 
        for arg in self.matched_args:
            output.add_item(
                title=path.basename(arg[0]),
                subtitle='',#self.read_firstline(path.join(directory, arg[0] + arg[1])),
                arg=''
            )
 
        output.display()
 
    def create_fuzzy_pattern(self, word):
        return re.compile(''.join(['.*' + l + '.*' for l in word]), re.IGNORECASE)
 
    def read_firstline(self, f):
        with open(f, 'r') as readfile:
            return readfile.readline().encode('ascii', 'ignore')
 
    def traverse_directory(self, directory):
        filelist = []
        for root, dirs, files in walk(directory):
            files = [f for f in files if not f[0] == '.']
            dirs[:] = [d for d in dirs if not d[0] == '.']
            for file in files:
                filelist.append(path.join(root, file))
        return filelist
 
 
def main():
    parser = optparse.OptionParser()
    parser.add_option('-s', help='Create fuzzy search for script filter', dest='searchpages', default=False, action='store_true')
    parser.add_option('-d', help='Set the directory for the clipactions', dest='directory', default=False, action='store')
 
    try:
        (opts, args) = parser.parse_args()
    except:
        # print parser.print_help()
        exit(0)
 
    if opts.searchpages and not opts.directory:
        print "mandatory option is missing\n"
        parser.print_help()
        exit(0)
 
    if opts.searchpages:
        SearchPages(opts.directory)
 
if __name__ == '__main__':
    main()