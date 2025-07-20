#!/usr/bin/env python3
"""
Example script to run the VC Agent Framework with a specific industry
"""

import subprocess
import sys
import os

def main():
    """Run the VC Agent Framework with a specific industry"""
    # Default industry
    industry = "artificial intelligence"
    
    # Check if an industry was provided as a command-line argument
    if len(sys.argv) > 1:
        industry = sys.argv[1]
    
    print(f"Running VC Agent Framework for industry: {industry}")
    
    # Check if Ollama is installed and running
    try:
        # Try to connect to Ollama server
        import requests
        requests.get("http://localhost:11434/api/tags")
        print("✅ Ollama server is running")
    except:
        print("❌ Ollama server is not running or not installed")
        print("Please install Ollama from https://ollama.ai/ and start the server")
        print("Then run: ollama pull mistral")
        sys.exit(1)
    
    # Run the VC Agent Framework
    try:
        subprocess.run(["python", "vc_agent_framework.py", "--industry", industry], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running VC Agent Framework: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 