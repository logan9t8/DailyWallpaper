# Daily new wallpaper on desktop and lockscreen

## Setup
* Make sure Python is installed and install the following packages using pip
```shell
pip install requests urlextract
```
* The scripts can be set to run automatically using [Task Scheduler](https://en.wikipedia.org/wiki/Windows_Task_Scheduler) on Windows or using [cron](https://en.wikipedia.org/wiki/Cron) on Linux
* The scripts can be edited to change 'en-US' and 'us' to other locales for localized images

## Desktop
* The desktop wallpaper is sourced from [Bing Wallpaper](https://www.microsoft.com/en-us/bing/bing-wallpaper)
* Microsoft's app adds an overlay to the image, the Desktop.py script doesn't
* Desktop.py works both on Windows and Linux

## LockScreen
* The lockscreen wallpaper is sourced from [Windows Spotlight](https://learn.microsoft.com/en-us/windows/configuration/windows-spotlight/?pivots=windows-11)
* LockScreen.py works on Linux for KDE Plasma
* On Windows the feature is in-built
![image](https://github.com/user-attachments/assets/2a9bc787-de78-4f58-ac9a-37f2e5877cb1)

## Credits
* https://www.microsoft.com
* https://github.com/psf/requests
* https://github.com/lipoja/URLExtract
* https://github.com/ORelio/Spotlight-Downloader/blob/master/SpotlightAPI.md
