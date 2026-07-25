import asyncio
import json
import random
import time
import websockets

# 1. Mock Data Generator (Simulating iRacing / Assetto Corsa)
def generate_mock_telemetry():
    return {
        "timestamp": time.time(),
        "speed_kmh": round(random.uniform(120.0, 240.0), 2),
        "rpm": random.randint(4000, 8000),
        "gear": random.randint(3, 6),
        "lap": 2,
        "throttle": round(random.uniform(0.5, 1.0), 2)
    }

# 2. Async Broadcaster & Logger Core
class TelemetryBridge:
    def __init__(self):
        self.connected_clients = set()

    async def register(self, websocket):
        self.connected_clients.add(websocket)
        try:
            await websocket.wait_closed()
        finally:
            self.connected_clients.remove(websocket)

    async def broadcast_loop(self):
        print("Telemetry Bridge Active. Streaming at 60Hz...")
        while True:
            # Native simulator frequency simulation (e.g., high speed)
            raw_data = generate_mock_telemetry()
            
            # Simulated High-Frequency Historic Log (Parquet/CSV dump logic would go here)
            # self.log_to_file(raw_data) 

            # Throttled Live Stream to 60Hz (~0.016 seconds interval)
            if self.connected_clients:
                message = json.dumps(raw_data)
                websockets.broadcast(self.connected_clients, message)
                
            await asyncio.sleep(1 / 60) 

# 3. Main Server Execution
async def main():
    bridge = TelemetryBridge()
    async with websockets.serve(bridge.register, "localhost", 8765):
        await bridge.broadcast_loop()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nBridge stopped cleanly.")
