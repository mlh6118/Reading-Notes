# Bash Command Line
The command line is a text based interface to the system.

It is so nice to come back to Linux and the command line after being away 
for so many years.  It is like seeing an old friend.  There are a few 
commands I did not know, such as `man -k <search term>` which will be quite 
handy in the future.  Below are most of the commands that were in our 
reading to create my own little reference guide.

Commands and other useful information.
* `echo`: used to display messages
* `pwd`: print working directory
* `ls [options] [location]`: list what is in the current location
* absolute path: specify location in relation to root directly and always 
  start with '/.'
* relative path: specify a location in relation to current location and do 
  not begin with a slash.
* `~`: shortcut for home directory.
* `.`: reference to current directory.
* `..`: reference to parent directory.
* `cd`: change directory
* tab completion: assistive device to finish word.  If the one that appears 
  is not correct, press `tab` again to see all options and keep pressing 
  `tab` until the correct one is selected.
* `file [path]`: Used to determine the type of file a particular file is.  
  Linux is an extensionless system, so just looking at a file name may not 
  tell the type of file it is.
* Linux is case sensitive!
* Spaces in file names are handled in two ways:
  * Quotes around the file name
  * Using a `\ ` before the space in the file name
* Hidden files and directories: start with a `.`
  * View hidden files and directories with `ls -a`
* Manual "man" pages give info on every command available, how to run them 
  and what command line arguments are used.
  * `man <command to look up>`
  * `man -k <search term>`: looks for keyword in the man pages
  * `/<term>`: search for keyword within a specific man page
  * `n`: used after `/<term>` to find the next instance
* `mkdir [options] <Directory>`: create a new directory
  * `-p`: option to create parent directories, as needed
  * `-v`: option to show what is being done as the command runs
* `rmdir [options] <Directory>`: remove directory
  * `-p` and `-v` are options here.
  * Directory must be empty prior to removal.
* `touch [options] <filename>`: create a blank file.
* `rm [options] <file>`: remove a file.
* `rm [options] <Directory>`: remove a directory.
  * `r`: recursive
  * `i`: interactive which will prompt for removing each file and directory, 
    plus allows for cancellation

##### Reference: [Linux Tutorial - 1. The Command Line](https://ryanstutorials.net/linuxtutorial/commandline.php)