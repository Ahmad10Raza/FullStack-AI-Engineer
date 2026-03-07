## Python `logging` Module (Complete Guide)

The `logging` module is used to  **record events that happen during program execution** .

Instead of using `print()` statements, professional systems use **logging** to:

```text
track errors
debug applications
monitor systems
record events
```

It is heavily used in:

```text
production systems
machine learning pipelines
APIs
data engineering pipelines
automation scripts
```

Example problem with `print()`:

```python
print("Error occurred")
```

Problems:

```text
no log levels
no timestamps
no file storage
no log management
```

Logging solves these problems.

## 1. Basic Logging Example

```python
import logging

logging.warning("This is a warning")
```

Output:

```text
WARNING:root:This is a warning
```

Logging automatically adds:

```text
log level
logger name
message
```

## 2. Logging Levels

Logging supports multiple severity levels.

| Level    | Meaning                 |
| -------- | ----------------------- |
| DEBUG    | detailed debugging info |
| INFO     | normal program events   |
| WARNING  | something unexpected    |
| ERROR    | serious problem         |
| CRITICAL | program failure         |

Example:

```python
import logging

logging.debug("Debug message")
logging.info("Info message")
logging.warning("Warning message")
logging.error("Error message")
logging.critical("Critical error")
```

Default output:

```text
WARNING:root:Warning message
ERROR:root:Error message
CRITICAL:root:Critical error
```

By default Python logs  **WARNING and above** .

## 3. Configuring Logging

To show all log levels:

```python
import logging

logging.basicConfig(level=logging.DEBUG)

logging.debug("Debug message")
logging.info("Info message")
```

Now output includes debug and info logs.

## 4. Logging Format

We can customize log output.

Example:

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Application started")
```

Output:

```text
2026-03-07 12:45:10 - INFO - Application started
```

Common format fields:

| Field             | Meaning     |
| ----------------- | ----------- |
| `%(asctime)s`   | timestamp   |
| `%(levelname)s` | log level   |
| `%(message)s`   | log message |
| `%(name)s`      | logger name |
| `%(filename)s`  | file name   |

Example:

```python
format="%(asctime)s %(filename)s %(levelname)s %(message)s"
```

## 5. Logging to a File

Instead of printing logs in terminal, we can save them.

Example:

```python
import logging

logging.basicConfig(
    filename="app.log",
    level=logging.INFO
)

logging.info("Program started")
logging.error("Something failed")
```

This creates:

```text
app.log
```

Example content:

```text
INFO:root:Program started
ERROR:root:Something failed
```

## 6. Using Loggers

Instead of using root logger, we create custom loggers.

Example:

```python
import logging

logger = logging.getLogger("myapp")

logger.warning("Warning message")
```

Output:

```text
Warning message
```

Loggers help organize logs in  **large applications** .

Example structure:

```text
app
 ├── database
 ├── api
 └── services
```

Each module can have its  **own logger** .

Example:

```python
logger = logging.getLogger(__name__)
```

## 7. Handlers

Handlers determine  **where logs are sent** .

Examples:

```text
console
file
remote server
database
```

Example:

```python
import logging

logger = logging.getLogger()

handler = logging.FileHandler("app.log")

logger.addHandler(handler)

logger.error("File logging example")
```

Now logs go to  **file handler** .

## 8. Multiple Handlers

We can log to  **console and file simultaneously** .

Example:

```python
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler("app.log")
stream_handler = logging.StreamHandler()

logger.addHandler(file_handler)
logger.addHandler(stream_handler)

logger.info("Application started")
```

Output:

```text
Console → printed
File → saved
```

## 9. Rotating Logs

Large applications generate huge logs.

We use  **rotating log files** .

Example:

```python
from logging.handlers import RotatingFileHandler
import logging

handler = RotatingFileHandler(
    "app.log",
    maxBytes=1000,
    backupCount=3
)

logger = logging.getLogger()
logger.addHandler(handler)

logger.warning("Rotating log example")
```

When file exceeds size:

```text
app.log
app.log.1
app.log.2
```

Old logs are preserved.

## 10. Logging Exceptions

Example:

```python
import logging

try:
    x = 1 / 0
except Exception:
    logging.exception("Error occurred")
```

Output:

```text
ERROR:root:Error occurred
Traceback...
```

This logs  **full stack trace** .

## 11. Logging in Large Projects

Typical structure:

```text
project/
   main.py
   config.py
   database.py
   api.py
```

Each module:

```python
import logging

logger = logging.getLogger(__name__)
```

Example:

```python
logger.info("Database connected")
```

Logs will show module name.

## 12. Logging Configuration File

Advanced projects use configuration.

Example:

```python
logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s %(name)s %(levelname)s %(message)s"
)
```

## 13. Example: Logging in Data Pipeline

Example:

```python
import logging

logging.basicConfig(level=logging.INFO)

def process_file(file):

    logging.info(f"Processing {file}")

    try:
        # processing code
        pass

    except Exception:
        logging.error("Processing failed")

process_file("data.csv")
```

Output:

```text
INFO Processing data.csv
```

## 14. Logging Best Practices

Professional developers follow these rules:

Use logging instead of `print()`.

Use correct log levels.

```text
DEBUG → development
INFO → normal operation
WARNING → unusual situation
ERROR → failures
CRITICAL → system crash
```

Log useful information:

```text
timestamps
module names
error details
```

Rotate logs in production.

## 15. Logging Architecture

```text
Logger
   |
Handlers
   |
Formatters
```

Example flow:

```text
Application
    |
Logger
    |
Handler
    |
Output (console/file)
```

## Real Systems Using Logging

Logging is used everywhere:

```text
FastAPI
Django
microservices
ML pipelines
data engineering
monitoring systems
```

Example ML pipeline log:

```text
INFO Loading dataset
INFO Training model
ERROR Training failed
```

## Key Logging Components

```text
Logger
Handler
Formatter
Log Levels
```

These form the  **logging system architecture** .

---

## Advanced Logging in Production Systems

In production environments (APIs, microservices, ML pipelines), logging becomes **much more structured and scalable** than simple `logging.basicConfig()`.

Production logging systems usually include:

```text
structured logging
JSON logs
centralized logging
log rotation
correlation IDs
monitoring integration
```

These allow logs to be  **analyzed automatically by monitoring systems** .

We will cover the most important production techniques.

## 1. Structured Logging

Normal logs are just text:

```
INFO User logged in
```

This is hard for machines to analyze.

Structured logging uses  **key-value data** .

Example:

```
INFO user_id=42 action=login status=success
```

Example in Python:

```python
import logging

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger("app")

logger.info("User login", extra={"user_id":42})
```

Structured logs help with:

```text
searching logs
analytics
monitoring
alerting
```

## 2. JSON Logging

Production systems often store logs as **JSON** so monitoring tools can parse them easily.

Example log:

```json
{
 "timestamp": "2026-03-07",
 "level": "INFO",
 "message": "User login",
 "user_id": 42
}
```

Python library:

```text
python-json-logger
```

Install:

```
pip install python-json-logger
```

Example:

```python
import logging
from pythonjsonlogger import jsonlogger

logger = logging.getLogger()

handler = logging.StreamHandler()

formatter = jsonlogger.JsonFormatter()

handler.setFormatter(formatter)

logger.addHandler(handler)

logger.warning("Application started")
```

Output:

```json
{"message":"Application started","levelname":"WARNING"}
```

This format works well with:

```text
ELK stack
Splunk
Datadog
CloudWatch
```

## 3. Centralized Logging

Large distributed systems have  **many services** .

Example architecture:

```
API service
Worker service
ML service
Database service
```

Each service generates logs.

Instead of storing logs locally, they are sent to a  **central logging system** .

Architecture:

```
Application
    |
Logger
    |
Log collector
    |
Central logging system
```

Common tools:

```text
ELK Stack (Elasticsearch + Logstash + Kibana)
Grafana Loki
Splunk
Datadog
AWS CloudWatch
```

Example pipeline:

```
Python app
   ↓
JSON logs
   ↓
Logstash
   ↓
Elasticsearch
   ↓
Kibana dashboard
```

Now logs become  **searchable dashboards** .

## 4. Log Rotation (Production Requirement)

Production systems generate  **huge logs** .

Example:

```
API server → 1GB logs per day
```

If we don't rotate logs:

```
disk full
application crash
```

Solution: rotating logs.

Example:

```python
from logging.handlers import RotatingFileHandler
import logging

handler = RotatingFileHandler(
    "app.log",
    maxBytes=1000000,
    backupCount=5
)

logger = logging.getLogger()

logger.addHandler(handler)

logger.warning("Rotating log example")
```

Now logs rotate:

```
app.log
app.log.1
app.log.2
```

Older logs are archived automatically.

## 5. Time-Based Log Rotation

Sometimes we rotate logs by  **time instead of size** .

Example:

```python
from logging.handlers import TimedRotatingFileHandler
import logging

handler = TimedRotatingFileHandler(
    "app.log",
    when="midnight",
    interval=1,
    backupCount=7
)

logger = logging.getLogger()

logger.addHandler(handler)
```

This creates:

```
app.log
app.log.2026-03-06
app.log.2026-03-07
```

## 6. Correlation IDs (Distributed Systems)

In microservices, one request might pass through multiple services.

Example:

```
User request
   ↓
API service
   ↓
Auth service
   ↓
Database service
```

To track the request across services we use  **correlation IDs** .

Example log:

```
request_id=abc123 user_login started
request_id=abc123 database query executed
request_id=abc123 response sent
```

Implementation example:

```python
import logging
import uuid

request_id = uuid.uuid4()

logger = logging.getLogger()

logger.info("Processing request", extra={"request_id": str(request_id)})
```

Now logs across services share the same ID.

## 7. Logging in FastAPI / Web APIs

Example production logger.

```python
import logging

logger = logging.getLogger("api")

def get_user():

    logger.info("Fetching user")

    try:
        pass
    except Exception:
        logger.exception("Database error")
```

Example output:

```
2026-03-07 INFO api Fetching user
```

## 8. Logging Performance Considerations

Logging can slow applications if done incorrectly.

Bad:

```python
logger.debug(f"Result is {expensive_function()}")
```

Even if debug logs are disabled, the function still runs.

Better:

```python
logger.debug("Result is %s", expensive_function())
```

The message is formatted  **only if needed** .

## 9. Async Logging

High-performance systems use  **non-blocking logging** .

Example:

```python
from logging.handlers import QueueHandler, QueueListener
```

Architecture:

```
Application
    |
QueueHandler
    |
Logging Queue
    |
QueueListener
    |
Log File
```

This prevents logging from  **blocking application threads** .

## 10. Logging Best Practices in Production

Professional systems follow these rules.

Use structured logs.

```
key=value format
```

Use JSON logs for observability tools.

Rotate logs.

Avoid logging sensitive data.

Example:

```
password
tokens
private keys
```

Use correct log levels.

```
DEBUG → development
INFO → normal events
WARNING → unexpected situation
ERROR → failure
CRITICAL → system crash
```

## Production Logging Architecture

```
Application
     |
Logger
     |
Handler
     |
Formatter
     |
Log Collector
     |
Central Logging System
```

Monitoring dashboards analyze logs automatically.

## Real Systems Using Advanced Logging

Production logging is used heavily in:

```
FastAPI
Django
microservices
data pipelines
ML training pipelines
DevOps systems
```

Example ML pipeline logs:

```
INFO Loading dataset
INFO Training started
ERROR Training failed
```

These logs help with  **debugging and monitoring large systems** .
