test:
	pytest; behave backend/tests/features/

lint:
	pylint backend/

security:
	bandit -r backend/ -x backend/tests
