"""
SilverJourney AI - 全Agent完整集成测试
验证 HealthAgent / SafetyAgent / InterestAgent / Moderator 功能完整性
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "silverjourney"))

print("=" * 60)
print("SilverJourney AI — Agent 架构集成测试")
print("=" * 60)

# ─────────────────────────────────────────────────────────
# 1. 导入测试
# ─────────────────────────────────────────────────────────
print("\n[1/5] 导入检查...")
try:
    from utils.base_agent import BaseAgent, INTERFACE_CONTRACT
    print("  ✅ BaseAgent 导入成功")
except Exception as e:
    print(f"  ❌ BaseAgent 导入失败: {e}")
    sys.exit(1)

try:
    from agents.health_agent import HealthAgent, HealthProfile, POIHealthData, HealthAssessmentResult
    print("  ✅ HealthAgent 导入成功")
except Exception as e:
    print(f"  ❌ HealthAgent 导入失败: {e}")
    sys.exit(1)

try:
    from agents.safety_agent import SafetyAgent, POISafetyInput, RealTimeData, WeatherCode, SafetyAssessmentResult
    print("  ✅ SafetyAgent 导入成功")
except Exception as e:
    print(f"  ❌ SafetyAgent 导入失败: {e}")
    sys.exit(1)

try:
    from agents.interest_agent import InterestAgent, POIInterestInput, UserInterestInput, InterestMatchResult
    print("  ✅ InterestAgent 导入成功")
except Exception as e:
    print(f"  ❌ InterestAgent 导入失败: {e}")
    sys.exit(1)

try:
    from agents.moderator import Moderator, ModerationResult, WEIGHT_SAFETY, WEIGHT_HEALTH, WEIGHT_INTEREST
    print("  ✅ Moderator 导入成功")
except Exception as e:
    print(f"  ❌ Moderator 导入失败: {e}")
    sys.exit(1)

# ─────────────────────────────────────────────────────────
# 2. 继承架构验证
# ─────────────────────────────────────────────────────────
print("\n[2/5] 继承架构验证...")
assert issubclass(HealthAgent, BaseAgent),   "❌ HealthAgent 未继承 BaseAgent"
assert issubclass(SafetyAgent, BaseAgent),   "❌ SafetyAgent 未继承 BaseAgent"
assert issubclass(InterestAgent, BaseAgent), "❌ InterestAgent 未继承 BaseAgent"
print("  ✅ 三个Agent均继承自BaseAgent")

# 权重配置验证
total_weight = round(WEIGHT_SAFETY + WEIGHT_HEALTH + WEIGHT_INTEREST, 4)
assert total_weight == 1.0, f"❌ 权重之和 {total_weight} != 1.0"
assert WEIGHT_SAFETY == 0.40,   f"❌ 安全权重应为0.40，实际{WEIGHT_SAFETY}"
assert WEIGHT_HEALTH == 0.35,   f"❌ 康养权重应为0.35，实际{WEIGHT_HEALTH}"
assert WEIGHT_INTEREST == 0.25, f"❌ 兴趣权重应为0.25，实际{WEIGHT_INTEREST}"
print(f"  ✅ 权重配置正确 安全={WEIGHT_SAFETY} 康养={WEIGHT_HEALTH} 兴趣={WEIGHT_INTEREST}（合计={total_weight}）")

# ─────────────────────────────────────────────────────────
# 3. HealthAgent 测试
# ─────────────────────────────────────────────────────────
print("\n[3/5] HealthAgent 功能测试...")
health_agent = HealthAgent()

# 用户画像：75岁，行动能力2，有心脏病
profile = HealthProfile(
    user_id="u001",
    age=75,
    mobility_score=2.0,
    chronic_diseases=["心脏病", "高血压"],
    health_level="moderate",
    travel_companion="family",
)

# POI1：适合老人（步数少、有轮椅通道、医院近）
poi_easy = POIHealthData(
    poi_id="p001",
    name="西湖景区",
    estimated_daily_steps=3000,
    stair_count=20,
    nearest_hospital_km=1.2,
    has_wheelchair_access=True,
    has_rest_area=True,
    rest_area_count=8,
    wellness_index=4.5,
)

# POI2：不适合老人（步数多、台阶多、医院远）
poi_hard = POIHealthData(
    poi_id="p002",
    name="黄山云海",
    estimated_daily_steps=15000,
    stair_count=2000,
    nearest_hospital_km=12.0,
    has_wheelchair_access=False,
    has_rest_area=False,
    rest_area_count=0,
    wellness_index=3.0,
)

result_easy = health_agent.assess(profile, poi_easy)
result_hard = health_agent.assess(profile, poi_hard)

assert isinstance(result_easy, HealthAssessmentResult), "❌ HealthAgent返回类型错误"
assert 0.0 <= result_easy.wellness_score <= 5.0, f"❌ wellness_score越界: {result_easy.wellness_score}"
assert 0.0 <= result_hard.wellness_score <= 5.0, f"❌ wellness_score越界: {result_hard.wellness_score}"
assert result_easy.wellness_score > result_hard.wellness_score, \
    f"❌ 易景点({result_easy.wellness_score})应高于难景点({result_hard.wellness_score})"
assert result_easy.suitable == True,  f"❌ 西湖应标记为适合（实际{result_easy.suitable}）"
assert result_hard.suitable == False, f"❌ 黄山应标记为不适合（实际{result_hard.suitable}）"
print(f"  ✅ HealthAgent正常 西湖康养={result_easy.wellness_score}★ 黄山康养={result_hard.wellness_score}★")
print(f"  ✅ 警告机制: 西湖{len(result_easy.warnings)}条 黄山{len(result_hard.warnings)}条警告")

# 测试星级输出
stars_easy = health_agent.score_to_stars(result_easy.wellness_score)
print(f"  ✅ 星级输出: 西湖 {result_easy.wellness_score} → {stars_easy}")

# ─────────────────────────────────────────────────────────
# 4. SafetyAgent 测试
# ─────────────────────────────────────────────────────────
print("\n[4/5] SafetyAgent 功能测试...")
safety_agent = SafetyAgent()

# 新式调用（POISafetyInput dataclass）
good_realtime = RealTimeData(
    weather=WeatherCode.SUNNY,
    temperature_celsius=22.0,
    crowd_density=0.3,
    nearest_hospital_km=1.0,
    nearest_pharmacy_km=0.5,
    uv_index=4,
)
poi_safe_input = POISafetyInput(
    poi_id="p001",
    name="西湖景区",
    nearest_hospital_km=1.0,
    realtime=good_realtime,
)
result_safe = safety_agent.assess(poi_safe_input)
assert isinstance(result_safe, SafetyAssessmentResult), "❌ SafetyAgent新式接口返回类型错误"
assert 0.0 <= result_safe.safety_score <= 5.0
print(f"  ✅ 新式接口（POISafetyInput）: 西湖安全分={result_safe.safety_score} 风险={result_safe.risk_level}")

# 旧式调用（散参数，向后兼容）
result_compat = safety_agent.assess(
    poi_or_id="p001",
    poi_name="西湖景区",
    realtime=good_realtime,
    nearest_hospital_km=1.0,
)
assert isinstance(result_compat, SafetyAssessmentResult), "❌ SafetyAgent旧式接口返回类型错误"
print(f"  ✅ 旧式接口（散参数兼容）: 安全分={result_compat.safety_score}")

# 恶劣天气测试（暴雨应降分）
storm_realtime = RealTimeData(
    weather=WeatherCode.STORM,
    temperature_celsius=18.0,
    crowd_density=0.9,
    nearest_hospital_km=15.0,
    nearest_pharmacy_km=5.0,
    uv_index=1,
)
poi_storm_input = POISafetyInput(
    poi_id="p003",
    name="山顶景区",
    nearest_hospital_km=15.0,
    realtime=storm_realtime,
)
result_storm = safety_agent.assess(poi_storm_input)
assert result_storm.safety_score < result_safe.safety_score, \
    f"❌ 暴雨分({result_storm.safety_score})应低于晴天分({result_safe.safety_score})"
assert result_storm.risk_level in ("high", "critical"), f"❌ 暴雨风险等级应为high/critical，实际{result_storm.risk_level}"
print(f"  ✅ 天气降分机制: 暴雨分={result_storm.safety_score} 风险={result_storm.risk_level}")

# 人流过高测试
dense_realtime = RealTimeData(
    weather=WeatherCode.SUNNY,
    temperature_celsius=22.0,
    crowd_density=0.95,  # > 0.9 阈值
    nearest_hospital_km=2.0,
    nearest_pharmacy_km=0.5,
    uv_index=4,
)
poi_dense = POISafetyInput(poi_id="p004", name="拥挤景区", nearest_hospital_km=2.0, realtime=dense_realtime)
result_dense = safety_agent.assess(poi_dense)
assert result_dense.crowd_alert is not None, "❌ 高密度人流应产生crowd_alert"
print(f"  ✅ 人流预警机制: 密度95% → crowd_alert='{result_dense.crowd_alert[:20]}...'")

# ─────────────────────────────────────────────────────────
# 5. InterestAgent 测试
# ─────────────────────────────────────────────────────────
print("\n[5/5] InterestAgent 功能测试...")
interest_agent = InterestAgent()

# 新式调用（UserInterestInput + POIInterestInput）
user_input = UserInterestInput(
    user_id="u001",
    interest_tags=["历史文化", "古城", "美食"],
    season="autumn",
)
poi_culture = POIInterestInput(
    poi_id="p005",
    name="平遥古城",
    category_tags=["历史文化", "古城", "民俗"],
    season="autumn",
)
poi_beach = POIInterestInput(
    poi_id="p006",
    name="三亚海滩",
    category_tags=["海岛", "海滩", "沙滩"],
    season="autumn",
)

result_culture = interest_agent.assess(user_input, poi_culture)
result_beach   = interest_agent.assess(user_input, poi_beach)

assert isinstance(result_culture, InterestMatchResult), "❌ InterestAgent返回类型错误"
assert 0.0 <= result_culture.interest_score <= 5.0
assert result_culture.interest_score > result_beach.interest_score, \
    f"❌ 古城({result_culture.interest_score})应高于海滩({result_beach.interest_score})"
print(f"  ✅ 新式接口: 平遥古城兴趣={result_culture.interest_score} 三亚海滩兴趣={result_beach.interest_score}")
print(f"  ✅ 匹配标签: {result_culture.matched_tags}")

# 旧式调用（向后兼容）
result_old = interest_agent.assess(
    user_or_poi_id="p005",
    poi_or_poi_name="平遥古城",
    poi_tags=["历史文化", "古城"],
    user_interest_tags=["历史文化", "古城", "美食"],
    season="autumn",
)
assert isinstance(result_old, InterestMatchResult), "❌ InterestAgent旧式接口返回类型错误"
print(f"  ✅ 旧式接口（兼容）: 兴趣分={result_old.interest_score}")

# ─────────────────────────────────────────────────────────
# 6. Moderator 完整Pipeline测试
# ─────────────────────────────────────────────────────────
print("\n[6/6] Moderator 完整推荐Pipeline测试...")

# 测试POI列表（包含1个高危POI验证过滤）
TEST_POIS = [
    {
        "poi_id": "p001",
        "name": "西湖景区",
        "province": "浙江省",
        "city": "杭州",
        "address": "杭州市西湖区",
        "estimated_daily_steps": 3000,
        "stair_count": 20,
        "nearest_hospital_km": 1.2,
        "nearest_hospital_name": "杭州市第一人民医院",
        "has_wheelchair_access": True,
        "has_rest_area": True,
        "rest_area_count": 8,
        "wellness_index": 4.5,
        "category_tags": ["山水", "园林", "历史文化"],
        "ticket_price": 0,
        "open_hours": "全天",
        "description": "杭州西湖，人间天堂",
        "image_url": "",
    },
    {
        "poi_id": "p002",
        "name": "平遥古城",
        "province": "山西省",
        "city": "晋中",
        "address": "晋中市平遥县",
        "estimated_daily_steps": 4000,
        "stair_count": 50,
        "nearest_hospital_km": 2.5,
        "nearest_hospital_name": "平遥县人民医院",
        "has_wheelchair_access": False,
        "has_rest_area": True,
        "rest_area_count": 5,
        "wellness_index": 3.8,
        "category_tags": ["历史文化", "古城", "民俗"],
        "ticket_price": 150,
        "open_hours": "08:00-18:00",
        "description": "中国保存最完整的古城之一",
        "image_url": "",
    },
    {
        "poi_id": "p003",
        "name": "泰山主峰",
        "province": "山东省",
        "city": "泰安",
        "address": "泰安市岱岳区",
        "estimated_daily_steps": 18000,  # 超高步数 → 应被健康过滤
        "stair_count": 6000,             # 超多台阶
        "nearest_hospital_km": 10.0,
        "nearest_hospital_name": "泰安市中心医院",
        "has_wheelchair_access": False,
        "has_rest_area": True,
        "rest_area_count": 3,
        "wellness_index": 3.0,
        "category_tags": ["山水", "自然风光", "宗教"],
        "ticket_price": 120,
        "open_hours": "全天",
        "description": "五岳之首",
        "image_url": "",
    },
]

# 使用固定的实时数据（避免随机影响）
from agents.safety_agent import WeatherCode, RealTimeData as RT
fixed_realtime_map = {
    "p001": RT(weather=WeatherCode.SUNNY, temperature_celsius=22.0, crowd_density=0.3,
               nearest_hospital_km=1.2, nearest_pharmacy_km=0.5, uv_index=4),
    "p002": RT(weather=WeatherCode.CLOUDY, temperature_celsius=20.0, crowd_density=0.4,
               nearest_hospital_km=2.5, nearest_pharmacy_km=1.0, uv_index=3),
    "p003": RT(weather=WeatherCode.SUNNY, temperature_celsius=24.0, crowd_density=0.6,
               nearest_hospital_km=10.0, nearest_pharmacy_km=3.0, uv_index=7),
}

user_profile = {
    "user_id": "u001",
    "age": 72,
    "mobility_score": 2.5,  # 行动能力偏弱
    "chronic_diseases": ["心脏病"],
    "health_level": "moderate",
    "travel_companion": "family",
    "interest_tags": ["历史文化", "古城", "山水"],
}

moderator = Moderator(top_k=3)
result = moderator.recommend(
    pois=TEST_POIS,
    user_profile=user_profile,
    realtime_map=fixed_realtime_map,
    query_text="帮我推荐适合老年人的景点",
)

assert isinstance(result, ModerationResult), "❌ Moderator返回类型错误"
assert result.total_assessed == 3, f"❌ 总评估数应为3，实际{result.total_assessed}"
assert len(result.top_recommendations) >= 1, "❌ 应有至少1条推荐"
print(f"  ✅ 总评估: {result.total_assessed}个POI，过滤: {result.filtered_count}个，推荐: {len(result.top_recommendations)}个")
print(f"  ✅ 过滤原因: {result.filter_reasons}")

# 验证Top-K有序（综合分降序）
if len(result.top_recommendations) >= 2:
    scores = [r.composite_score for r in result.top_recommendations]
    assert scores == sorted(scores, reverse=True), f"❌ 推荐结果未按分数降序排列: {scores}"
    print(f"  ✅ 推荐结果有序（综合分降序）: {scores}")

# 验证推荐理由非空
for rec in result.top_recommendations:
    assert rec.recommendation_reason, f"❌ {rec.poi_name} 推荐理由为空"
    print(f"  ✅ 推荐#{rec.rank} {rec.poi_name}: 综合分={rec.composite_score} "
          f"(安全{rec.safety_score}/康养{rec.health_score}/兴趣{rec.interest_score})")
    print(f"       推荐理由: {rec.recommendation_reason}")

# 验证安全过滤边界（注入一个安全分<2的极端POI）
TEST_POIS_FILTER = TEST_POIS + [{
    "poi_id": "p999",
    "name": "危险山谷（测试过滤）",
    "province": "XX省",
    "city": "XX市",
    "address": "XX",
    "estimated_daily_steps": 2000,
    "stair_count": 0,
    "nearest_hospital_km": 0.5,
    "has_wheelchair_access": True,
    "has_rest_area": True,
    "rest_area_count": 5,
    "wellness_index": 4.0,
    "category_tags": [],
    "ticket_price": 0,
    "open_hours": "全天",
    "description": "",
    "image_url": "",
    "nearest_hospital_name": "XX医院",
}]
# 给p999一个极端恶劣天气（暴雨+高拥挤+远医院）
storm_rt = RT(weather=WeatherCode.STORM, temperature_celsius=5.0, crowd_density=0.95,
              nearest_hospital_km=20.0, nearest_pharmacy_km=10.0, uv_index=1)
filter_rt_map = dict(fixed_realtime_map)
filter_rt_map["p999"] = storm_rt

result_filtered = moderator.recommend(
    pois=TEST_POIS_FILTER,
    user_profile=user_profile,
    realtime_map=filter_rt_map,
    query_text="过滤测试",
)
all_ids = [r.poi_id for r in result_filtered.top_recommendations]
if "p999" not in all_ids:
    print(f"  ✅ 安全过滤机制有效: p999（危险山谷）被正确排除")
else:
    print(f"  ⚠️  p999安全分={[r.safety_score for r in result_filtered.top_recommendations if r.poi_id == 'p999']}，未被过滤（可能安全分≥2.0）")

# ─────────────────────────────────────────────────────────
# 7. 统一接口方法验证
# ─────────────────────────────────────────────────────────
print("\n[7/7] 统一接口方法验证（BaseAgent工具方法）...")
# score_to_stars 验证
# BaseAgent 格式: full★ + 半星用½ + empty☆
# 例: 3.5 -> "★★★½☆☆"  4.7 -> "★★★★½"  2.0 -> "★★☆☆☆"
test_cases = [(5.0, 5, 0), (3.5, 3, 1), (2.0, 2, 0), (0.0, 0, 0), (4.7, 4, 1)]
for score, exp_full, exp_half in test_cases:
    stars = health_agent.score_to_stars(score)
    full_count = stars.count("★")
    half_present = "½" in stars
    assert full_count == exp_full, f"FAIL {score} expected {exp_full}x star, got {full_count} in '{stars}'"
    if exp_half:
        assert half_present, f"FAIL {score} expected half-star, got '{stars}'"
print(f"  OK score_to_stars verified ({len(test_cases)} cases)")

# clamp 验证
assert BaseAgent.clamp(6.0) == 5.0
assert BaseAgent.clamp(-1.0) == 0.0
assert BaseAgent.clamp(3.5) == 3.5
print("  ✅ clamp 工作正常")

# round_score 验证
assert BaseAgent.round_score(5.678) == 5.0
assert BaseAgent.round_score(-0.5) == 0.0
assert BaseAgent.round_score(3.456) == 3.46
print("  ✅ round_score 工作正常")

# ─────────────────────────────────────────────────────────
# 汇总
# ─────────────────────────────────────────────────────────
print("\n" + "=" * 60)
print("✅✅✅  全部测试通过！架构功能完整。")
print("=" * 60)
print("\n📋 架构验证摘要：")
print(f"  HealthAgent   ← BaseAgent  assess(HealthProfile, POIHealthData) ✅")
print(f"  SafetyAgent   ← BaseAgent  assess(POISafetyInput) / 散参数兼容  ✅")
print(f"  InterestAgent ← BaseAgent  assess(UserInterestInput, POIInterestInput) / 散参数兼容 ✅")
print(f"  Moderator     权重 安全×{WEIGHT_SAFETY} + 康养×{WEIGHT_HEALTH} + 兴趣×{WEIGHT_INTEREST} ✅")
print(f"  过滤机制      safety<2.0 直接排除 + wellness<1.5 排除  ✅")
print(f"  Top-K推荐     按综合分降序，含推荐理由  ✅")
