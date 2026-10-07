# Xtra Computing 服务器新人使用指南

本文帮助新同学从申请账号走到成功建立 SSH 会话，仅介绍普通用户接入。

!!! info "重要"
    获得 Xtra 账号不代表自动获得所有机器的权限。请仅使用管理员明确分配或授权的服务器。

## 从申请到可用的完整步骤

1. 阅读并接受[服务器使用条款](terms.md)，特别是 GPU、存储、备份、
   安全和账号到期规则。
2. 填写 [Xtra 服务器账号申请表](https://forms.gle/Wf8qbNeuSPS2ia8u6)。
   如需使用 FPGA 服务器，请填写 [FPGA 服务器账号申请表](https://forms.gle/fvfPgJypd1sSWzHm8)。
3. 等待管理员确认。申请通过后，您会收到一封单独的邮件，包含用户名、密码、服务器地址以及各服务器拥有的资源。
4. 使用 SSH 登录，并完成本文的首次登录检查。
5. 为重要数据保留独立备份，为长任务保存 checkpoint。服务器不保证数据持久性，
   也不保证计算任务不中断。

## 连接服务器

!!! warning "警告"
    自 2026 年 8 月 1 日起，Xtra Computing 服务器不再提供公网访问。

请按以下路径连接：

```text
NUS VPN  ->  SoC sjump 跳板机  ->  Xtra Computing 服务器
```

1. 连接 [NUS VPN](https://nusit.nus.edu.sg/services/wifi_internet/nvpn/)。
2. SSH 登录 [SoC sjump](https://dochub.comp.nus.edu.sg/cf/services/network/sjump) 跳板机。
3. 从 sjump 再 SSH 登录分配给你的 Xtra Computing 服务器。

## 服务器地址

本站不公开服务器地址。申请通过后，您会收到一封单独的邮件，告知您可使用的服务器地址及各服务器拥有的资源。

!!! danger "保密"
    服务器地址与资源信息属于保密内容，请勿泄露。

## 登录失败被封禁

10 分钟内 SSH 登录失败 **6 次**，服务器会封禁该 IP 地址 **15 分钟**。如果多次输错密码后突然无法登录，请等待 15 分钟再试。若之后仍无法登录，请联系管理员。

## 负责任地使用组内资源

同时确认以下基本规则：

- 每位用户默认可同时使用最多 2 块 GPU，无需额外申请。空闲 GPU 可机会性使用，但在其他用户需要时应主动释放。
- 博士生的 home 配额通常为 512 GiB，其他用户通常为 256 GiB。
- 如果服务器上存在 `/shared/hdd` 和 `/shared/ssd`，它们是共享存储。RAID 不是备份，重要数据必须另存一份独立副本。
- 不得进行未经授权的扫描、绕过监控或配额、共享账号，或把凭据写入代码和 shell 历史。
