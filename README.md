<div align="center">
	<a href="https://thinknxg.com/hr">
		<img src=".github/thinkNXG-logo.jpg" height="80px" width="80px" alt="thinkNXG HR Logo">
	</a>
	<h2>thinkNXG HR</h2>
	<p align="center">
		<p>Open Source, modern, and easy-to-use HR and Payroll Software</p>
	</p>

[![CI](https://github.com/thinkNXG/thinkNXG-hrms/actions/workflows/ci.yml/badge.svg?branch=develop)](https://github.com/thinkNXG/hrms/actions/workflows/ci.yml)
[![codecov](https://codecov.io/gh/thinkNXG/thinkNXG-hrms/branch/develop/graph/badge.svg?token=0TwvyUg3I5)](https://codecov.io/gh/thinkNXG/hrms)

<a href="https://trendshift.io/repositories/10972" target="_blank"><img src="https://trendshift.io/api/badge/repositories/10972" alt="thinkNXG%2Fhrms | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/></a>
</div>

<div align="center">
	<img src=".github/hrms-hero.png"/>
</div>

<div align="center">
	<a href="https://thinknxg.com/hr">Website</a>
	-
	<a href="https://docs.thinknxg.io/hr/introduction">Documentation</a>
</div>

## thinkNXG HR

thinkNXG HR has everything you need to drive excellence within the company. It's a complete HRMS solution with over 13 different modules right from Employee Management, Onboarding, Leaves, to Payroll, Taxation, and more!

## Motivation
When thinkNXG team started growing in terms of size, we needed an open-source HR and Payroll software. We didn't find any "true" open-source HR software out there and so decided to build one ourselves.
Initially, it was a set of modules within ERPNext but version 14 onwards, as the modules became more mature, thinkNXG HR was created as a separate product.

## Key Features

- **Employee Lifecycle**: From onboarding employees, managing promotions and transfers, all the way to documenting feedback with exit interviews, make life easier for employees throughout their life cycle.
- **Leave and Attendance**: Configure leave policies, pull regional holidays with a click, check-in and check-out with geolocation capturing, track leave balances and attendance with reports.
- **Expense Claims and Advances**: Manage employee advances, claim expenses, configure multi-level approval workflows, all this with seamless integration with ERPNext accounting.
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

- [**thinkNXG Framework**](https://github.com/thinkNXG/thinkNXG-hrms): A full-stack web application framework written in Python and Javascript. The framework provides a robust foundation for building web applications, including a database abstraction layer, user authentication, and a REST API.

- [**thinkNXG UI**](https://github.com/thinkNXG/thinkNXG-ui): A Vue-based UI library, to provide a modern user interface. The thinkNXG UI library provides a variety of components that can be used to build single-page applications on top of the thinkNXG Framework.

## Production Setup

### Managed Hosting

You can try [thinkNXG Cloud](https://thinkNXGcloud.com), a simple, user-friendly and sophisticated [open-source](https://github.com/thinkNXG/press) platform to host thinkNXG applications with peace of mind.

It takes care of installation, setup, upgrades, monitoring, maintenance and support of your thinkNXG deployments. It is a fully featured developer platform with an ability to manage and control multiple thinkNXG deployments.

<div>
	<a href="https://thinkNXGcloud.com/hrms/signup" target="_blank">
		<picture>
			<source media="(prefers-color-scheme: dark)" srcset="https://thinkNXG.io/files/try-on-fc-white.png">
			<img src="https://thinkNXG.io/files/try-on-fc-black.png" alt="Try on thinkNXG Cloud" height="28" />
		</picture>
	</a>
</div>


## Development setup
### Docker
You need Docker, docker-compose and git setup on your machine. Refer [Docker documentation](https://docs.docker.com/). After that, run the following commands:
```
git clone https://github.com/thinkNXG/thinkNXG-hrms
cd hrms/docker
docker-compose up
```

Wait for some time until the setup script creates a site. After that you can access `http://localhost:8000` in your browser and the login screen for HR should show up.

Use the following credentials to log in:

- Username: `Administrator`
- Password: `admin`

### Local

1. Set up bench by following the [Installation Steps](https://thinkNXGframework.com/docs/user/en/installation) and start the server and keep it running
	```sh
	$ bench start
	```
2. In a separate terminal window, run the following commands
	```sh
	$ bench new-site hrms.local
	$ bench get-app erpnext
	$ bench get-app hrms
	$ bench --site hrms.local install-app hrms
	$ bench --site hrms.local add-to-hosts
	```
3. You can access the site at `http://hrms.local:8080`

## Learning and Community

1. [thinkNXG School](https://thinkNXG.school) - Learn thinkNXG Framework and ERPNext from the various courses by the maintainers or from the community.
2. [Documentation](https://docs.thinkNXG.io/hr) - Extensive documentation for thinkNXG HR.
3. [User Forum](https://discuss.thinknxg-erp.com/) - Engage with the community of ERPNext users and service providers.
4. [Telegram Group](https://t.me/thinkNXGhr) - Get instant help from the community of users.


## Contributing

1. [Issue Guidelines](https://github.com/thinkNXG/erpnext/wiki/Issue-Guidelines)
1. [Report Security Vulnerabilities](https://erpnext.com/security)
1. [Pull Request Requirements](https://github.com/thinkNXG/erpnext/wiki/Contribution-Guidelines)


## Logo and Trademark Policy

Please read our [Logo and Trademark Policy](TRADEMARK_POLICY.md).

<br />
<br />
<div align="center" style="padding-top: 0.75rem;">
	<a href="https://thinkNXG.io" target="_blank">
		<picture>
			<source media="(prefers-color-scheme: dark)" srcset="https://thinkNXG.io/files/thinkNXG-white.png">
			<img src="https://thinkNXG.io/files/thinkNXG-black.png" alt="thinkNXG Technologies" height="28"/>
		</picture>
	</a>
</div>

