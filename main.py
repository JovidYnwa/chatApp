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

    try:
        msisdn = websocket.request_headers.get('msisdn') #retriving token from websocket headers
    except: #Custom exection should be added
            pass
    
    try:
        # Register user

        USERS[msisdn] = websocket
        websockets.broadcast([v for k, v in USERS.items()], users_event())
        # Send current state to user
        await websocket.send(value_event())
        print(f"======>  {USERS}")

        # Manage state changes
        async for message in websocket:
            event = json.loads(message)
            print(f"=====> {event}")
            dest_msisdn = event["destination_msisdn"]
            print(f"----->  {USERS[dest_msisdn]}")
            message_val = event["message"]
            await USERS[dest_msisdn].send(message_val)

    finally:
        # Unregister user
        del USERS[msisdn]
        websockets.broadcast([v for k, v in USERS.items()], users_event())
        

async def main():
    async with websockets.serve(counter, "localhost", 6789):
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())