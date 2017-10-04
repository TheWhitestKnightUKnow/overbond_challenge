yield:
	python yield.py $(filter-out $@,$(MAKECMDGOALS))

curve:
	python curve.py $(filter-out $@,$(MAKECMDGOALS))

test all: test1 test2 test3 test4 test5
	

test1:
	python yield.py sample1.csv
	python curve.py sample1.csv

test2:
	python yield.py sample2.csv
	python curve.py sample2.csv

test3:
	python yield.py sample3.csv
	python curve.py sample3.csv

test4:
	python yield.py sample4.csv
	python curve.py sample4.csv

test5:
	python yield.py sample5.csv
	python curve.py sample5.csv