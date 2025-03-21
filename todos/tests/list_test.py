import json
import unittest
from src.handlers.list import all
from unittest.mock import MagicMock, patch


class TestListTasks(unittest.TestCase):

    @patch("src.handlers.list.TaskService")
    def test_all_empty(self, MockTaskService):
        mock_service = MockTaskService.return_value
        mock_service.all.return_value = []

        response = all({}, {})

        self.assertEqual(response['statusCode'], 200)

        body = json.loads(response['body'])
        self.assertEqual(body["status"], "success")
        self.assertEqual(len(body["data"]), 0)
        self.assertEqual(body["message"], "Task list retrieved successfully")

    @patch("src.handlers.list.TaskService")
    def test_all_with_tasks(self, MockTaskService):
        mock_service = MockTaskService.return_value
        mock_service.all.return_value = [
            MagicMock(dict=lambda: {"id": "1",
                      "title": "Task 1", "status": "por hacer"}),
            MagicMock(dict=lambda: {"id": "2",
                      "title": "Task 2", "status": "completada"})
        ]

        response = all({}, {})

        self.assertEqual(response['statusCode'], 200)

        body = json.loads(response['body'])
        self.assertEqual(body["status"], "success")
        self.assertEqual(len(body["data"]), 2)
        self.assertEqual(body["data"][0]["title"], "Task 1")
        self.assertEqual(body["data"][1]["title"], "Task 2")


if __name__ == '__main__':
    unittest.main()
