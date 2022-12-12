default: clean build test

clean:
	find . -name '__pycache__' -delete -print \
		-o -name '*.pyc' -delete -print

build:
	docker build --target builder -t advent_build .

build-test:
	docker build --target tester -t advent_test .

run: build
	docker rm -f advent_2020 || echo "container removed"
	docker run --name advent_2020 advent_build
	docker rm -f advent_2020 || echo "container removed"

test: build-test
	docker rm -f advent_2020_test || echo "container removed"
	docker run --name advent_2020_test advent_test
	docker rm -f advent_2020_test || echo "container removed"
