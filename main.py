#!/usr/bin/env python

import asyncio
import json
import logging
import websockets

logging.basicConfig()

USERS = dict()
#USERS = set()

VALUE = 0

def users_event():
    return json.dumps({"type": "users", "count": len(USERS)})

def value_event():
    return json.dumps({"type": "value", "value": VALUE})


async def counter(websocket):
    global USERS, VALUE

    # Register user
    try:
        msisdn = websocket.request_headers.get('msisdn')
    except: #Custom exection should be added
            pass
    
    try:
        USERS[msisdn] = websocket
        websockets.broadcast([v for k, v in USERS.items()], users_event())
        # Send current state to user
        await websocket.send(value_event())
        print(f"======>  {USERS}")

        # Manage state changes
        async for message in websocket:
            event = json.loads(message)
            print(event)
            if event["action"] == "minus":
                VALUE -= 1
                websockets.broadcast([v for k, v in USERS.items()], value_event())
            elif event["action"] == "plus":
                VALUE += 1
                websockets.broadcast([v for k, v in USERS.items()], value_event())

                try:
                    await list([v for k, v in USERS.items()])[0].send("some")
                except:
                    pass
            else:
                websockets.broadcast([v for k, v in USERS.items()], value_event())
                #logging.error("unsupported event: %s", event)   
    finally:
        # Unregister user
        del USERS[msisdn]
        print(f"======>  {USERS}")
        websockets.broadcast([v for k, v in USERS.items()], users_event())
        

async def main():
    async with websockets.serve(counter, "localhost", 6789):
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())