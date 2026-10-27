import time


print("Agent Loop started...")

max_steps = 3
steps = 0
fake_api_call = 0
while True:
    steps += 1
    print(f"AI Thinking... (step {steps})")

    if steps > max_steps:
        print("Error: Max steps reached! AI ko rok diya gaya")
        break

    time.sleep(1)
    print("Action failed, Ai trying again...\n")