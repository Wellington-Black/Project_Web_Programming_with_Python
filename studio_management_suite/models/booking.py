from dataclasses import dataclass

@dataclass(init=True)
class Booking:

    member_id: int = None
    activity_id: int = None
    first_name: str = None
    last_name: str = None
    activity_name: str = None

