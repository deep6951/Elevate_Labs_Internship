================================================================================
TECHNICAL AUDIT SYSTEM TRAIL: WINDOWS ADVANCED FIREWALL CONFIGURATION LOG
================================================================================

[ACTION 01]: ENVIRONMENT INITIALIZATION
--------------------------------------------------------------------------------
- Launched Windows Start Menu -> Typed "PowerShell".
- Right-clicked "Windows PowerShell" -> Selected "Run as Administrator".
- Verified administrative context token validation inside the shell.

[ACTION 02]: INITIAL METRIC AUDIT
--------------------------------------------------------------------------------
- Ran the core system grouping command to inspect the operational profiles:
    Get-NetFirewallRule -DisplayGroup "Core Networking"
- Confirmed that baseline outbound and inbound network handling profiles were active.

[ACTION 03]: SECURITY CONTROL IMPLEMENTATION (PORT BLOCK)
--------------------------------------------------------------------------------
- Created a persistent explicit block rule targeting the Telnet protocol:
    New-NetFirewallRule -DisplayName "Block_Telnet_Inbound" -Direction Inbound -LocalPort 23 -Protocol TCP -Action Block
- Checked terminal feedback message to ensure parameters matched successfully.

[ACTION 04]: VERIFICATION & ASSURANCE TESTING
--------------------------------------------------------------------------------
- Tested loopback socket connectivity state against the firewall profile:
    Test-NetConnection -ComputerName 127.0.0.1 -Port 23
- Captured output results verifying that traffic was dropped or timed out.

[ACTION 05]: PROFILE RESTORATION (CLEANUP STATE)
--------------------------------------------------------------------------------
- Cleared out the customized testing firewall entry using the display name reference:
    Remove-NetFirewallRule -DisplayName "Block_Telnet_Inbound"
- Confirmed removal, completing the audit procedure and returning the host to its original security baseline.
================================================================================
