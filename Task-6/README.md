# Task 6: Password Entropy Analysis and Strength Evaluation

## 📌 Project Objective
To evaluate the mathematical and structural mechanics of password complexity, test varying character configurations against a cryptographic metric validation checker, research common authentication layer attack vectors, and outline best practices for password defense.

---

## 🧪 Phase 1: Password Complexity Testing Matrix

Multiple password profiles were generated using distinct character classes (uppercase, lowercase, numerical digits, special symbols) and varying lengths. Each profile was analyzed using standard entropy and heuristic verification metrics:

| # | Password Profile Evaluated | Structural Composition | Strength Score / Meter Rating | Core Feedback / Vulnerabilities Noted |
| :--- | :--- | :--- | :--- | :--- |
| **1** | `password123` | 11 Chars (Lowercase + Numbers) | 🔴 **Very Weak** (0% - 20%) | High predictability. Contains sequential numbers and common dictionary words. |
| **2** | `P@ssword123!` | 12 Chars (Mixed Case + Symbols + Numbers) | 🟡 **Medium** (40% - 50%) | While it uses all character types, it follows a highly predictable substitution pattern (`a` $\rightarrow$ `@`) easily guessed by modern tools. |
| **3** | `Kj9#mQ2!pX` | 10 Chars (High Randomness Mixed Class) | 🟠 **Strong** (70% - 80%) | Good algorithmic randomness. Main drawback is length; 10 characters can still be calculated over time via high-speed hardware. |
| **4** | `CorrectHorseBatteryStaple` | 26 Chars (Diceware Multi-Word Passphrase) | 🟢 **Very Strong** (95% - 100%) | Exceptional length overpowers basic randomness. High resistance to brute-force calculations due to massive character count. |
| **5** | `Tr0p!c#K@li2026!$` | 16 Chars (High Random Mixed Class + Length) | 🟢 **Exceptional** (100%) | Maximum structural complexity combined with optimal character length. |

---

## 🔬 Phase 2: Cyber Security Research – Common Password Attacks

To design defensive credential baselines, we must analyze the offensive automation mechanisms utilized by threat actors to compromise authentication structures:

### 1. Brute-Force Attacks
An algorithmic guessing strategy where an attacking application sequentially calculates every possible permutation of characters (AAAA, AAAB, AAAC...) until it strikes a match. 
* **Complexity Impact:** Directly proportional to the password's search space. Adding characters exponentially increases the time required for a brute-force application to complete calculations.

### 2. Dictionary Attacks
Instead of guessing randomly, a dictionary attack targets an authentication interface using a pre-compiled wordlist containing millions of real words, default system configurations, names, and previously leaked compromised credentials (e.g., the `rockyou.txt` collection).
* **Complexity Impact:** Basic vocabulary variations or simple letter swaps (like `e` $\rightarrow$ `3`) are easily anticipated by modern dictionary attack tools.

### 3. Credential Stuffing
An automated attack vector where threat actors take massive lists of leaked username/password combinations from a previous corporate data breach and automatically test them across hundreds of other popular platforms (social media, banking, email). This attack exploits human user credential reuse.

---

## 🛡️ Phase 3: Cryptographic Best Practices for Credential Hardening

1. **Prioritize Length over Symbol Subscriptions:** A longer passphrase (e.g., 4 or 5 random combined words) possesses inherently higher mathematical entropy than a short, complicated password. 
2. **Implement Multifactor Authentication (MFA):** Even if an elite threat actor perfectly calculates a strong password, MFA stops the attack vector cold by requiring an out-of-band secondary verification code.
3. **Deploy Zero-Reuse Scopes:** Every single application interface must utilize a unique master secret key. Employ a local or cloud-based **Password Manager** to maintain random records securely.
4. **Avoid Predictable Anchors:** Never use contextual personal variables (birth years, pet names, location details) or predictable keyboard patterns (like `qwerty` or `12345`).

---

## 💡 Key Lessons Learned & Evaluation Summary

* **The Length vs. Complexity Paradox:** Traditional enforcement rules often forced users to create short, confusing passwords (like `P@ss1!`). This evaluation proves that **length provides a massive mathematical advantage** against computational guessing engines.
* **Algorithmic Strength:** A strong password's true power is determined by its mathematical resistance to offline calculation. By stretching lengths past **14+ characters** and using all character classes randomly, the time required to crack the string expands from minutes into centuries.
