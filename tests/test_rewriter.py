import pytest
from agents.rewriter import GenzRewriter

# Mock LLM output
class FakeLLM:
    def generate(self, prompt):
        return "GENZ: This is rewritten."

def test_rewriter_genz():
    llm = FakeLLM()
    rewriter = GenzRewriter(llm=llm)

    sample_news = "Stock market rises."

    output = rewriter.rewrite(sample_news)

    assert "GENZ" in output
    assert "rewritten" in output
