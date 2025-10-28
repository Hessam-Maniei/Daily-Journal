name: Daily Commit

on:
  workflow_dispatch:  # lets you run it manually
  schedule:
    - cron: "0 9 * * *"  # runs every day at 9:00 UTC

jobs:
  run_journal:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.x'

      - name: Run Journal script
        run: python Journal.py
