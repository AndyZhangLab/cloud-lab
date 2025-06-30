# System Monitoring Script

This script logs CPU and memory usage every time it's run and appends onto system_log.txt. Useful for basic diagnostics or logging resource consumption on a Linux machine.

## Files
- `monitor.py`: Python script that reads CPU and memory usage using `psutil`
- `system_log.txt`: Output log file with timestamps and metrics

## How to Run
Make sure `psutil` is installed:

``` bash
pip3 install psutil
python3 monitor.py
```

## Pushing to GitHub:
```bash
git add monitor.py system_log.txt README.md
git commit -m "Add system monitor script and README"
git push
```

## For first push:
```bash
git push -u origin main
```
Flag -u is short for --set-upstream, from now onwards associates local "main" branch with remote "origin/main" branch, no longer need to specify "origin main" for PR

## Future Improvements:
Making script run automatically (cron job)