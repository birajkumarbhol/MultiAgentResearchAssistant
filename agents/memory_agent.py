
import os
import json


class MemoryAgent:
    def __init__(self):
        self.memory_path = os.path.join("data", "reports", "memory.json")

        os.makedirs(os.path.dirname(self.memory_path), exist_ok=True)

        if not os.path.exists(self.memory_path):
            with open(self.memory_path, "w") as f:
                json.dump([], f)

    def save_memory(self, query, analysis):
        try:
            # safe read
            if os.path.getsize(self.memory_path) == 0:
                data = []
            else:
                with open(self.memory_path, "r") as f:
                    data = json.load(f)

        except Exception:
            data = []

        data.append({
            "query": query,
            "analysis": analysis
        })

        with open(self.memory_path, "w") as f:
            json.dump(data, f, indent=4)

        return "Memory saved successfully ✔"

    def load_memory(self):
        try:
            if os.path.getsize(self.memory_path) == 0:
                return []

            with open(self.memory_path, "r") as f:
                return json.load(f)

        except Exception:
            return []