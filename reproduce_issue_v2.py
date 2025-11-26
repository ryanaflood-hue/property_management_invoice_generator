import os
import sys

# Set the environment variable to simulate Vercel environment
os.environ["VERCEL"] = "1"

try:
    import invoice_generator
    print(f"OUTPUT_DIR: {invoice_generator.OUTPUT_DIR}")
    
    if invoice_generator.OUTPUT_DIR == "/tmp":
        print("SUCCESS: OUTPUT_DIR is correctly set to /tmp")
    else:
        print(f"FAILURE: OUTPUT_DIR is {invoice_generator.OUTPUT_DIR}, expected /tmp")
        sys.exit(1)

except Exception as e:
    print(f"An error occurred: {e}")
    sys.exit(1)
