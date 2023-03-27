import asyncio

async def square(x):
    print('Square', x)
    await asyncio.sleep(1)
    print('End square', x)
    return x * x

# Create event loop
loop = asyncio.get_event_loop()

# Run async function and wait for completion
results = loop.run_until_complete(asyncio.gather(
    square(1),
    square(2),
    square(3)
))
print(results)

# Close the loop
loop.close()


import asyncio

async def square(x):
    print('Square', x)
    await asyncio.sleep(1)
    print('End square', x)
    return x * x

# Create event loop
loop = asyncio.get_event_loop()

async def when_done(tasks):
    for res in asyncio.as_completed(tasks):
        print('Result:', await res)

loop.run_until_complete(when_done([
    square(1),
    square(2),
    square(3)
]))