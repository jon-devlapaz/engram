---
name: web-article-reader
description: "文章抓取阅读器 (Article-Reader) - 根据 URL 自动选择最佳抓取方式，将网页文章内容提取为干净的 Markdown 并保存到本地。当用户说'帮我读一下'并附带一个链接时触发此 skill。支持微信公众号文章、X (Twitter) 推文/长文、以及其他通用网页链接。对于 x.com/twitter.com 链接使用 fxtwitter API（备用 Playwright）；对于微信公众号链接使用 Playwright 本地抓取；对于其他链接优先使用 Jina Reader，失败则降级为 Playwright。"
---

# 文章抓取阅读器 (Article-Reader)

## 工作流程

当用户输入"帮我读一下 [URL]"时，按以下流程执行：

### 第一步：首次使用时询问保存路径

如果是第一次使用此 skill，询问用户希望将抓取的文章保存到哪个目录。将用户回答记住用于后续所有抓取。

默认推荐路径：`/Users/tal/Documents/Obsidian/Inbox`

### 第二步：识别链接类型并选择抓取策略

根据 URL 域名自动路由：

| URL 匹配规则 | 抓取策略 |
|---|---|
| `x.com/*` 或 `twitter.com/*` | **X 平台策略**：运行 `scripts/scrape_tweet.py` |
| `mp.weixin.qq.com/*` | **微信策略**：运行 `scripts/fetch_wechat.py` |
| 其他所有链接 | **通用策略**：先用 Jina Reader，失败则用 Playwright |

#### X 平台策略

1. 主要方式：通过 fxtwitter API 获取（无需认证，速度快）
2. 备用方式：通过 Playwright 模拟浏览器（当 API 失败时自动降级）

执行命令：
```bash
python3 <skill_path>/scripts/scrape_tweet.py <URL>
```

#### 微信公众号策略

通过 Playwright 模拟移动端浏览器打开页面提取：

执行命令：
```bash
python3 <skill_path>/scripts/fetch_wechat.py <URL>
```

#### 通用网页策略

1. **优先 Jina Reader**：使用 WebFetch 工具访问 `https://r.jina.ai/<URL>`，prompt 设为 "Extract the full article content in markdown format, preserving all text, headings, and structure"
2. **降级 Playwright**：如果 Jina Reader 失败或返回内容不完整，使用 `scripts/fetch_wechat.py` 的 Playwright 逻辑作为降级方案

### 第三步：语言检测与翻译

抓取完成后，自动判断文章语言：

1. **检测方式**：检查抓取到的正文内容，如果英文字符占比超过 50%，判定为英文文章
2. **英文文章处理**：将全文翻译为中文后再保存。翻译要求：
   - 保留 Markdown 格式（标题、加粗、链接、图片等不变）
   - 保留专有名词、品牌名、技术术语的英文原文，可在首次出现时括号标注中文
   - 译文自然流畅，符合中文阅读习惯
   - 文章标题也翻译为中文
3. **中文文章处理**：直接进入下一步，无需翻译

### 第四步：保存文件

- 将最终的 Markdown 内容（如为英文则是翻译后的版本）保存到用户指定的目录
- 文件名使用文章标题（如已翻译则用中文标题，清理不安全字符）
- 格式：`{标题}.md`

### 第五步：展示结果

保存成功后，向用户展示：
1. 文章标题（如有翻译则同时展示原标题）
2. 作者（如有）
3. 保存路径
4. 文章内容的前 500 字作为预览
5. 如进行了翻译，标注"已从英文自动翻译"

## 注意事项

- `<skill_path>` 指的是此 skill 所在目录的实际路径，即包含此 SKILL.md 的目录
- 脚本需要 Playwright 已安装（`pip install playwright && playwright install chromium`）
- Jina Reader 无需额外安装，通过 WebFetch 工具的 URL 前缀方式调用
- 如果所有方式都失败，告知用户并建议手动复制内容
