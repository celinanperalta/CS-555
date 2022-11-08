install:
	pip3 install -r requirements.txt

run-tests:
	python3 -m pytest --no-header -v > tests.txt

run-demo:
	python src/main.py --file data/demo_sprint2.ged > output.txt

zip:
	zip -r Deliverable.zip output.txt tests.txt Team11Report.xlsx data/demo_sprint2.ged