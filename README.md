# Port Scanner

This is a simple Python script that scans for open ports on a specified website. It retrieves the IP address of the website and checks which ports are open within a specified range.

## Requirements

- Python 3.x
- `socket` and `logging` modules (included in the Python standard library)

## Installation

1. Clone the repository or download the script file.
2. Ensure you have Python 3.x installed on your machine.

## Usage

1. Open the script file (`script.py`) in a text editor.
2. Modify the `website_url` variable to the target website you want to scan. For example:
   ```python
   website_url = "example.com"
   ```
3. Run the script from the command line:
   ```bash
   python script.py
   ```

## Output

- The script will log the IP address of the specified website.
- It will then scan ports from 1 to 1024 and log which ports are open.

## Example

To scan the website `example.com`, simply set:
