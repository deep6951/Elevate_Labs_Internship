# Task 5: Capture and Analyze Network Traffic Using Wireshark

## 📌 Project Objective
To deploy a localized packet-capture engine, intercept raw network layer transmissions across an active network interface card (NIC), apply structural syntax filters to isolate core protocols, and analyze packet header fields to understand network data communication.

---

## 🛠️ Step-by-Step Execution Log (Windows Environment)

### 1 & 2. Environment Setup & Interface Capture Initialization
* **Installation:** Downloaded and installed the Wireshark packet analyzer suite alongside the mandatory `Npcap` packet capture driver engine on Windows.
* **Capture Initiation:** Launched Wireshark with administrative elevation tokens, identified the primary active network driver interface showing live traffic fluctuations, and initiated a raw promiscuous-mode capture sequence.

### 3 & 4. Traffic Generation & Capture Lifecycle Management
* **Stimulus Action:** Opened a browser interface and navigated to a public domain, while simultaneously executing ICMP echo requests via the Windows command prompt:
```cmd
  ping 8.8.8.8
