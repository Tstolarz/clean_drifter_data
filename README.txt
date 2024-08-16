This package is an automator application for Mac OS systems

This package takes csv's of drifter data and cleans them and separates them into individual netcdf files based on the ID's of the drifters in the csv. 

The clean_drifter_data_app_local.py script cleans the drifter data by:
1. Separating the drifters by IDs
2. Removes duplicate time stamps
3. Resamples the data to be on the hour at T 00:00
4. Removes duplicate times again if needed
5. Exports individual netcdf files for each ID of drifter in the csv


Installation:

1. If python is not installed on the system yet, install it with miniforge using the corresponding operating system (https://github.com/conda-forge/miniforge). Open a terminal window and navigate to where the miniforge.sh was installed. Change the permissions on the file to all with the common chmod +rwx Miniforge.... If you hit tab after typing Mini it should auto complete. Then drag and drop the Miniforge.sh file onto the terminal window and complete the install process.
- If the installation process does not complete for whatever reason, then make sure to delete the Miniforge file before trying again


2. Change the permissions for the shell script to be able to execute code

3. In order to run this package you have to change the directories of the all the scripts to correspond to your system and installation of python directory.

- Edit the clean_drifter_data_local.sh file to copy over the directory of your python3 file (default install location is usually /Users/USER/miniforge3/bin/python3) and the clean_drifter_data_app_local.py script, replacing 
  the paths already there
-- If this is your first time installing python, upon completion open a terminal window and install the following packages: pandas, netcdf4 via the command "conda install pandas", "conda install netcdf4" (with no quotes).
-- If this is NOT your first time installing python, and you have virtual environments set up already, you can select the python3 in those environments which may or may not have pandas and netcdf4 installed for your personal    use

- In the search bar in the top right, search for the Automator app and open it. Open the Clean_drifter_data_local.app file with it by going to File>Open and navigating to the directory with the app. Copy the directory of the clean_drifter_data_local.sh and place into the automator script, replacing the text already there.

With these steps, the package SHOULD work. 


Use:

To use this application, drag and drop a drifter.csv file onto the Clean_drifter_data_local.app. This should create netcdf files for each drifter in the csv with the suffix CLEANED. This data is ready to process.

