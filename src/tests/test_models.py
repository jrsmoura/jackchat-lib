"""
Unit tests for the models module.
"""
import unittest
from src import LLM, EMBEDDINGS

class TestModels(unittest.TestCase):
    def test_llm_instance(self):
        self.assertIsNotNone(LLM)

    def test_embeddings_instance(self):
        self.assertIsNotNone(EMBEDDINGS)

if __name__ == "__main__":
    unittest.main()