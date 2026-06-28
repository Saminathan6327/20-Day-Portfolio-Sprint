# 1. Install and load ggplot2 automatically if missing
if (!require(ggplot2)) {
  install.packages("ggplot2", repos = "http://cran.us.r-project.org")
  library(ggplot2)
}

print("Loading dataset...")
# 2. Read the CSV data
data <- read.csv("tech_salaries.csv")

print("Generating visualization...")
# 3. Create a dynamic scatter plot with a trend line
salary_plot <- ggplot(data, aes(x = Experience_Years, y = Salary_USD, color = Department)) +
  geom_point(size = 4, alpha = 0.8) +
  geom_smooth(method = "lm", se = FALSE, linetype = "dashed", color = "darkgray") +
  scale_y_continuous(labels = scales::dollar_format()) +
  labs(
    title = "Tech Salaries vs. Years of Experience",
    subtitle = "Analysis across Data, Engineering, and Product departments",
    x = "Years of Experience",
    y = "Annual Salary (USD)",
    color = "Department"
  ) +
  theme_minimal() +
  theme(
    plot.title = element_text(face = "bold", size = 16),
    legend.position = "bottom"
  )

# 4. Export the visualization to a PNG file
output_filename <- "salary_analysis_report.png"
ggsave(output_filename, plot = salary_plot, width = 8, height = 5, dpi = 300)

print(paste("✅ Success! Visualization saved as", output_filename))