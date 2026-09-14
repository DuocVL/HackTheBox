# Hack The Box

Repository lưu trữ quá trình học tập và thực hành **Hack The Box (HTB)**, bao gồm Academy modules, Starting Point machines, các machine đã thực hiện và nội dung Reverse Engineering.

Repository tập trung vào việc ghi lại **quá trình phân tích, khai thác và giải quyết vấn đề**, thay vì chỉ lưu đáp án.

## Cấu trúc Repository

```text
.
├── Academy/
│   └── ...
│
├── Machines/
│   └── Easy/
│       └── ...
│
├── Reversing/
│   └── ...
│
├── Starting_Points/
│   └── ...
│
└── README.md
```

## Academy

`Academy/` chứa các module học tập trên HTB Academy.

Nội dung có thể bao gồm:

* Notes
* Commands
* Concepts
* Lab exercises
* Techniques
* Examples
* Writeups

## Machines

`Machines/` chứa các machine đã thực hành trên HTB.

Hiện tại có nhóm:

```text
Machines/
└── Easy/
    └── Machine-Name/
```

### Quy trình phân tích Machine

```text
Reconnaissance
      ↓
Port Scanning
      ↓
Enumeration
      ↓
Service Analysis
      ↓
Vulnerability Discovery
      ↓
Initial Access
      ↓
Privilege Escalation
      ↓
Flags
      ↓
Post-Exploitation
```

## Reverse Engineering

`Reversing/` dành cho các bài tập và challenge liên quan đến **Reverse Engineering**.

Các chủ đề có thể bao gồm:

* Static Analysis
* Dynamic Analysis
* Binary Analysis
* Disassembly
* Decompilation
* Control Flow
* ELF
* PE
* .NET
* Java
* Android
* Obfuscation
* Anti-Debugging
* Cryptographic Analysis


## Writeup Format

Các writeup thường tuân theo quy trình:

```text
1. Challenge / Machine Information
2. Reconnaissance
3. Enumeration
4. Vulnerability Analysis
5. Exploitation
6. Initial Access
7. Privilege Escalation
8. Post-Exploitation
9. Flags
10. Tổng kết
```

Đối với Reverse Engineering:

```text
1. File Identification
2. Static Analysis
3. Strings / Metadata
4. Disassembly
5. Decompilation
6. Control Flow Analysis
7. Important Functions
8. Algorithm Analysis
9. Bypass / Exploitation
10. Solution
```

## Công cụ

### Reconnaissance

* Nmap
* RustScan
* Netcat
* curl
* wget

### Web

* Burp Suite
* ffuf
* Gobuster
* Nikto
* SQLMap

### Password Cracking

* John the Ripper
* Hashcat
* Hydra

### Exploitation

* Metasploit
* SearchSploit
* Netcat

### Reverse Engineering

* Ghidra
* x64dbg
* Rizin
* radare2
* Cutter
* JADX
* dnSpyEx
* ILSpy

### Scripting

* Python
* Bash
* PowerShell

## Mục tiêu học tập

Repository được sử dụng để phát triển các kỹ năng:

* Penetration Testing
* Network Security
* Web Security
* Linux
* Windows
* Privilege Escalation
* Active Directory
* Reverse Engineering
* Binary Analysis
* Cryptography
* Scripting
* Vulnerability Analysis

Mục tiêu chính là hiểu được **quy trình từ phát hiện vấn đề → phân tích → khai thác → giải quyết**, thay vì chỉ tìm flag.
