import json
import unittest
from unittest.mock import patch
from src.handlers.update import update


class TestUpdateTask(unittest.TestCase):

    @patch("src.handlers.update.TaskService")
    def test_update_task_success(self, MockTaskService):

        mock_service = MockTaskService.return_value
        mock_service.update.return_value = None

        event = {
            'pathParameters': {'id': '1'},
            'body': json.dumps({
                "status": "completed"
            })
        }

        response = update(event, {})

        self.assertEqual(response['statusCode'], 200)

        body = json.loads(response['body'])
        self.assertEqual(body["status"], "success")
        self.assertEqual(
            body["message"], "Item marked as completed successfully")

    @patch("src.handlers.update.TaskService")
    def test_update_task_invalid_input(self, MockTaskService):

        event = {
            'pathParameters': {'id': '1'},
            'body': 'invalid json'
        }

        response = update(event, {})

        self.assertEqual(response['statusCode'], 400)

        body = json.loads(response['body'])
        self.assertEqual(body["status"], "error")
        self.assertEqual(body["message"], "Invalid input")


if __name__ == '__main__':
    unittest.main()
