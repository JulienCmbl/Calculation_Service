from fastapi import FastAPI
from fastapi.responses import JSONResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field
from fastapi import Request
import math
from pathlib import Path
from fastapi.exceptions import RequestValidationError

from app.calculations import Fibonacci, Factorial, Loan

app = FastAPI(title="Calculation Service", description="Fibonacci, Factorial and Loan repayment calculator", version="1.0.0",)
STATIC_DIR = Path(__file__).parent / "static"
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")


class FactorialRequest(BaseModel):
    n: int = Field(..., ge=0, description="Non-negative integer")

class FactorialResponse(BaseModel):
    n: int
    result: str


class FibonacciRequest(BaseModel):
    n: int = Field(..., ge=0, description="Non-negative integer index")
 
class FibonacciResponse(BaseModel):
    n: int
    result: str


class LoanRequest(BaseModel):
    principal: float = Field(..., gt=0, description="Loan amount (positive)")
    annual_rate_percent: float = Field(..., ge=0, description="Annual interest rate as a percentage, e.g. 5 for 5%")
    months: int = Field(..., gt=0, description="Loan term in months")
 
class LoanResponse(BaseModel):
    principal: float
    annual_rate_percent: float
    months: int
    monthly_repayment: float



@app.get("/", include_in_schema=False)
def root():
    return FileResponse(STATIC_DIR / "index.html")


def scientific_notation_fibonacci(n: int, digits: int = 6) -> str:
    s = str(n)
    exponent = len(s) - 1
    decimal_part = s[1:digits] if len(s) > 1 else "0"
    mantissa = f"{s[0]}.{decimal_part}"
    sci_not = f"{mantissa}e+{exponent}"
    if n < 1000000: 
        return str(n)
    else: 
        return sci_not

@app.post("/fibonacci", response_model=FibonacciResponse, summary="Compute nth Fibonacci number")
def get_fibonacci(req: FibonacciRequest):
    result = Fibonacci(req.n)
    return FibonacciResponse(n=req.n, result=scientific_notation_fibonacci(result))


def scientific_notation_factorial(n: int, digits: int = 6) -> str:
    s = str(n)
    exponent = len(s) - 1
    decimal_part = s[1:digits] if len(s) > 1 else "0"
    mantissa = f"{s[0]}.{decimal_part}"
    sci_not = f"{mantissa}e+{exponent}"
    if n < 1000000: 
        return str(n)
    else: 
        return sci_not


@app.post("/factorial", response_model=FactorialResponse, summary="Compute n!")
def get_factorial(req: FactorialRequest):
    result = Factorial(req.n)
    return FactorialResponse(n=req.n, result=scientific_notation_factorial(result))


@app.post("/loan", response_model=LoanResponse, summary="Calculate monthly loan repayment")
def get_loan_repayment(req: LoanRequest):
    monthly = Loan(req.principal, req.annual_rate_percent, req.months)
    return LoanResponse(
        principal=req.principal,
        annual_rate_percent=req.annual_rate_percent,
        months=req.months,
        monthly_repayment=monthly,
    )

@app.exception_handler(ValueError)
async def value_error_handler(request: Request, exc: ValueError):
    return JSONResponse(status_code=400, content={"error": str(exc)})
