# Fast Clicker Script

This script is designed to automate and optimize clicking tasks, ideal for scenarios where fast clicking is required. The script can simulate a mouse click at high speeds at a precise time.

## Features

- **High-Speed Clicking**: Simulates a mouse click at a high speed at a precise time.

## Prerequisites

- Python 3.11
- miniconda or anaconda

---

## Installation

1. Clone this repository:

   ```bash
   https://github.com/alipe1998/fast_clicker.git
   ```

2. Navigate to the project directory:

   ```bash
   cd fast_clicker
   ```

3. Install the required Python libraries:

   ```bash
   conda env create -f environments.yml
   ```

---

## Usage and Configuration

- **--time**: Specify the time to click in HH:MM:SS format. For example, `--time 9:00:00` will click at 9:00:00 AM.
- **--timezone**: Sets the timezone for the specified time. For example, `--timezone US/Eastern` will use US Eastern Time. Default is US Central Time.

---

## Example

Here is an example of how to run the script to click at 9:00:00 AM US Central Time:


```bash
python fast_clicker.py --time 9:00:00
```


