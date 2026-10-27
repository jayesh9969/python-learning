from unittest.mock import MagicMock
from testing_and_logging.agent_service import ask_ai_service

def test_ask_ai_service_success():
    mock_client = MagicMock()
    mock_client.models.generate_content.return_value.text = "Mocked AI Jawab"
    result = ask_ai_service(mock_client, "Hi")
    assert result == "Mocked AI Jawab"


def test_ask_ai_service_failure():
    mock_client = MagicMock()
    mock_client.models.generate_content.side_effect = ConnectionError("503 Service Unavailable")
    result = ask_ai_service(mock_client, "Hi")

    assert result == "Service temporarily unavailable"