import argparse
from pathlib import Path
import sys
from sys import stderr

class Logger:
    def __init__(self,verbose = True):
        self.verbose = verbose

    def setVerbose(self,verbose):
        self.verbose = verbose

    def message(self,message):
        if self.verbose:
            print(message)
    
    def error(self,message):
        print(message,file=stderr)
        

logger =  Logger()

def create_clean_folders(folder_name:str):
    src_dest = Path(folder_name)
    if src_dest.exists():
        logger.error(f'{src_dest} already exits')
        sys.exit(1)
    else:
        
        src_dest.mkdir(parents=True)
        logger.message(f'Creada: {src_dest}')
        domain_folders = ('entities','repositories')
        data_folders = ('models','repositories')
        presentation_folders = ('components','screens')
        data_folder = src_dest / 'data'
        domain_folder = src_dest / 'domain'
        presentation_folder = src_dest / 'presentation'
        domain_folder.mkdir()
        logger.message(f'Creada: {domain_folder}')
        data_folder.mkdir()
        logger.message(f'Creada: {data_folder}')

        presentation_folder.mkdir()
        logger.message(f'Creada: {presentation_folder}')
        

        for folder_name in domain_folders:
            new_folder = (domain_folder/folder_name)
            new_folder.mkdir()
            logger.message(f'Creada: {new_folder}')

        for folder_name in data_folders:
            new_folder = (data_folder/folder_name)
            new_folder.mkdir()
            logger.message(f'Creada: {new_folder}')

        for folder_name in presentation_folders:
            new_folder = (presentation_folder/folder_name)
            new_folder.mkdir()
            logger.message(f'Creada: {new_folder}')
        
             
        sys.exit(0)


def main():
    parser = argparse.ArgumentParser(
        description='Crea una estructura de carpetas de clean arquitecture'
    )
    parser.add_argument("-v","--verbose",action='store_true')
    parser.add_argument("foldername",help='Nombre de la carpeta principal')
  

    args = parser.parse_args()
    logger.setVerbose(args.verbose)
    create_clean_folders(args.foldername)
    

if __name__== '__main__':
    main()