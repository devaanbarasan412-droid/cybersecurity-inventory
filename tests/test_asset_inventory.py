import unittest
import json
from src.asset_inventory import AssetInventory, DATA_FILE

class TestAssetInventory(unittest.TestCase):
    def setUp(self):
        with open(DATA_FILE, "w") as f:
            json.dump([], f)
        self.inv = AssetInventory()

    def test_add_asset(self):
        asset = {
            "AssetID": "T001",
            "AssetName": "Finance-PC",
            "AssetType": "Workstation",
            "IPAddress": "192.168.1.30",
            "OperatingSystem": "Windows 10",
            "Department": "Finance",
            "RiskLevel": "Low",
            "SecurityStatus": "Secure"
        }
        self.inv.add_asset(asset)
        assets = self.inv._load_assets()
        self.assertEqual(len(assets), 1)

    def test_invalid_ip(self):
        asset = {
            "AssetID": "T002",
            "AssetName": "Bad-IP",
            "AssetType": "Server",
            "IPAddress": "999.999.999.999",
            "OperatingSystem": "Linux",
            "Department": "IT",
            "RiskLevel": "Medium",
            "SecurityStatus": "Secure"
        }
        with self.assertRaises(ValueError):
            self.inv.add_asset(asset)

if __name__ == "__main__":
    unittest.main()
