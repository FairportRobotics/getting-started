# Getting Started
Welcome to Fairport Robotics software team!  Here are the steps to take to get started.

## First Steps

1. [Download](https://code.visualstudio.com/) VS Code.  There is [full setup instructions](https://code.visualstudio.com/docs/setup/setup-overview).
2. [Create a GitHub account](https://github.com/signup).  GitHub is where the team's software repository.
3. Authenticate with SSH
   - [Generate a New SSH Key](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)
   - [Add the SSH Key to your GitHub Account](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account)
4. Clone this repository `git clone git@github.com:FairportRobotics/getting-started.git`
5. Checkout the next-step branch by typing `git checkout next-step`

## Next Step
Did you notice how the README.md file has changed?  This is the magic of git.  Let's teach you some more tricks but first what is this git you speak of?

### Git Introduction
Git is a decentralized version control system.  That means it tracks files.  It basically takes a picture of what all your files look like at that moment and stores a reference to that snapshot.  It is made up of three parts: a repository of the history, the user's working directory and the staging area.

![](https://marklodato.github.io/visual-git-guide/basic-usage.svg)

Our team uses GitHub as our code repository.  Team members create a working directory by a `git clone` command.  As the name implies it will create a clone of the git repository on your local machine.  Git allows for branching of the source code.  You can switch to a specific branch by using the `git checkout` command followed by the name of the branch.

### Git First Steps
Once cloned, you can make changes to your local repository.  Once you have changes you want to save you *add* them to the staging area by a `git add` followed by the name of the file.  One shortcut is to use `git add .` which will add all changes.  The changes are still in your local staging area.  If you want to make it part of the history you type `git commit`.  After providing a helpful message about the changes, it will be ready to send to our repository.  To send your changes you use `git push`.  This will "push" your changes to GitHub.

Now you will probably be working with other people.  It is important to have their changes they have pushed reflected in your repository.  Use `git pull` to pull down all the changes from GitHub to your repository.

One other helpful command is `git status`.  It will tell you what has changed, and what has been staged.

One nice thing of working with git is that you can undo any changes.  `git reset` can be used to undo all changes.  This can be really helpful when you have broken working code (unintentionally of course).

These commands are often represented in the GUI of your IDE so you may not need to type them into a command prompt.  However, it is important to have a basic understanding of how they work.

### Now Let's Practice

Let's  practice these fundamentals by checking out the "practice" branch (`git checkout practice`).
