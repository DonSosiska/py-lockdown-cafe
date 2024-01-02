import datetime
from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:

    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("All friends should be vaccinated")
        else:
            if visitor["vaccine"]["expiration_date"] < datetime.date.today():
                raise (
                    OutdatedVaccineError("All friends should be vaccinated"))
            else:
                if not visitor["wearing_a_mask"]:
                    raise NotWearingMaskError("Friends should buy 2 masks")
                else:
                    return f"Welcome to {self.name}"