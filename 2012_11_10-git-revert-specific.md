Date: 2012-11-19
Title: Git revert to commit
Tags: git, revert, undo
Category: rand
Slug: git-revert-specific

Have you ever made a commit only to figure out that it wasn't such a good idea? How about wanting to go back in your history and reverting to a specific commit? It's actually simple once you know how:

	:::git
	git reset 56e05fced #resets index to former commit; replace '56e05fced' with your commit code
	git reset --soft HEAD@{1} #moves pointer back to previous HEAD
	git commit -m "Revert to 56e05fced"
	git reset --hard #updates working copy to reflect the new commit

Just replace 56e05fced with the commit code you want to rever to

The first line resets the index to a former commit, 56e05fced in this case.
The second line moves the pointer back to the previous head.
Third line is self explanatory
Last tine updates the working copy to reflect the new commit

Then all you have to do is push the changes with a ```git push origin master``` or whatever your branch may be.