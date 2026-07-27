# Calculation_Service
A small application that computes Fibonacci numbers, factorials, and monthly loan repayments.

## Quickstart

Requirements: Python 3.11 or newer. Install the dependencies given in ```requirements.txt``` and start the API using the following lines (or similar) in the terminal: 

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

The API is now running at: `http://localhost:8000`. Copy and paste into browser to display the web UI.
The interactive docs are auto-generated and can be found at: `http://localhost:8000/docs`

## Build with Docker

To build with Docker, run the following commands in the terminal:

```bash
docker build -t calculation .
docker run -p 8000:8000 calculation
```

## Run tests

20 tests are built into the test suite. These tests check standard as well as disallowed values (negatives, non-integers, etc.), as well as special cases (0 and 1). To run the tests:

```bash
python -m pytest tests/ -v
```

## Assumptions & Limitations

- No authentication or rate limiting — this is a local/demo service.
- Fibonacci and factorial inputs must be non-negative integers.
- Support for very large input values is achieved by: 1- Using an iterative method instead of recursive. 2- Setting the result in main as a string. 3- Inserting `sys.set_int_max_str_digits(0)`
- For simplicity, calculation results for Fibonacci and factorial are displayed in scientific notation for numbers above 1,000,000.
- Loan repayment is rounded to 2 decimals using ROUND_HALF_UP.
- `annual_rate_percent` is a percentage value (e.g. `5` means 5% p.a., not `0.05`).




## Endpoints

| Method | Path | Description |
|--------|------|-------------|
| GET | `/` | Web UI |
| POST | `/fibonacci` | nth Fibonacci number |
| POST | `/factorial` | n! |
| POST | `/loan` | Monthly loan repayment |

### Example requests

**Fibonacci**
```bash
curl -X POST http://localhost:8000/fibonacci \
  -H "Content-Type: application/json" \
  -d '{"n": 10}'
# → {"n": 10, "result": 55}
```

**Factorial**
```bash
curl -X POST http://localhost:8000/factorial \
  -H "Content-Type: application/json" \
  -d '{"n": 5}'
# → {"n": 5, "result": 120}
```

**Loan repayment**
```bash
curl -X POST http://localhost:8000/loan \
  -H "Content-Type: application/json" \
  -d '{"principal": 10000, "annual_rate_percent": 5, "months": 24}'
# → {"principal": 10000, "annual_rate_percent": 5.0, "months": 24, "monthly_repayment": 438.71}
```

