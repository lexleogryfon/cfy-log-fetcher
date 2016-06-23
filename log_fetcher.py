from cloudify_rest_client import CloudifyClient
import requests

client = CloudifyClient('172.25.1.15')
events = client.events.list(_include=["id,event_type","message","timestamp","context"], _sort="@timestamp", event_type=["workflow_started", "workflow_succeeded", "workflow_failed"])
for event in events:
    print event['timestamp'], event['context']['blueprint_id'], event['context']['deployment_id'], event['message']["text"], event['event_type']
