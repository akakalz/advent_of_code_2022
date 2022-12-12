default: clean build test

clean:
	find . -name '__pycache__' -delete -print \
		-o -name '*.pyc' -delete -print

run:
	python advent_of_code_2022/main.py

test:
	pytest
