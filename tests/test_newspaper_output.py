import pytest
from agents.newspaper_output import NewspaperFormatter

def test_newspaper_formatting():
    formatter = NewspaperFormatter()

    sample_data = [
        {
            "title": "AI Breakthrough",
            "summary": "A big discovery in AI.",
            "priority": 1
        },
        {
            "title": "Sports Win",
            "summary": "Team won the match.",
            "priority": 2
        }
    ]

    output = formatter.build_front_page(sample_data)

    # Check merged output
    assert "AI Breakthrough" in output
    assert "Sports Win" in output

    # Ensure ordering by priority
    assert output.index("AI Breakthrough") < output.index("Sports Win")

    # Basic "newspaper" markers
    assert "=== FRONT PAGE ===" in output
