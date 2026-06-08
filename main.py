import threading
import time

from capture import start_capture
from dashboard import show_dashboard
from rich_dashboard import show_rich_dashboard
from reports import generate_csv_report

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
show_rich_dashboard()
generate_csv_report()