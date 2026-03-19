# Mac Browser Automation (Physical Override)

## 简介 (Introduction)
这是一个专为 macOS 环境下 Chrome 浏览器设计的**物理级（硬件级）自动化操控技能**。

当遇到常规 JS 脚本（如 `click()`, `value = 'xxx'`）被带有严密防刷/反爬机制的网站（如 Bilibili、Waline 等使用 Vue/React 深层绑定的应用）拦截时，传统的自动化填表会失效（表现为输入内容无法保存、点击按钮无响应等）。

本技能通过**“降维打击”**的物理外挂方式，彻底绕过前端 DOM 层的安全限制：
1. **Shadow DOM 穿透定位**：利用 JavaScript 穿透 `Shadow Root`，精准捕捉深层元素的屏幕物理坐标 (X, Y)。
2. **物理鼠标点击**：通过 macOS 底层工具（如 `peekaboo`）直接在屏幕绝对坐标上模拟人类真实的鼠标点击事件（事件自带 `isTrusted: true`）。
3. **物理键盘输入**：借助 AppleScript 和 System Events 操作系统剪贴板，使用真实的 `Cmd+V` 组合键将文本“敲”进输入框。

## 使用场景 (Use Cases)
- **B 站自动评论/发弹幕**（绕过前端 `isTrusted` 检测）
- **高防系统表单填写**（绕过 Vue/React 的事件双向绑定检测）
- 一切阻挡自动化脚本执行的常规网页。

## 核心依赖 (Dependencies)
- **macOS** 操作系统
- **Google Chrome** 浏览器
- **AppleScript / osascript**（macOS 内置）
- **System Events** 权限（需在 Mac 设置中授予终端/终端模拟器控制权限）
- **peekaboo**（可选，用于执行精准坐标点击，亦可纯用 AppleScript 实现部分逻辑）

## 原理说明 (How it Works)

1. **获取屏幕绝对坐标**：
   网页内的 `getBoundingClientRect()` 获取的是相对窗口的坐标。我们需要加上浏览器的窗口偏移量：
   ```javascript
   var winX = window.screenX;
   var winY = window.screenY + (window.outerHeight - window.innerHeight); // 计算工具栏带来的偏差
   var finalX = rect.x + rect.width/2 + winX;
   var finalY = rect.y + rect.height/2 + winY;
   ```

2. **硬件级操控**：
   获取到准确坐标后，脱离浏览器上下文，在操作系统层面发起真实的鼠标移动与点击。接着通过模拟剪贴板粘贴（`keystroke "v" using {command down}`）完成文字输入。整个过程对目标网页而言，完全等同于人类用户的真实操作。

## 注意事项
在使用此技能期间，建议用户不要操作鼠标和键盘，以免打断自动化的物理焦点。