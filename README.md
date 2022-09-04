# Stock Trading Application

[![CI](https://github.com/micpst/stock-trading-app/actions/workflows/ci.yml/badge.svg)](https://github.com/micpst/stock-trading-app/actions/workflows/ci.yml)
[![Coverage](https://codecov.io/gh/micpst/stock-trading-app/branch/master/graph/badge.svg?token=CR61K0OVIR)](https://codecov.io/gh/micpst/stock-trading-app)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 🛠️ Setup
_Requires Python>=3.10, Node>=17, and yarn_

Before you run this app, make sure you have Python and Node.js installed on your machine. You'll also need to run the Postgres database service to create a persistence layer. If you prefer to run everything inside a Docker container, see the 🐳 Docker Setup section.

### Run REST service
From `services/rest` root directory run following commands:
```bash
# Install dependencies
$ pip install -r requirements-dev.txt

# Export environment variables (adjust for database configuration)
$ export DJANGO_DEBUG=True \
         DJANGO_SECRET_KEY=dev-secret-key \
         DJANGO_DB_NAME=app_db \
         DJANGO_DB_TEST_NAME=test_db \
         DJANGO_DB_USER=postgres \
         DJANGO_DB_PASSWORD=postgres \
         DJANGO_DB_HOST=localhost \
         DJANGO_DB_PORT=5432

# Apply migrations and populate the database
$ python manage.py migrate
$ python manage.py loaddata users accounts

# Run development server
$ python manage.py runserver

# Run tests with coverage
$ coverage run manage.py test
$ coverage report

```
## 🐳 Docker Setup

```bash
# Initialize containers
$ ./scripts/start.sh dev

# Stop containers
$ ./scripts/stop.sh dev

# Run tests
$ ./scripts/test.sh dev
```

## 💡 Inspirations
- [Design online stock brokerage system](https://github.com/tssovi/grokking-the-object-oriented-design-interview/blob/master/object-oriented-design-case-studies/design-an-online-stock-brokerage-system.md)
- [Design stock exchange](https://www.grokkingsystemdesigns.com/design-stock-exchange/)

## 📄 License
All my code is MIT licensed. Libraries follow their respective licenses.
