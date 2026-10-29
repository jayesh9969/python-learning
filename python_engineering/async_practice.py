import asyncio
import time

async def fetch_job(job_id: int, delay: float) -> str:
    await asyncio.sleep(delay)
    return f"Job {job_id} fetched"


async def main():
    start = time.time()

    results = await asyncio.gather(
        fetch_job(1, 1.0),
        fetch_job(2, 1.0),
        fetch_job(3, 1.0)
    )

    print(results)

    print(f"Total Time: {time.time() - start:.2f}s")


asyncio.run(main())

