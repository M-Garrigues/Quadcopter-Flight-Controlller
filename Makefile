pre:
	pre-commit run --all-files -c ./config/.pre-commit-config.yaml

lint:
	pylint --rcfile=config/.pylintrc quad-flight-controller
