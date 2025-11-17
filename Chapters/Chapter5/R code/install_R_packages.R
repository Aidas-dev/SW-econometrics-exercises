# Install packages for econometrics project, jupyter notebook, and R kernel in RStudio
packages <- c("devtools", "repr", "IRdisplay", "pbdZMQ", "uuid", "IRkernel", "data.table", "tidyverse", "readODS", "conflicted")

# Install all packages with dependencies
install.packages(packages, dependencies = TRUE)

# Set up IRkernel for Jupyter
IRkernel::installspec(user = FALSE)

cat("Installation complete! Restart Jupyter and select R as kernel.\n")