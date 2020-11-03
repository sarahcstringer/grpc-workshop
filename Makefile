lint:
	@echo "Running isort and black"
	@find . -name "*.py" ! -name "*_pb2*" ! -path "./venv/*" -exec isort {} \+ -exec black {} \+

setup:
	@bash scripts/install.sh
	@echo "Checking setup"
	@bash scripts/check-setup.sh
