#!/usr/bin/env python3
"""
감다살 첼린지 인트로 영상 자동 생성 스크립트
무료 AI 도구들을 활용한 영상 생성
"""

import webbrowser
import time
import os

def open_dreamina():
    """Dreamina 웹사이트 열기"""
    print("🌐 Dreamina 웹사이트 열기...")
    webbrowser.open("https://dreamina.capcut.com")
    print("✅ Dreamina가 브라우저에서 열렸습니다.")
    print("📝 다음 단계를 따라해주세요:")
    print("1. 회원가입/로그인")
    print("2. 'AI 동영상 생성' 선택")
    print("3. 아래 프롬프트 복사-붙여넣기:")
    print()
    print("=" * 60)
    print("🎬 감다살 첼린지 프롬프트:")
    print("=" * 60)
    print("감다살 첼린지에 참여하세요! 매일 감사한 순간을 기록하고 공유하는 특별한 챌린지입니다. 따뜻한 미소의 한국 여성이 감사한 마음을 전하는 모습, 부드러운 조명, 친근한 분위기, 감사와 긍정의 에너지가 느껴지는 영상, 고품질, 시네마틱 스타일")
    print("=" * 60)
    print()
    print("4. 스타일: '감사/긍정적' 또는 '따뜻한 분위기' 선택")
    print("5. 영상 생성 버튼 클릭")
    print("6. 완성 후 다운로드")

def create_sample_video():
    """샘플 감사 영상 생성 (대안)"""
    print("🎬 샘플 감사 영상 생성 중...")
    
    # 간단한 HTML5 비디오 생성
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>감다살 첼린지 인트로</title>
        <style>
            body {
                margin: 0;
                padding: 0;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                font-family: 'Arial', sans-serif;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                color: white;
            }
            .container {
                text-align: center;
                max-width: 800px;
                padding: 2rem;
            }
            h1 {
                font-size: 3rem;
                margin-bottom: 1rem;
                text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
            }
            p {
                font-size: 1.5rem;
                margin-bottom: 2rem;
                opacity: 0.9;
            }
            .challenge-box {
                background: rgba(255,255,255,0.1);
                padding: 2rem;
                border-radius: 20px;
                backdrop-filter: blur(10px);
                border: 1px solid rgba(255,255,255,0.2);
                margin: 2rem 0;
            }
            .gratitude-text {
                font-size: 1.2rem;
                line-height: 1.6;
                margin: 1rem 0;
            }
            .heart {
                color: #ff6b6b;
                font-size: 2rem;
                animation: heartbeat 1.5s ease-in-out infinite;
            }
            @keyframes heartbeat {
                0% { transform: scale(1); }
                50% { transform: scale(1.1); }
                100% { transform: scale(1); }
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>감다살 첼린지</h1>
            <p>감사하는 마음으로 시작하는 특별한 챌린지</p>
            
            <div class="challenge-box">
                <div class="gratitude-text">
                    <span class="heart">💝</span> 매일 감사한 순간을 기록하고 공유해보세요
                </div>
                <div class="gratitude-text">
                    <span class="heart">🌟</span> 작은 감사가 큰 행복을 만들어갑니다
                </div>
                <div class="gratitude-text">
                    <span class="heart">🤝</span> 함께 감사하는 마음을 나누어요
                </div>
            </div>
            
            <p style="font-size: 1.1rem; opacity: 0.8;">
                지금 바로 시작해보세요! 🚀
            </p>
        </div>
    </body>
    </html>
    """
    
    # HTML 파일 저장
    with open("gamdasal_intro.html", "w", encoding="utf-8") as f:
        f.write(html_content)
    
    print("✅ 샘플 감사 영상 HTML 생성 완료!")
    print("📁 파일: gamdasal_intro.html")
    print("🌐 브라우저에서 열기...")
    
    # 브라우저에서 열기
    webbrowser.open(f"file://{os.path.abspath('gamdasal_intro.html')}")
    
    return "gamdasal_intro.html"

def create_video_script():
    """영상 제작 스크립트 생성"""
    script_content = """
# 🎬 감다살 첼린지 인트로 영상 제작 스크립트

## 📝 영상 구성 (15-30초)

### 1. 오프닝 (0-3초)
- 화면: "감다살 첼린지" 타이틀
- 음성: "감사하는 마음으로 시작하는 감다살 첼린지에 오신 것을 환영합니다"

### 2. 메인 메시지 (3-20초)
- 화면: 따뜻한 미소의 한국 여성 (AI 생성)
- 음성: "매일 감사한 순간을 기록하고 공유하는 특별한 챌린지입니다"
- 화면: 감사하는 모습들 (가족, 친구, 자연 등)
- 음성: "작은 감사가 큰 행복을 만들어갑니다"

### 3. 클로징 (20-30초)
- 화면: "지금 바로 시작해보세요!"
- 음성: "함께 감사하는 마음을 나누어요"
- 화면: 감다살 첼린지 로고

## 🎨 시각적 요소
- 색상: 따뜻한 톤 (오렌지, 핑크, 골드)
- 조명: 부드러운 자연광
- 분위기: 친근하고 따뜻한 느낌

## 🎵 음악
- 감사/긍정적인 배경음악
- 부드럽고 따뜻한 멜로디
- 15-30초 길이

## 📱 최종 결과물
- 해상도: 1080p (1920x1080)
- 형식: MP4
- 길이: 15-30초
- 용량: 10MB 이하
"""
    
    with open("video_script.md", "w", encoding="utf-8") as f:
        f.write(script_content)
    
    print("📝 영상 제작 스크립트 생성 완료!")
    print("📁 파일: video_script.md")

def main():
    """메인 실행 함수"""
    print("=" * 60)
    print("🎬 감다살 첼린지 인트로 영상 생성기")
    print("=" * 60)
    
    print("\n🚀 영상 생성 방법을 선택해주세요:")
    print("1. Dreamina (CapCut) - AI 자동 생성")
    print("2. 샘플 HTML 영상 생성")
    print("3. 영상 제작 스크립트만 생성")
    
    choice = input("\n선택 (1-3): ").strip()
    
    if choice == "1":
        open_dreamina()
    elif choice == "2":
        create_sample_video()
    elif choice == "3":
        create_video_script()
    else:
        print("❌ 잘못된 선택입니다.")
        return
    
    print("\n✅ 완료!")
    print("📁 생성된 파일들을 확인해보세요.")

if __name__ == "__main__":
    main()
