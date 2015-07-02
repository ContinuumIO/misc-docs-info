#Contributing to this GitHub test repository

Welcome! This GitHub repository aspires to become a comprehensive tutorial for GitHub, git, rst and Sphinx, GitHub Pages, and Travis CI. The repository contains a guest book, so for your first edit to a GitHub repository using these tools, you can simply sign the guest book.

To begin, on an OS X or Linux machine, make a GitHub account if you don't already have one, and log in.

Open a terminal window.

A quick refresher on unix commands:

*pwd* ("print working directory") prints the path of the current directory.

*ls* lists the files in the current directory.

*cd* changes the directory to a new one. *cd* with no argument changes to your home directory, often /home/username on Linux or /Users/username on OS X. The home directory is also abbreviated with a single character, the tilde, "~". So ``cd``, ``cd ~``, and ``cd /Users/jsmith`` may all do the same thing.

*mkdir* makes a new directory.

*rm* removes files and directories.

*mv* moves files and directories.

*cp* copies files and directories.

If you haven't already, install Anaconda or Miniconda.

If you haven't already, set up SSH with GitHub using the instructions at https://help.github.com/articles/generating-ssh-keys/ .

If you haven't already, install git. Enter ``git --version`` on the command line, and you'll either see the version of git you have installed, or a message telling you how to install git on your system.

If you haven't already, set your name and email address in git:

    git config --global user.email "you@example.com"
    git config --global user.name "Your Name"

Unless you have another preferred editor, set git to use the friendlier nano editor instead of the default vi editor for commit messages:

    git config --global core.editor "nano"

Make a GitHub working directory, which we will somewhat arbitrarily call 'ghw', and go into it:

    mkdir ghw
    cd ghw

Go to https://github.com/electronwill/sphinx . On the right there's a box that says "HTTPS clone URL". Click the "SSH" link underneath it so it shows the "SSH clone URL" instead. Copy that URL, such as git@github.com:electronwill/sphinx.git .

Next, "clone" the repository to create a copy of it on your local computer, where you can make edits before publishing them to the repository on GitHub:

    git clone git@github.com:electronwill/sphinx.git

Go into the sphinx directory in the local copy of the repository:

    cd sphinx

Now we'll build a conda environment with the tools needed for documentation. Conda developer Aaron Meurer has already created a conda package named "conda-docs-deps" to help with this process. Enter the following:

    conda update conda
    conda create -n docs -c asmeurer conda-docs-deps python=3
    conda install -n root conda-build pycrypto
    conda update --all
    source activate docs
    conda update --all

If you're not yet familiar with conda, try the tutorials at http://conda.pydata.org/docs/using/index.html .

The history of a repository is a bit like a tree, with copies branching off away from each other as changes are made. However, unlike a tree, these "branches" can be merged back into the main pathway of the repository, which is also called a branch, and is usually named "master". In our workflow, after cloning the repository from GitHub to our local machine, we'll make a new branch, make our changes, upload or "push" that branch back to the GitHub repository, and make a "pull request" on GitHub asking the repository's maintainers to merge our branch into the master branch. Once our pull request is approved and merged, or denied and closed, we can delete that branch on GitHub and locally.

As long as everyone makes their changes on a new branch, it's easy for multiple people to work on a repository at the same time, and for all these changes to be merged back together without causing interference.

Conceptually, these categories nest within each other: GitHub has organizations and users, which have repositories, which have branches, which have directories, which have directories and files.

The ``git branch`` command displays the branches of your current repository, with a star next to the branch you're in. Try it:

    git branch

Next, make up a branch name for the change you’re about to make. The best branch names are short, descriptive, and unique, such as "fix-install", "docs-cleanup", or "add-travis-ci", rather than vague branch names such as "feature", "fix", or "patch". For this first test branch, we can use "sign-guest-book", so enter this:

    git checkout -b sign-guest-book

This creates a new branch with that name, and "checks it out", moving you into it. You can see this by running ``git branch`` again:

    git branch

You can also use ``git status`` to see git's view of the files in the repository:

    git status

Currently, git should say that there are no changed files.

Build the html files from the rst file sources:

    make clean; make html

Now open ~/ghw/sphinx/build/html/index.html in a browser. As well as the browser's "file/open file" option, you can use ``open build/html/index.html`` on OS X or ``firefox build/html/index.html`` on Linux. Use the link on the index page to look at the guest book. Then you can close that browser tab.

Now choose your favorite editor. nano is a cross platform editor that runs in the terminal, and there are also many good graphical editors such as gedit on Linux and Atom on OS X. Use your editor to open the file ``source/guest.rst``. This is a simple rst file, with little formatting, and it should just display the text almost the same way a text editor does. Add your name and the date, and save and close the file.

Now open index.html in a browser again and look at the guest book to see that it hasn't changed. The rst file is different, but to make the html different, we will need to rebuild it. Close the browser tab.

Now rebuild the html files:

    make clean; make html

Now open index.html in a browser again and look at the guest book. You should see your name added to the list. Close the browser tab.

Sometimes `make html` will produce errors or warnings. If so, edit the rst files again to fix the problems, then ``make clean; make html`` again. Repeat this until there are no errors or warnings, and you like the way the local html files look, and then proceed.

Use ``git status`` to see git's view of the current files:

    git status

Git should report that you have modified the file ``source/guest.rst``. Add that file to git's list of changes to be made:

    git add source/guest.rst

If you wish to remove or move files in a repository and then commit that change, use "git rm" and "git mv", which work the same way as the Linux and OS X "rm" and "mv" commands.

Once you're done making changes, you will put these changes into a "commit", which describes them to the repository maintainer who will merge them into the repository:

    git commit

This will open the nano text editor so you can write a commit message. Before writing your first commit message, please read these two brief lessons on how to write them well.

https://robots.thoughtbot.com/5-useful-tips-for-a-better-commit-message

http://tbaggery.com/2008/04/19/a-note-about-git-commit-messages.html

Once your message has been written, use control-x to exit nano, and follow its prompts to save your file with the filename suggested.

Now we are ready to push the changes from our local machine to GitHub with the ``git push`` command:

    git push origin sign-guest-book

In a browser, go to https://github.com/electronwill/sphinx . You should see a message that you recently pushed branches and a green "Compare & pull request" button. You can use that button to request that the repository's maintainers pull your changes into the repository. Once the pull request is made, you can leave comments below it, and communicate with other users such as the repository owners using "@name" mentions.

They may ask you to make further changes before they approve the pull request, and you can do this by editing the files again, using ``git add``, ``git commit``, and ``git push`` again, and leaving another comment asking them to review the changes again. These changes will appear on the same pull request, so you don't need to make a new pull request.

Once the changes are merged, go back to the terminal window, go back to the master branch, use ``git pull`` to pull the latest changes in the GitHub repository down to our local copy, and delete the sign-guest-book branch:

    git branch
    git checkout master
    git branch
    git pull
    git branch -d sign-guest-book
    git branch

You can view the history of a file with ``git log``:

    git log source/guest.rst

When you're done, deactivate the conda environment and return to the home directory:

    source deactivate
    cd

##Making more changes

Many of the previous steps don't need to be done every time. For example, ``git clone`` is only done once for each repository, and ``conda create`` only once. For edits after the first one, do this:

    cd ~/ghw/sphinx
    source activate docs
    git checkout master
    git pull
    git checkout -b make-another-change

Now edit the rst files.

Now build the html files:

    make clean; make html

Check the files in a browser to confirm the changes.

Repeat the edit, make, and open steps as needed until your rst files build with no errors or warnings and you like the way they look.

Add the files to be put into the next commit, and repeat the ``git add`` command for each file you created or edited, until ``git status`` no longer shows untracked changes. Create a commit, with a commit message. And push the files to GitHub:

    git add source/index.rst
    git commit
    git push origin make-another-change

Go to the GitHub repository page and use the green “Compare & pull request” button to request that the repository maintainers pull in your changes.

Once the changes are merged, return git to the master branch and update it, delete the branch, deactivate your conda environment, and return to your home directory:

    git checkout master
    git pull
    git branch -d make-another-change
    source deactivate
    cd

##Other notes

This is only one possible workflow, and different repositories and their owners and maintainers may have different ways of doing things. For example, a maintainer may ask that you fork a repository to your own GitHub account, and still pull from the main repository, but add your own repository as a named remote repository and push to that instead of to the origin, and make pull requests from those pushes. Although slightly more complex for the users, this method keeps the branch history of the main project simpler.

Many projects such as https://github.com/conda/conda-docs and https://github.com/ContinuumIO/docs have a README.md file like this on the front page of the repository explaining their process and how to contribute to that repository.

It is possible to make the current branch name display in your command prompt, so that you don't have to rely on ``git branch`` as much: http://stackoverflow.com/questions/15883416/adding-git-branch-on-the-bash-command-prompt/24716445#24716445
