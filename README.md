# A2
ece1779 assignment2
Achieved Requirements:
1. Manually add/delete worker
2. Worker numbers chart(Healthy host count)
3. For each worker: details, cpu utilization chart
4. Display load balanced user-app entry url


Doing now:
1. Auto-scalling (User-app is ready now, we can test it!)[crontab is supposed to run check_cpu.py every 1min
2. Stop the manager(Not tested yet)

To do list:
1. The http requests received by each worker in 30 mins : cloudwatch custom metrics, publish metrics
2. Terminate all workers

HTTP requests received by each worker:
1. Having problem in cloudwatch custome metrics.
2. Create a table in the database to record the http requests
3. Can create graph without cloudwatch custome metrics

!!!!
It takes about 7min from launching an instance to registering it successfully to the target group(healthy). So the if condition in get_all_targets is '!= draining' in case the auto-scaling falls in unreliable algorithm(ref: ece1779a2.pdf-requirements-8). :|

https://utoronto.zoom.us/rec/share/bJGqDzkIQgVKwZzsSyhJQNRt8Cb6UEXmHmCoJnBbEO1ZK5IHHi-0_NEMWnbxch3X._NlUAUHnIuNKfJM6?startTime=1602094724000





