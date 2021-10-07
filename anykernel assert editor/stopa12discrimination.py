#!/bin/python
import argparse, sys, argparse, os, zipfile, re, shutil, textwrap

'''
removes a11 assert line from anykernelsh zip by @jayrfs
http://jayrfs.github.io/
'''


class MyParser(argparse.ArgumentParser):
    def error(self, message):
        sys.stderr.write('error: %s\n' % message)
        self.print_help()
        sys.exit(2)

parser = MyParser(prog='PROG',
formatter_class=argparse.RawDescriptionHelpFormatter,
description=textwrap.dedent('''\
            Stop A12 discrimination!
         ----------------------------------------
             script to remove a11 assert line
             from anykernelsh zip and make
             it flashable on any android
             version. 

             standard xda copypasta warning applies

            \tby @jayrfs

            http://jayrfs.github.io/
'''))

parser.add_argument('filename')
args = parser.parse_args()
file_name=args.filename
with zipfile.ZipFile(file_name) as zip_ref:
    try: 
        os.makedirs(f"./temp")
    except:
        shutil.rmtree(f"./temp")
        os.makedirs(f"./temp")
    zip_ref.extractall(f"./temp")

with open("./temp/anykernel.sh", "r") as anykernel_sh:
    lines = anykernel_sh.readlines()
with open("./temp/anykernel.sh", "w") as anykernel_sh:
    for line in lines:
        anykernel_sh.write(re.sub(r'supported.versions=11', 'supported.versions=', line))

shutil.make_archive(f"{file_name[:-4]}_a12", 'zip', "./temp")
shutil.rmtree(f"./temp")
os.rename(f"{file_name}",f"{file_name[:-4]}_a11.zip")
print(
    f"\n"
    f"SUCCESS!\n"
    f"\n⠄⠄⠄⢰⣧⣼⣯⠄⣸⣠⣶⣶⣦⣾⠄⠄⠄⠄⡀⠄⢀⣿⣿⠄⠄⠄⢸⡇⠄⠄+\n⠄⠄⠄⣾⣿⠿⠿⠶⠿⢿⣿⣿⣿⣿⣦⣤⣄⢀⡅⢠⣾⣛⡉⠄⠄⠄⠸⢀⣿⠄+\n⠄⠄⢀⡋⣡⣴⣶⣶⡀⠄⠄⠙⢿⣿⣿⣿⣿⣿⣴⣿⣿⣿⢃⣤⣄⣀⣥⣿⣿⠄+\n⠄⠄⢸⣇⠻⣿⣿⣿⣧⣀⢀⣠⡌⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠿⣿⣿⣿⠄+\n⠄⢀⢸⣿⣷⣤⣤⣤⣬⣙⣛⢿⣿⣿⣿⣿⣿⣿⡿⣿⣿⡍⠄⠄⢀⣤⣄⠉⠋⣰+\n⠄⣼⣖⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⢇⣿⣿⡷⠶⠶⢿⣿⣿⠇⢀⣤+\n⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣽⣿⣿⣿⡇⣿⣿⣿⣿⣿⣿⣷⣶⣥⣴⣿⡗+\n⢀⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠄+\n⢸⣿⣦⣌⣛⣻⣿⣿⣧⠙⠛⠛⡭⠅⠒⠦⠭⣭⡻⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠄+\n⠘⣿⣿⣿⣿⣿⣿⣿⣿⡆⠄⠄⠄⠄⠄⠄⠄⠄⠹⠈⢋⣽⣿⣿⣿⣿⣵⣾⠃⠄+\n⠄⠘⣿⣿⣿⣿⣿⣿⣿⣿⠄⣴⣿⣶⣄⠄⣴⣶⠄⢀⣾⣿⣿⣿⣿⣿⣿⠃⠄⠄+\n⠄⠄⠈⠻⣿⣿⣿⣿⣿⣿⡄⢻⣿⣿⣿⠄⣿⣿⡀⣾⣿⣿⣿⣿⣛⠛⠁⠄⠄⠄+\n⠄⠄⠄⠄⠈⠛⢿⣿⣿⣿⠁⠞⢿⣿⣿⡄⢿⣿⡇⣸⣿⣿⠿⠛⠁⠄⠄⠄⠄⠄+\n⠄⠄⠄⠄⠄⠄⠄⠉⠻⣿⣿⣾⣦⡙⠻⣷⣾⣿⠃⠿⠋⠁⠄⠄⠄⠄⠄⢀⣠⣴+\n⣿⣿⣿⣶⣶⣮⣥⣒⠲⢮⣝⡿⣿⣿⡆⣿⡿⠃⠄⠄⠄⠄⠄⠄⠄⣠⣴⣿⣿⣿+\n"
    f"\n"
    f"use {file_name[:-4]}_a12.zip instead of {file_name}\n"
    )

'''zf = zipfile.ZipFile(f"{file_name[:-4]}_impartial.zip", "w")
for dirname, subdirs, files in os.walk("./temp/"):
    zf.write(dirname)
    for filename in files:
        zf.write(os.path.join(dirname, filename))
zf.close()'''

if len(sys.argv) <= 1:
    sys.argv.append('--help')

options = parser.parse_args()


# If you add command-line options, consider passing them to the function,
# e.g. `options.func(options)`
