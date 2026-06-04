# Task 4: Firewall Configuration and Traffic Filtering Audit

## 📌 Project Objective
To interact with the native host security boundary framework, audit existing host-based firewall policy layouts, deploy custom access control list (ACL) rules to isolate network ports, test boundary enforcement states, and analyze the mechanics of packet-level filtering.

---

## 🛠️ Step-by-Step Execution Log (Windows PowerShell)

All operational adjustments were executed using an elevated administrative PowerShell console interface to interface directly with the Windows Advanced Firewall driver.

### 1 & 2. Open Configuration Tool & List Rules
To audit the current configuration state and list core networking rules natively, the following query block was executed:
```powershell
Get-NetFirewallRule -DisplayGroup "Core Networking" | Select-Object DisplayName, Enabled, Action -First 10
