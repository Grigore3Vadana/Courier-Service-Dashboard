# Courier Service Dashboard

## Introduction
The Courier Service Dashboard is a web application designed for managing and tracking courier services. It allows users to add, manage, and view customers, couriers, packages, deliveries, and other related entities. The application also supports complex queries to generate reports and insights into the operations.

## Features
- **Customer Management**: Add, update, and delete customer information and view all customers.
- **Courier Management**: Manage courier details including their availability and vehicle types.
- **Package Tracking**: Add and manage package details and track them through their delivery lifecycle.
- **Delivery Scheduling**: Schedule and track deliveries, assign couriers, and update delivery statuses.
- **Location Services**: Keep track of package locations and update current positions.
- **Billing and Invoicing**: Manage billing details for customers and generate invoices.
- **Ratings**: View and manage customer and courier ratings.
- **Service Types**: Define and manage different types of courier services offered.
- **Complex Reporting**: Generate complex reports based on multiple criteria for in-depth analysis.

## Technologies Used
- **Backend**: Python, Flask
- **Frontend**: HTML, CSS, JavaScript
- **Database**: SQL Server
- **Others**: Font Awesome for icons

## Setup and Installation

Before setting up the project, ensure that Python and SQL Server are installed on your system. The application utilizes Windows Authentication to connect to the SQL Server, thus it should be configured to allow trusted connections. For development purposes, the connection settings are specified in the db.py file. Modify the connection string to match your SQL Server configuration. Consider using environment variables or a secure configuration management tool for handling sensitive information in production environments.

## Database Connection Management

The application establishes a new database connection for each transaction. In a production environment, consider implementing connection pooling to optimize performance and resource utilization. Always ensure that connections are properly closed after transactions to prevent resource leaks.

## Scalability and Security

Scalability: To enhance scalability, consider using a load balancer and deploying the application in a distributed environment.
Security: Implement input validation to prevent SQL injection and other common security vulnerabilities. Regularly update the application and its dependencies to mitigate security risks.

# License

- This project is protected by copyright and is not available under any public license. All rights are reserved. No part of this project may be reproduced, distributed, or transmitted in any form or by any means, including photocopying, recording, or other electronic or mechanical methods, without prior written permission from the author.

- © 2024 Vadana Ioan-Grigore. All rights reserved.

# Contact
For support or to report issues, please email grigorevadana3@gmail.com
