Hello World!!

My name is Sandeep.

git branch <branchname>
creates a new branch with branchname specified


git checkout <branchname>
switches to the branchname specified


git config --global user.email "sandy.sandeepgarg@gmail.com"
set an email address that will be associated with each history marker


git config --global alias.ci commit
creates a global Git alias named ci that serves as a shortcut for the git commit command


git config --global color.ui false
set automatic command line coloring for Git for easy reviewing


git log
show the commit history for the currently active branch


git log featureOne featureTwo
show the commits on featureTwo branch that are not on featureOne

touch test.txt
The touch command creates a new, empty file if the file does not already exist.If the file already exists, it updates the file’s last modified timestamp instead of overwriting it.

mv test.txt sample.txt
This command is used to move files and directories from one location to another or to rename them. It changes the file's location or name without creating a duplicate.

mkdir testing
The mkdir command is used to make (create) a new directory

cd testing
The cd command is used to change the current working directory

find ./testing/ -name test.txt
./testing/test.txt

This command will locate and display the path to the file if it exists in the specified directory or its subdirectories.

sudo apt install tree
The command sudo apt install is used to install software packages.

tree -a ./testing
./testing
├── sample1
│   └── sample1.txt
├── sample2
│   ├── sample2.txt
│   └── sample3
│       └── sample3.txt
└── test.txt

4 directories, 4 files

The tree command displays the complete hierarchical structure of a directory, showing all its subdirectories and files in a tree-like format

awk '{print}' sample.txt
awk -F' ' '{print $1, $4}' sample.txt
awk -F' ' '{print $1, "has salary", $4}' sample.txt
awk -f print_salary.awk sample.txt
The AWK command is a text-processing and pattern-scanning tool in Linux used for manipulating data and generating formatted reports. It reads files line by line, applies patterns, and performs specified actions on matching lines.

md5sum sample.txt
The md5sum is designed to verify data integrity using Message Digest Algorithm 5. MD5 is 128-bit cryptographic hash and if used properly it can be used to verify file authenticity and integrity.

date
Sun Jan 25 21:37:11 EST 2026
date -u
Mon Jan 26 02:37:24 UTC 2026
date -d "12/25/2025"
Thu Dec 25 00:00:00 EST 2025
date --date "2 year ago"
Thu Jan 25 21:38:08 EST 2024
date --date "yesterday"
Sat Jan 24 21:38:21 EST 2026
date -d "next tuesday"
Tue Jan 27 00:00:00 EST 2026
date -d "1 year"
Mon Jan 25 21:38:39 EST 2027

The date command displays the current date and time in a variety of formats and set the system date and time. It can also be used to display future or old dates and check the system timezone which may be helpful in determining various issues.

file sample.txt
sample.txt: ASCII text

file testing/*
testing/sample1:  directory
testing/sample2:  directory
testing/test.txt: empty

The 'file' command is used for determining the type of a file. It identifies file types by examining their content rather than their file extensions, making it an indispensable tool for users who work with various file formats.

ls -ltr sample.txt
-rw-r--r-- 1 garsande garsande 110 Jan 25 20:13 sample.txt
chmod 755 sample.txt
ls -ltr sample.txt
-rwxr-xr-x 1 garsande garsande 110 Jan 25 20:13 sample.txt
chmod 744 sample.txt
ls -ltr sample.txt
-rwxr--r-- 1 garsande garsande 110 Jan 25 20:13 sample.txt
chmod 644 sample.txt
ls -ltr sample.txt
-rw-r--r-- 1 garsande garsande 110 Jan 25 20:13 sample.txt


The chmod (change mode) command is used to set or modify file and directory permissions. Every file in Linux has an owner, a group, and associated permissions that determine who can read, write, or execute the file. Using chmod, users can control these permissions to ensure proper access and security.

for command - for i in {1..5}; do  echo $i; done
The for command is used in shell scripting to iterate over a set of values or perform set of tasks repeatedly. The for loop allows users to create easy to maintain automated operations.


