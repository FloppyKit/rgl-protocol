# Security Policy

## Supported versions

This repository publishes protocol docs, schemas, and public demonstration samples only.

| Surface | Security updates |
|---------|------------------|
| Current `main` | Yes (docs/schema/sample corrections) |
| Older commits / forks | Best-effort only |

## Reporting a vulnerability

**Please do not open a public GitHub issue for security-sensitive reports** (e.g. anything that could enable harm, leak private findings, or disclose an unfixed vulnerability in software discussed by samples).

Email: **floppykit@gitfkt.dev**

Include, if applicable:

- description of the issue
- steps to reproduce
- affected path / commit / file
- impact assessment (your best estimate)
- whether you plan coordinated disclosure and preferred timeline

We will acknowledge receipt when we can and work with you on next steps.

## Scope of this repository

**In scope for reports about this repo:**

- Issues in published schemas, examples, or documentation that could cause people to mishandle security findings
- Accidental inclusion of secrets, private data, or live vulnerability detail in this repository
- Problems with how samples instruct residual/process handling of finding reports

**Out of scope / not our disclosure channel:**

- Vulnerabilities in third-party Bitcoin (or other) projects — report those to **that** project’s own `SECURITY.md` / security contact
- Requests to run red-team scans or receive private finding dumps via this email without prior agreement
- General product/support questions (use normal public channels)

## Residual / finding-stream note

This project describes a **process residual** layer on multi-agent *finding reports*.  
An elevated residual score is **not** the same as a confirmed vulnerability.  
We do not accept “please disclose this as critical for project X” through this policy unless you are reporting an issue **in this repository**.

## Preferred practice for other maintainers

If you maintain open-source software: add a `SECURITY.md` (or `.github/SECURITY.md`) with a **reachable contact** (email or private vulnerability reporting). That is the standard front door for coordinated disclosure.
