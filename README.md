# A2
This is the manager web application that can resize the worker pool on demand(according to average CPU utilization), the manager can set the auto scaling policy on their own.
1. Manually add/delete worker
2. Worker numbers chart(Healthy host count)
3. For each worker: details, cpu utilization chart, http requests chart
4. Display load balanced user-app entry url
5. Initia.py: initialize the worker pool size to 1 once the manager-app starts, only run once when manager starts
6. auto-scaling.py auto scaling and load balanced cpu utilization by start/terminate AWS EC2 instance
7. Stop the manager
8. Terminate all workers






