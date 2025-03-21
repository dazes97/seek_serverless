import json
import unittest
from src.handlers.create import create
from unittest.mock import patch, MagicMock

class TestCreateTask(unittest.TestCase):

    @patch("src.handlers.create.TaskService")
    def test_create_task_success(self, MockTaskService):
        
        mock_service = MockTaskService.return_value
        mock_service.create.return_value = MagicMock(dict=lambda: {"id": "1", "title": "New Task", "status": "pendiente"})

        event = {
            'body': json.dumps({
                "title": "New Task",
                "status": "pendiente"
            })
        }

        response = create(event, {})

        self.assertEqual(response['statusCode'], 201)

        body = json.loads(response['body'])
        self.assertEqual(body["status"], "success")
        self.assertEqual(body["message"], "Task created successfully")
        self.assertEqual(body["data"][0]["title"], "New Task")
        self.assertEqual(body["data"][0]["status"], "pendiente")

if __name__ == '__main__':
    unittest.main()