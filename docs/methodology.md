# Methodology

How we run the Xtra Computing servers, and the reasons behind the rules.

## Why we deploy monitoring probes

The servers are shared by a growing number of users. Some jobs hold GPUs,
memory, or CPU for long periods without regard to other users, and on a shared
machine one such job can leave everyone else waiting.

Monitoring probes on each server record resource usage per user. This lets us:

- see who is using which resources, so allocation stays fair;
- find the source of a problem quickly when a server becomes slow or unusable;
- apply the rules in the [Terms of Use](terms.md) consistently, based on
  recorded data, including [automatic termination](terms.md#automatic-termination-policy).

What is collected and how it is used is described under
[Privacy](disk.md#privacy).

## Why we use Apptainer

Docker access for regular users was removed by default from 2026-09-30.
Containers now run with [Apptainer](apptainer.md), for two reasons:

- **Security.** Membership in the `docker` group is effectively root access on
  the host. Apptainer runs containers as your own user, with no daemon and no
  root-equivalent group.
- **Resource accounting.** Workloads inside Docker are invisible to per-user
  memory and GPU accounting, and single users have taken whole servers down this
  way. Apptainer workloads stay visible to the same accounting as any other
  process you run.

See [Containers: Docker Deprecation and Apptainer](apptainer.md) for migration
instructions.
