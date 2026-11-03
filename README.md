<div align="center">
	<a href="https://thinknxg.com/hr">
		<img src=".github/thinkNXG-logo.jpg" height="80px" width="80px" alt="thinkNXG HR Logo">
	</a>
	<h2>thinkNXG HR</h2>
	<p align="center">
		<p>Open Source, modern, and easy-to-use HR and Payroll Software</p>
	</p>
</div>

<div align="center">
	<img src=".github/hrms-hero.png"/>
</div>

<div align="center">
	<a href="https://thinknxg.com/hr">Website</a>
	-
	<a href="https://docs.thinknxg.com/thinknxghr">Documentation</a>
	-
	<a href="https://thinknxg.com/support">Support</a>
</div>

## thinkNXG HR

thinkNXG HR has everything you need to drive excellence within the company. It's a complete HRMS solution with over 13 different modules right from Employee Management, Onboarding, Leaves, to Payroll, Taxation, and more!

thinkNXG HR runs on the thinkNXG Framework and integrates with thinkNXG ERP for accounting, expenses and payroll postings.

## Key Features

- **Employee Lifecycle**: From onboarding employees, managing promotions and transfers, all the way to documenting feedback with exit interviews, make life easier for employees throughout their life cycle.
- **Leave and Attendance**: Configure leave policies, pull regional holidays with a click, check-in and check-out with geolocation capturing, track leave balances and attendance with reports.
- **Expense Claims and Advances**: Manage employee advances, claim expenses, configure multi-level approval workflows, all this with seamless integration with thinkNXG ERP accounting.
- **Performance Management**: Track goals, align goals with key result areas (KRAs), enable employees to evaluate themselves, make managing appraisal cycles easy.
- **Payroll & Taxation**: Create salary structures, configure income tax slabs, run standard payroll, accomodate additional salaries and off cycle payments, view income breakup on salary slips and so much more.
- **thinkNXG HR Mobile App**: Apply for and approve leaves on the go, check-in and check-out, access employee profile right from the mobile app.

<details open>

<summary>View Screenshots</summary>
	<img src=".github/hrms-appraisal.png"/>
	<img src=".github/hrms-requisition.png"/>
	<img src=".github/hrms-attendance.png"/>
	<img src=".github/hrms-salary.png"/>
	<img src=".github/hrms-pwa.png"/>
</details>

### Under the Hood

- [**thinkNXG Framework**](https://docs.thinknxg.com/thinknxgframework): A full-stack web application framework written in Python and Javascript. The framework provides a robust foundation for building web applications, including a database abstraction layer, user authentication, and a REST API.

- [**thinkNXG ERP**](https://docs.thinknxg.com/thinknxgerp): The ERP that thinkNXG HR depends on for companies, accounting, expenses and payroll postings.

## Production Setup

### Managed Hosting

You can host thinkNXG HR on [thinkNXG Cloud](https://thinknxgcloud.com/), a simple, user-friendly platform to host thinkNXG applications with peace of mind. It takes care of installation, setup, upgrades, monitoring, maintenance and support of your thinkNXG deployments. See the [thinkNXG Cloud documentation](https://docs.thinknxg.com/thinknxgcloud).

## Development setup
### Docker
You need Docker, docker-compose and git setup on your machine. Refer [Docker documentation](https://docs.docker.com/). After that, run the following commands:
```
git clone https://github.com/thinknxg/thinkNXG-HRMS hrms
cd hrms/docker
docker-compose up
```

Wait for some time until the setup script creates a site. After that you can access `http://localhost:8000` in your browser and the login screen for HR should show up.

Use the following credentials to log in:

- Username: `Administrator`
- Password: `admin`

### Local

1. Set up bench by following the installation steps in the [thinkNXG Framework documentation](https://docs.thinknxg.com/thinknxgframework) and start the server and keep it running
	```sh
	$ bench start
	```
2. In a separate terminal window, run the following commands
	```sh
	$ bench new-site hrms.local
	$ bench get-app erpnext https://github.com/thinknxg/thinkNXG-ERP-M --branch version-16
	$ bench get-app hrms https://github.com/thinknxg/thinkNXG-HRMS --branch version-16
	$ bench --site hrms.local install-app hrms
	$ bench --site hrms.local add-to-hosts
	```
3. You can access the site at `http://hrms.local:8080`

## Documentation and Support

1. [thinkNXG HR Documentation](https://docs.thinknxg.com/thinknxghr) - Guides for every thinkNXG HR module.
2. [thinkNXG ERP Documentation](https://docs.thinknxg.com/thinknxgerp) - Accounting, expenses and other ERP topics.
3. [thinkNXG Support](https://thinknxg.com/support) - Get help from the thinkNXG team.
4. [thinkNXG Insights](https://thinknxg.com/insights) - Reporting and analytics for your HR data.

## Logo and Trademark Policy

Please read our [Logo and Trademark Policy](TRADEMARK_POLICY.md).

## License and Attribution

thinkNXG HR is distributed under the GNU General Public License v3 (see [license.txt](license.txt)). It is based on the open-source [Frappe HR](https://github.com/frappe/hrms) project by Frappe Technologies Pvt. Ltd. and is kept in sync with its `version-16` branch.
