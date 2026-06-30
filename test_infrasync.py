# test_infrasync.py
"""
Tests for InfraSync module.
"""

import unittest
from infrasync import InfraSync

class TestInfraSync(unittest.TestCase):
    """Test cases for InfraSync class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = InfraSync()
        self.assertIsInstance(instance, InfraSync)
        
    def test_run_method(self):
        """Test the run method."""
        instance = InfraSync()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
