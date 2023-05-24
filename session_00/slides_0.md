# KPMG: Code
## Python — Session 0 — Lesson

---

# Course Overview


---

# Course Overview
- 10 weeks
- Tuesday 11am - 12pm —> Virtual lesson / Thursday 11am - 12pm —> In person lesson (at CSQ - London).
- Friday 11am - 11.30am —> Virtual drop in session.

---

## Any Questions?

---

# Operating Systems (OS), Command-line interface (CLI), Git & IDE​s

---

# Objectives

- Brief overview of Operating Systems​
- Understand and use Terminal/CLI​
- Understand and use Source Control Management & Git​
- Brief overview of Markdown and IDEs

---

# Operating Systems (OS)

---

# Operating systems (OS)

- **Software that communicates with machine hardware.​**

- Can you name some popular examples? 

 ---

# Operating systems

- Some include a graphical user interface (GUI) for manipulation (Windows, MAC OS)​.

- Linux has multiple distributions - some can include a GUI (e.g. Ubuntu), while some don’t.​

- When would we want or not want to have a GUI?

---

# Linux

- Popular operating system based on **UNIX​.**

- **Open-source, multiple distributions​.**

- Commonly used for **hosting web servers and scientific computing.**

---

# Command-line interface (CLI) and Bash

---


# CLI - Command-line interface

- Also referred to as the **‘Console’** or **‘Terminal’**.​

- **Used to run programs, manage files and interact with the computer.**

---

# Bash - Bourne Again SHell

- **Command Language for most Linux distributions​.**

- **sh = Bourne Shell​**

- The Shell is the **layer between** the Operating System (OS) and the User (or other services).

- Can be found it in the **Terminal app** on your Mac (you will have it by default because Mac OS is UNIX based) or in **Git Bash** on your Windows (not native -> needs to be installed).

---

# Bash commands

```bash
pwd # Prints to the console the path of your current working directory 
  # (short for "Print Working Directory")

ls # Lists the files in the current directory (short for "LiSt")


cd <directory_name> # Gets in a given directory (short for "Change current working Directory")

cd .. # Gets out of the current directory

```

---

# More bash commands

```bash
mkdir <directory_name> # Creates new directory (short for "MaKe DIRectory")

rmdir <directory_name> # Deletes an empty Directory (short for "ReMove DIRectory")

rm -r <directory_name> # Deletes the directory and its contents recursively
        # the "-" is called a "flag parameter" and it modifies the behaviour of the command


touch <file_name.txt/file_name.py> # Creates new file

rm <file_name.txt/file_name.py> # Deletes file


mv original_file1 /home/newfile1 # Moves a file (can be used for renaming) ​

cp original_filename copy_filename # Makes a copy of a file

```

---

# More bash commands

```bash
echo <text> # Displays in the terminal a line of text, Ex: echo Hello! --> Hello!

echo <text> > <file_name.txt>  # Writes a line of text in a file, Ex: echo Bonjour! > file.txt
        # The > overwrites the file if it exists or creates it if it doesn't exist.
        # The >> appends to a file or creates the file if it doesn't exist. 
        
cat <file_name.txt> # Reads the file and displays it line by line in the terminal,
        # (short for "conCATenates files"). Ex: cat file.txt --> Bonjour!


history  # Displays your recently run Bash Commands​

date # Displays the date

man <command> # Displays the manual and description for the chosen command -> ex: man ls/pwd/cd/mkdir


clear  # Clears the terminal screen



```

---

# Bash shortcuts

- TAB - autocompletes commands, file names, or directory names for you​.

- UP / DOWN Arrows - Scroll backward and forwards through previous commands you’ve typed in the current session. ​

- CTRL + C - Abort the current line you’re typing or a command that is currently executing​.


---


# Coding Time 
## Section A


---


# Steps

### I. On [Github](https://github.com/)

1. Fork the intro-to-python repo → https://github.com/sergiuHudrea/intro-to-python. 
   - The "Fork" icon will be situated in the top right hand corner.
   - When creating the new fork, select your account as the "Owner".
2. Copy the link of your newly forked repository. 
   - The link should have this format: https://github.com/YOUR_GITHUB_USERNAME/intro-to-python


---


### II. On [Replit](https://replit.com/)

1. Click on "Create Repl" in the top right hand corner. 
2. Select "Import from GitHub" 
3. Paste link of your newly forked repo into the "GitHub URL" section.
4. Click on "Import from GitHub".
5. When loaded, click on the "Git" icon from the "Tools" section, situated in the bottom left side.
6. In the newly opened Git window, click on "Connect to GitHub" and follow the steps. Click on "Only selected repositories", select your forked repository, and then click on "Install and Authorize".
7. Open a Shell window and a second window for displaying the contents of the exercises_0.md file.
8. Start Section A from exercises_0.md. Make sure you click on "Open preview", so you can see the content nicely formatted.


---

# Versioning problem

### Did you ever find yourself in this situation while working on an essay or document?
- essay, essay2, essay2.5, essay_final, essay_FINAL, essay_FINAL2, ESSAY_REALLY_LAST_ONE


---


# So what is the solution?

---

# Source Control Management(SCM) and Git


---


# Source Control Management(SCM)

- Refers to **tools used to track modifications** to a source code repository.​

- **Source Control Management = Version Control​**

---

# Why do we use Source Control?

- Helps teams work **collaboratively.**

- Developers can edit shared code **without unknowingly overwriting each other’s work**.

- Serves as a **protection mechanism.**


--- 

# Git

- **Git (Global Information Tracker) = a version control system.​**

- **Why Git?** - Because of its popularity, community, opensource nature, and decentralised approach.

---

# Git - What does it do?

- Allows you to **collaborate** on a project **without interfering with each other’s work.​**

- Keeps a **historical record of everyone's work** so you can go back to previous records.​

- You can work on your **local copy of the codebase** and then **merge your changes with the main codebase.​**

- Uses a **series of snapshots**, called **commits**, to **track changes** to the codebase over time, along with the timestamp and user who made the changes.

---

# Terminology

### Remote Repository​

- This is where everyone shares their code centrally (ex: GitHub) -> Think OneDrive, but for source code. 


### Local Repository​

 - A local version of the source code which resides on your machine. -> Think making a local copy of a file from OneDrive to your computer.

 ---

 # Basic Git commmands

 ```bash
git clone <https://github.com/sergiuHudrea/intro-to-python.git>  
          # Copies an existing Git repository from a remote location to your local machine.​


git init  # Initializes an existing directory as a Git repository.


git status  # Shows the current status of the repository, including which files have been modified, 
    # which files have been added to the staging area, and which files are not being tracked by Git.
 ```

 ---

 # Basic Git commands

 ```bash

git add . # Adds ALL changes to the staging area in preparation for committing them to the repository.​

git commit -m "<Short description of what you have worked on.>" 
        # Saves changes to the local repository, along with your commit message, usually describing the changes.

git push origin main # Uploads local changes to your remote repository, on the main branch.

git pull origin main # Downloads changes from the remote repository (main branch) 
                # and incorporates them into your local repository.

 ```

---

# Markdown and IDEs

---

# Markdown and README.md

- When creating a repository, you usually start off by writing a **README.md** file in a Markup language called Markdown.​

- The **README.md** **summarises important information** about the contents of the repo, **instructions** on how to edit or run the software, etc.​

- ***Markdown* is a lightweight markup language for creating formatted text using a plain-text editor.**

- **Fun fact:** This presentation was actually made by converting a markdown file into slides.

---

# IDEs

- **IDE** = An **Integrated development environment** is a software for application building. It combines tools into a single graphical user interface (GUI).​

- **Why use an IDE?** - The tools needed are already there and ready to use. It is efficient and makes life easier.​

- Imagine repairing a car in a parking lot VS repairing it in a garage.​

- **You can develop applications without an IDE**, but the you would have to build your own IDE by manually integrating the tools you need.​

- **Replit** = a **cloud IDE** -> No need for downloading software and configuring local environments. No more "But it works on my machine".

---

# Coding Time
## Section B
