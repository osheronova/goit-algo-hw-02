import queue
import time
from itertools import count

# Request queue
application_queue = queue.Queue()

# Unique ID counter
request_id_counter = count(1)


def generate_request(q: queue.Queue) -> None:
    """Create a new request and add it to the queue."""
    request_id = next(request_id_counter)
    print(f"Created request: {request_id}")
    q.put(request_id)


def process_request(q: queue.Queue) -> None:
    """Process one request from the queue."""
    if not q.empty():
        request_id = q.get()
        print(f"Processing request: {request_id}")
    else:
        print("Queue is empty")


def main(delay: float = 1.0) -> None:
    """Main loop: create and process requests."""
    try:
        while True:
            generate_request(application_queue)
            process_request(application_queue)
            time.sleep(delay)
    except KeyboardInterrupt:
        print("\nExiting program.")


if __name__ == "__main__":
    main()
