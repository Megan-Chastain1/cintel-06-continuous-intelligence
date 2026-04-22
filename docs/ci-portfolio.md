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

### Insights

This analysis pulled out any value that existed above or below our set min and max reasonable values and saved them to a CSV. The code worked as expected.

## 3. Signal Design

### Repository Link

[(Signal Design Repository)](https://github.com/Megan-Chastain1/nlp-03-text-exploration)

### Signals

(List the custom signals you created and why.)

### Artifacts

(clickable link to artifacts/ folder and explain result files)

### Insights

(What did the signals reveal?)

## 4. Rolling Monitoring

### Repository Link

(clickable link to your repository)

### Techniques

(Explain how rolling windows were used.)

### Artifacts

(clickable link to artifacts/ folder and explain result files)

### Insights

(What patterns appeared?)

## 5. Drift Detection

### Repository Link

(clickable link to your repository)

### Techniques

(Explain how reference and current periods were compared.)

### Artifacts

(clickable link to artifacts/ folder and explain result files)

### Insights

(What changed? How do you know? How does this help make actionable decisions?)

## 6. Continuous Intelligence Pipeline

### Repository Link

(clickable link to your repository)

### Techniques

(Describe how signals and monitoring techniques were combined.)

### Artifacts

(clickable link to artifacts/ folder and explain result files)

### Assessment

(What does the pipeline say about the system state?)
