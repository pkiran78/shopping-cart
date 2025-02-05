####################################################################################################
# Author: Kiran Patil
# Author Email: pkiran78@gmail.com
####################################################################################################

PROJECT_NAME  = shopping-cart
PROJECT_PATH  = pkiran78
.PHONY: help clean help dependencies lint image distribute bandit format

help:
	@echo "Use 'make <target>' where <target> is one of"
	@echo ""
	@echo "--------------------------------------------------------------------"
	@echo "                        Development tools                           "
	@echo "--------------------------------------------------------------------"
	@echo " bandit               Run security check"
	@echo " format               Format the code with black"
	@echo " lint                 run flake8 and markdown lint"
	@echo " dependencies         install all dependencies"
	@echo " clean                remove development directories"
	@echo ""
	@echo "--------------------------------------------------------------------"
	@echo "                        Container image                             "
	@echo "--------------------------------------------------------------------"
	@echo " image                build docker container image"
	@echo " distribute           Distribute the container image to artifactory"
	@echo ""

clean:
	@echo ""
	@echo "--------------------------------------------------------------------"
	@echo "Removing *.pyc *.c and __pycache__/ files"
	@find . -type f -name "*.pyc" | xargs rm -vrf
	@find . -type d -name "__pycache__" | xargs rm -vrf
	@rm -rf banditreport.html
	@echo ""
	@echo "Done."
	@echo ""

dependencies:
	@echo "--------------------------------------------------------------------"
	@echo "Installing dependencies"
	@pip3 install -r requirements.txt

lint:
	@echo ""
	@echo "Running linters"
	@flake8 --exit-zero --max-line-length 100
	@echo

image:
	@echo ""
	@echo "--------------------------------------------------------------------"
	@echo "Building docker image"
	@docker build -t $(PROJECT_PATH)$(PROJECT_NAME):latest -f Dockerfile .
	@echo ""
	@echo "Done."
	@echo ""

distribute: image
	@echo ""
	@echo "--------------------------------------------------------------------"
	@echo "Distribute the docker image to Docker hub"
	@docker push $(PROJECT_PATH)$(PROJECT_NAME):latest
	@echo ""

bandit:
	@echo ""
	@echo "--------------------------------------------------------------------"
	@echo "Running Bandit"
	@bandit -r . -f html -o banditreport.html  --configfile .bandit.yaml
	@echo ""

format:
	@echo ""
	@echo "--------------------------------------------------------------------"
	@echo "Formating the code"
	@black -l 100 .
	@echo ""
