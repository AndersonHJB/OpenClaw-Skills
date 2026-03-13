# feishu-image-sender - 飞书图片发送技能

## 概述
这是一个专门用于发送图片到飞书的技能，支持系统截图和本地图片发送功能。

## 技能组成
包含三个主要工具：
1. **feishu-image-screenshot** - 系统截图并发送
2. **feishu-image-send** - 发送指定图片文件
3. **feishu-image-interactive** - 交互式区域截图

## 使用方法

### 1. 系统截图并发送
```bash
cd "/Users/bornforthis/.openclaw/skills/feishu-image-screenshot" && ./screenshot.sh
```
- 功能：截取整个屏幕并发送到飞书
- 特点：自动保存到工作空间，自动发送

### 2. 发送指定图片
```bash
cd "/Users/bornforthis/.openclaw/skills/feishu-image-send" && ./send.sh /path/to/image.png
```
- 功能：发送指定的本地图片文件
- 参数：需要提供图片的完整路径
- 特点：自动复制到工作空间并发送

### 3. 交互式截图
```bash
cd "/Users/bornforthis/.openclaw/skills/feishu-image-interactive" && ./interactive.sh
```
- 功能：交互式选择区域截图
- 特点：用户可以手动选择要截图的区域

## 核心功能

### 系统截图功能
- 使用 macOS 原生 screencapture 命令
- 支持 PNG 格式，保持最佳质量
- 自动时间戳命名，避免文件冲突
- 自动保存到工作空间目录
- 自动调用 message 工具发送到飞书

### 图片发送功能
- 支持多种图片格式（PNG、JPEG、GIF等）
- 自动复制文件到工作空间
- 使用标准化的 message 工具发送
- 支持批量发送（通过循环调用）

### 交互式功能
- 支持用户手动选择截图区域
- 提供友好的交互提示
- 支持取消操作

## 最佳实践

### 1. 截图发送
```bash
# 推荐使用方式
cd "/Users/bornforthis/.openclaw/skills/feishu-image-screenshot" && ./screenshot.sh
```

### 2. 发送本地图片
```bash
# 发送桌面上的图片
cd "/Users/bornforthis/.openclaw/skills/feishu-image-send" && ./send.sh ~/Desktop/screenshot.png

# 发送下载的图片
cd "/Users/bornforthis/.openclaw/skills/feishu-image-send" && ./send.sh ~/Downloads/image.jpg
```

### 3. 交互式截图
```bash
# 需要选择特定区域时使用
cd "/Users/bornforthis/.openclaw/skills/feishu-image-interactive" && ./interactive.sh
```

## 技术特点

### 标准化流程
1. 截图 → 保存到临时目录
2. 复制到工作空间目录
3. 调用 message 工具发送
4. 清理临时文件

### 错误处理
- 检查文件是否存在
- 验证文件路径有效性
- 提供友好的错误提示

### 自动化
- 自动时间戳命名
- 自动文件路径处理
- 自动清理临时文件
- 自动发送到飞书

## 支持的图片格式
- PNG（推荐，无损压缩）
- JPEG（有损压缩，适合照片）
- GIF（动图支持）
- WebP（现代格式）
- BMP（无压缩）

## 注意事项

1. **文件路径**：必须使用完整路径
2. **文件权限**：确保有读取权限
3. **文件大小**：建议不超过10MB
4. **工作空间**：文件必须保存到工作空间目录
5. **系统兼容性**：目前仅支持macOS系统

## 示例应用

### 快速截图分享
```bash
# 截图并发送
cd "/Users/bornforthis/.openclaw/skills/feishu-image-screenshot" && ./screenshot.sh
```

### 发送设计稿
```bash
# 发送设计图片
cd "/Users/bornforthis/.openclaw/skills/feishu-image-send" && ./send.sh ~/Design/mockup.png
```

### 问题截图
```bash
# 截取错误界面
cd "/Users/bornforthis/.openclaw/skills/feishu-image-interactive" && ./interactive.sh
```

## 故障排除

### 常见问题
1. **截图失败**：检查 screencapture 命令是否可用
2. **发送失败**：检查工作空间目录权限
3. **文件不存在**：检查图片路径是否正确

### 解决方案
1. 使用完整路径：`/usr/sbin/screencapture`
2. 检查文件权限：`chmod +x script.sh`
3. 验证工作空间路径

---

**总结**：这个技能提供了标准化的飞书图片发送流程，支持三种主要使用场景，确保图片发送的稳定性和可靠性。