import os
import sys
from unittest.mock import patch

# Mock os.makedirs to raise OSError for the first call (simulating read-only)
# and succeed for the second call (simulating /tmp)
original_makedirs = os.makedirs

def mock_makedirs(path, exist_ok=False):
    if "generated_invoices" in path and "/tmp" not in path:
        raise OSError("Read-only file system")
    return original_makedirs(path, exist_ok=exist_ok)

with patch("os.makedirs", side_effect=mock_makedirs):
    try:
        # Reload the module to trigger the top-level code execution
        if "invoice_generator" in sys.modules:
            del sys.modules["invoice_generator"]
        import invoice_generator
        
        print(f"OUTPUT_DIR: {invoice_generator.OUTPUT_DIR}")
        
        if invoice_generator.OUTPUT_DIR == "/tmp":
            print("SUCCESS: OUTPUT_DIR fell back to /tmp")
        else:
            print(f"FAILURE: OUTPUT_DIR is {invoice_generator.OUTPUT_DIR}, expected /tmp")
            sys.exit(1)

    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)
