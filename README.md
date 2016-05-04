# HHFH_Movie


##What it does:

This script was made to help the moderators and VIPs at HiT Hi FiT Hai DC++ Hub.
It generates a valid entry for latest movies after its magnet has been copied.
This greatly reduces the effort to make an entry for the movie category.

The script fetches the correct imdb link for the file and then parses the 
html to get the movie tags like genre, country, language. Currently it can automatically
determine when to use 'Eng-Subs','HIN' and 'TAM' tags.

Size tag is fetched from system.log file of the DC Client. So make sure that you have system logging enabled. It can also determine the correct format of size tag.

=========================================
##Usage:
- Create a shortcut of the exe on desktop.
- Right click on shortcut>Properties and assign a hotkey like {CTRL} + {M} to it.
- Once you've downloaded a movie, wait for it to hash.
- After it shows 'Finished hashing..' in the bottom, open your filelist and copy the magnet of the file.
- Hit the hotkey you defined ({CTRL} + {M} in this example). This would start the script.
- Switch to BOT_Offliner in the meantime.
- Afer it finishes successfully, you will see a message saying "You can now use {CTRL} + {V} to get the entry".
- Paste it in BOT_Offliner and check for any errors.
- Add the entry if everything is OK. Contact me in case of error.

=======================================

##Note:
	
- Files must be named properly for it to work. For example:
	* Title (2015) BluRay m720p [nick].mkv
	* Title (2015) [BluRay m720p] [nick].mkv
	* Title (2015) WEBHD 1080p [nick].mkv
	* Title (2015) WEB-DL 720p [nick].mkv
	* Title (2015) HDRip 720p (KOR Hard-Subs/EXTENDED) [usernick].mp4
	* Title (2015) DVDRip (Malyalam) E-Subs [usernick].avi 
	* Title (2015) DVDRip (Tamil) E-Subs [usernick].avi 

- If you need to add tags of your own to the file, make sure you add them after the quality tag (DVDRip/WEBHD/BluRay m720p).
- If the script exits without any alert, its probably because you either named your file incorrectly or the country code support has not yet been added. PM me

=======================================

##Updates v1.0.2:

* Fixed wrong country tag placement ( Thanks Cipher da :) )

##Updates v1.0.1:

* Added support for AKA tag
* Added support for sdmovies
* Added support for EXTENDED tag
* Added support for Tamil & Malyalam movies

