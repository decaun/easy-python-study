import asyncio
import datetime

async def wait(delay):
    now = datetime.datetime.now()
    print("wait for {} seconds at {}:{}:{}".format(
        delay, now.hour, now.minute, now.second))
    await asyncio.sleep(delay)
    now = datetime.datetime.now()
    print("waited for {} seconds at {}:{}:{}".format(
        delay, now.hour, now.minute, now.second))
    return True

def main():
    #loop = asyncio.get_event_loop()
    #loop.run_until_complete(wait(2))
    #loop.close()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.gather(
        wait(2),
        wait(1)))
    loop.close()

if __name__=="__main__":
    main()