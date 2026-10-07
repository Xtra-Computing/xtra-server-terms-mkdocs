# Disk Storage

## Disk Space Allocation

| User Category          | `home` Disk Quota |
|------------------------|-----------------|
| PhD Students           | 512 GiB         |
| Others | 256 GiB         |

Additional disk space requests are possible via email to the administrator and are considered based on project justification and resource availability.

For hosting large datasets, please contact the administrator. Dataset hosting will not count against your quota.

## Data Integrity

Data integrity is **not** guaranteed. Users must perform regular backups. Weekly backups are recommended, with more frequent backups suggested for critical data. The `/shared/hdd` and `/shared/ssd` directories use RAIDZ2 for fault tolerance against up to two drive failures. RAIDZ2 is **not a backup** and does not protect against every form of data loss. There is currently no per-user quota on these shared directories; please use them responsibly.

!!! info "Important"
    Backup responsibility belongs to the user. Always maintain restorable checkpoints for critical work.

## Privacy

Administrators may collect and review necessary access, security, audit, system, and resource-usage logs and metrics for operations, security, capacity planning, incident response, and policy enforcement. Administrators may also review files when investigating incidents, abnormal resource usage, security concerns, or suspected policy violations. By using the servers, users consent to this monitoring and review.

**Do not** store private or sensitive files (e.g., personal photos, videos, confidential documents).

## Disk Usage Accounting

Disk usage is tracked monthly (GB/month) across all servers, attributed uniquely per user. High usage users may be contacted to reduce disk usage.
