"""FastAPI main entrypoint file."""

from services import TimezoneService
from fastapi import FastAPI, Depends
from typing import Annotated
from models import TimeZones


app = FastAPI()


TIMEZONES = [
    "America/New_York",
    "Africa/Johannesburg",
]


@app.get("/")
def main(time_service: Annotated[TimezoneService, Depends()]) -> TimeZones:
    return time_service.get_current_times_in_timezones(TIMEZONES)
