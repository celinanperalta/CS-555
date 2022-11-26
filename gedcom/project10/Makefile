PYTHONEX := python
PYTHON3EX := python3
PIPEX := pip3


install:
	$(PIPEX) install -r requirements.txt

run-tests:
	$(PYTHON3EX) -m pytest --no-header -v > tests.txt

run-demo:
	$(PYTHONEX) src/main.py --file data/demo_sprint2.ged

zip:
	zip -r Deliverable.zip output.txt tests.txt Team11Report.xlsx data/demo_sprint2.ged