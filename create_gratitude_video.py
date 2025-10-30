#!/usr/bin/env python3
"""
감다살 첼린지 인트로 영상 생성 스크립트
Replicate API를 사용하여 감사하는 마음을 담은 영상 생성
"""

import replicate
import os
import time

def create_gratitude_video():
    """감사 영상 생성"""
    
    # Replicate API 토큰 설정 (무료 크레딧 사용)
    # 실제 사용시에는 환경변수로 설정: export REPLICATE_API_TOKEN="your_token"
    
    print("🎬 감다살 첼린지 인트로 영상 생성 시작...")
    
    try:
        # Stable Video Diffusion 모델 사용
        print("📝 프롬프트: 감사하는 마음을 담은 따뜻한 영상...")
        
        # 이미지 생성 (감사하는 마음을 담은 이미지)
        image_prompt = """
        A beautiful Korean woman with a warm, genuine smile, 
        expressing gratitude and appreciation, 
        soft natural lighting, 
        warm and inviting atmosphere, 
        high quality, cinematic style,
        peaceful and positive energy
        """
        
        print("🖼️  감사 이미지 생성 중...")
        
        # 이미지 생성 (DALL-E 스타일)
        image_output = replicate.run(
            "stability-ai/stable-diffusion:27b93a2413e7f36cd83da926f3656280b2931564ff050bf9575f1fdf9bcd747e",
            input={
                "prompt": image_prompt,
                "width": 1024,
                "height": 1024,
                "num_inference_steps": 50,
                "guidance_scale": 7.5
            }
        )
        
        print(f"✅ 이미지 생성 완료: {image_output}")
        
        # 동영상 생성 (이미지에서 동영상으로)
        print("🎥 동영상 생성 중...")
        
        video_output = replicate.run(
            "stability-ai/stable-video-diffusion:76d4df5d11d361a6c273d1c1b0b2a0f8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b",
            input={
                "input_image": image_output[0],
                "motion_bucket_id": 127,
                "cond_aug": 0.02,
                "steps": 25,
                "fps": 6
            }
        )
        
        print(f"🎉 감사 영상 생성 완료!")
        print(f"📁 다운로드 URL: {video_output}")
        
        return video_output
        
    except Exception as e:
        print(f"❌ 오류 발생: {e}")
        print("💡 대안: 무료 온라인 도구 사용을 권장합니다.")
        return None

def create_simple_gratitude_video():
    """간단한 감사 영상 생성 (대안 방법)"""
    
    print("🎬 대안 방법: 간단한 감사 영상 생성...")
    
    # 무료 온라인 도구 추천
    tools = [
        {
            "name": "Dreamina (CapCut)",
            "url": "https://dreamina.capcut.com",
            "description": "텍스트 프롬프트로 AI 동영상 생성",
            "prompt": "감다살 첼린지에 참여하세요! 매일 감사한 순간을 기록하고 공유하는 특별한 챌린지입니다. 따뜻한 미소의 한국 여성이 감사한 마음을 전하는 모습"
        },
        {
            "name": "Lumen5",
            "url": "https://lumen5.com",
            "description": "텍스트를 동영상으로 자동 변환",
            "prompt": "감사하는 마음으로 시작하는 감다살 첼린지. 매일 작은 감사한 순간들을 기록하고 공유해보세요."
        },
        {
            "name": "Canva",
            "url": "https://canva.com",
            "description": "템플릿 기반 동영상 제작",
            "prompt": "감사/긍정적인 분위기의 템플릿 사용"
        }
    ]
    
    print("\n🛠️  추천 무료 도구들:")
    for i, tool in enumerate(tools, 1):
        print(f"\n{i}. {tool['name']}")
        print(f"   URL: {tool['url']}")
        print(f"   설명: {tool['description']}")
        print(f"   프롬프트: {tool['prompt']}")
    
    return tools

if __name__ == "__main__":
    print("=" * 50)
    print("🎬 감다살 첼린지 인트로 영상 생성기")
    print("=" * 50)
    
    # API 토큰 확인
    if not os.getenv("REPLICATE_API_TOKEN"):
        print("⚠️  REPLICATE_API_TOKEN이 설정되지 않았습니다.")
        print("💡 무료 온라인 도구 사용을 권장합니다.")
        create_simple_gratitude_video()
    else:
        # API 사용 시도
        result = create_gratitude_video()
        if not result:
            print("\n🔄 대안 방법으로 전환...")
            create_simple_gratitude_video()
    
    print("\n✅ 완료! 위의 도구 중 하나를 사용하여 감사 영상을 제작해보세요.")
