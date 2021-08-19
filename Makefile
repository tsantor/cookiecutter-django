merge_upstream:
	git fetch upstream
	git checkout master
	git merge upstream/master

preview_upstream:
	git difftool master upstream/master -y
