# Add scheduler for script on unix
```bash
crontab -e
```

---

```
# Check server status regularly (every min)
*/1 * * * * /usr/bin/python3.9 /path/to/steam-server-status/steam_status.py --check-status

# Maintenance reminders on Tuesdays
0 22 * * 2 /usr/bin/python3.9 /path/to/steam-server-status/steam_status.py --maintenance-reminder --two-hour
0 23 * * 2 /usr/bin/python3.9 /path/to/steam-server-status/steam_status.py --maintenance-reminder --one-hour
30 23 * * 2 /usr/bin/python3.9 /path/to/steam-server-status/steam_status.py --maintenance-reminder --thirty-minutes
```
