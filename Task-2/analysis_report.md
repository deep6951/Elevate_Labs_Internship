# Phishing Email Analysis Report

---

## Sample Email Information

| Field | Value |
|---|---|
| Sender | account-security@amazon-supportverify.com |
| Claimed Organization | Amazon |
| Subject | Action Required: Unusual Sign-In Activity Detected |

---

## 1. Sender Analysis

**Observed Sender:** `account-security@amazon-supportverify.com`

**Legitimate Amazon Domain:** `amazon.com`

**Analysis:** The domain `amazon-supportverify.com` is not owned by Amazon. It is crafted to visually mimic a legitimate Amazon security domain — a classic brand impersonation technique used in phishing attacks.

**Risk:** 🔴 High

---

## 2. Header & Domain Analysis

**Tool Used:** MXToolbox Domain Health Report

| Check | Result |
|---|---|
| SPF Record | ❌ Not Found |
| DMARC Record | ❌ Not Found |
| DNS Record | ⚠️ Issues Found |
| Mail Server | ❌ Multiple Errors |

**Analysis:** Legitimate organizations deploy SPF and DMARC records to prevent email spoofing. The complete absence of both records is a strong signal that this domain was set up for malicious purposes, not legitimate business communication.

**Risk:** 🔴 High

---

## 3. URL Analysis

**URL Found in Email:**
`https://amazon-security-login.verify-account.net`
**Actual Registered Domain:** `verify-account.net`

**Deception Technique:** The URL is structured as a subdomain trick — `amazon.com` appears as a subdomain prefix to make the link look legitimate at a glance. The real domain, which the browser actually connects to, is `account-verification-secure.net` — a site entirely unrelated to Amazon.

**Risk:** 🔴 High

---

## 4. Social Engineering Analysis

**Manipulative Phrases Detected:**
- "Action Required"
- "Verify your account within 24 hours"
- "Unusual Sign-In Activity Detected"

**Analysis:** The email deliberately induces urgency and fear to pressure the recipient into acting before verifying the request. This is a textbook application of *manufactured urgency* — one of the most common social engineering vectors in phishing campaigns.

**Risk:** 🔴 High

---

## 5. Greeting Analysis

**Greeting Used:** `"Dear Customer"`

**Analysis:** Legitimate services like Amazon address customers by their registered name. Generic salutations indicate a mass-blast campaign where the attacker does not have access to personalized recipient data.

**Risk:** 🟡 Medium

---

## 6. Phishing Indicators Summary

| Indicator | Status |
|---|---|
| Sender Spoofing | ✅ Detected |
| Brand Impersonation | ✅ Detected |
| SPF Record Missing | ✅ Detected |
| DMARC Record Missing | ✅ Detected |
| Suspicious URL | ✅ Detected |
| Urgency Tactics | ✅ Detected |
| Generic Greeting | ✅ Detected |

---

## Final Verdict

The analyzed email contains multiple confirmed indicators of phishing activity — including sender impersonation, suspicious domain usage, missing email authentication records, misleading URLs, and social engineering tactics.

**Classification:** Phishing Email

**Risk Level:** 🔴 High
