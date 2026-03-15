---
name: feishu-share-link
description: 飞书专属分享链接生成规范。当生成文档、多维表格、知识库等链接时，必须使用此规则构建专属企业域名的分享链接。支持多租户动态读取。
---

# 飞书专属分享链接生成规范 (Feishu Share Link)

## 📌 核心规则
在向用户发送飞书文件（文档、多维表格、知识库、电子表格等）的分享链接时，**严禁使用默认的 `feishu.cn` 根域名**。
必须使用当前企业/租户的专属域名前缀。

## 🔍 获取专属域名的方法
作为大模型，当你准备生成链接时，请执行以下步骤获取当前用户的专属域名：
1. 读取 `~/.openclaw/workspace/TOOLS.md`，查找是否有类似 `Feishu Custom Domain: xxx.feishu.cn` 的记录。
2. 如果有，使用该域名拼接链接。
3. 如果没有，优先询问用户其飞书企业专属域名前缀是什么，或者提示用户将前缀写入 `TOOLS.md`。如果用户未提供，则暂时使用 `feishu.cn` 作为兜底方案。

## 🔗 各类型链接拼接格式
假设获取到的专属域名为 `{CUSTOM_DOMAIN}`（例如 `czpn2fds56.feishu.cn`）：

### 1. 多维表格 (Bitable)
- **格式**: `https://{CUSTOM_DOMAIN}/base/{APP_TOKEN}?from=from_copylink`

### 2. 新版云文档 (Docx)
- **格式**: `https://{CUSTOM_DOMAIN}/docx/{DOC_TOKEN}`

### 3. 知识库 (Wiki)
- **格式**: `https://{CUSTOM_DOMAIN}/wiki/{WIKI_TOKEN}`

### 4. 电子表格 (Sheet)
- **格式**: `https://{CUSTOM_DOMAIN}/sheets/{SPREADSHEET_TOKEN}`
