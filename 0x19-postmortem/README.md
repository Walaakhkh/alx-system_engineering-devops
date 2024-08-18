Postmortem Task


Postmortem: Web Server Outage During Docker and Apache Installation

Issue Summary:
Impact: The web application hosted on the affected server was inaccessible to 70% of users during the outage. Users reported errors when attempting to access the site, including 503 Service Unavailable messages. This led to a significant drop in active sessions and potential revenue loss.
Root Cause: Conflict between Docker and Apache services due to overlapping port usage, combined with improper service configuration during the installation process.
Timeline:
10:00 UTC: Issue detected when monitoring alerts indicated that the web server was down and not responding to HTTP requests.
10:05 UTC: On-call engineer investigated Apache logs and noticed repeated errors related to binding to port 80.
10:15 UTC: Initial assumption was that Apache had crashed; attempts were made to restart the service, but it failed to bind to port 80.
10:30 UTC: Issue escalated to the DevOps team, who began investigating Docker as a potential source of the conflict, as a recent Docker installation had been performed.
10:45 UTC: Misleading investigation into potential firewall or network issues was conducted, but no problems were found.
11:00 UTC: Docker containers running on the server were inspected, revealing that a container was using port 80, causing a conflict with Apache.
11:15 UTC: The Docker container was stopped, and Apache was successfully restarted, restoring partial service.
11:30 UTC: Further testing revealed intermittent issues due to improper Docker configuration, which were resolved by adjusting Docker's settings to avoid port conflicts.
12:00 UTC: Full service was restored, and all web server functionalities were verified as operational.
12:45 UTC: Final checks and monitoring confirmed the resolution, and normal operations resumed.
Root Cause and Resolution:
The root cause of the outage was a conflict between the Docker service and the Apache web server, both attempting to use port 80 on the same server. When Docker was installed, a container was set to use port 80, which conflicted with Apache's default configuration. This led to Apache failing to start, causing the web server to go down.

To resolve the issue, the Docker container using port 80 was stopped, allowing Apache to bind to the port as expected. Further configuration changes were made to Docker to ensure it does not interfere with Apache's port usage in the future. This involved assigning non-conflicting ports to Docker containers and updating service scripts to avoid similar conflicts during startup.

Corrective and Preventative Measures:
Improvements:

Service Configuration Management:

Implement stricter service configuration protocols to ensure that ports are explicitly defined and checked for conflicts during installation.
Enhance the documentation for setting up Docker and Apache on the same server to highlight potential conflicts and their resolutions.
Monitoring and Alerts:

Set up specific alerts for port conflicts on critical services like Apache to enable quicker diagnosis.
Improve monitoring for Docker containers to catch potential issues before they impact other services.
Automation Enhancements:

Automate the detection of port conflicts during deployment using pre-deployment checks.
Develop a script to automatically reassign ports for Docker containers if a conflict is detected with existing services.
Tasks:

Task 1: Update the Docker installation process to include a check for existing services using critical ports and prompt for alternate port assignments.
Task 2: Configure Apache to use a non-standard port in situations where Docker is also required to run on the same server, with clear documentation provided to the team.
Task 3: Implement a post-installation script that verifies the health of all services, ensuring no port conflicts are present.
Task 4: Conduct a training session for the DevOps team on best practices for managing services that use common ports like 80 and 443.
Task 5: Review and revise the server architecture to better separate concerns, such as running Docker and Apache on different servers where feasible.
This postmortem underscores the importance of proper service configuration and conflict management when running multiple services on the same server. By addressing these issues, we can prevent similar outages and ensure higher availability for our users.
