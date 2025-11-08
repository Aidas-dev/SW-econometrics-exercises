# Jupyter Notebook configuration with R support
# This config provides R kernel support and automatic output sizing

c = get_config()

# Set high rate limits to allow for larger outputs
c.NotebookApp.iopub_data_rate_limit = 10000000  # 10MB/sec
c.NotebookApp.iopub_msg_rate_limit = 1000       # 1000 messages/sec

# Configure output area to auto-size
c.OutputArea.auto_scroll_threshold = 9999       # Always auto-scroll
c.OutputArea.max_output_size = 100000           # 100KB max output size
c.OutputArea.auto_resize_height = True          # Auto-resize height to content

# Enable all notebook extensions
c.NotebookApp.nbserver_extensions = {
    'jupyterlab': True
}

# R kernel configuration
c.KernelSpecManager.ensure_native_kernel = False  # Allow non-Python kernels
c.MultiKernelManager.default_kernel_name = 'python3'  # Default to Python
