# System and process monitoring

## Requirements
- The app should receive a process id as input
- The app should receive a TTL (Time to Loop) (in seconds) to get the system and processes info
- The app should get the memory usage, processor usage, network usage (cumulative and now)  
- For each http request to a port binded to the pid, calculate the time to response
- The app should save the gotten information on a log file
