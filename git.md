# GIT

## General

### Rebase in a nice way

git pull --rebase

### status

git status

### Add the local changes

git add filename

### Check local changes before commit

git diff --cached

### Create change message using the -m, don't do this overall

git commit -m "added file x jira 6523"

### Amend

git commit --amend

### Remove your latest commit

git reset HEAD~

### Show

git show

### Reset your repo, use carfully

git reset --hard origin/master

### Reset a file from the last commit

git checkout -- puppet-modules/Puppetfile

### A compressed overview of the log

git reflog

### Fetch remote heads

git fetch --all

### view all the branches that we can use

cat .git/FETCH_HEAD

### Show changed files over time

From time to time people perform multiple changes to a file so you can't perform a git blame.
But in my case i needed to find when the first changed happed, bellow you will find a few ways of doing this.

#### Go through changed files. from current data to a very old random commit

git show --stat --oneline 42516364da7f283aa2e8851d335c5762cfd4d62c..HEAD

#### Another way is bellow, it shows the same stuff as git log but adds all the files that was changed

git log --stat

#### A third way is but it seems overkill overall for us. But a cool function

git-bisect

### Overwrite a filechange from a earlier commit

git show 8e1b479e71a438e57e5c884437ed4bddc218ec57 -- puppet-modules-eis/ | git apply -R

## Gerrit

git gerrit init

### Push stuff to gerrit for code review

git push origin HEAD:refs/for/master

### Download gerrit hook

I think this is the default url, but overall you should be able to find the commit-msg in gerrit somewhere. Ask your admin

curl -Lo .git/hooks/commit-msg http://gerrit.domain.se/tools/hooks/commit-msg

chmod +x .git/hooks/commit-msg

### Send message to gerrit

ssh selngerrit gerrit review ${SHA1} --message "Blaha"

SHA1=git log -1 --pretty=format:%H HEAD

### Squash commits

Where ~5 is how many commits you want to go back and put together.

git rebase -i HEAD~5
