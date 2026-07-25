# Motorsports Telemetry Bridge (PoC)
A lightweight Python prototype demonstrating async telemetry capture and streaming.

## Features
- **Asyncio Loop**: Prevents UI/main thread blocking during high-frequency data ingestion.
- **60Hz Throttled Broadcast**: Built using `websockets` for downstream front-end clients.
- **Mock Engine**: Simulated telemetry generator for headless testing environment.
