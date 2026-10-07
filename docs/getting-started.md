# Getting Started with Xtra Computing Servers

This guide takes new users from applying for an account to establishing a
working SSH session. It covers regular user access only.

!!! info "Important"
    An Xtra account does not automatically grant access to every machine. Use only
    servers explicitly assigned or authorized by the administrator.

## End-to-end onboarding

1. Read and accept the [Terms of Use](terms.md), especially the rules on
   GPUs, storage, backups, security, and account expiration.
2. Submit the [Xtra server account application](https://forms.gle/Wf8qbNeuSPS2ia8u6).
3. Wait for confirmation. The administrator will send you an email containing
   the hostname, username, and password.
4. Log in using SSH and complete the first-login checks in this guide.
5. Keep independent backups of important data and checkpoint long-running jobs.
   Server storage and uninterrupted computation are not guaranteed.

## Connecting to the servers

!!! warning
    Since 1 August 2026, Xtra Computing servers are no longer reachable from the
    public network.

Connect through this path:

```text
NUS VPN  ->  SoC sjump (jump host)  ->  Xtra Computing server
```

1. Connect to the [NUS VPN](https://nusit.nus.edu.sg/services/wifi_internet/nvpn/).
2. SSH into the [SoC sjump](https://dochub.comp.nus.edu.sg/cf/services/network/sjump) jump host.
3. From sjump, SSH into the Xtra Computing server assigned to you.

## Server addresses

Prefer the published DNS hostnames over numeric IP addresses because the
addresses behind `*.ddns.comp.nus.edu.sg` may change.

### SoC private servers

| Server | SSH hostname | Resource or role | Notes |
|---|---|---|---|
| `xtra3090` | `xtra3090.ddns.comp.nus.edu.sg` | 8 × RTX 3090 |  |
| `xtrah100` | `xtrah100.ddns.comp.nus.edu.sg` | 4 × H100 |  |
| `xtrah200` | `xtrah200.ddns.comp.nus.edu.sg` | 4 × H200 |  |
| `xtraa100` | `xtraa100.ddns.comp.nus.edu.sg` | 8 × HGX A100 80 GB |  |
| `xtraa6k01` | `xtraa6k01.ddns.comp.nus.edu.sg` | 2 × A6000 48 GB |  |
| `xtraa6k02` | `xtraa6k02.ddns.comp.nus.edu.sg` | 2 × A6000 48 GB |  |
| `xtraa6k03` | `xtraa6k03.ddns.comp.nus.edu.sg` | 2 × A6000 48 GB |  |
| `xtraa6k04` | `xtraa6k04.ddns.comp.nus.edu.sg` | 2 × A6000 48 GB |  |
| `xtra-v80-0` | `xtra-v80-0.ddns.comp.nus.edu.sg` | Resource not recorded in the inventory | Confirm suitability with the administrator before use. |
| `xtra-v80-1` | `xtra-v80-1.ddns.comp.nus.edu.sg` | Resource not recorded in the inventory | Confirm suitability with the administrator before use. |
| `xacchead` | `xacchead.ddns.comp.nus.edu.sg` | HACC entry; 11 FPGA/AMD GPU nodes | Submit the [FPGA server account application](https://forms.gle/fvfPgJypd1sSWzHm8). |

## Locked out after failed logins

The servers block an IP address for **15 minutes** after **6 failed SSH login
attempts within 10 minutes**. If your login is suddenly refused after several
wrong passwords, wait 15 minutes before trying again. If you are still blocked
after that, contact the administrator.

## Responsible use of group resources

Please also observe these basic rules:

- Each user may use up to two GPUs concurrently by default without additional
  approval. Idle GPUs may be used opportunistically, but should be released
  proactively when other users need them.
- Home-directory quotas are normally 512 GiB for PhD students and 256 GiB for
  other users.
- `/shared/hdd` and `/shared/ssd`, where present, are shared storage. RAID is not
  a backup; keep an independent copy of important data.
- Do not run unauthorized scans, bypass monitoring or quotas, share accounts,
  or store credentials in code or shell history.
