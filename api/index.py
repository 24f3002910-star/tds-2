from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response
import numpy as np
import json

app = FastAPI()

# Enable CORS for POST from any origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)

@app.get("/")
def root():
    return {"status": "ok"}

@app.options("/api/latency")
async def options_handler():
    return Response(status_code=200)

TELEMETRY_DATA = json.loads("""
[
  {
    "region": "apac",
    "service": "recommendations",
    "latency_ms": 221.94,
    "uptime_pct": 97.826,
    "timestamp": 20250301
  },
  {
    "region": "apac",
    "service": "support",
    "latency_ms": 209.66,
    "uptime_pct": 98.302,
    "timestamp": 20250302
  },
  {
    "region": "apac",
    "service": "recommendations",
    "latency_ms": 164.76,
    "uptime_pct": 98.001,
    "timestamp": 20250303
  },
  {
    "region": "apac",
    "service": "checkout",
    "latency_ms": 150.95,
    "uptime_pct": 97.827,
    "timestamp": 20250304
  },
  {
    "region": "apac",
    "service": "checkout",
    "latency_ms": 121.58,
    "uptime_pct": 97.259,
    "timestamp": 20250305
  },
  {
    "region": "apac",
    "service": "analytics",
    "latency_ms": 181.21,
    "uptime_pct": 99.489,
    "timestamp": 20250306
  },
  {
    "region": "apac",
    "service": "support",
    "latency_ms": 118.32,
    "uptime_pct": 98.476,
    "timestamp": 20250307
  },
  {
    "region": "apac",
    "service": "recommendations",
    "latency_ms": 142.38,
    "uptime_pct": 97.774,
    "timestamp": 20250308
  },
  {
    "region": "apac",
    "service": "catalog",
    "latency_ms": 231.56,
    "uptime_pct": 97.314,
    "timestamp": 20250309
  },
  {
    "region": "apac",
    "service": "checkout",
    "latency_ms": 203.12,
    "uptime_pct": 97.427,
    "timestamp": 20250310
  },
  {
    "region": "apac",
    "service": "support",
    "latency_ms": 165.96,
    "uptime_pct": 98.56,
    "timestamp": 20250311
  },
  {
    "region": "apac",
    "service": "catalog",
    "latency_ms": 120.17,
    "uptime_pct": 99.087,
    "timestamp": 20250312
  },
  {
    "region": "emea",
    "service": "payments",
    "latency_ms": 148.48,
    "uptime_pct": 99.3,
    "timestamp": 20250301
  },
  {
    "region": "emea",
    "service": "checkout",
    "latency_ms": 171.97,
    "uptime_pct": 97.895,
    "timestamp": 20250302
  },
  {
    "region": "emea",
    "service": "support",
    "latency_ms": 221.55,
    "uptime_pct": 97.122,
    "timestamp": 20250303
  },
  {
    "region": "emea",
    "service": "analytics",
    "latency_ms": 115.18,
    "uptime_pct": 98.258,
    "timestamp": 20250304
  },
  {
    "region": "emea",
    "service": "checkout",
    "latency_ms": 146.42,
    "uptime_pct": 99.21,
    "timestamp": 20250305
  },
  {
    "region": "emea",
    "service": "support",
    "latency_ms": 179.28,
    "uptime_pct": 98.58,
    "timestamp": 20250306
  },
  {
    "region": "emea",
    "service": "payments",
    "latency_ms": 151.45,
    "uptime_pct": 99.226,
    "timestamp": 20250307
  },
  {
    "region": "emea",
    "service": "analytics",
    "latency_ms": 187.55,
    "uptime_pct": 99.484,
    "timestamp": 20250308
  },
  {
    "region": "emea",
    "service": "analytics",
    "latency_ms": 108.84,
    "uptime_pct": 97.797,
    "timestamp": 20250309
  },
  {
    "region": "emea",
    "service": "payments",
    "latency_ms": 198.78,
    "uptime_pct": 98.07,
    "timestamp": 20250310
  },
  {
    "region": "emea",
    "service": "catalog",
    "latency_ms": 144.82,
    "uptime_pct": 97.127,
    "timestamp": 20250311
  },
  {
    "region": "emea",
    "service": "checkout",
    "latency_ms": 182.44,
    "uptime_pct": 98.153,
    "timestamp": 20250312
  },
  {
    "region": "amer",
    "service": "payments",
    "latency_ms": 188.57,
    "uptime_pct": 97.577,
    "timestamp": 20250301
  },
  {
    "region": "amer",
    "service": "support",
    "latency_ms": 130.67,
    "uptime_pct": 97.206,
    "timestamp": 20250302
  },
  {
    "region": "amer",
    "service": "catalog",
    "latency_ms": 188.92,
    "uptime_pct": 98.779,
    "timestamp": 20250303
  },
  {
    "region": "amer",
    "service": "support",
    "latency_ms": 157.07,
    "uptime_pct": 98.503,
    "timestamp": 20250304
  },
  {
    "region": "amer",
    "service": "checkout",
    "latency_ms": 226.7,
    "uptime_pct": 97.942,
    "timestamp": 20250305
  },
  {
    "region": "amer",
    "service": "recommendations",
    "latency_ms": 215.84,
    "uptime_pct": 97.742,
    "timestamp": 20250306
  },
  {
    "region": "amer",
    "service": "payments",
    "latency_ms": 148.46,
    "uptime_pct": 97.18,
    "timestamp": 20250307
  },
  {
    "region": "amer",
    "service": "analytics",
    "latency_ms": 140.5,
    "uptime_pct": 98.222,
    "timestamp": 20250308
  },
  {
    "region": "amer",
    "service": "checkout",
    "latency_ms": 129.37,
    "uptime_pct": 98.331,
    "timestamp": 20250309
  },
  {
    "region": "amer",
    "service": "recommendations",
    "latency_ms": 198.81,
    "uptime_pct": 97.29,
    "timestamp": 20250310
  },
  {
    "region": "amer",
    "service": "catalog",
    "latency_ms": 183.66,
    "uptime_pct": 98.817,
    "timestamp": 20250311
  },
  {
    "region": "amer",
    "service": "analytics",
    "latency_ms": 146.81,
    "uptime_pct": 98.504,
    "timestamp": 20250312
  }
]
""")

@app.post("/api/latency")
async def latency_analytics(request: Request):
    body = await request.json()
    regions = body.get("regions", [])
    threshold_ms = body.get("threshold_ms", 180)

    results = []
    for region in regions:
        records   = [r for r in TELEMETRY_DATA if r["region"] == region]
        latencies = [r["latency_ms"] for r in records]
        uptimes   = [r["uptime_pct"]  for r in records]
        results.append({
            "region":      region,
            "avg_latency": round(float(np.mean(latencies)), 2),
            "p95_latency": round(float(np.percentile(latencies, 95)), 2),
            "avg_uptime":  round(float(np.mean(uptimes)), 3),
            "breaches":    int(sum(1 for l in latencies if l > threshold_ms))
        })

    return {"regions": results}
