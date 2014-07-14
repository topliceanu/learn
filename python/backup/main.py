import os
import time

def backup (source, destination):
    """ Function backs up a list of files/directories to a destination file.

        Files a are grouped using tar then archived using zip.
    """
    target = destination + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'

    if not os.path.exists(target):
        os.mkdir(target)

    zip_command = 'zip -r {0} {1}'.format(target, ' '.join(source))
    run = os.system(zip_command)

    if run is 0:
        print 'Successfully backed up', target
    else:
        print 'Backup failed'
