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
   For FPGA servers, submit the [FPGA server account application](https://forms.gle/fvfPgJypd1sSWzHm8).
3. Wait for confirmation. **After approval, you will receive a separate email
   with your username, password, server addresses, and the resources on each
   server.** These details are confidential. Do not share them.
4. Log in using SSH and complete the first-login checks in this guide.
5. Keep independent backups of important data and checkpoint long-running jobs.
   Server storage and uninterrupted computation are not guaranteed.

## Connecting to the servers

!!! warning
    [Since 29 June 2026](https://dochub.comp.nus.edu.sg/cf/tech/network/security-2026-06), Xtra Computing servers are no longer reachable from the
    public network.

    > All inbound SSH to Research Server computers must be from within NUS. NUS
    > users who are outside NUS must use NUS VPN. Non-NUS users must obtain a NUS
    > visitor account from their NUS host to use NUS VPN.

Connect through this path:

**[NUS VPN](https://nusit.nus.edu.sg/services/wifi_internet/nvpn/) → [SoC sjump](https://dochub.comp.nus.edu.sg/cf/guides/sjump/start) (jump host) → Xtra Computing server**

1. Connect to the [NUS VPN](https://nusit.nus.edu.sg/services/wifi_internet/nvpn/).
2. SSH into the [SoC sjump](https://dochub.comp.nus.edu.sg/cf/guides/sjump/start) jump host.
3. From sjump, SSH into the Xtra Computing server assigned to you.

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
