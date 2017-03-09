import os
import datetime
import shutil


today = datetime.date.today()
today_str = today.isoformat()


confdir = os.getenv("my_config")
conffile = "services.conf"
conffilename = os.path.join(confdir, conffile)
dropbox = os.getenv("dropbox")
sourcedir = os.getenv("source_dirs")

destinationdir = os.path.join(dropbox, "backup", today_str)

os.makedirs(destinationdir)



def main():
    for file_name in open(conffilename):
        fname = file_name.strip()
        if fname:
            source_file = os.path.join(sourcedir, fname)
            dest_file = os.path.join(destinationdir, fname)
            shutil.copytree(source_file, dest_file)

if __name__ == '__main__':
    main()


