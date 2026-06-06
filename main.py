import threading
import time

from capture import start_capture
from dashboard import show_dashboard

# Start packet capture in background
threading.Thread(
    target=start_capture,
    daemon=True
).start()

print("Capturing packets for 20 seconds...")

# Give analyzer time to collect data
time.sleep(20)

# Now show graphs
show_dashboard()