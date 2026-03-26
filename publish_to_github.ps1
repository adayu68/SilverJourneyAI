# SilverJourney AI — GitHub 开源上线脚本
# 使用前请替换 YOUR_GITHUB_USERNAME

$USERNAME = "adayu68"
$REPO = "SilverJourneyAI"
$REMOTE = "https://github.com/$USERNAME/$REPO.git"

Write-Host "🚀 SilverJourney AI GitHub 开源上线" -ForegroundColor Cyan
Write-Host "======================================" -ForegroundColor Cyan

# 1. 初始化 Git
if (-not (Test-Path ".git")) {
    Write-Host "`n📦 初始化 Git 仓库..." -ForegroundColor Yellow
    git init
    Write-Host "✅ Git 初始化完成" -ForegroundColor Green
} else {
    Write-Host "`n✅ Git 仓库已存在" -ForegroundColor Green
}

# 2. 设置主分支为 main
git branch -M main

# 3. 添加所有文件
Write-Host "`n📁 添加文件到暂存区..." -ForegroundColor Yellow
git add .

# 4. 查看将要提交的文件
Write-Host "`n📋 将要提交的文件：" -ForegroundColor Yellow
git status --short

# 5. 首次提交
Write-Host "`n💾 创建初始提交..." -ForegroundColor Yellow
git commit -m "feat: 🎉 初始发布 SilverJourney AI v1.0.0

- 三智能体协作推荐引擎（HealthAgent/SafetyAgent/InterestAgent+Moderator）
- 适老化微信小程序（语音输入+大字体高对比度）
- GPS实时安全守护（自动追踪+SOS一键求助）
- Canvas行程图片生成+云函数小程序码分享
- 完整适老化POI数据库（13城市30+景点）
- Flask REST API + Streamlit Web界面
- 完整单元测试套件 + GitHub Actions CI"

# 6. 关联远程仓库
Write-Host "`n🔗 关联远程仓库..." -ForegroundColor Yellow
git remote remove origin 2>$null   # 如果已存在则先删除
git remote add origin $REMOTE
Write-Host "✅ 远程仓库：$REMOTE" -ForegroundColor Green

# 7. 推送到 GitHub
Write-Host "`n⬆️  推送到 GitHub..." -ForegroundColor Yellow
git push -u origin main

# 8. 打 v1.0.0 Tag
Write-Host "`n🏷️  创建 v1.0.0 标签..." -ForegroundColor Yellow
git tag -a v1.0.0 -m "🌟 SilverJourney AI v1.0.0 正式发布

首个完整覆盖推荐+安全+适老化输出全链路的银发旅游开源项目"
git push origin v1.0.0

Write-Host "`n======================================" -ForegroundColor Cyan
Write-Host "🎉 开源上线完成！" -ForegroundColor Green
Write-Host ""
Write-Host "📌 仓库地址：https://github.com/$USERNAME/$REPO" -ForegroundColor Cyan
Write-Host "📌 Releases：https://github.com/$USERNAME/$REPO/releases" -ForegroundColor Cyan
Write-Host ""
Write-Host "💡 下一步：" -ForegroundColor Yellow
Write-Host "   1. 在 GitHub 仓库设置 Topics（关键词标签）" -ForegroundColor White
Write-Host "   2. 在掘金/知乎发文推广" -ForegroundColor White
Write-Host "   3. 提交到 awesome-python 列表" -ForegroundColor White
