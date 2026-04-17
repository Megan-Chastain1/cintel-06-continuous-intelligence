import numpy as np
import polars as pl


def generate_monitoring_data(total_requests=10000):
    requests = [f"{i:05d}" for i in range(1, total_requests + 1)]

    # 2. Generate Base Latency (random noise around 200ms)
    n = len(requests)
    latency = np.random.normal(200, 20, n)

    # 3. Inject a "Latency Spike" (e.g., a server overload on Wednesday)
    # Wednesday is roughly indices 4320 to 5760
    latency[4320:4600] += np.random.uniform(500, 1000, 280)

    # 4. Generate Errors (mostly 0, with spikes during latency)
    errors = np.random.choice([0, 1], size=n, p=[0.98, 0.02])
    errors[4320:4600] = np.random.choice([0, 1], size=280, p=[0.70, 0.30])

    # 5. Create Polars DataFrame
    df = pl.DataFrame({"requests": requests, "latency_ms": latency, "errors": errors})

    return df


# Save it for your Cintel project
df = generate_monitoring_data()
# Change the last part of your script to this:
df = generate_monitoring_data()

# The "data/" prefix tells Python to save it inside that specific folder
df.write_csv("data/new_data.csv")

print("Dataset generated and saved to: data/new_data.csv")
print("Dataset generated: 10,080 rows of monitoring data.")
