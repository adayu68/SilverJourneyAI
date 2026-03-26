"""
SilverJourney AI - 微信小程序后端API
基于 Flask 提供 RESTful API
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
import sys, os
import uuid
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BASE_DIR)

app = Flask(__name__)
CORS(app)

# ── 启动时初始化DB ─────────────────────────────
from silverjourney.database.models import init_db, get_session
from silverjourney.database.seed_data import insert_seed_data
from silverjourney.agents.moderator import Moderator

_engine = init_db()
_session = get_session(_engine)
insert_seed_data(_session)
_session.close()
_moderator = Moderator(top_k=3)


def _poi_to_dict(poi_obj):
    return {
        "poi_id": poi_obj.poi_id, "name": poi_obj.name, "city": poi_obj.city,
        "province": poi_obj.province, "address": poi_obj.address,
        "latitude": poi_obj.latitude, "longitude": poi_obj.longitude,
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


# ── 健康检查 ───────────────────────────────────
@app.route("/api/health", methods=["GET"])
def health_check():
    return jsonify({"status": "ok", "service": "SilverJourney AI API", "version": "1.0.0"})


# ── 推荐接口 ───────────────────────────────────
@app.route("/api/recommend", methods=["POST"])
def recommend():
    """
    POST /api/recommend
    Body: {
        "user_profile": {...},
        "city": "杭州",
        "query_text": "想去有山有水的地方",
        "top_k": 3
    }
    """
    try:
        data = request.get_json()
        user_profile = data.get("user_profile", {})
        city = data.get("city", "")
        query_text = data.get("query_text", "")
        top_k = data.get("top_k", 3)

        from silverjourney.database.models import POI
        session = get_session(_engine)
        query = session.query(POI)
        if city and city != "全国":
            query = query.filter(POI.city == city)
        pois_db = query.all()
        if not pois_db:
            pois_db = session.query(POI).all()
        session.close()

        pois = [_poi_to_dict(p) for p in pois_db]
        _moderator.top_k = top_k
        result = _moderator.recommend(
            pois=pois,
            user_profile=user_profile,
            query_text=query_text,
        )

        recs = []
        for rec in result.top_recommendations:
            recs.append({
                "rank": rec.rank,
                "poi_id": rec.poi_id,
                "poi_name": rec.poi_name,
                "city": rec.city,
                "province": rec.province,
                "address": rec.address,
                "health_score": rec.health_score,
                "safety_score": rec.safety_score,
                "interest_score": rec.interest_score,
                "composite_score": rec.composite_score,
                "ticket_price": rec.ticket_price,
                "open_hours": rec.open_hours,
                "description": rec.description,
                "nearest_hospital_km": rec.nearest_hospital_km,
                "nearest_hospital_name": rec.nearest_hospital_name,
                "recommendation_reason": rec.recommendation_reason,
                "health_recommendations": rec.health_recommendations,
                "health_warnings": rec.health_warnings,
                "safety_risk_tips": rec.safety_risk_tips,
                "weather_alert": rec.weather_alert,
                "matched_interest_tags": rec.matched_interest_tags,
                "has_wheelchair_access": rec.has_wheelchair_access,
                "rest_area_count": rec.rest_area_count,
                "estimated_daily_steps": rec.estimated_daily_steps,
                "category_tags": rec.category_tags,
            })

        return jsonify({
            "code": 0,
            "message": "success",
            "data": {
                "session_id": result.session_id,
                "recommendations": recs,
                "total_assessed": result.total_assessed,
                "filtered_count": result.filtered_count,
            }
        })

    except Exception as e:
        return jsonify({"code": 500, "message": str(e), "data": None}), 500


# ── 生成语音导览文本 ────────────────────────────
@app.route("/api/voice-guide", methods=["POST"])
def voice_guide():
    """生成语音导览脚本"""
    try:
        data = request.get_json()
        recommendation = data.get("recommendation", {})
        user_profile = data.get("user_profile", {})

        from silverjourney.output import generate_voice_guide_text
        text = generate_voice_guide_text(recommendation, user_profile)
        return jsonify({"code": 0, "message": "success", "data": {"voice_text": text}})
    except Exception as e:
        return jsonify({"code": 500, "message": str(e)}), 500


# ── 生成紧急联系卡 ──────────────────────────────
@app.route("/api/emergency-card", methods=["POST"])
def emergency_card():
    """生成紧急联系卡数据"""
    try:
        data = request.get_json()
        recommendation = data.get("recommendation", {})
        user_profile = data.get("user_profile", {})

        from silverjourney.output import generate_emergency_card_text
        card = generate_emergency_card_text(recommendation, user_profile)
        return jsonify({"code": 0, "message": "success", "data": card})
    except Exception as e:
        return jsonify({"code": 500, "message": str(e)}), 500


# ── 生成分享二维码 ──────────────────────────────
@app.route("/api/qrcode", methods=["POST"])
def qrcode_gen():
    """生成分享二维码（返回base64图片）"""
    try:
        data = request.get_json()
        url = data.get("url", "https://github.com/silverjourney-ai")

        from silverjourney.output import generate_share_qrcode
        qr_b64 = generate_share_qrcode(url=url)
        return jsonify({"code": 0, "message": "success", "data": {"qrcode": qr_b64}})
    except Exception as e:
        return jsonify({"code": 500, "message": str(e)}), 500


# ── 城市列表 ───────────────────────────────────
@app.route("/api/cities", methods=["GET"])
def get_cities():
    from silverjourney.database.models import POI
    session = get_session(_engine)
    cities = [c[0] for c in session.query(POI.city).distinct().all() if c[0]]
    session.close()
    return jsonify({"code": 0, "message": "success", "data": {"cities": ["全国"] + sorted(cities)}})


# ── 保存安全日志 ───────────────────────────────
@app.route("/api/safety-log", methods=["POST"])
def save_safety_log():
    """记录安全事件"""
    try:
        data = request.get_json()
        from silverjourney.database.models import SafetyLog
        session = get_session(_engine)
        log = SafetyLog(
            log_id=str(uuid.uuid4()),
            user_id=data.get("user_id", "anonymous"),
            log_type=data.get("log_type", "location_deviation"),
            description=data.get("description", ""),
            latitude=data.get("latitude"),
            longitude=data.get("longitude"),
            severity=data.get("severity", "low"),
        )
        session.add(log)
        session.commit()
        session.close()
        return jsonify({"code": 0, "message": "安全日志已记录"})
    except Exception as e:
        return jsonify({"code": 500, "message": str(e)}), 500


if __name__ == "__main__":
    print("🌟 SilverJourney AI API 服务启动中...")
    print("📡 API地址：http://localhost:5000")
    app.run(host="0.0.0.0", port=5000, debug=False)
