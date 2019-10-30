from watchdog.observers import Observer
import time
from watchdog.events import FileSystemEventHandler
import os 
import json
import shutil
from datetime import datetime
from time import gmtime, strftime

class FolderOrganizer(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            i = 1
            if filename != 'almeida':
                try:
                    new_name = filename
                    extension = 'noname'
                    try:
                        extension = str(os.path.splitext(folder_to_track + '/' + filename)[1])
                        path = extensions_folders[extension]
                    except Exception:
                        extension = 'noname'

                    now = datetime.now()
                    year = now.strftime("%Y")
                    month = now.strftime("%m")

                    destination_folder_path = extensions_folders[extension]
                    
                    year_exists = False
                    month_exists = False

                    try:
                        os.listdir(extensions_folders[extension])
                    except Exception as ex:
                        os.makedirs(extensions_folders[extension])

                    for folder_name in os.listdir(extensions_folders[extension]):
                        if folder_name == year:
                            destination_folder_path = extensions_folders[extension] + "/" +year
                            year_exists = True
                            for folder_month in os.listdir(destination_folder_path):
                                if month == folder_month:
                                    destination_folder_path = extensions_folders[extension] + "/" + year + "/" + month
                                    month_exists = True
                    if not year_exists:
                        os.mkdir(extensions_folders[extension] + "/" + year)
                        destination_folder_path = extensions_folders[extension] + "/" + year
                    if not month_exists:
                        os.mkdir(destination_folder_path + "/" + month)
                        destination_folder_path = destination_folder_path + "/" + month
 
                    file_exists = os.path.isfile(destination_folder_path + "/" + new_name)
                    while file_exists:
                        i += 1
                        new_name = os.path.splitext(folder_to_track + '/' + filename)[0] + str(i) + os.path.splitext(folder_to_track + '/' + filename)[1]
                        new_name = new_name.split("/")[4]
                        file_exists = os.path.isfile(destination_folder_path + "/" + new_name)
                    src = folder_to_track + "/" + filename

                    new_name = destination_folder_path + "/" + new_name
                    os.rename(src, new_name)
                except Exception as ex:
                    print(ex)


folder_to_track = '/home/almeida/Desktop'
destination_folder = '/home/almeida/Desktop/Organized'
extensions_folders = {
#No name
    'noname' : "{}/Other/Uncategorized".format(destination_folder),
#Audio
    '.aif' : "{}/Media/Audio".format(destination_folder),
    '.cda' : "{}/Media/Audio".format(destination_folder),
    '.mid' : "{}/Media/Audio".format(destination_folder),
    '.midi' : "{}/Media/Audio".format(destination_folder),
    '.mp3' : "{}/Media/Audio".format(destination_folder),
    '.mpa' : "{}/Media/Audio".format(destination_folder),
    '.ogg' : "{}/Media/Audio".format(destination_folder),
    '.wav' : "{}/Media/Audio".format(destination_folder),
    '.wma' : "{}/Media/Audio".format(destination_folder),
    '.wpl' : "{}/Media/Audio".format(destination_folder),
    '.m3u' : "{}/Media/Audio".format(destination_folder),
#Text
    '.txt' : "{}/Text/TextFiles".format(destination_folder),
    '.doc' : "{}/Text/Microsoft/Word".format(destination_folder),
    '.docx' : "{}/Text/Microsoft/Word".format(destination_folder),
    '.odt ' : "{}/Text/TextFiles".format(destination_folder),
    '.pdf': "{}/Text/PDF".format(destination_folder),
    '.rtf': "{}/Text/TextFiles".format(destination_folder),
    '.tex': "{}/Text/TextFiles".format(destination_folder),
    '.wks ': "{}/Text/TextFiles".format(destination_folder),
    '.wps': "{}/Text/TextFiles".format(destination_folder),
    '.wpd': "{}/Text/TextFiles".format(destination_folder),
#Video
    '.3g2': "{}/Media/Video".format(destination_folder),
    '.3gp': "{}/Media/Video".format(destination_folder),
    '.avi': "{}/Media/Video".format(destination_folder),
    '.flv': "{}/Media/Video".format(destination_folder),
    '.h264': "{}/Media/Video".format(destination_folder),
    '.m4v': "{}/Media/Video".format(destination_folder),
    '.mkv': "{}/Media/Video".format(destination_folder),
    '.mov': "{}/Media/Video".format(destination_folder),
    '.mp4': "{}/Media/Video".format(destination_folder),
    '.mpg': "{}/Media/Video".format(destination_folder),
    '.mpeg': "{}/Media/Video".format(destination_folder),
    '.rm': "{}/Media/Video".format(destination_folder),
    '.swf': "{}/Media/Video".format(destination_folder),
    '.vob': "{}/Media/Video".format(destination_folder),
    '.wmv': "{}/Media/Video".format(destination_folder),
#Images
    '.ai': "{}/Media/Images".format(destination_folder),
    '.bmp': "{}/Media/Images".format(destination_folder),
    '.gif': "{}/Media/Images".format(destination_folder),
    '.ico': "{}/Media/Images".format(destination_folder),
    '.jpg': "{}/Media/Images".format(destination_folder),
    '.jpeg': "{}/Media/Images".format(destination_folder),
    '.png': "{}/Media/Images".format(destination_folder),
    '.ps': "{}/Media/Images".format(destination_folder),
    '.psd': "{}/Media/Images".format(destination_folder),
    '.svg': "{}/Media/Images".format(destination_folder),
    '.tif': "{}/Media/Images".format(destination_folder),
    '.tiff': "{}/Media/Images".format(destination_folder),
    '.CR2': "{}/Media/Images".format(destination_folder),
#Internet
    '.asp': "{}/Other/Internet".format(destination_folder),
    '.aspx': "{}/Other/Internet".format(destination_folder),
    '.cer': "{}/Other/Internet".format(destination_folder),
    '.cfm': "{}/Other/Internet".format(destination_folder),
    '.cgi': "{}/Other/Internet".format(destination_folder),
    '.pl': "{}/Other/Internet".format(destination_folder),
    '.css': "{}/Other/Internet".format(destination_folder),
    '.less': "{}/Other/Internet".format(destination_folder),
    '.sass': "{}/Other/Internet".format(destination_folder),
    '.scss': "{}/Other/Internet".format(destination_folder),
    '.htm': "{}/Other/Internet".format(destination_folder),
    '.html': "{}/Other/Internet".format(destination_folder),
    '.js': "{}/Other/Internet".format(destination_folder),
    '.ts': "{}/Other/Internet".format(destination_folder),
    '.jsp': "{}/Other/Internet".format(destination_folder),
    '.part': "{}/Other/Internet".format(destination_folder),
    '.php': "{}/Other/Internet".format(destination_folder),
    '.rss': "{}/Other/Internet".format(destination_folder),
    '.xhtml': "{}/Other/Internet".format(destination_folder),
#Compressed
    '.7z': "{}/Other/Compressed".format(destination_folder),
    '.arj': "{}/Other/Compressed".format(destination_folder),
    '.deb': "{}/Other/Compressed".format(destination_folder),
    '.pkg': "{}/Other/Compressed".format(destination_folder),
    '.rar': "{}/Other/Compressed".format(destination_folder),
    '.rpm': "{}/Other/Compressed".format(destination_folder),
    '.tar.gz': "{}/Other/Compressed".format(destination_folder),
    '.z': "{}/Other/Compressed".format(destination_folder),
    '.zip': "{}/Other/Compressed".format(destination_folder),
#Disc
    '.bin': "{}/Other/Disc".format(destination_folder),
    '.dmg': "{}/Other/Disc".format(destination_folder),
    '.iso': "{}/Other/Disc".format(destination_folder),
    '.toast': "{}/Other/Disc".format(destination_folder),
    '.vcd': "{}/Other/Disc".format(destination_folder),
#Data
    '.csv': "{}/Programming/Database".format(destination_folder),
    '.dat': "{}/Programming/Database".format(destination_folder),
    '.db': "{}/Programming/Database".format(destination_folder),
    '.dbf': "{}/Programming/Database".format(destination_folder),
    '.log': "{}/Programming/Database".format(destination_folder),
    '.mdb': "{}/Programming/Database".format(destination_folder),
    '.sav': "{}/Programming/Database".format(destination_folder),
    '.sql': "{}/Programming/Database".format(destination_folder),
    '.tar': "{}/Programming/Database".format(destination_folder),
    '.xml': "{}/Programming/Database".format(destination_folder),
    '.json': "{}/Programming/Database".format(destination_folder),
#Executables
    '.apk': "{}/Other/Executables".format(destination_folder),
    '.bat': "{}/Other/Executables".format(destination_folder),
    '.com': "{}/Other/Executables".format(destination_folder),
    '.exe': "{}/Other/Executables".format(destination_folder),
    '.gadget': "{}/Other/Executables".format(destination_folder),
    '.jar': "{}/Other/Executables".format(destination_folder),
    '.wsf': "{}/Other/Executables".format(destination_folder),
#Fonts
    '.fnt': "{}/Other/Fonts".format(destination_folder),
    '.fon': "{}/Other/Fonts".format(destination_folder),
    '.otf': "{}/Other/Fonts".format(destination_folder),
    '.ttf': "{}/Other/Fonts".format(destination_folder),
#Presentations
    '.key': "{}/Text/Presentations".format(destination_folder),
    '.odp': "{}/Text/Presentations".format(destination_folder),
    '.pps': "{}/Text/Presentations".format(destination_folder),
    '.ppt': "{}/Text/Presentations".format(destination_folder),
    '.pptx': "{}/Text/Presentations".format(destination_folder),
#Programming
    '.c': "{}/Programming/C&C++".format(destination_folder),
    '.class': "{}/Programming/Java".format(destination_folder),
    '.dart': "{}/Programming/Dart".format(destination_folder),
    '.py': "{}/Programming/Python".format(destination_folder),
    '.sh': "{}/Programming/Shell".format(destination_folder),
    '.swift': "{}/Programming/Swift".format(destination_folder),
    '.h': "{}/Programming/C&C++".format(destination_folder),
#Spreadsheets
    '.ods' : "{}/Text/Microsoft/Excel".format(destination_folder),
    '.xlr' : "{}/Text/Microsoft/Excel".format(destination_folder),
    '.xls' : "{}/Text/Microsoft/Excel".format(destination_folder),
    '.xlsx' : "{}/Text/Microsoft/Excel".format(destination_folder),
#System
    '.bak' : "{}/Text/Other/System".format(destination_folder),
    '.cab' : "{}/Text/Other/System".format(destination_folder),
    '.cfg' : "{}/Text/Other/System".format(destination_folder),
    '.cpl' : "{}/Text/Other/System".format(destination_folder),
    '.cur' : "{}/Text/Other/System".format(destination_folder),
    '.dll' : "{}/Text/Other/System".format(destination_folder),
    '.dmp' : "{}/Text/Other/System".format(destination_folder),
    '.drv' : "{}/Text/Other/System".format(destination_folder),
    '.icns' : "{}/Text/Other/System".format(destination_folder),
    '.ico' : "{}/Text/Other/System".format(destination_folder),
    '.ini' : "{}/Text/Other/System".format(destination_folder),
    '.lnk' : "{}/Text/Other/System".format(destination_folder),
    '.msi' : "{}/Text/Other/System".format(destination_folder),
    '.sys' : "{}/Text/Other/System".format(destination_folder),
    '.tmp' : "{}/Text/Other/System".format(destination_folder),
}


event_handler = FolderOrganizer()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()

try:
    while True:         
        cleaning_time_loop_in_seconds = 25
        print('cleaning... every {} seconds'.format(cleaning_time_loop_in_seconds))  
        time.sleep(cleaning_time_loop_in_seconds)
except KeyboardInterrupt:
    observer.stop()
observer.join()