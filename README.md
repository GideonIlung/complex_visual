### Prerequisites

Before installing `complex-visual`, ensure you have the following:

- Python 3.6 or later
- pip (Python package installer)

You can check your Python version by running:

```bash
python --version
```

And check if `pip` is installed using:

```bash
pip --version
```

### Installing from PyPI

If `complex-visual` is available on the Python Package Index (PyPI), you can install it using `pip`:

```bash
pip install complex-visual
```

This command will download and install the `complex-visual` package along with its dependencies.

### Installing from GitHub

To install the package directly from the GitHub repository, run:

```bash
pip install git+https://github.com/GideonIlung/complex_visual.git
```

This will install the latest version of the package from the repository. If you want to install a specific version, branch, or commit, you can append an `@` symbol followed by the branch name, tag, or commit hash:

```bash
pip install git+https://github.com/GideonIlung/complex_visual.git@main
```

### Verifying Installation

After installation, you can verify that the package was installed correctly by running:

```bash
pip list | grep complex-visual
```

You should see `complex-visual` and its version in the output.

### Updating the Package

To update `complex-visual` to the latest version, run:

```bash
pip install --upgrade complex-visual
```

### Usage

Below is an example of using the script in order to visualise complex functions

```python
import complex_visual as cv
import numpy as np


phi = lambda t: [t*np.cos(t),(t**2)*np.sin(t)]
f = lambda z: 1/z
cv.curve_plot(f,phi,a=-10,b=10)

```