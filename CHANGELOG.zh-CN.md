# Claude Code 更新日志（非官方简体中文翻译）

> Unofficial translation of the [Claude Code CHANGELOG](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md). Not affiliated with Anthropic. Original © Anthropic PBC. Machine-translated; the English original is authoritative.

## 2.1.294 (2026-10-08)

- 修复了以指令形式编写（例如 "Block commands that..."）的 `prompt` 和 `agent` hook 放行了本应拦截操作的问题
- 优化了 Stop 和 SubagentStop 上以指令形式编写（例如 "Carry on if the build is broken"）的 `prompt` hook 的判定逻辑，降低了 Claude 过早停止的可能性

## 2.1.293 (2026-10-07)

- 新增 Claude Haiku 5.5（`claude-haiku-5-5`），现已成为 Anthropic API 上的默认 Haiku 模型——1M 上下文，每 Mtok $0.10/$0.50（超过 100K 的 prompt 为 $0.50/$2.50）
- 在 `subagentStatusLine` 负载中新增 `agentType`，以便脚本区分自定义 subagent 类型
- 为 mod 在 `$.tool.register` 中新增 `isDeferred`：设为 `false` 可在 prompt 中一开始就列出工具的 schema，而不是隐藏在工具搜索之后
- 修复了 Claude 有时将上下文压缩前的最后操作误认为是在压缩后完成的，从而撤销或重做已完成工作的问题
- 修复了 HTTP MCP 连接在关闭前会保留其发送过的每个请求从而导致的内存泄漏问题
- 修复了在 Claude 运行期间发送的消息在按下 `←` 将会话切到后台时丢失的问题；若排队中的消息无法迁移，`←` 现在会保持在当前界面并提示
- 修复了 `/model` effort 在使用 ←/→ 时会循环越过最高或最低级别，可能导致意外将 Low 保存为模型默认 effort 的问题
- 修复了 `/tui` 在使用 `--chrome` 启动的会话中会断开 Claude in Chrome 连接、以及忽略 `--no-chrome` 的问题
- 修复了在宿主、权限规则或 `--tools` 列表移除了 `SendMessage` 工具的会话（包括恢复的会话）中，Claude 仍被提示继续或使用该工具向 subagent 发送消息的问题
- 修复了当某个内置工具仅被 subagent 或 `--agent` 会话自身的工具列表排除时，系统却提示该工具在整个会话中均已禁用的问题
- 修复了与 claude.ai 同步的 skill 在编辑描述后，有时直到新会话或执行 `/clear` 才能被模型感知的问题
- 修复了在登录已过期或即将过期时，运行 `claude logs`、`stop`、`kill`、`rm` 以及 `claude daemon status`、`stop`、`uninstall` 有时会导致退出的问题
- 修复了因临时无法读取 sessions 目录（例如打开文件数过多）导致页脚的 agents 计数消失的问题
- 修复了名为 `worker` 的自定义 agent 在启动时显示为 "Agent"，以及在 agent 结束后详情弹窗标题丢失 agent 类型的问题
- 修复了在发布调用仍在流式传输时，Artifact 工具的 transcript 行短暂显示为 `Artifact("(unprintable path)")` 的问题
- 修复了在 Linux 上运行沙箱命令时，`/ultrareview` 上传因配置文件 "could not be parsed" 而错误拒绝某些仓库（如嵌套在另一个检出目录中的仓库）的问题
- 修复了 `/ultrareview` 上传因 split-index 文件拒绝时，建议执行的 git 命令可能导致 git 无法读取其索引的问题
- 修复了在超长 Remote Control 和云端会话中回复仍可能整块出现而非流式输出的问题
- 修复了 Remote Control 在每次凭据恢复后重新上传会话初始历史记录的问题
- 修复了在通过 `claude remote-control` 启动的会话中 PushNotification 报错 "Remote Control inactive" 的问题
- 修复了插件 hook worker 重启期间 mod 针对 `classic.*` 事件的 hook 被跳过，导致 settings hook 在缺少它们的情况下响应的问题
- 修复了调用 `$.session.append` 的 mod 运行 `claude plugin test` 失败的问题；测试现在可以使用新的 `mock.session` 读回追加的行
- 修复了在装有 Docker Desktop 的 Mac（链接位于 `~/.docker/bin` 下）上 `claude plugin eval` 拒绝所有授予 Bash 权限的运行的问题；拒绝信息现在会指明凭据存储中包含该链接的具体位置
- 修复了当 `desktop` 策略配置了 Claude Desktop 内置浏览器键（如 `builtinBrowserEnabled`）时 Claude apps 网关拒绝启动的问题
- 修复了当授权仅保存在 `.claude/settings.local.json` 或 `--settings` 文件中时，`claude agents` 提供的 bypass 权限会被后台会话忽略的问题；现在会优先请求授权，且忽略 bypass 的会话会显示常驻的简短提示
- 修复了在输入框有未发送文本或等待回答提问时，按下 `←` 会在 10 秒后将自身切到后台的问题（现在会取消切换）
- 修复了在刚按下 `←` 将会话切到后台时，在权限提示中按 Esc 或选择不带反馈的 No 无法停止当前轮次的问题
- 修复了当 sessions 目录无法读取时（例如打开文件数过多），agents 视图短暂将整个会话列表替换为占位行的问题
- 修复了当 Claude 使用 Bash 工具中的单文件 cat、head、tail、sed -n 或 grep 命令而非 Read 工具查看文件时，路径作用域规则和嵌套的 CLAUDE.md 文件未加载的问题
- 修复了开头和结尾词语相同的粘贴文本有时会被误当作手动键入内容发送给 Claude 的问题
- 修复了粘贴文本中的 skill 名称在紧随其后键入或粘贴的重音符号与其最后一个字母合并时，被误当作手动键入的问题
- 修复了在报告发送期间按 Ctrl+O 或 Ctrl+Z 会导致 `/feedback` 返回草稿列表，从而无法取消发送的问题
- 修复了当文件或文件夹无法删除时 `claude purge` 静默停止（退出码 0 或终端卡死）的问题；现在会删除其余内容，列出无法删除的项，并以退出码 1 退出
- 修复了 keybindings.json 校验：单独的 " "（空格键）不再报错，且像 "ctrl+ k" 这样的按键现在会收到警告
- 修复了 vim 模式下在仅包含空格的行上执行 `>>` 和 `<<` 会导致光标超出行尾、进而导致随后的 `x` 无法删除任何内容的问题
- 修复了 vim 模式：在 Visual 模式下删除整行（`V` 后按 `d`）后光标落在首个非空字符上，且随后的 `.` 会作用于光标所在行
- Windows：修复了停止状态行、hook 或 shell 命令时有时会终止分配了相同进程 ID 的无关进程的问题
- 还原了 2.1.281 中关于 auto 模式拒绝消息的更改（该更改曾提示 Claude 拒绝涵盖整个执行结果，而不仅是具体命令）
- 还原了 2.1.290 中针对容器重启丢失未决的 `/loop` 唤醒或计划任务后云端会话保持休眠的修复；不再通知 Claude，会话继续保持休眠
- 改进了 Team 和 Enterprise 组织的启动体验：策略和托管设置获取时机提前，卡住的请求将在 3 秒后重试
- 改进了 Claude in Chrome：当浏览器上报标签页较慢时，被拒绝的页面操作更少
- 改进了云端会话中无法连接浏览器时 Claude in Chrome 的提示信息：若您属于多个组织，现在会提示插件必须登录到同一组织，并说明如何更改
- 改进了 Bash 编辑 diff 提示，注明所列文件在命令运行期间发生变化（可能包含其他进程的写入）
- 改进了 artifact：Claude 会将库固定为两周或更早以前发布的精确版本
- 更改了 claude.ai skill 同步策略：在没有会话使用时，检查变更的频率从每 10 分钟一次调整为约每 40 分钟一次
- 更改了向模型宣告的 agent 列表和 MCP 服务的排序：包含非 ASCII 字符的名称现在排在 ASCII 名称之后
- 更改了 OpenTelemetry `claude_code.at_mention` 日志：每次读取 prompt 最多发送 100 个 agent 和 100 个 MCP-resource 事件
- Self-hosted runner：将编排器的轮询间隔从固定的 5 秒改为 4 至 6 秒休眠，避免同一环境的多个副本在同一时刻轮询
- [Claude Tag] 修复了跨工作区共享的 Enterprise Grid 频道中，当 Slack 标记的消息来自未连接的工作区时，Claude in Slack 提示工作区尚未设置的问题
- [Claude Tag] 修复了管理员修改频道的 connector、plugin、skill 或 rule 时，Claude in Slack 在该频道中途停止任务的问题；更改现在将在 Claude 完成后生效
- [Claude Tag] 修复了要求 Claude in Slack 附带额外备注立即运行线程例行任务时会启动无法发回消息的独立运行的问题；该运行现在会在该线程内继续进行
- [Claude Tag] 修复了在 Claude Tag 管理员设置中，访问捆绑包的 Add a connector 对话框在完成一次 Google 登录后将所有 Google connector 显示为已连接的问题
- [Claude Tag] 改进了 Claude Tag 管理员设置，列出尚未连接的 Enterprise Grid 并提供 Connect 按钮
- [Claude Tag] 更改了 Claude in Slack 加入仅管理员可发帖的公告频道的行为：加入时不再发送自我介绍消息
- [Claude Tag] 在 Claude Tag 管理员设置中，将每个工作区以及全组织 Slack 页面的频道规则数量限制从 20 提高到 50
- [Code Review] 改进了 Code Review 的 Add a repository 对话框，列出无法添加的各个仓库及其原因（如缺少 GitHub 写入权限）
