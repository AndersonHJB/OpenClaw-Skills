# github-skills-sync - 同步本地技能到 GitHub 仓库

**管理 OpenClaw 技能本地开发与远程 GitHub 仓库的双向同步工具。**

## 📌 技能位置
**统一管理目录**: `/Users/bornforthis/.openclaw/workspace/skills/github-skills-sync/`
**主仓库位置**: `/Users/bornforthis/OpenClaw-Skills/`

## 关联关系映射 (Mapping)
维护本地开发技能到 GitHub 仓库目录的对应关系：
- `feishu-image-sender` -> `/Users/bornforthis/OpenClaw-Skills/feishu-image-sender`
*(之后有新的 Skills 需要推送到 GitHub 时，会自动加到上面的列表中)*

## 使用场景
- 用户说："把这个技能推送到 github"
- 用户说："同步 skills"
- 用户更新了本地某个技能代码，希望做一键版本管理

## 工作流 (Workflow)
1. **对比同步**：使用 `rsync -av --delete --exclude='.git'` 自动将 `/Users/bornforthis/.openclaw/workspace/skills/[SKILL_NAME]/` 同步到 `/Users/bornforthis/OpenClaw-Skills/[SKILL_NAME]/`。
2. **Git 提交**：在 `/Users/bornforthis/OpenClaw-Skills/` 目录执行 `git add .`。
3. **Commit 描述生成**：根据变动内容或用户的指示生成语义化的 Commit Message。
4. **推送到远程**：执行 `git push origin main`。

## 示例命令
```bash
# 执行同步（调用该脚本并传入具体的技能名称或 all）
cd /Users/bornforthis/.openclaw/workspace/skills/github-skills-sync/
python3 sync.py feishu-image-sender "feat: update image processing logic"
```
