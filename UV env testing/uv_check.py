# script.py
import sys
import platform

print("=" * 50)
print("UV Environment Test")
print("=" * 50)

# Check Python version
print(f"Python Version: {sys.version}")

# Check Python executable path
print(f"Python Path: {sys.executable}")

# Check if running in virtual environment
in_venv = sys.prefix != sys.base_prefix
print(f"In Virtual Environment: {in_venv}")

# Check virtual environment path
print(f"Virtual Env Path: {sys.prefix}")

# Check platform
print(f"Platform: {platform.system()} {platform.release()}")

print("=" * 50)
print("✓ UV environment is working!")
print("=" * 50)