# ChangePulse

A simple CLI tool that monitors a single URL and detects content changes.  
It stores the last known state in `state.json` and can print a short diff when a change is detected.

## Requirements
- Python 3.11+ (works with 3.13)

## Specification
- starts with main.py and prints "initialized"
- loads url from config