Register Chatwork Task
=======================

## Install



## Usage

```
CHATWORK_API_TOKEN="fdsafasldkfjasdkkfaksdka"\
   TASK_ROOM_ID=12345\
   TASK_USER_ID="99988,92882"\
   TASK_BODY="一週間以内にやってほしいこと！"\
   TASK_LIMIT=1534489879\
   python ./main.py
```

## Environment Variables:

- `CHATWORK_API_TOKEN`: [Chatwork API Token](https://help.chatwork.com/hc/ja/articles/115000172402-API-Token%E3%82%92%E7%99%BA%E8%A1%8C%E3%81%99%E3%82%8B)
- `TASK_ROOM_ID`: Room ID to register the task
- `TASK_USER_ID`: User ID to register the task
- `TASK_BODY`: What you want to do
- `TASK_LIMIT`: Task deadline (UnixTime)