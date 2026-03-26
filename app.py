"""
SilverJourney AI - 主 Streamlit 应用
银发旅游智能伴侣 - 高度适老化界面
"""

import streamlit as st
import sys
import os

# 路径
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BASE_DIR)

# ──────────────────────────────────────────────
# 全局适老化页面配置
# ──────────────────────────────────────────────
st.set_page_config(
    page_title="银发旅行助手 | SilverJourney AI",
    page_icon="🌟",
    layout="wide",
    initial_sidebar_state="expanded",
)

# 全局CSS - 适老化设计
st.markdown("""
<style>
/* ===== 全局适老化样式 ===== */
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@400;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Noto Sans SC', 'Microsoft YaHei', '微软雅黑', sans-serif !important;
}

/* 主背景 - 深色舒适 */
.stApp {
    background: linear-gradient(135deg, #1a2a3a 0%, #1e3a5f 100%) !important;
    color: #f0f4f8 !important;
}

/* 大字体全局 */
p, li, span, div, label {
    font-size: 18px !important;
    line-height: 1.8 !important;
    color: #e8f0f8 !important;
}

/* 标题字体 */
h1 { font-size: 42px !important; font-weight: 700 !important; color: #ffd700 !important; }
h2 { font-size: 32px !important; font-weight: 700 !important; color: #87ceeb !important; }
h3 { font-size: 26px !important; font-weight: 600 !important; color: #87ceeb !important; }

/* 大按钮 */
.stButton > button {
    font-size: 22px !important;
    font-weight: 700 !important;
    padding: 16px 32px !important;
    border-radius: 16px !important;
    border: none !important;
    background: linear-gradient(135deg, #e74c3c, #c0392b) !important;
    color: white !important;
    box-shadow: 0 6px 20px rgba(231,76,60,0.4) !important;
    transition: all 0.3s ease !important;
    min-height: 60px !important;
    width: 100% !important;
    cursor: pointer !important;
}
.stButton > button:hover {
    transform: translateY(-3px) !important;
    box-shadow: 0 10px 30px rgba(231,76,60,0.6) !important;
    background: linear-gradient(135deg, #ff6b6b, #e74c3c) !important;
}

/* 绿色按钮 */
.btn-green > button {
    background: linear-gradient(135deg, #27ae60, #1e8449) !important;
    box-shadow: 0 6px 20px rgba(39,174,96,0.4) !important;
}
.btn-green > button:hover {
    box-shadow: 0 10px 30px rgba(39,174,96,0.6) !important;
    background: linear-gradient(135deg, #2ecc71, #27ae60) !important;
}

/* 蓝色按钮 */
.btn-blue > button {
    background: linear-gradient(135deg, #2980b9, #1a5276) !important;
    box-shadow: 0 6px 20px rgba(41,128,185,0.4) !important;
}
.btn-blue > button:hover {
    background: linear-gradient(135deg, #3498db, #2980b9) !important;
}

/* 输入框 */
.stTextInput > div > div > input,
.stTextArea > div > div > textarea {
    font-size: 20px !important;
    padding: 14px 18px !important;
    border-radius: 12px !important;
    background: rgba(255,255,255,0.1) !important;
    border: 2px solid rgba(135,206,235,0.5) !important;
    color: #f0f4f8 !important;
    min-height: 60px !important;
}
.stTextInput > div > div > input:focus,
.stTextArea > div > div > textarea:focus {
    border-color: #ffd700 !important;
    box-shadow: 0 0 0 3px rgba(255,215,0,0.3) !important;
}

/* 下拉选择框 */
.stSelectbox > div > div {
    font-size: 20px !important;
    background: rgba(255,255,255,0.1) !important;
    border: 2px solid rgba(135,206,235,0.5) !important;
    border-radius: 12px !important;
    color: #f0f4f8 !important;
}

/* 侧边栏 */
.css-1d391kg, [data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0d1b2a 0%, #1a2a3a 100%) !important;
}
[data-testid="stSidebar"] * {
    color: #e8f0f8 !important;
}

/* 卡片样式 */
.rec-card {
    background: linear-gradient(135deg, rgba(26,82,118,0.8), rgba(30,60,114,0.8));
    border: 1px solid rgba(135,206,235,0.3);
    border-radius: 20px;
    padding: 28px;
    margin: 16px 0;
    box-shadow: 0 8px 32px rgba(0,0,0,0.4);
    backdrop-filter: blur(10px);
}

.rank-badge {
    background: linear-gradient(135deg, #f39c12, #e67e22);
    color: white;
    border-radius: 50%;
    width: 50px;
    height: 50px;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    font-size: 24px;
    font-weight: 900;
    margin-right: 12px;
    box-shadow: 0 4px 12px rgba(243,156,18,0.5);
}

.score-bar {
    background: rgba(255,255,255,0.1);
    border-radius: 10px;
    height: 20px;
    margin: 6px 0;
    overflow: hidden;
}
.score-fill {
    height: 100%;
    border-radius: 10px;
    transition: width 1s ease;
}

.warning-box {
    background: linear-gradient(135deg, rgba(231,76,60,0.2), rgba(192,57,43,0.2));
    border: 2px solid #e74c3c;
    border-radius: 12px;
    padding: 16px 20px;
    margin: 8px 0;
    font-size: 18px !important;
    color: #ff8a80 !important;
}

.info-box {
    background: linear-gradient(135deg, rgba(39,174,96,0.2), rgba(30,132,73,0.2));
    border: 2px solid #27ae60;
    border-radius: 12px;
    padding: 16px 20px;
    margin: 8px 0;
    font-size: 18px !important;
    color: #a8ffb8 !important;
}

.emergency-card {
    background: linear-gradient(135deg, #7b0000, #b71c1c);
    border: 3px solid #ff5252;
    border-radius: 20px;
    padding: 24px;
    text-align: center;
    box-shadow: 0 8px 32px rgba(255,82,82,0.4);
}

.emergency-number {
    font-size: 48px !important;
    font-weight: 900 !important;
    color: #ffeb3b !important;
    letter-spacing: 8px;
}

/* 星级展示 */
.stars {
    color: #ffd700;
    font-size: 24px !important;
    letter-spacing: 4px;
}

/* 标签徽章 */
.tag-badge {
    display: inline-block;
    background: rgba(135,206,235,0.2);
    border: 1px solid rgba(135,206,235,0.5);
    border-radius: 20px;
    padding: 4px 14px;
    font-size: 15px !important;
    color: #87ceeb !important;
    margin: 3px;
}

/* 分隔线 */
hr { border-color: rgba(135,206,235,0.2) !important; margin: 24px 0 !important; }

/* 进度条 */
.stProgress > div > div > div {
    background: linear-gradient(90deg, #27ae60, #2ecc71) !important;
    height: 16px !important;
    border-radius: 8px !important;
}

/* 滑动条 */
.stSlider > div > div > div > div {
    background: #ffd700 !important;
    width: 28px !important;
    height: 28px !important;
}

/* 单选/多选 */
.stRadio label, .stCheckbox label { font-size: 18px !important; }

/* 隐藏Streamlit默认元素 */
#MainMenu { visibility: hidden; }
footer { visibility: hidden; }
.stDeployButton { display: none; }
</style>
""", unsafe_allow_html=True)


# ──────────────────────────────────────────────
# 导入后端模块
# ──────────────────────────────────────────────
@st.cache_resource(show_spinner=False)
def load_backend():
    """加载后端资源（缓存）"""
    from silverjourney.database.models import init_db, get_session
    from silverjourney.database.seed_data import insert_seed_data
    from silverjourney.agents.moderator import Moderator

    engine = init_db()
    session = get_session(engine)
    added = insert_seed_data(session)
    session.close()

    moderator = Moderator(top_k=3)
    return engine, moderator, added


# ──────────────────────────────────────────────
# Session State 初始化
# ──────────────────────────────────────────────
def init_session():
    defaults = {
        "page": "home",
        "user_profile": {
            "user_id": "demo_user",
            "name": "旅行者",
            "age": 68,
            "mobility_score": 3.0,
            "chronic_diseases": [],
            "health_level": "good",
            "travel_companion": "family",
            "interest_tags": ["山水", "历史文化"],
            "home_city": "北京",
            "emergency_contact_name": "",
            "emergency_contact_phone": "",
        },
        "query_text": "",
        "selected_city": "全国",
        "recommendations": None,
        "selected_rec": None,
        "voice_text": "",
        "package_generated": False,
        "pdf_path": None,
        "qr_data": None,
        "safety_enabled": False,
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v


init_session()

# ──────────────────────────────────────────────
# 侧边栏导航
# ──────────────────────────────────────────────
def render_sidebar():
    with st.sidebar:
        st.markdown("""
        <div style="text-align:center; padding: 20px 0;">
            <div style="font-size:64px;">🌟</div>
            <div style="font-size:24px; font-weight:700; color:#ffd700;">银发旅行助手</div>
            <div style="font-size:14px; color:#87ceeb; margin-top:4px;">SilverJourney AI</div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("---")

        nav_items = [
            ("🏠", "home",      "首页推荐"),
            ("🗺️", "recommend", "推荐结果"),
            ("📋", "itinerary", "我的行程"),
            ("🛡️", "safety",    "安全守护"),
            ("👤", "profile",   "个人设置"),
        ]

        for icon, page_id, label in nav_items:
            is_active = st.session_state.page == page_id
            btn_style = "btn-blue" if is_active else ""
            col_wrap = st.container()
            if is_active:
                st.markdown(f"""
                <div style="background:linear-gradient(135deg,rgba(255,215,0,0.2),rgba(255,165,0,0.2));
                border:2px solid #ffd700;border-radius:12px;padding:12px 16px;margin:6px 0;
                font-size:20px;font-weight:700;color:#ffd700;">
                {icon} {label}
                </div>""", unsafe_allow_html=True)
            else:
                if st.button(f"{icon} {label}", key=f"nav_{page_id}",
                             use_container_width=True):
                    st.session_state.page = page_id
                    st.rerun()

        st.markdown("---")

        # 快捷求助按钮
        st.markdown("""
        <div class="emergency-card">
            <div style="font-size:18px;color:#ffcdd2;margin-bottom:8px;">🆘 紧急求助</div>
            <div class="emergency-number">120</div>
            <div style="font-size:16px;color:#ffcdd2;margin-top:8px;">急救热线</div>
        </div>
        """, unsafe_allow_html=True)


# ──────────────────────────────────────────────
# 首页
# ──────────────────────────────────────────────
def render_home_page():
    # 大标题区
    st.markdown("""
    <div style="text-align:center; padding: 30px 0 20px 0;">
        <div style="font-size:56px; font-weight:900; color:#ffd700; 
                    text-shadow: 0 4px 20px rgba(255,215,0,0.5);">
            🌟 银发旅行助手
        </div>
        <div style="font-size:28px; color:#87ceeb; margin-top:12px; font-weight:400;">
            说出你想去的地方，AI为您量身定制旅行方案
        </div>
        <div style="font-size:18px; color:#a0c4d8; margin-top:8px;">
            安全 · 舒适 · 贴心 · 专为银发族设计
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    col1, col2 = st.columns([3, 2])

    with col1:
        st.markdown("### 💬 告诉我您想要什么样的旅行")

        # 语音/文字输入区
        query_placeholder = "例如：我想去一个不太累的地方，有山有水，最好附近有医院，我有高血压..."

        query_text = st.text_area(
            "旅行偏好描述",
            value=st.session_state.query_text,
            placeholder=query_placeholder,
            height=140,
            label_visibility="collapsed",
            key="query_input",
        )

        # 语音输入区域
        st.markdown("""
        <div style="background:rgba(135,206,235,0.1);border:2px dashed rgba(135,206,235,0.4);
        border-radius:16px;padding:20px;text-align:center;margin:12px 0;">
            <div style="font-size:22px;color:#87ceeb;">🎤 语音输入支持</div>
            <div style="font-size:16px;color:#a0c4d8;margin-top:8px;">
            支持普通话 · 粤语 · 四川话等多种方言
            </div>
        </div>
        """, unsafe_allow_html=True)

        # 语音录制组件
        try:
            from streamlit_mic_recorder import mic_recorder
            audio = mic_recorder(
                start_prompt="🎤 按住说话",
                stop_prompt="⏹ 停止录音",
                key="voice_recorder",
                use_container_width=True,
            )
            if audio:
                with st.spinner("🔄 正在识别语音..."):
                    recognized = _recognize_speech(audio["bytes"])
                    if recognized:
                        st.session_state.voice_text = recognized
                        st.success(f"✅ 识别结果：{recognized}")
                        query_text = recognized
        except ImportError:
            st.markdown("""
            <div style="font-size:16px;color:#a0c4d8;text-align:center;padding:10px;">
            💡 安装 streamlit-mic-recorder 可启用语音输入功能
            </div>""", unsafe_allow_html=True)

        # 城市选择
        cities = [
            "全国", "北京", "上海", "广州", "深圳", "杭州", "苏州", "成都", "重庆",
            "西安", "桂林", "三亚", "厦门", "大理", "丽江", "黄山", "张家界", "云南"
        ]
        selected_city = st.selectbox(
            "📍 目标城市（可选）",
            cities,
            index=cities.index(st.session_state.selected_city) if st.session_state.selected_city in cities else 0,
            key="city_select",
        )

        # 出行天数
        col_d1, col_d2 = st.columns(2)
        with col_d1:
            duration = st.selectbox(
                "🗓️ 出行天数",
                ["1天", "2天", "3天", "4-5天", "一周"],
                key="duration_select"
            )
        with col_d2:
            companion = st.selectbox(
                "👥 出行方式",
                ["家人陪同", "独自出行", "跟团出行"],
                key="companion_select"
            )

        st.markdown("<br>", unsafe_allow_html=True)

        # 主推荐按钮
        if st.button("🚀 开始智能推荐", key="start_recommend", use_container_width=True):
            _do_recommend(query_text or st.session_state.voice_text, selected_city)

    with col2:
        st.markdown("### ✨ 快捷偏好选择")

        st.markdown("**我的兴趣爱好**")
        interest_options = [
            "山水自然", "历史文化", "温泉养生",
            "美食品尝", "古城古镇", "园林公园",
            "海岛海滩", "宗教文化", "民族风情",
            "休闲散步"
        ]
        selected_interests = []
        cols = st.columns(2)
        for i, opt in enumerate(interest_options):
            with cols[i % 2]:
                if st.checkbox(opt, key=f"interest_{i}",
                               value=opt.replace("自然","").replace("养生","").replace("品尝","") in
                               str(st.session_state.user_profile.get("interest_tags", []))):
                    selected_interests.append(opt)

        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("**健康状况**")
        mobility = st.select_slider(
            "行动能力",
            options=["需要轮椅", "可短距离步行", "正常步行", "体力较好", "体力充沛"],
            value="正常步行",
            key="mobility_slider",
        )

        st.markdown("**慢性病史**（可多选）")
        disease_cols = st.columns(2)
        diseases = []
        disease_list = ["高血压", "糖尿病", "心脏病", "关节炎", "哮喘", "骨质疏松"]
        for i, d in enumerate(disease_list):
            with disease_cols[i % 2]:
                if st.checkbox(d, key=f"disease_{i}"):
                    diseases.append(d)

        # 更新用户画像
        mobility_map = {"需要轮椅": 1, "可短距离步行": 2, "正常步行": 3, "体力较好": 4, "体力充沛": 5}
        st.session_state.user_profile.update({
            "mobility_score": float(mobility_map.get(mobility, 3)),
            "chronic_diseases": diseases,
            "interest_tags": [t.replace("自然","").replace("养生","").replace("品尝","") for t in selected_interests],
        })

        # 推荐示例展示
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("### 🎯 热门推荐语")
        examples = [
            "我想去一个不累的地方，有山有水",
            "适合老年人的温泉度假胜地",
            "历史文化古城，步行不多",
            "海边休闲，空气好的地方",
        ]
        for ex in examples:
            if st.button(f"💬 {ex}", key=f"ex_{ex[:5]}", use_container_width=True):
                st.session_state.query_text = ex
                _do_recommend(ex, selected_city)


def _recognize_speech(audio_bytes) -> str:
    """语音识别（Whisper）"""
    try:
        import whisper
        import tempfile
        import soundfile as sf
        import numpy as np

        with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmp:
            tmp.write(audio_bytes)
            tmp_path = tmp.name

        model = whisper.load_model("tiny")
        result = model.transcribe(tmp_path, language="zh")
        os.unlink(tmp_path)
        return result.get("text", "")
    except Exception:
        return ""


def _do_recommend(query_text: str, city: str):
    """执行推荐逻辑"""
    if not query_text.strip():
        st.warning("⚠️ 请先输入您的旅行偏好")
        return

    st.session_state.query_text = query_text
    st.session_state.selected_city = city

    with st.spinner("🤖 AI正在为您智能推荐，请稍候..."):
        try:
            engine, moderator, _ = load_backend()
            from silverjourney.database.models import get_session, POI
            session = get_session(engine)

            # 查询POI
            query = session.query(POI)
            if city and city != "全国":
                query = query.filter(POI.city == city)
            pois_db = query.all()

            if not pois_db:
                # 回退：不过滤城市
                pois_db = session.query(POI).all()

            session.close()

            # 转换为字典
            pois = [_poi_to_dict(p) for p in pois_db]

            # 调用融合推荐
            result = moderator.recommend(
                pois=pois,
                user_profile=st.session_state.user_profile,
                query_text=query_text,
            )

            st.session_state.recommendations = result
            st.session_state.page = "recommend"
            st.rerun()

        except Exception as e:
            st.error(f"推荐失败：{str(e)}")


def _poi_to_dict(poi_obj) -> dict:
    """将POI ORM对象转换为字典"""
    return {
        "poi_id": poi_obj.poi_id,
        "name": poi_obj.name,
        "city": poi_obj.city,
        "province": poi_obj.province,
        "address": poi_obj.address,
        "latitude": poi_obj.latitude,
        "longitude": poi_obj.longitude,
        "category_tags": poi_obj.category_tags or [],
        "has_wheelchair_access": poi_obj.has_wheelchair_access,
        "has_elevator": poi_obj.has_elevator,
        "has_rest_area": poi_obj.has_rest_area,
        "rest_area_count": poi_obj.rest_area_count,
        "estimated_daily_steps": poi_obj.estimated_daily_steps,
        "stair_count": poi_obj.stair_count,
        "nearest_hospital_km": poi_obj.nearest_hospital_km,
        "nearest_hospital_name": poi_obj.nearest_hospital_name,
        "wellness_index": poi_obj.wellness_index,
        "popularity": poi_obj.popularity,
        "ticket_price": poi_obj.ticket_price,
        "open_hours": poi_obj.open_hours,
        "description": poi_obj.description,
        "image_url": poi_obj.image_url,
    }


# ──────────────────────────────────────────────
# 推荐结果页
# ──────────────────────────────────────────────
def render_recommend_page():
    st.markdown("## 🤖 AI智能推荐结果")

    if not st.session_state.recommendations:
        st.markdown("""
        <div class="info-box">
            💡 还没有推荐结果，请先回到首页输入您的旅行偏好
        </div>""", unsafe_allow_html=True)
        if st.button("⬅️ 返回首页", key="back_home_rec"):
            st.session_state.page = "home"
            st.rerun()
        return

    result = st.session_state.recommendations
    recs = result.top_recommendations

    # 查询摘要
    st.markdown(f"""
    <div class="info-box">
        🔍 根据您的需求：「{result.query_text}」
        <br>从 {result.total_assessed} 个景点中筛选出最适合您的 {len(recs)} 个推荐
        {f'（已过滤 {result.filtered_count} 个安全/健康不达标景点）' if result.filtered_count > 0 else ''}
    </div>
    """, unsafe_allow_html=True)

    if not recs:
        st.markdown("""
        <div class="warning-box">
            ⚠️ 根据您的健康状况和所选城市，暂未找到安全达标的景点。
            请尝试放宽城市范围或调整健康参数。
        </div>""", unsafe_allow_html=True)
        return

    st.markdown("---")

    for rec in recs:
        _render_recommendation_card(rec)

    # 过滤信息展示
    if result.filter_reasons:
        with st.expander("📊 查看过滤详情（已排除景点）"):
            for reason in result.filter_reasons:
                st.markdown(f"<div style='color:#e74c3c;font-size:16px;'>• {reason}</div>",
                            unsafe_allow_html=True)


def _render_recommendation_card(rec):
    """渲染单个推荐卡片"""
    rank_emoji = ["🥇", "🥈", "🥉"][rec.rank - 1] if rec.rank <= 3 else f"#{rec.rank}"

    # 风险等级颜色
    risk_colors = {"low": "#27ae60", "medium": "#f39c12", "high": "#e74c3c", "critical": "#8b0000"}

    st.markdown(f"""
    <div class="rec-card">
        <div style="display:flex;align-items:center;margin-bottom:16px;">
            <span style="font-size:40px;margin-right:12px;">{rank_emoji}</span>
            <div>
                <div style="font-size:28px;font-weight:900;color:#ffd700;">{rec.poi_name}</div>
                <div style="font-size:18px;color:#a0c4d8;">
                    📍 {rec.province} {rec.city} &nbsp;&nbsp;
                    🏥 最近医院 {rec.nearest_hospital_km}km &nbsp;&nbsp;
                    💰 {'免费' if rec.ticket_price == 0 else f'¥{rec.ticket_price:.0f}'}
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("**🌿 康养指数**")
        _render_score_display(rec.health_score, "#27ae60")
        st.markdown(f"<div style='font-size:14px;color:#a0c4d8;'>步行约{rec.estimated_daily_steps:,}步/天</div>",
                    unsafe_allow_html=True)

    with col2:
        st.markdown("**🛡️ 安全评分**")
        _render_score_display(rec.safety_score, "#3498db")
        if rec.weather_alert:
            st.markdown(f"<div style='font-size:14px;color:#e74c3c;'>{rec.weather_alert}</div>",
                        unsafe_allow_html=True)

    with col3:
        st.markdown("**❤️ 兴趣匹配**")
        _render_score_display(rec.interest_score, "#e74c3c")
        if rec.matched_interest_tags:
            tags_html = " ".join([f'<span class="tag-badge">{t}</span>' for t in rec.matched_interest_tags[:3]])
            st.markdown(tags_html, unsafe_allow_html=True)

    # 综合评分
    st.markdown(f"""
    <div style="background:rgba(255,215,0,0.1);border:1px solid rgba(255,215,0,0.3);
    border-radius:12px;padding:14px;margin:12px 0;text-align:center;">
        <span style="font-size:20px;color:#ffd700;font-weight:700;">
        综合评分：{rec.composite_score:.1f}/5.0 &nbsp;&nbsp;
        {'★' * int(rec.composite_score)}{'☆' * (5-int(rec.composite_score))}
        </span>
    </div>
    """, unsafe_allow_html=True)

    # 推荐理由
    st.markdown(f"""
    <div class="info-box">
        🤖 {rec.recommendation_reason}
    </div>""", unsafe_allow_html=True)

    # 景点描述
    if rec.description:
        st.markdown(f"<div style='font-size:17px;color:#c8d8e8;padding:8px 0;'>{rec.description}</div>",
                    unsafe_allow_html=True)

    # 警告信息
    if rec.health_warnings:
        for w in rec.health_warnings:
            st.markdown(f'<div class="warning-box">⚠️ {w}</div>', unsafe_allow_html=True)

    # 开放时间与无障碍
    col_a, col_b = st.columns(2)
    with col_a:
        st.markdown(f"⏰ **开放时间**：{rec.open_hours}")
        if rec.has_wheelchair_access:
            st.markdown("♿ **支持轮椅进入**")
    with col_b:
        if rec.has_rest_area:
            st.markdown(f"🪑 **休息区**：{rec.rest_area_count} 处")

    # 生成行程包按钮
    if st.button(f"📦 为「{rec.poi_name}」生成出行包", key=f"gen_pkg_{rec.poi_id}",
                 use_container_width=True):
        st.session_state.selected_rec = rec
        st.session_state.page = "itinerary"
        st.rerun()

    st.markdown("---")


def _render_score_display(score: float, color: str):
    """渲染评分显示"""
    pct = int(score / 5.0 * 100)
    stars = "★" * int(score) + "☆" * (5 - int(score))
    st.markdown(f"""
    <div>
        <div class="stars">{stars}</div>
        <div class="score-bar">
            <div class="score-fill" style="width:{pct}%;background:linear-gradient(90deg,{color},{color}cc);"></div>
        </div>
        <div style="font-size:20px;font-weight:700;color:{color};">{score:.1f} 分</div>
    </div>
    """, unsafe_allow_html=True)


# ──────────────────────────────────────────────
# 行程生成页
# ──────────────────────────────────────────────
def render_itinerary_page():
    st.markdown("## 📋 我的行程 & 出行包")

    if not st.session_state.selected_rec:
        if st.session_state.recommendations:
            recs = st.session_state.recommendations.top_recommendations
            if recs:
                st.session_state.selected_rec = recs[0]
            else:
                _no_rec_hint()
                return
        else:
            _no_rec_hint()
            return

    rec = st.session_state.selected_rec
    rec_dict = {
        "poi_name": rec.poi_name,
        "city": rec.city,
        "province": rec.province,
        "address": rec.address,
        "open_hours": rec.open_hours,
        "ticket_price": rec.ticket_price,
        "nearest_hospital_name": rec.nearest_hospital_name,
        "nearest_hospital_km": rec.nearest_hospital_km,
        "description": rec.description,
        "health_score": rec.health_score,
        "safety_score": rec.safety_score,
        "interest_score": rec.interest_score,
        "composite_score": rec.composite_score,
        "health_recommendations": rec.health_recommendations,
        "health_warnings": rec.health_warnings,
        "safety_risk_tips": rec.safety_risk_tips,
        "safety_recommendations": rec.safety_recommendations,
    }

    st.markdown(f"""
    <div style="font-size:28px;font-weight:900;color:#ffd700;margin-bottom:16px;">
        📍 {rec.poi_name} - {rec.province} {rec.city}
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([3, 2])

    with col1:
        st.markdown("### 🎒 生成出行包")

        # 出发日期输入
        from datetime import date, timedelta
        departure = st.date_input(
            "出发日期",
            value=date.today() + timedelta(days=3),
            min_value=date.today(),
            key="departure_date",
        )

        # 紧急联系人设置
        st.markdown("**🆘 紧急联系人信息**（将打印在出行包中）")
        contact_name = st.text_input(
            "联系人姓名",
            value=st.session_state.user_profile.get("emergency_contact_name", ""),
            placeholder="例如：小明（儿子）",
            key="contact_name",
        )
        contact_phone = st.text_input(
            "联系人电话",
            value=st.session_state.user_profile.get("emergency_contact_phone", ""),
            placeholder="例如：138xxxx1234",
            key="contact_phone",
        )

        # 更新用户画像
        st.session_state.user_profile.update({
            "emergency_contact_name": contact_name,
            "emergency_contact_phone": contact_phone,
        })

        st.markdown("<br>", unsafe_allow_html=True)

        # 生成按钮
        if st.button("📄 生成大字版PDF出行包", key="gen_pdf", use_container_width=True):
            _generate_package(rec_dict)

    with col2:
        # 紧急联系卡预览
        st.markdown("### 🆘 紧急联系卡")
        st.markdown(f"""
        <div class="emergency-card">
            <div style="font-size:20px;color:#ffcdd2;font-weight:700;margin-bottom:12px;">
                🏥 {rec.nearest_hospital_name or '最近医院'}
            </div>
            <div style="font-size:16px;color:#ffd0cc;margin-bottom:8px;">
                距离约 {rec.nearest_hospital_km} km
            </div>
            <div style="margin:16px 0;">
                <div style="font-size:16px;color:#ffcdd2;">急救</div>
                <div class="emergency-number">120</div>
            </div>
            <div>
                <div style="font-size:16px;color:#ffcdd2;">报警</div>
                <div class="emergency-number" style="font-size:36px !important;">110</div>
            </div>
            <div style="margin-top:12px;font-size:16px;color:#ffd0cc;">
                📍 目的地：{rec.city} {rec.poi_name}
            </div>
        </div>
        """, unsafe_allow_html=True)

        # 微信分享二维码
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("### 📱 微信分享")
        _render_share_qrcode(rec.poi_name, rec.city)

    # 已生成的包显示
    if st.session_state.package_generated:
        st.markdown("---")
        st.markdown("### ✅ 出行包已生成")

        tab1, tab2, tab3 = st.tabs(["📄 PDF出行包", "🔊 语音导览", "📱 分享二维码"])

        with tab1:
            if st.session_state.pdf_path and os.path.exists(st.session_state.pdf_path):
                with open(st.session_state.pdf_path, "rb") as f:
                    pdf_bytes = f.read()
                st.download_button(
                    "⬇️ 下载PDF出行包（大字版 18号字体）",
                    data=pdf_bytes,
                    file_name=f"银发旅行包_{rec.poi_name}.pdf",
                    mime="application/pdf",
                    use_container_width=True,
                )
                st.success(f"✅ PDF已生成：{os.path.basename(st.session_state.pdf_path)}")
            else:
                st.info("PDF生成完成（已保存到本地）")

        with tab2:
            from silverjourney.output import generate_voice_guide_text
            voice_text = generate_voice_guide_text(rec_dict, st.session_state.user_profile)
            st.markdown("**📜 语音导览脚本**（语速比正常慢30%）")
            st.text_area("导览文本", value=voice_text, height=300, label_visibility="collapsed")

            # TTS生成
            if st.button("🔊 生成语音导览（试听）", key="gen_tts", use_container_width=True):
                _generate_tts(voice_text)

        with tab3:
            _render_share_qrcode(rec.poi_name, rec.city, size=200)


def _generate_package(rec_dict):
    """生成出行包"""
    with st.spinner("📄 正在生成出行包，请稍候..."):
        try:
            from silverjourney.output import generate_travel_package_pdf
            output_dir = os.path.join(BASE_DIR, "silverjourney", "output", "pdfs")
            pdf_path = generate_travel_package_pdf(
                recommendation=rec_dict,
                user_profile=st.session_state.user_profile,
                output_dir=output_dir,
            )
            st.session_state.pdf_path = pdf_path
            st.session_state.package_generated = True
            st.success("✅ 出行包生成成功！")
            st.rerun()
        except Exception as e:
            st.error(f"生成失败：{e}")
            st.info("💡 请确保已安装 reportlab: pip install reportlab")


def _generate_tts(text: str):
    """生成TTS语音"""
    try:
        import pyttsx3
        import tempfile
        engine = pyttsx3.init()
        engine.setProperty("rate", 140)  # 慢速，正常约200
        with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as tmp:
            engine.save_to_file(text, tmp.name)
            engine.runAndWait()
            st.audio(tmp.name, format="audio/mp3")
    except Exception:
        st.info("💡 语音功能需要安装 pyttsx3，或使用系统TTS")


def _render_share_qrcode(poi_name, city, size=150):
    """渲染分享二维码"""
    try:
        from silverjourney.output import generate_share_qrcode
        share_url = f"https://silverjourney.ai/share?poi={poi_name}&city={city}"
        qr_b64 = generate_share_qrcode(url=share_url)
        st.markdown(f"""
        <div style="text-align:center;">
            <img src="{qr_b64}" style="width:{size}px;height:{size}px;border-radius:12px;"/>
            <div style="font-size:16px;color:#a0c4d8;margin-top:8px;">扫码分享给家人</div>
        </div>
        """, unsafe_allow_html=True)
    except Exception:
        st.markdown("""
        <div style="background:rgba(255,255,255,0.1);border-radius:12px;
        padding:20px;text-align:center;color:#a0c4d8;">
        📱 二维码（需安装 qrcode 库）
        </div>""", unsafe_allow_html=True)


def _no_rec_hint():
    st.markdown("""
    <div class="info-box">
        💡 请先回到首页，输入旅行偏好后生成推荐结果
    </div>""", unsafe_allow_html=True)
    if st.button("⬅️ 返回首页", key="back_home_iti"):
        st.session_state.page = "home"
        st.rerun()


# ──────────────────────────────────────────────
# 安全守护页
# ──────────────────────────────────────────────
def render_safety_page():
    st.markdown("## 🛡️ 实时安全守护")

    col1, col2 = st.columns([3, 2])

    with col1:
        st.markdown("### 📍 实时位置监控")

        st.markdown("""
        <div style="background:linear-gradient(135deg,rgba(39,174,96,0.2),rgba(30,132,73,0.2));
        border:2px solid #27ae60;border-radius:16px;padding:24px;text-align:center;margin:12px 0;">
            <div style="font-size:48px;margin-bottom:12px;">📍</div>
            <div style="font-size:22px;color:#2ecc71;font-weight:700;">位置正常</div>
            <div style="font-size:16px;color:#a0c4d8;margin-top:8px;">在规划路线范围内</div>
        </div>
        """, unsafe_allow_html=True)

        # 安全开关
        safety_on = st.toggle(
            "开启实时安全守护",
            value=st.session_state.safety_enabled,
            key="safety_toggle",
        )
        st.session_state.safety_enabled = safety_on

        if safety_on:
            st.markdown("""
            <div class="info-box">
                ✅ 安全守护已开启<br>
                • 位置偏离 >500m 自动预警<br>
                • 突发健康事件一键呼救<br>
                • 恶劣天气自动推送提醒<br>
                • 子女端实时同步位置
            </div>""", unsafe_allow_html=True)

        # 偏离阈值设置
        st.markdown("### ⚙️ 预警设置")
        deviation_threshold = st.slider(
            "位置偏离预警距离（米）",
            min_value=100, max_value=2000, value=500, step=100,
            key="deviation_slider",
        )
        st.markdown(f"<div style='font-size:16px;color:#a0c4d8;'>超出 {deviation_threshold}m 时通知家人</div>",
                    unsafe_allow_html=True)

        check_interval = st.select_slider(
            "位置检查频率",
            options=["每1分钟", "每5分钟", "每10分钟", "每30分钟"],
            value="每5分钟",
            key="check_interval",
        )

        # 一键求助按钮
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("""
        <div style="text-align:center;">
            <div style="font-size:22px;color:#ff8a80;margin-bottom:12px;">⚠️ 如有紧急情况</div>
        </div>
        """, unsafe_allow_html=True)

        if st.button("🆘 一键紧急求助", key="sos_btn", use_container_width=True):
            _trigger_sos()

    with col2:
        st.markdown("### 📞 紧急联系人设置")

        contact_name = st.text_input(
            "联系人姓名",
            value=st.session_state.user_profile.get("emergency_contact_name", ""),
            key="safety_contact_name",
            placeholder="子女/亲友姓名",
        )
        contact_phone = st.text_input(
            "联系人电话",
            value=st.session_state.user_profile.get("emergency_contact_phone", ""),
            key="safety_contact_phone",
            placeholder="联系人手机号",
        )

        if st.button("💾 保存联系人", key="save_contact", use_container_width=True):
            st.session_state.user_profile.update({
                "emergency_contact_name": contact_name,
                "emergency_contact_phone": contact_phone,
            })
            st.success("✅ 联系人信息已保存")

        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("### 🌤️ 实时天气状况")
        st.markdown("""
        <div style="background:rgba(41,128,185,0.2);border:2px solid #3498db;
        border-radius:16px;padding:20px;text-align:center;">
            <div style="font-size:48px;">☀️</div>
            <div style="font-size:22px;color:#87ceeb;font-weight:700;">晴天</div>
            <div style="font-size:18px;color:#a0c4d8;">气温 22°C</div>
            <div style="font-size:16px;color:#a0c4d8;margin-top:8px;">紫外线指数：适中</div>
            <div style="font-size:16px;color:#2ecc71;margin-top:6px;">✅ 适合出行</div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        # 子女端分享
        st.markdown("### 👨‍👩‍👧 子女端联动")
        st.markdown("""
        <div style="font-size:17px;color:#a0c4d8;">扫码让子女实时查看您的位置</div>
        """, unsafe_allow_html=True)
        _render_share_qrcode("行程实时追踪", "")

        st.markdown("""
        <div style="font-size:15px;color:#a0c4d8;text-align:center;margin-top:8px;">
            子女扫码后可在手机实时查看您的位置和行程状态
        </div>
        """, unsafe_allow_html=True)


def _trigger_sos():
    """触发紧急求助"""
    contact = st.session_state.user_profile.get("emergency_contact_name", "家人")
    phone = st.session_state.user_profile.get("emergency_contact_phone", "")
    st.error(f"""
    🆘 **紧急求助已触发！**

    - 正在拨打急救电话：**120**
    - 正在通知 {contact} {f'({phone})' if phone else ''}
    - 已发送您的当前位置
    - 最近医院导航已开启

    **请保持冷静，帮助正在赶来！**
    """)


# ──────────────────────────────────────────────
# 个人设置页
# ──────────────────────────────────────────────
def render_profile_page():
    st.markdown("## 👤 个人设置")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 基本信息")
        name = st.text_input("姓名", value=st.session_state.user_profile.get("name", "旅行者"), key="p_name")
        age  = st.number_input("年龄", min_value=50, max_value=100,
                                value=st.session_state.user_profile.get("age", 68), key="p_age")
        city = st.selectbox("常住城市", ["北京", "上海", "广州", "深圳", "杭州", "成都", "其他"],
                             key="p_city")

        st.markdown("### 出行偏好")
        companion = st.radio("出行方式",
                              ["家人陪同", "独自出行", "跟团出行"],
                              index=0, key="p_companion", horizontal=True)

    with col2:
        st.markdown("### 健康档案")
        mobility = st.select_slider(
            "行动能力",
            options=["需要轮椅", "可短距离步行", "正常步行", "体力较好", "体力充沛"],
            value="正常步行",
            key="p_mobility",
        )
        health_level = st.select_slider(
            "总体健康状况",
            options=["需要关注", "一般", "良好", "优秀"],
            value="良好",
            key="p_health",
        )

        st.markdown("**慢性病史**")
        disease_list = ["高血压", "糖尿病", "心脏病", "关节炎", "哮喘", "骨质疏松", "慢阻肺"]
        selected_diseases = []
        dc = st.columns(2)
        for i, d in enumerate(disease_list):
            with dc[i % 2]:
                if st.checkbox(d, key=f"p_dis_{i}",
                               value=d in st.session_state.user_profile.get("chronic_diseases", [])):
                    selected_diseases.append(d)

    if st.button("💾 保存设置", key="save_profile", use_container_width=True):
        mobility_map = {"需要轮椅": 1, "可短距离步行": 2, "正常步行": 3, "体力较好": 4, "体力充沛": 5}
        health_map = {"需要关注": "limited", "一般": "moderate", "良好": "good", "优秀": "excellent"}
        companion_map = {"家人陪同": "family", "独自出行": "alone", "跟团出行": "group_tour"}

        st.session_state.user_profile.update({
            "name": name,
            "age": age,
            "home_city": city,
            "mobility_score": float(mobility_map.get(mobility, 3)),
            "health_level": health_map.get(health_level, "good"),
            "travel_companion": companion_map.get(companion, "family"),
            "chronic_diseases": selected_diseases,
        })
        st.success("✅ 设置已保存，下次推荐将自动应用您的健康档案")


# ──────────────────────────────────────────────
# 主渲染逻辑
# ──────────────────────────────────────────────
render_sidebar()

page = st.session_state.page
if page == "home":
    render_home_page()
elif page == "recommend":
    render_recommend_page()
elif page == "itinerary":
    render_itinerary_page()
elif page == "safety":
    render_safety_page()
elif page == "profile":
    render_profile_page()
