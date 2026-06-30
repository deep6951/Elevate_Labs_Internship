# 🎣 Phishing Email Analysis

> A structured analysis of a phishing email impersonating Amazon, identifying key attack vectors and social engineering techniques.

---

## 📋 Objective

Analyze a suspicious email to identify common phishing indicators including sender spoofing, malicious links, social engineering tactics, and email authentication failures.

---

## 🛠️ Tools Used

| Tool | Purpose |
|---|---|
| [MXToolbox](https://mxtoolbox.com) | Domain health & email authentication checks |
| Web Browser | URL and domain inspection |
| Manual Analysis | Header review, social engineering identification |

---

## 📧 Sample Email Details

| Field | Value |
|---|---|
| **Sender** | `account-security@amazon-supportverify.com` |
| **Claimed Organization** | Amazon |
| **Subject** | `Action Required: Unusual Sign-In Activity Detected` |
| **Suspicious URL** | `https://amazon-security-login.verify-account.net` |
| **Verdict** | 🔴 Phishing |

---

## 🔍 Analysis

### 1. Sender Address Analysis

The email claims to be from Amazon Security, but the sender domain is:

```
account-security@amazon-supportverify.com
                  ^^^^^^^^^^^^^^^^^^^^^^
                  NOT an official Amazon domain
```

**Legitimate Amazon domains:**

```
amazon.com
amazon.in
```

`amazon-supportverify.com` is an unregistered third-party domain crafted to visually resemble an official Amazon security address.

> **Finding:** Sender spoofing / domain impersonation detected.

---

### 2. Domain & Header Analysis

Sender domain analyzed via **MXToolbox Domain Health Report**.

| Check | Result | Implication |
|---|---|---|
| SPF Record | ❌ Not Found | No sender authorization policy |
| DMARC Record | ❌ Not Found | No email spoofing protection |
| DNS Record | ⚠️ Issues Detected | Domain misconfiguration |
| Mail Server | ❌ Multiple Errors | Not set up for legitimate email |

Legitimate organizations always configure SPF and DMARC records. Their complete absence strongly indicates this domain was registered for malicious purposes.

> **Finding:** Suspicious domain with poor email security configuration.

---

### 3. URL Analysis

The email contains the following link:

```
https://amazon-security-login.verify-account.net
        ^^^^^^^^^^^^^^^^^^^^^
        Subdomain trick — NOT amazon.com
```

| Component | Value |
|---|---|
| **Displayed as** | `amazon-security-login.verify-account.net` |
| **Actual registered domain** | `verify-account.net` |
| **Technique** | Subdomain spoofing — embeds `amazon-security-login` as a subdomain to impersonate Amazon |

Although the URL contains the word **Amazon**, browsers connect to the rightmost domain before the first `/`. The `amazon-security-login` portion is just a subdomain; the real destination is `verify-account.net`, which has no affiliation with Amazon.

> **Finding:** Potential phishing URL designed to impersonate Amazon.

---

### 4. Social Engineering Analysis

The email contains urgency-based language designed to pressure the recipient:

| Phrase | Technique |
|---|---|
| `"Action Required"` | Manufactured urgency |
| `"Verify your account within 24 hours"` | Artificial deadline |
| `"Unusual Sign-In Activity Detected"` | Fear of account compromise |

This is a classic **Fear, Urgency, Scarcity (FUS)** manipulation pattern intended to bypass critical thinking and prompt immediate, unverified action.

> **Finding:** Urgency and fear tactics identified.

---

### 5. Greeting Analysis

```
"Dear Customer"
```

Legitimate services like Amazon address users by their **registered first name**. A generic greeting indicates:

- The attacker has no access to real customer data
- This is a mass phishing campaign sent to many recipients simultaneously

> **Finding:** Generic greeting commonly used in phishing campaigns.

---

## 🚩 Phishing Indicators Summary

| # | Indicator | Status |
|---|---|---|
| 1 | Sender Spoofing | ✅ Detected |
| 2 | Domain Impersonation | ✅ Detected |
| 3 | Missing SPF Record | ✅ Detected |
| 4 | Missing DMARC Record | ✅ Detected |
| 5 | Suspicious / Spoofed URL | ✅ Detected |
| 6 | Urgency & Fear Tactics | ✅ Detected |
| 7 | Generic Greeting | ✅ Detected |

**Total indicators found: 7 / 7**

---

## 📸 Screenshots

The repository includes screenshots demonstrating:

- `domain_analysis.png` —  MXToolbox analysised domain
- `malicious_url.png` — Suspicious phishing URL

---

## ✅ Conclusion

The analyzed email exhibits multiple confirmed phishing characteristics including sender impersonation, suspicious domain usage, misleading URLs, and social engineering tactics. Based on the findings, this email is classified as a **phishing email** and should be treated as malicious.

**Classification:** `Phishing Email`  
**Risk Level:** 🔴 `High`

---

## 🛡️ Recommended Actions

- **Do not** click any links in the email
- **Do not** enter credentials on any page linked from this email
- **Report** the email as phishing via your email client
- **Delete** the email immediately
- If credentials were already entered, **change your Amazon password** and enable 2FA immediately
- Report to Amazon directly at: `stop-spoofing@amazon.com`

---

## 📁 Repository Structure

```
Phishing-Email-Analysis/
├── README.md
├── analysis_report.md
├── phishing_email.txt
└── screenshots/
    ├── domain_analysis.png
    ├── malicious_link.png
```

---

## 📚 References

- [Amazon Security Help](https://www.amazon.com/gp/help/customer/display.html?nodeId=GFT9STXPSCBZQHMS)
- [MXToolbox Domain Health](https://mxtoolbox.com/domain)
- [VirusTotal — URL & Domain Analysis](https://www.virustotal.com)
- [How to Identify Phishing Emails — CISA](https://www.cisa.gov/phishing)
