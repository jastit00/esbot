# Backend

## Dependencies
1. Docker
2. VSCode
3. Dev Containers extension

## Run
1. Press `Ctrl+Shift+P`.
2. Run `Dev Containers: Reopen in Container`.
3. Wait for the container build and setup to finish.
4. Start the backend server:

```bash
uvicorn backend.app:app --reload --host 0.0.0.0 --port 8000
```

The API will then be available at `http://localhost:8000`.
