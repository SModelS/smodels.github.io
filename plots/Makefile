all: copy

copy: .PHONY
	cp ../../smodels-utils/covariances/com*png .
	./mkPage.py
	git add --all .
	git commit -m 'automated update'
	git push

.PHONY:
