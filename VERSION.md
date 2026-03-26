# SilverJourney AI — 版本号管理

## 当前版本

| 字段           | 值       |
|----------------|----------|
| version        | 1.0.0    |
| versionCode    | 1        |
| releaseDate    | 2026-03-26 |
| minPlatformVer | 3.0.0    |

## 版本历史

### v1.0.0（2026-03-26）
- 首次正式发布
- 功能：三智能体推荐（HealthAgent + SafetyAgent + InterestAgent + Moderator）
- 功能：适老化首页（语音/文字输入、方言支持、健康档案）
- 功能：推荐结果页（综合评分卡片 + 出行包生成）
- 功能：行程规划页（PDF 导出）
- 功能：安全守护页（SOS + 紧急联系 + 附近医院）
- 功能：用户反馈页（评分 + 统计分析，分包加载）
- 性能：LazyCodeLoading 分包 + 图片懒加载 + 防抖节流
- 多语言：中文/英文 i18n 框架
- 离线地图：瓦片缓存 + createMapContext 封装

## 版本号规范

格式：`MAJOR.MINOR.PATCH`

- **MAJOR**：不兼容的接口变更（Agent 协议升级、数据库 schema 变更）
- **MINOR**：向后兼容的新功能（新 Agent、新页面、新语言包）
- **PATCH**：向后兼容的 bug 修复（样式调整、文案更新、逻辑修复）

## 发布 Checklist

发布前必须完成以下检查（CI/CD 将自动验证带 ✅ 的项目）：

### 代码质量
- [ ] ✅ `pytest tests/` 全部通过
- [ ] ✅ `python -m py_compile` 无语法错误
- [ ] ✅ 微信开发者工具"体验版"跑完主流程无报错

### 功能验证
- [ ] 首页语音/文字输入正常
- [ ] 推荐引擎三智能体评分有效（非全零/全满）
- [ ] 推荐页跳转反馈页正常（分包加载）
- [ ] 行程页 PDF 导出可下载
- [ ] 安全守护页 SOS 按钮逻辑正常
- [ ] 反馈页提交后统计数据更新

### 性能
- [ ] ✅ 小程序包体积 < 2 MB（主包）
- [ ] ✅ 分包体积各 < 2 MB
- [ ] 首屏渲染 < 2s（弱网 3G 模拟）

### 文档
- [ ] ✅ README.md 版本号已更新
- [ ] ✅ CHANGELOG.md 已追加本版本记录
- [ ] API 文档（api_server.py Swagger）已更新
