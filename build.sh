#!/usr/bin/env bash
source ./util.sh

info_message "Installing Requirements"
poetry install

info_message "Installing pre-commit"
pre-commit install
pre-commit install --hook-type commit-msg
pre-commit run --all-files


info_message "Checking unused steps"
output=$(behave -f steps.usage --dry-run features/)
unused_steps=$(echo "$output" | grep -A 1000 "UNUSED STEP DEFINITIONS")
if [ -n "$unused_steps" ]; then
  echo "There are some unused step definitions:"
  echo "$unused_steps"
  exit 1
fi


info_message "Running Unit Tests"
if ! pytest; then
    fail_message "One or more unit tests failed"
    exit 1
fi

info_message "Running System Tests"
if ! behave --logging-clear-handlers --format progress; then
    fail_message "One or more system tests failed"
    exit 1
fi

success_message "Build Done!"
