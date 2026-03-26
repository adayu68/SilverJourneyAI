# Changelog — SilverJourney AI

所有版本的重要变更记录于此文件，格式遵循 [Keep a Changelog](https://keepachangelog.com/zh-CN/)。

---

## [1.0.0] — 2026-03-26

### 新增
- 三智能体评分引擎（HealthAgent / SafetyAgent / InterestAgent）+ Moderator 裁判器
- BaseAgent 抽象基类，统一 `assess()` / `score_to_stars()` / `batch_assess()` 接口
- 适老化微信小程序（语音输入、方言选择、大字体高对比度）
- 多语言 i18n 框架（中文 + 英文，支持系统语言自动检测）
- 离线地图支持（瓦片 LRU 缓存 + `wx.createMapContext` 封装）
- 性能优化模块（防抖/节流/图片懒加载/LazyCodeLoading 分包）
- 用户反馈页（星级评分 + 维度标签 + 统计分析视图，分包加载）
- PDF 行程导出（ReportLab 生成，含健康提示/安全提示）
- 完整 pytest 单元测试套件（tests/ 目录，覆盖三智能体 + Moderator + PDF）
- GitHub Actions CI/CD 流水线（测试 → 代码检查 → 构建报告）

### 技术架构
- 后端：Flask API + SQLite（silverjourney.db）
- 前端：微信小程序（原生 WXML/WXSS/JS）
- AI 层：Python 规则引擎（无依赖外部大模型）
- 分包：`packageFeedback`（反馈页）/ `packageDetail`（POI 详情页）

---
