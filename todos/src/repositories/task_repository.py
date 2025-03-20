import os
import boto3
from datetime import datetime
from ..models.task_model import TodoItem
from boto3.dynamodb.conditions import Attr


class TaskRepository:
    def __init__(self):
        self.table_name = os.getenv('DYNAMODB_TABLE')
        dynamodb = boto3.resource('dynamodb')
        self.table = dynamodb.Table(self.table_name)

    def all(self):
        response = self.table.scan(
            FilterExpression=Attr('deleted_at').eq(None)
        )
        return [TodoItem(**item) for item in response['Items']]

    def create(self, todo_item: TodoItem):
        self.table.put_item(Item=todo_item.dict())

    def update(self, todo_id: str, status: str):
        now = datetime.now().isoformat()
        self.table.update_item(
            Key={
                'id': todo_id
            },
            UpdateExpression="set #s = :c, updated_at = :u",
            ExpressionAttributeNames={
                '#s': 'status'
            },
            ExpressionAttributeValues={
                ':c': status,
                ':u': now
            },
            ReturnValues="UPDATED_NEW"
        )

    def delete(self, todo_id: str):
        now = datetime.now().isoformat()
        self.table.update_item(
            Key={
                'id': todo_id
            },
            UpdateExpression="set deleted_at = :d",
            ExpressionAttributeValues={
                ':d': now
            },
            ReturnValues="UPDATED_NEW"
        )
