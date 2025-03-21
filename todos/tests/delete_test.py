import json
import unittest
from unittest.mock import patch, MagicMock
from src.handlers.delete import delete

class TestDeleteTask(unittest.TestCase):

    @patch("src.handlers.delete.TaskService")
    def test_delete_task_success(self, MockTaskService):

        mock_service = MockTaskService.return_value
        mock_service.delete.return_value = None

        event = {
            'pathParameters': {'id': '1'}
        }

        response = delete(event, {})


        self.assertEqual(response['statusCode'], 201)

        body = json.loads(response['body'])
        self.assertEqual(body["status"], "success")
        self.assertEqual(body["message"], "Item deleted successfully")

    @patch("src.handlers.delete.TaskService")
    def test_delete_task_failure(self, MockTaskService):

        mock_service = MockTaskService.return_value
        mock_service.delete.side_effect = Exception("Database error")


        event = {
            'pathParameters': {'id': '1'}
        }

        response = delete(event, {})


        self.assertEqual(response['statusCode'], 500)

        body = json.loads(response['body'])
        self.assertEqual(body["status"], "error")
        self.assertIn("Database error", body["error"])

if __name__ == '__main__':
    unittest.main()