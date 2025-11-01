# 감다살 영상 아카이브 (Gamdasal Video Archive)

감다살 셀의 미션/첼린지(Challenge)와 감사 모음(Thanks) 영상을 한 페이지에서 업로드·관리·시청할 수 있는 정적 웹 앱입니다. Supabase Storage/Database를 사용해 클라우드에 영상을 저장하고, 최신 목록을 불러옵니다.

## 데모
- 로컬 파일 `index.html`을 브라우저로 열거나 GitHub Pages로 배포해 바로 사용 가능합니다.

## 주요 기능
- 업로드: 영상/이미지 파일을 드래그&드롭 또는 파일 선택으로 업로드
- 저장: Supabase Storage 업로드 + Database 메타데이터 저장
- 목록: 최신 업로드를 카드 형태로 열람 및 삭제
- QR 공유: 현재 페이지 URL을 QR 코드로 생성해 모바일 접속 용이
- 반응형 UI: 데스크톱/모바일 모두 보기 좋게 최적화

## 빠른 시작
1) 저장소 클론
```bash
git clone <YOUR_REPO_URL>
cd github-actions-text-banner
```

2) 로컬 실행
- 정적 사이트이므로 `index.html`을 브라우저에서 직접 열면 됩니다.
- 또는 임시 서버를 띄워 접근할 수 있습니다.

3) Supabase 설정
- `index.html`의 다음 상수 값을 본인 프로젝트로 교체하세요:
  - `SUPABASE_URL`
  - `SUPABASE_ANON_KEY`
  - `SUPABASE_BUCKET` (예: `videos`)
  - `SUPABASE_TABLE` (예: `video_uploads`)
- Database에 `video_uploads` 테이블이 필요합니다. 예시 컬럼: `id (uuid)`, `title (text)`, `subtitle (text)`, `src (text)`, `poster (text)`, `created_at (timestamp)`

## 배포 (GitHub Pages)
이 저장소는 정적 사이트이므로 GitHub Pages로 손쉽게 배포할 수 있습니다.

1) 브랜치 푸시
```bash
git add .
git commit -m "chore: 초기 커밋"
git push origin main
```

2) GitHub → Settings → Pages에서 배포 소스를 `GitHub Actions` 또는 `main /(root)`로 설정합니다.
- `.github/workflows/pages.yml`가 있다면 Actions로 자동 배포됩니다.
- 정적 자산 폴더 구조를 유지하기 위해 `.nojekyll` 파일이 포함되어 있습니다.

배포 후 GitHub Pages URL로 접속해 동작을 확인하세요.

## 파일 구조
```
├── index.html                 # 앱 본문(HTML/CSS/JS 일체, Supabase 연동)
├── README.md                  # 프로젝트 설명
├── auto_generate_video.py     # 동영상 생성/자동화 스크립트(옵션)
├── create_gratitude_video.py  # 감사 영상 생성 스크립트(옵션)
├── 감사, 하루의 발견.mp4       # 샘플 영상
└── .github/workflows/pages.yml # GitHub Pages 배포 워크플로우
```

## 주의 사항
- 공개 저장소에 Supabase 익명 키를 포함하면 누구나 읽기 API 호출이 가능해집니다. 쓰기 권한/버킷 정책을 반드시 제한하고, 필요한 경우 서버 프록시를 고려하세요.
- 대용량 영상 업로드는 네트워크 상태에 따라 지연될 수 있습니다.

## 라이선스
이 저장소는 MIT 라이선스를 따릅니다. 자세한 내용은 `LICENSE` 파일을 참고하세요.

## 기여
이슈/PR 환영합니다. 버그 리포트, 기능 제안, 문서 개선 등 언제든지 참여해주세요.
