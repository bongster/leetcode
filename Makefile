prerequirements:
	python3 -m venv venv
	. venv/bin/activate
	pip3 install -r req.txt


sync: prerequirements
	. venv/bin/activate; python3 leetcode_generate.py

clean:
	rm -rf venv
