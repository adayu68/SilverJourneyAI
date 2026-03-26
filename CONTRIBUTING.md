# 贡献指南 — SilverJourney AI

感谢您有意为 **SilverJourney AI** 做出贡献！🎉

无论是修复一个 Bug、添加一个城市的 POI 数据、改善适老化 UI，还是优化 Agent 算法，所有贡献都弥足珍贵。本文档将帮助您快速上手。

---

## 📋 目录

- [行为准则](#行为准则)
- [贡献方式](#贡献方式)
- [开发环境配置](#开发环境配置)
- [分支与提交规范](#分支与提交规范)
- [提交 Pull Request](#提交-pull-request)
- [代码规范](#代码规范)
- [测试要求](#测试要求)
- [添加 POI 数据](#添加-poi-数据)

---

## 行为准则

参与本项目即表示您同意遵守我们的 [行为准则](CODE_OF_CONDUCT.md)。  
我们致力于为所有参与者创造一个友好、包容的环境。

---

## 贡献方式

| 贡献类型 | 说明 | 门槛 |
|---------|------|------|
| 📍 **POI 数据** | 为更多城市贡献适老化景点数据 | 🟢 无需编程经验 |
| 🐛 **Bug 修复** | 修复 [Issues](../../issues?q=is:issue+label:bug) 中的已知问题 | 🟡 中等 |
| 📝 **文档改进** | 完善 README、注释、Wiki | 🟢 低 |
| 🌏 **翻译/方言** | 新增语言包或扩展方言支持 | 🟡 中等 |
| 🎨 **UI 优化** | 改进适老化界面设计 | 🟡 中等 |
| 🤖 **Agent 增强** | 改进三智能体评分算法 | 🔴 较高 |
| 📡 **API 集成** | 接入高德地图、天气等数据源 | 🔴 较高 |

---

## 开发环境配置

### 1. Fork & Clone

```bash
# 1. 在 GitHub 点击右上角 "Fork" 按钮
# 2. Clone 您的 Fork
git clone https://github.com/YOUR_USERNAME/SilverJourneyAI.git
cd SilverJourneyAI
```

### 2. 安装依赖

```bash
# 推荐使用虚拟环境
python -m venv venv
source venv/bin/activate      # macOS/Linux
venv\Scripts\activate         # Windows

# 安装依赖
pip install -r requirements.txt
pip install pytest pytest-cov flake8   # 开发工具
```

### 3. 验证安装

```bash
# 运行测试，确认环境正常
pytest tests/ -v

# 启动 Web 版
python start.py
```

---

## 分支与提交规范

### 分支命名

```
feature/add-guangzhou-pois      # 新功能
fix/safety-agent-score-bug      # Bug 修复
docs/update-api-documentation   # 文档
refactor/health-agent-logic     # 重构
```

### Commit Message 格式

遵循 [Conventional Commits](https://conventionalcommits.org/)：

```
<类型>(<范围>): <简短描述>

[可选的详细描述]

[可选的 Breaking Change 或 Issue 关联]
```

**类型列表：**

| 类型 | 用途 |
|------|------|
| `feat` | 新功能 |
| `fix` | Bug 修复 |
| `docs` | 仅文档变更 |
| `style` | 代码格式（不影响功能） |
| `refactor` | 重构（非新增功能，非Bug修复） |
| `test` | 新增或修改测试 |
| `chore` | 构建过程或辅助工具变更 |
| `data` | POI 数据新增或修改 |

**示例：**

```bash
git commit -m "feat(poi): 添加广州20个适老化景点数据"
git commit -m "fix(safety-agent): 修复医疗距离为空时的崩溃问题"
git commit -m "docs: 补充 API Server 接口说明"
```

---

## 提交 Pull Request

### PR 前检查清单

```bash
# ✅ 1. 所有测试通过
pytest tests/ -v

# ✅ 2. 无语法错误
python -m py_compile $(find . -name "*.py" -not -path "./.venv/*")

# ✅ 3. 代码风格检查（警告可接受，错误须修复）
flake8 silverjourney/ app.py api_server.py --max-line-length=100

# ✅ 4. 微信小程序（如修改了小程序代码）
#    在微信开发者工具中编译无报错
```

### PR 描述模板

提交 PR 时请说明：

- **改动内容**：做了什么？
- **为什么这样做**：解决了什么问题？
- **测试方式**：如何验证改动有效？
- **截图**（如涉及 UI 变化，请附前后对比图）

---

## 代码规范

### Python

- 遵循 **PEP 8**，单行最大长度 100 字符
- 函数和类必须有 **docstring**
- 复杂逻辑请添加行内注释（中文注释优先）
- Agent 类必须继承 `BaseAgent` 并实现 `assess()` 接口

```python
# ✅ 好的示例
def assess(self, profile: HealthProfile, poi: POIHealthData) -> HealthAssessmentResult:
    """
    评估用户健康画像与POI的康养适配度。
    
    Args:
        profile: 用户健康画像，包含年龄、慢性病、行动能力等信息
        poi: POI的健康适配数据，包含步行量、台阶数等指标
    
    Returns:
        HealthAssessmentResult: 包含康养指数和详细健康建议
    """
    ...
```

### 微信小程序

- JS 文件函数必须有注释说明用途
- 避免使用 `console.log` 提交（调试完请删除）
- 页面数据初始化必须在 `data` 中声明
- 适老化要求：最小字号 32rpx，最小点击区域 88rpx

---

## 测试要求

- 新功能必须附带 **单元测试**（位于 `tests/` 目录）
- 测试文件命名：`test_<模块名>.py`
- 目标覆盖率：**> 80%**
- Agent 测试须覆盖：正常场景、边界条件（空数据/极值）

```python
# 测试示例
def test_health_agent_high_stairs_filter():
    """台阶数超过用户承受能力时应降低评分"""
    profile = HealthProfile(user_id="test", mobility_score=2.0)
    poi = POIHealthData(stair_count=500, ...)
    result = health_agent.assess(profile, poi)
    assert result.score < 3.0, "高台阶应导致低评分"
```

---

## 添加 POI 数据

这是最欢迎的贡献类型，**无需编程经验**！

### 数据格式

参考 `silverjourney/database/seed_data.py` 中的现有数据格式：

```python
{
    "poi_id": "poi_guangzhou_001",
    "name": "白云山风景区",
    "city": "广州",
    "province": "广东",
    "address": "广州市白云区广园中路白云山风景区",
    "latitude": 23.1667,
    "longitude": 113.2833,
    "category_tags": ["山水", "公园", "休闲"],
    "has_wheelchair_access": True,
    "has_elevator": False,
    "has_rest_area": True,
    "rest_area_count": 20,
    "estimated_daily_steps": 6000,   # 步/天
    "stair_count": 200,
    "nearest_hospital_km": 3.5,
    "nearest_hospital_name": "广州市第一人民医院",
    "wellness_index": 3.8,           # 0-5，您的主观评估
    "popularity": 0.85,              # 0-1，知名度
    "ticket_price": 0,               # 元，0表示免费
    "open_hours": "06:00-21:00",
    "description": "适合老年人晨练和休闲散步，有多条缓坡路线...",
    "image_url": ""
}
```

### 提交方式

1. 直接编辑 `silverjourney/database/seed_data.py`，在 `POI_DATA` 列表末尾添加数据
2. 或者，通过 **Issue** 提交数据（使用 POI 贡献模板），由维护者代为添加

---

## 🙋 有问题？

- 查看 [已有 Issues](../../issues) 看是否已有解答
- 提交新 [Issue](../../issues/new/choose) 描述您的问题
- 项目维护者会在 **3个工作日内** 回复

感谢您让银发旅游变得更美好！❤️
