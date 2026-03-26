#!/usr/bin/env python3
"""
SilverJourney AI - 一键启动脚本
运行此脚本即可启动完整服务
"""

import sys
import os
import subprocess
import threading
import time
import webbrowser

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

BANNER = """
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║       🌟  SilverJourney AI  银发旅游智能伴侣                  ║
║                                                              ║
║   首个完整覆盖「推荐+安全+适老化输出」全链路的银发旅游项目     ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝

启动中...
"""

def check_dependencies():
    """检查并安装依赖"""
    print("📦 检查依赖...")
    try:
        import streamlit
        import flask
        import sqlalchemy
        print("  ✅ 核心依赖已就绪")
    except ImportError as e:
        print(f"  ⚠️  缺少依赖：{e}")
        print("  📥 正在安装依赖...")
        subprocess.run(
            [sys.executable, "-m", "pip", "install", "-r",
             os.path.join(BASE_DIR, "requirements.txt")],
            check=True
        )
        print("  ✅ 依赖安装完成")


def start_api_server():
    """启动Flask API服务器"""
    print("\n🔧 启动后端API服务 (端口 5000)...")
    api_path = os.path.join(BASE_DIR, "api_server.py")
    proc = subprocess.Popen(
        [sys.executable, api_path],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    time.sleep(2)
    print("  ✅ API服务已启动: http://localhost:5000")
    return proc


def start_streamlit():
    """启动Streamlit Web应用"""
    print("\n🚀 启动Web界面 (端口 8501)...")
    app_path = os.path.join(BASE_DIR, "app.py")
    proc = subprocess.Popen([
        sys.executable, "-m", "streamlit", "run", app_path,
        "--server.port", "8501",
        "--server.headless", "true",
        "--browser.gatherUsageStats", "false",
        "--theme.base", "dark",
        "--theme.primaryColor", "#ffd700",
        "--theme.backgroundColor", "#1a2a3a",
        "--theme.secondaryBackgroundColor", "#0d1b2a",
        "--theme.textColor", "#e8f0f8",
    ])
    return proc


def open_browser():
    """延迟打开浏览器"""
    time.sleep(4)
    url = "http://localhost:8501"
    print(f"\n🌐 正在打开浏览器: {url}")
    webbrowser.open(url)


def main():
    print(BANNER)

    # 检查依赖
    check_dependencies()

    # 初始化数据库
    print("\n🗄️  初始化数据库...")
    sys.path.insert(0, BASE_DIR)
    try:
        from silverjourney.database.models import init_db, get_session
        from silverjourney.database.seed_data import insert_seed_data
        engine = init_db()
        session = get_session(engine)
        added = insert_seed_data(session)
        session.close()
        print(f"  ✅ 数据库就绪（新增 {added} 条POI数据）")
    except Exception as e:
        print(f"  ⚠️  数据库初始化: {e}")

    # 启动API服务
    api_proc = None
    try:
        api_proc = start_api_server()
    except Exception as e:
        print(f"  ⚠️  API服务启动失败: {e}（Web版仍可使用）")

    # 启动浏览器（后台线程）
    threading.Thread(target=open_browser, daemon=True).start()

    # 启动Streamlit（主线程，阻塞）
    web_proc = start_streamlit()

    print("""
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║   🌟 SilverJourney AI 已启动！                               ║
║                                                              ║
║   📱 Web界面:  http://localhost:8501                         ║
║   🔧 API服务:  http://localhost:5000                         ║
║                                                              ║
║   按 Ctrl+C 停止服务                                          ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
    """)

    try:
        web_proc.wait()
    except KeyboardInterrupt:
        print("\n\n👋 正在关闭服务...")
        web_proc.terminate()
        if api_proc:
            api_proc.terminate()
        print("✅ 服务已停止。感谢使用 SilverJourney AI！")


if __name__ == "__main__":
    main()
