import json
import os
import re

DATA_FILE = "../data/assets.json"

class AssetInventory:
    def __init__(self):
        if not os.path.exists(DATA_FILE):
            with open(DATA_FILE, "w") as f:
                json.dump([], f)

    def _load_assets(self):
        with open(DATA_FILE, "r") as f:
            return json.load(f)

    def _save_assets(self, assets):
        with open(DATA_FILE, "w") as f:
            json.dump(assets, f, indent=4)

    def validate_asset(self, asset):
        valid_types = ["Workstation", "Server", "Router", "Switch", "Application"]
        valid_risks = ["Low", "Medium", "High", "Critical"]
        valid_status = ["Secure", "Warning", "Vulnerable"]

        if asset["AssetType"] not in valid_types:
            raise ValueError("Invalid Asset Type")
        if asset["RiskLevel"] not in valid_risks:
            raise ValueError("Invalid Risk Level")
        if asset["SecurityStatus"] not in valid_status:
            raise ValueError("Invalid Security Status")
        if not re.match(r"^\d{1,3}(\.\d{1,3}){3}$", asset["IPAddress"]):
            raise ValueError("Invalid IP Address format")

    def add_asset(self, asset):
        self.validate_asset(asset)
        assets = self._load_assets()
        assets.append(asset)
        self._save_assets(assets)
        print(f"Asset {asset['AssetID']} added successfully.")

    def display_assets(self):
        assets = self._load_assets()
        print("\nCYBERSECURITY ASSET INVENTORY\n")
        for asset in assets:
            for key, value in asset.items():
                print(f"{key} : {value}")
            print("-" * 40)
        print(f"Total Assets : {len(assets)}")

    def search_asset(self, asset_id):
        assets = self._load_assets()
        for asset in assets:
            if asset["AssetID"] == asset_id:
                print("Asset Found:")
                for key, value in asset.items():
                    print(f"{key} : {value}")
                return
        print("Asset not found.")

    def update_asset(self, asset_id, updates):
        assets = self._load_assets()
        for asset in assets:
            if asset["AssetID"] == asset_id:
                asset.update(updates)
                self.validate_asset(asset)
                self._save_assets(assets)
                print(f"Asset {asset_id} updated successfully.")
                return
        print("Asset not found.")

    def delete_asset(self, asset_id):
        assets = self._load_assets()
        new_assets = [a for a in assets if a["AssetID"] != asset_id]
        if len(new_assets) == len(assets):
            print("Asset not found.")
        else:
            self._save_assets(new_assets)
            print(f"Asset {asset_id} deleted successfully.")

    def security_summary(self):
        assets = self._load_assets()
        risk_count = {"Low":0, "Medium":0, "High":0, "Critical":0}
        status_count = {"Secure":0, "Warning":0, "Vulnerable":0}

        for asset in assets:
            risk_count[asset["RiskLevel"]] += 1
            status_count[asset["SecurityStatus"]] += 1

        print("\nSecurity Summary:")
        for risk, count in risk_count.items():
            print(f"{risk} Risk Assets : {count}")
        for status, count in status_count.items():
            print(f"{status} Assets : {count}")
