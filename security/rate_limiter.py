import time
from collections import defaultdict

class SlidingWindowRateLimiter:
    """
    In-memory Rate Limiter using Sliding Window algorithm.
    Tracks timestamps of requests per client (IP or User ID).
    """
    def __init__(self, max_requests: int = 3, window_seconds: int = 2):
        self.max_requests = max_requests
        self.window_seconds = window_seconds
        # client_id -> list of float timestamps
        self.client_history = defaultdict(list)

    def is_allowed(self, client_id: str) -> bool:
        """
        Returns True if client has not exceeded max_requests in the last window_seconds.
        Otherwise returns False.
        """
        now = time.time()

        self.client_history[client_id] = [t for t in self.client_history[client_id] if now - t < self.window_seconds]

        if len(self.client_history[client_id]) < self.max_requests:
            self.client_history[client_id].append(now)
            return True

        else:
            return False


        # TODO: 1. self.client_history[client_id] me se wo saari purani timestamps filter kijiye
        #          jo window_seconds se purani ho chuki hain (i.e. now - t < self.window_seconds)

        # TODO: 2. Check kijiye: agar active timestamps ka count < self.max_requests hai:
        #          - current timestamp 'now' ko client_history[client_id] me append kijiye
        #          - return True

        # TODO: 3. Agar limit cross ho chuki hai:
        #          - return False
        pass


if __name__ == "__main__":
    limiter = SlidingWindowRateLimiter(max_requests=3, window_seconds=2)
    user_ip = "192.168.1.1"

    print("--- Burst Requests Test (Limit = 3 per 2s) ---")
    for i in range(1, 5):
        allowed = limiter.is_allowed(user_ip)
        status = "ALLOWED ✅" if allowed else "BLOCKED (429 Too Many Requests) 🛑"
        print(f"Request {i}: {status}")

    print("\n⏳ Sleeping 2.2 seconds for window to reset...")
    time.sleep(2.2)

    print("\n--- After Cooldown ---")
    allowed = limiter.is_allowed(user_ip)
    status = "ALLOWED ✅" if allowed else "BLOCKED 🛑"
    print(f"Request 5: {status}")

