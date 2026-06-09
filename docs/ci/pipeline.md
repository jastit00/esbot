
## CI configuration explanation 

### Triggers
```yaml
on:
  push:
  pull_request:
```

The ci workflow is triggered on every push and every pull request, because we use working branches for each assignment. Consequently the code needs to be tested on each push to that branch. On pull requests the code is tested again on merge.

Workflow dispatches for manual runs are not implemented, because for this rare case the few commands can be executed manually.


### Runner
```yaml
runs-on: ubuntu-latest
```

Ubuntu-latest was the recommended one which is a standard linux distribution, free for use and well maintained.


### Environment
```yaml
- name: Set up Python
  uses: actions/setup-python@v6
  with:
    python-version: '3.12'
```

Our ESBot project uses Python 3.12, which is configured in the backend setup. 
The 6th version (`actions/setup-python@v6`) is the newest and also compatible version for the python setup.


### Jobs and steps
```yaml
- name: Install dependencies
  run: |
    python -m pip install --upgrade pip
    pip install -r requirements.txt
    pip install pylint
- name: Run Unit tests
  run: |
    DATABASE_URL="sqlite:///./test.db" python -m pytest
- name: Run static analysis
  run: |
    python -m pylint backend/
```

First the dependencies are installed with `pip install -r requirements.txt` (also `pylint` is installed). 
Then the unit tests are run with `DATABASE_URL="sqlite:///./test.db" python -m pytest` with a SQL in-memory database.
Finally the static analysis is run with `python -m pylint backend/`.

Intentionally out of CI is the live LLM, because it doesn't make sense to use such dependency in a CI workflow. Also the production DB is not used in CI to seperate concerns.


### Parity with local

The locally executed commands from phase A are directly mapped to the CI steps.

When CI fails locally but passes on GitHub (or vice versa):
- the python version should be the same
- the environment should be the same or not needed for the run
- the same codebase should be used
