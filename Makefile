install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv --cov=main --cov=mylib test_*.py

format:	
	black *.py mylib/*.py

lint:
	pylint --disable=R,C --extension-pkg-whitelist='pydantic' main.py --ignore-patterns=test_.*?py *.py  mylib/*.py

container-lint:
	docker run --rm -i hadolint/hadolint < Dockerfile

refactor: format lint

deploy:
	aws ecr get-login-password --region eu-west-2 | docker login --username AWS --password-stdin 927430616036.dkr.ecr.eu-west-2.amazonaws.com
	docker build -t logistics .
	docker tag logistics:latest 927430616036.dkr.ecr.eu-west-2.amazonaws.com/logistics:latest
	docker push 927430616036.dkr.ecr.eu-west-2.amazonaws.com/logistics:latest
		
		
all: install lint test format deploy