# Continuous Intelligence Portfolio

Megan Chastain

2026-04

This page summarizes my work on **continuous intelligence** projects.

## 1. Professional Project

### Repository Link

[(Github repository)](https://github.com/Megan-Chastain1/cintel-06-continuous-intelligence)

### Brief Overview of Project Tools and Choices

## 2. Anomaly Detection

### Repository Link

[(Anomoly detection repository)](https://github.com/Megan-Chastain1/cintel-02-static-anomalies)

### Techniques

To detect anomalies, a threshold code was written to define the maximum and minimum reasonable values(1). Next, a code was written to detect any value above the maximum or below the minimum(2). The values detected as anomalies were saved in a CSV file in a folder labeled "Artifacts"(3).

1.  # x is age in years, so 18 is the lower limit for adults
    MIN_REASONABLE_X_VALUE: Final[float] = 18.0

    # y is height in inches, so maybe 6 feet (72 inches) is a reasonable upper limit
    MAX_REASONABLE_Y_VALUE: Final[float] = 72.0

2. anomalies_df: pl.DataFrame = df.filter(
        (pl.col("age_years") < MIN_REASONABLE_X_VALUE)

        | (pl.col("height_inches") >= MAX_REASONABLE_Y_VALUE)
    )

3. anomalies_df.write_csv(OUTPUT_FILE)
    LOG.info(f"Wrote anomalies file: {OUTPUT_FILE}")

### Artifacts

[Results)](https://github.com/Megan-Chastain1/cintel-02-static-anomalies/tree/main/artifacts)

The results show heights above the max threshold of 72 inches or an age less than 18 years old.

### Insights

This analysis pulled out any value that existed above or below our set min and max reasonable values and saved them to a CSV. The code worked as expected.

## 3. Signal Design

### Repository Link

[(Signal Design Repository)](https://github.com/Megan-Chastain1/cintel-03-signal-design)

### Signals

The signals used for this project were error rate and average latency.

Error rate was calulated by taking the data point in the 'errors' column and dividing it by it's corresponding value in the 'requests' column (1). Then a code was written to create a new column for 'error_rates'(2). Error rate was used because the project was looking at requests to a system and the errors were the requests that failed to go through. This is a good signal because it showed if the system was reliable.

Average latency was calculated by taking a data point in the 'total_latency_ms' column and dividing it with the corresponding value in the 'requests' column (3). Then a code was written to create a new column for 'average_latency'(4). Average latency was used because it tells how long it takes for a system to respond to a request.


1.  calculated_error_rate: pl.Expr = pl.col("errors") / pl.col("requests")

2.  error_rate_signal_recipe: pl.Expr = (
        pl.when(is_requests_positive)
        .then(calculated_error_rate)
        .otherwise(0.0)
        .alias("error_rate")
    )

3. calculated_avg_latency: pl.Expr = pl.col("total_latency_ms") / pl.col("requests")

4. avg_latency_signal_recipe: pl.Expr = (
        pl.when(is_requests_positive)
        .then(calculated_avg_latency)
        .otherwise(0.0)
        .alias("avg_latency_ms")
    )

### Artifacts

[(Results)](https://github.com/Megan-Chastain1/cintel-03-signal-design/tree/main/artifacts)

The results show a CSV file with the added columns and the calculated values of each row.

### Insights

These signals were great to use, however without a threshold they don't show much.

## 4. Rolling Monitoring

### Repository Link

[(Rolling Monitoring Repository)](https://github.com/Megan-Chastain1/cintel-04-rolling-monitoring)

### Techniques

Rolling windows monitor series data by calculating a statistic of an interval of rows, adding one row to the statistic at a time.

For a rolling window computing mean with an interval of 3 you'd get:

row 1 → mean of [1]
row 2 → mean of [1,2]
row 3 → mean of [1,2,3]
row 4 → mean of [2,3,4]

This is useful to see how a system is changing over time.

### Artifacts

[(Results)](https://github.com/Megan-Chastain1/cintel-04-rolling-monitoring/tree/main/artifacts)

As seen in the results, using mean as the statistic, the values change as different rows are included in the calulations.

### Insights

For the dataset used, patterns that formed are when mean rolling requests are high, the error rate rolling mean and the latency rolling mean are also high, indicating a positive relationshhip between them.

## 5. Drift Detection

### Repository Link

[Drift Detection Repository](https://github.com/Megan-Chastain1/cintel-05-drift-detection)

### Techniques

Dirft was determined by first setting a threshold for the signals being used (1). Then the average was calculated for historic (reference) and current data (2). The data points were combined into one table. Then the difference was taken between the historic and current data (3). Drift flags were added to check to see if the difference exceed a set threshold (4). The flags generate true/false values. If drift is occuring the value generated is 'true'.


1. REQUESTS_DRIFT_THRESHOLD: Final[float] = 10.0
   ERRORS_DRIFT_THRESHOLD: Final[float] = 5.0
   LATENCY_DRIFT_THRESHOLD: Final[float] = 1000.0

2.   reference_summary_df = reference_df.select(
        [
            pl.col("requests").mean().alias("reference_avg_requests"),
            pl.col("errors").mean().alias("reference_avg_errors"),
            pl.col("total_latency_ms").mean().alias("reference_avg_latency_ms"),
        ]
    )

    current_summary_df = current_df.select(
        [
            pl.col("requests").mean().alias("current_avg_requests"),
            pl.col("errors").mean().alias("current_avg_errors"),
            pl.col("total_latency_ms").mean().alias("current_avg_latency_ms"),
        ]
    )

3. requests_mean_difference_recipe: pl.Expr = (
        (pl.col("current_avg_requests") - pl.col("reference_avg_requests"))
        .round(2)
        .alias("requests_mean_difference")
    )

    errors_mean_difference_recipe: pl.Expr = (
        (pl.col("current_avg_errors") - pl.col("reference_avg_errors"))
        .round(2)
        .alias("errors_mean_difference")
    )

    latency_mean_difference_recipe: pl.Expr = (
        (pl.col("current_avg_latency_ms") - pl.col("reference_avg_latency_ms"))
        .round(2)
        .alias("latency_mean_difference_ms")
    )

4. requests_is_drifting_flag_recipe: pl.Expr = (
        pl.col("requests_mean_difference").abs() > REQUESTS_DRIFT_THRESHOLD
    ).alias("requests_is_drifting_flag")

    errors_is_drifting_flag_recipe: pl.Expr = (
        pl.col("errors_mean_difference").abs() > ERRORS_DRIFT_THRESHOLD
    ).alias("errors_is_drifting_flag")

    latency_is_drifting_flag_recipe: pl.Expr = (
        pl.col("latency_mean_difference_ms").abs() > LATENCY_DRIFT_THRESHOLD
    ).alias("latency_is_drifting_flag")



### Artifacts

[Results](https://github.com/Megan-Chastain1/cintel-05-drift-detection/tree/main/artifacts)

The results for this dataset generate values of 'true' for all drift flags, meaning drift is occuring for all tested statistics.

### Insights

Being able to detect dirft, and where drift is occuring, is essential to knowing what issues are happening in a system and where fixes should be applied. If no drift is occuring, the system is stable and working as it should.

## 6. Continuous Intelligence Pipeline

### Repository Link

[Continuous Intelligence Pipeline Repository](https://github.com/Megan-Chastain1/cintel-06-continuous-intelligence)

### Techniques

This project implemented signals, anomalies, and drift detection to determine if a system was stable or needed fixing.

Signals were determined (latency and error rate) and thersholds were set(1). Then a simple drift detection code was added. The pipeline then executed the code and the results were saved in a CSV file. The results could be 'stable', 'degraded', or 'failure'(2).

1. MAX_ERROR_RATE: Final[float] = 0.05
   MAX_AVG_LATENCY: Final[float] = 40.0

2. summary_df = summary_df.with_columns(
        pl.when(
            (pl.col("avg_error_rate") > MAX_ERROR_RATE)
            | (pl.col("avg_latency_ms") > MAX_AVG_LATENCY)
        )
        .then(pl.lit("DEGRADED"))
        .otherwise(pl.lit("STABLE"))
        .alias("system_state")
    )

### Artifacts

[Results](https://github.com/Megan-Chastain1/cintel-06-continuous-intelligence/tree/main/artifacts)

The result of the system is stable for the signals looked at.

### Assessment

This system is stable based on the thresholds deteremined for the signals selected.
