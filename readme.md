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

