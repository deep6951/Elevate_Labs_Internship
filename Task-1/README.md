# CYBER SECURITY INTERNSHIP | Task 1: Scan Your Local Network for Open Ports

## 📌 Project Objective
The primary objective of this task is to perform active network reconnaissance on a local area network (LAN) to discover active hosts, identify open ports, and analyze network service exposure. Understanding open ports helps in assessing the attack surface and identifying potential security risks associated with exposed services.

---

## 💻 Environment & Methodology
- **Operating System:** Kali Linux (Running via Oracle VirtualBox)
- **Scanning Tool:** Nmap (Network Mapper)
- **Target Subnet Range:** 10.251.24.196

### Execution Command
The scan was executed with administrative privileges using a stealthy half-open scan technique targeting the most common ports, and the output was exported directly to a text file:

```bash
sudo nmap -sS -F 192.168.1.0/24 -oN nmap_report.txt
