"""
Unit tests for the readers module.
"""
import unittest
from ..rag_azure.readers import load_documents

class TestReaders(unittest.TestCase):
    def test_load_documents(self):
        self.assertIsInstance(load_documents(), list)

if __name__ == "__main__":
    unittest.main()