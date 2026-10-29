from typing import Any
from typing import Optional
def format_user_profile(name: str, skills: list[str], experience: int, bio: Optional[str] = None) -> dict[str, Any]:

    return {"name": name, "skills": skills, "experience": experience,"bio": bio}


print(format_user_profile("jayu", ["python", "sql"], 2, None))

print(format_user_profile("Amit", ["FastApi"], 3, "Ai Engineer"))


