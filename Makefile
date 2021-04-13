merge_upstream:
	git fetch upstream
	git checkout master
	git merge upstream/master
