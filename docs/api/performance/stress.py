from locust import HttpUser, LoadTestShape, between, task

class ESBotUser(HttpUser):
    wait_time = between(0.5, 2.0)

    def on_start(self):
        resp = self.client.post("/api/v1/sessions", name="POST /sessions (setup)")
        self.session_id = resp.json().get("id") if resp.status_code == 201 else None

    def on_stop(self):
        if self.session_id:
            self.client.delete(f"/api/v1/sessions/{self.session_id}", name="DELETE /sessions (teardown)")

    @task(4)
    def health(self):
        self.client.get("/api/v1/health", name="GET /health")

    @task(3)
    def list_sessions(self):
        self.client.get("/api/v1/sessions", name="GET /sessions")

    @task(3)
    def get_messages(self):
        if self.session_id:
            self.client.get(f"/api/v1/sessions/{self.session_id}/messages", name="GET /sessions/:id/messages")


class StressShape(LoadTestShape):
    # step up every 2 min: 50 -> 100 -> 150 -> 200 -> 250 virtual users
    stages = [
        {"duration": 120, "users": 50,  "spawn_rate": 5},
        {"duration": 240, "users": 100, "spawn_rate": 5},
        {"duration": 360, "users": 150, "spawn_rate": 5},
        {"duration": 480, "users": 200, "spawn_rate": 5},
        {"duration": 600, "users": 250, "spawn_rate": 5},
    ]

    def tick(self):
        t = self.get_run_time()
        for s in self.stages:
            if t < s["duration"]:
                return s["users"], s["spawn_rate"]
        return None

"""
Tool Used: Claude Opus 4.7
Purpose: Translating test plans into locust syntax.
"""