# Manual Test Cases

1. **Add Asset** → Expect "Asset added successfully."
2. **Display Assets** → Expect formatted inventory + total count.
3. **Search Asset (A102)** → Expect details of Web-Server.
4. **Update Asset (A103)** → Change SecurityStatus to Secure.
5. **Delete Asset (A101)** → Expect "Asset deleted successfully."
6. **Security Summary** → Expect counts of each risk/status.
7. **Validation** → Invalid IP, RiskLevel, SecurityStatus should raise ValueError.
