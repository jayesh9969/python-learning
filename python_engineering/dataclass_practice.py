from dataclasses import dataclass

@dataclass

class JobPost:
    title: str
    monthly_salary: int
    is_remote: bool = True

    def annual_salary(self) -> int:
        return self.monthly_salary * 12

job1 = JobPost("Ai Engineer", 100000)
job2 = JobPost("Ai Engineer", 100000)

print(f"Jobs Equal: {job1 ==  job2}")

print(f"Annual Salary: {job1.annual_salary()}")

print(job1)

        


