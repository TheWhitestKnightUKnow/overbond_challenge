yield:
	python yield.py $(filter-out $@,$(MAKECMDGOALS))

curve:
	python curve.py $(filter-out $@,$(MAKECMDGOALS))

test all: test1 test2 test3 test4 test5
	

test yield 1:
    python yield.py sample1.csv

test curve 1:
    python curve.py sample1.csv

test yield 2:
    python yield.py sample2.csv

test curve 2:
    python curve.py sample2.csv

test yield 3:
    python yield.py sample3.csv

test curve 3:
    python curve.py sample3.csv

test yield 4:
    python yield.py sample4.csv

test curve 4:
    python curve.py sample4.csv

test yield 5:
    python yield.py sample5.csv

test curve 5:
    python curve.py sample5.csv
