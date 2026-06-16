# Performance Test Report

## 1. Tool
**Locust** was chosen as the load testing tool. It is Python-native and integrates well with the FastAPI stack, supports headless execution, scriptable test profiles and generates HTML reports. Full reports are available in `docs/api/performance/reports/`.

## 2. Test Environment

| Item | Value |
|------|-------|
| Machine | Windows 11 IoT Enterprise LTSC, AMD Ryzen 9 9950X3D, 64 GB RAM |
| OS (Locust) | WSL2 Ubuntu 24.04.4 LTS |
| OS (Backend) | Ubuntu 22.04 (devcontainer) |
| Backend | FastAPI + Uvicorn, 1 worker (devcontainer) |
| Database | PostgreSQL 16 (devcontainer) |
| Note | Locust ran on WSL2 host, backend in devcontainer |

## 3. Results

### Smoke Test - 2 VUs, 30 s

```bash
~/.locust-venv/bin/locust -f smoke.py --headless --host http://localhost:8000 --html reports/smoke_report.html
```

| Metric | Value |
|--------|-------|
| Throughput (RPS) | 1.79 |
| Average response time | 6.01 ms |
| P90 / P95 / P99 | 10 ms / 38 ms / 50 ms |
| Error rate | 0 % |
| Peak concurrency reached | 2 VUs |

**Pass criteria:** all 2xx, response time < 1 s 
**Result: Pass**

---

### Load Test - 50 VUs, 60 s ramp-up, 5 min sustained

```bash
~/.locust-venv/bin/locust -f load.py --headless --host http://localhost:8000 --html reports/load_report.html
```

| Metric | Value |
|--------|-------|
| Throughput (RPS) | 39.84 |
| Average response time | 2.82 ms |
| P90 / P95 / P99 | 3 ms / 4 ms / 6 ms |
| Error rate | 0 % |
| Peak concurrency reached | 50 VUs |

**Pass criteria:** P95 ≤ 2 s, error rate < 1 % 
**Result: Pass**

---

### Stress Test - 50 -> 250 VUs, step-load over 10 min

```bash
~/.locust-venv/bin/locust -f stress.py --headless --host http://localhost:8000 --html reports/stress_report.html
```

| Metric | Value |
|--------|-------|
| Throughput (RPS) | 125.95 |
| Average response time | 6 ms |
| P90 / P95 / P99 | 5 ms / 7 ms / 47 ms |
| Error rate | 0.01 % |
| Peak concurrency reached | 250 VUs |

**Breaking point:** Not reached within 250 VUs: error rate stayed at 0.01% across all stages. 4 `RemoteDisconnected` errors observed at peak load.  
**Throughput ceiling:** ~126 RPS at 250 VUs.

## 4. Interpretation

**NFR:** up to 50 concurrent users, response time 2-5 s under normal load.

The load test passed well within the NFR. No breaking point was reached during the stress test; the backend handled 250 VUs with only 4 connection errors (0.01 %).

## 5. Recommendations

1. Change `GET /api/v1/sessions`: returning all sessions will slow down as the database grows.
2. Run Uvicorn with multiple workers (`--workers 4`) to improve throughput.
