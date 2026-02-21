# Installation Guide

This guide covers different ways to install VNCalendar on your system.

## I. Requirements

- **Python**: >= 3.7
- **Operating System**: Windows, macOS, Linux
- **Dependencies**: None (VNCalendar has no external dependencies)

## II. Installation Methods

### Method 1: Install from PyPI

The easiest way to install VNCalendar is using pip:
```bash
pip install vncalendar
```

To install a specific version:
```bash
pip install vncalendar==1.0.1
```

To upgrade to the latest version:
```bash
pip install --upgrade vncalendar
```

### Method 2: Install from Source

If you want the latest development version or want to contribute:
```bash
# Clone the repository
git clone https://github.com/hoangdtung-2013/vncalendar.git
cd vncalendar

# Install in editable mode
pip install -e .
```

### Method 3: Install from GitHub Release

Download a specific release directly from GitHub:
```bash
pip install https://github.com/hoangdtung-2013/vncalendar/archive/refs/tags/v1.0.1.zip
```

## III. Virtual Environment (Recommended)

It's best practice to use a virtual environment:

### Using venv
```bash
# Create virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (macOS/Linux)
source venv/bin/activate

# Install VNCalendar
pip install vncalendar
```

### Using conda
```bash
# Create conda environment
conda create -n vncalendar python=3.9

# Activate environment
conda activate vncalendar

# Install VNCalendar
pip install vncalendar
```

## IV. Verify Installation

After installation, verify it's working correctly:
```python
# Open Python interpreter
python

# Try importing
>>> from vncalendar import VanSu, Date
>>> print(VanSu.CanChi.nam(2026))
Bính Ngọ
>>> exit()
```

Or run this one-liner in terminal:
```bash
python -c "from vncalendar import VanSu; print(VanSu.CanChi.nam(2026))"
```

Expected output: `Bính Ngọ`

## V. Troubleshooting

### pip not found

If you get `pip: command not found`:
```bash
# Try using python -m pip instead
python -m pip install vncalendar

# Or python3 on some systems
python3 -m pip install vncalendar

# Or py
py -m pip install vncalendar
```

### Permission Denied

If you get permission errors:
```bash
# Install for current user only
pip install --user vncalendar

# Or use sudo (Linux/macOS, not recommended)
sudo pip install vncalendar
```

### Multiple Python Versions

If you have multiple Python versions:
```bash
# Use specific Python version
python3.9 -m pip install vncalendar
```

### Installation Behind Proxy

If you're behind a corporate proxy:
```bash
pip install --proxy http://proxy.company.com:8080 vncalendar
```

### Offline Installation

If you don't have internet access:

1. Download the package on a machine with internet:
```bash
   pip download vncalendar
```

2. Transfer the `.whl` file to offline machine

3. Install from the file:
```bash
   pip install vncalendar-1.0.1-py3-none-any.whl
```

## VI. Uninstallation

To remove VNCalendar:
```bash
pip uninstall vncalendar
```

## VII. Checking Installed Version

To check which version you have installed:
```bash
pip show vncalendar
```

Or in Python:
```python
import vncalendar
print(vncalendar.__version__)  # If version is defined in __init__.py
```

## VIII. System Requirements

### Minimum Requirements
- Python 3.7+
- 10 MB disk space
- No additional libraries required

### Recommended
- Python 3.9 or higher
- Virtual environment for project isolation

## IX. Next Steps

- **Quick Start**: Learn basic usage → [Quick Start Guide](quickstart.md)
- **Examples**: See real-world usage → [Examples](examples.md)

## X. Getting Help

If you encounter any issues during installation:

1. Check the [FAQ](faq.md)
2. Search [existing issues](https://github.com/hoangdtung-2013/vncalendar/issues)
3. Open a [new issue](https://github.com/hoangdtung-2013/vncalendar/issues/new)
4. Email: hoangdtung2021@gmail.com