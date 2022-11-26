# Stock Trading Application

[![CI](https://github.com/micpst/stock-trading-app/actions/workflows/ci.yml/badge.svg)](https://github.com/micpst/stock-trading-app/actions/workflows/ci.yml)
[![Coverage](https://codecov.io/gh/micpst/stock-trading-app/branch/master/graph/badge.svg?token=CR61K0OVIR)](https://codecov.io/gh/micpst/stock-trading-app)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 🛠️ Setup
_Requires Python>=3.11, Node>=17, and yarn_

Before you run this app, make sure you have Python and Node.js installed on your machine. You'll also need to run the Postgres database service to create a persistence layer. If you prefer to run everything inside a Docker container, see the 🐳 Docker Setup section.

### Run REST service
From `services/rest` directory run following commands:
```bash
# Start virtualenv
$ pipenv shell

# Install dependencies
$ pipenv install --dev

# Export environment variables
$ . ./scripts/setup-env.sh dev

# Apply migrations and populate the database
$ python manage.py migrate
$ python manage.py loaddata users accounts

# Run development server
$ python manage.py runserver

# Run tests with coverage
$ coverage run manage.py test
$ coverage report
```
### Run client service
From `services/client` directory run following commands:
```bash
# Install dependencies
$ yarn

# Run development server
$ yarn run start
```

## 🐳 Docker Setup
From project root run following commands:
```bash
# Initialize containers
$ ./scripts/compose.sh dev up -d

# Verify running containers
$ ./scripts/compose.sh dev ps

# Run REST service tests
$ ./scripts/compose.sh dev exec rest python manage.py test

# Stop containers
$ ./scripts/compose.sh dev stop
```

## 💡 Inspirations
- [Design online stock brokerage system](https://github.com/tssovi/grokking-the-object-oriented-design-interview/blob/master/object-oriented-design-case-studies/design-an-online-stock-brokerage-system.md)
- [Design stock exchange](https://www.grokkingsystemdesigns.com/design-stock-exchange/)

## 📄 License
All my code is MIT licensed. Libraries follow their respective licenses.
