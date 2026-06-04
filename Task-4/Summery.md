---

### 🛡️ Task 4 Executive Summary: Firewall Implementation

* **Objective:** To interact with the host-based security boundary framework (Windows Advanced Firewall), audit current rule profiles, and deploy custom Access Control Lists (ACLs) to manage the local network attack surface.
* **Implementation Vector:** Executed administrative **Windows PowerShell** command structures to dynamically view, build, and tear down firewall rule blocks without relying on the graphic interface.
* **Operational Actions:**
* **Audited:** Checked current system rules using `Get-NetFirewallRule`.
* **Enforced:** Created a custom inbound rule named `Block_Telnet_Inbound` to strictly intercept and discard all incoming traffic targeting legacy **TCP Port 23 (Telnet)**.
* **Verified:** Ran connection tests via `Test-NetConnection` to confirm packets were actively dropped and connection timeouts were successfully triggered.
* **Restored:** Purged the experimental rule using `Remove-NetFirewallRule` to bring the host OS back to its exact baseline state.


* **Core Takeaway:** Firewalls filter traffic through **Packet Inspection** (reading source/destination IPs and service ports), **Rule Matching** (evaluating traffic against an ordered access list), and **Action Execution** (making an instant decision to *Allow*, *Drop/Deny*, or *Reject* the connection).
