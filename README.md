# SW-econometrics-exercises
This is repository holds completed empirical exercises from "Introduction to Econometrics, 4th Edition" by Stock and Watson.
# Jupyter Notebook Configuration

To enable automatic output window sizing, you need to configure Jupyter to use the provided configuration file. Choose one of these methods:

## Option 1: Copy config file
```bash
mkdir -p ~/.jupyter
cp config/jupyter_notebook_config.py ~/.jupyter/
```

## Option 2: Use config flag
Start Jupyter with:
```bash
jupyter notebook --config=config/jupyter_notebook_config.py
```

The configuration includes:
- Automatic output window resizing
- Increased rate limits for larger outputs
- Always-on auto-scrolling