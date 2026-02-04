import pandas as pd

# Load dataset
df = pd.read_csv("../data/sales_pipeline.csv")

print("Columns in dataset:\n", df.columns)

# Clean Probability column (remove % and convert to float)
df["Probability"] = df["Probability"].str.replace("%", "").astype(float)

# Total number of deals
total_deals = len(df)

# Average deal size
avg_deal_size = df["Deal size"].mean()

# Average probability
avg_probability = df["Probability"].mean()

# Deals by sales stage
stage_distribution = df["Sales stage"].value_counts()

# Average deal size by stage
avg_deal_by_stage = df.groupby("Sales stage")["Deal size"].mean()

# Performance by sales channel
channel_performance = df.groupby("Sales Channel")["Deal size"].sum()

# Country-wise deal value
country_performance = df.groupby("Country")["Deal size"].sum()

print("\n--- Sales Pipeline Analysis Results ---")
print("Total Deals:", total_deals)
print("Average Deal Size:", avg_deal_size)
print("Average Probability of Closing:", avg_probability)

print("\nDeals by Sales Stage:\n", stage_distribution)
print("\nAverage Deal Size by Stage:\n", avg_deal_by_stage)
print("\nTotal Deal Value by Sales Channel:\n", channel_performance)
print("\nTotal Deal Value by Country:\n", country_performance)

# Save results to file
with open("../output/results.txt", "w") as f:
    f.write(f"Total Deals: {total_deals}\n")
    f.write(f"Average Deal Size: {avg_deal_size}\n")
    f.write(f"Average Probability of Closing: {avg_probability}\n\n")
    f.write("Deals by Sales Stage:\n")
    f.write(stage_distribution.to_string())
    f.write("\n\nAverage Deal Size by Stage:\n")
    f.write(avg_deal_by_stage.to_string())
    f.write("\n\nTotal Deal Value by Sales Channel:\n")
    f.write(channel_performance.to_string())
    f.write("\n\nTotal Deal Value by Country:\n")
    f.write(country_performance.to_string())
