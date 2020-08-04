.PHONY: test
test:
	pytest py --cov=pandas_pbf

.PHONY: testcov
testcov: test
	@echo "building coverage html"
	@coverage html

.PHONY: mypy
mypy:
	mypy py/pandas_pbf
