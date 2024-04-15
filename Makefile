merge_upstream:  ## Merge upstream changes into master
	git fetch upstream
	git checkout master
	git merge upstream/master

preview_upstream:  ## Preview changes from upstream
	git difftool master upstream/master -y
