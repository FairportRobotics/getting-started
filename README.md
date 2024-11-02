# Getting Started - Practice

Congratulations on your first successful pull request!  You have learned the skills needed to start contributing to open source projects. 

## The `main` Branch
Each project starts with the `main` branch.  This branch is the most important branch.  The cardinal rule of git is **never mess up the main branch.**  Git has some tools that can help prevent messing up the branch.  We will use them in this exercise.

## Multiple Workers Editing Same File
We will pretend that this branch is the **main** branch of our project.  Our project has one python file (main.py).  There is one function called `happy_birthday`.  You pass in the day and the month into the function and it will print a nice birthday message (how special).  Your task is to change main.py to print a birthday message for you.

You need to:
* Create a branch off of `practice-main`
* Edit main.py to add in your message
* Add the file to staging
* Commit the changes
* Push the changes to GitHub
* Create a PR to merge it into `practice-main`

## Something Bad Happened
There's a good chance this wasn't as smooth as last time.  This occured because there were a lot of changes to main.py over time and your main.py was out of date.  When your changes are being merged back into the `practice-main` branch there is a merge conflict.  This is one way git is trying to help you to **never mess up the main branch.**  Mentors and veteran team members will explain what it means, and how to resolve them.

Once you have successfully completed this practice, offer help to your fellow team members.

## How to Prevent Merge Conflicts
One way to prevent merge conflicts is to get into the habit of pulling changes from GitHub regularly.  This will keep the files in your local repository up to date.  VS Code has the option to do this automatically.

Once we have all successfully completed the practice, please checkout the `the-end` branch.
