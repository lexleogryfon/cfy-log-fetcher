from cloudify_rest_client import CloudifyClient
import requests
import logging
import os

journal_path='workflows.log'

try:
    os.remove(journal_path)
except: OSError


logging.basicConfig(filename=journal_path,level=logging.INFO)
client = CloudifyClient('172.25.1.15')
events = client.events.list(_include=["id,event_type","message","timestamp","context"], _sort="@timestamp", event_type=["workflow_started", "workflow_succeeded", "workflow_failed"])
for event in events:
    logging.info(str().join([event['timestamp'], " ", event['context']['blueprint_id'], " ", event['context']['deployment_id'], " ", event['message']["text"], " ", event['event_type']]))
    #print event['timestamp'], event['context']['blueprint_id'], event['context']['deployment_id'], event['message']["text"], event['event_type']
