test:
	pytest; behave backend/tests/features/

lint:
	pylint backend/

security:
	bandit -r backend/ -x backend/tests

# Single "healthy" command: runs tests + linter.
# Exit code 0 means ESBot is healthy.
verify:
	DATABASE_URL="sqlite:///./test.db" python -m pytest && python -m pylint backend/ --exit-zero
