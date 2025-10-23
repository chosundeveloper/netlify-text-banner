# 감다살 첼린지

감다살 첼린지는 `이하연셀 정요한`, `이하연셀 이하연`, `이하연셀 강민욱` 세 명 중 무작위로 한 사람을 뽑는 아주 간단한 웹 페이지입니다. 페이지에 접속하면 바로 `공 뽑기` 버튼이 보이고, 클릭할 때마다 오늘의 감다살 주인공이 정해집니다.

## 어떻게 작동하나요?
- 버튼을 누를 때마다 세 후보 중 한 명을 무작위로 선택합니다.
- 최근 10회 뽑힌 기록을 화면에서 바로 확인할 수 있습니다.
- 후보를 바꾸고 싶다면 `index.html` 상단의 `candidates` 배열을 수정하면 됩니다.

## 로컬 수정 뒤 배포하기
1. `index.html`에서 후보 배열이나 스타일을 원하는 대로 바꿉니다.
2. Git 커밋 및 푸시:
   ```bash
   git add .
   git commit -m "update: customize gamdasal challenge"
   git push origin main
   ```
3. Netlify CLI로 프로덕션 배포:
   ```bash
   netlify deploy --prod
   ```

자동 배포를 원하면 Netlify 대시보드에서 GitHub 저장소와 연동하고 아래 설정을 사용하세요.
- **Build command:** (빈 칸)
- **Publish directory:** `.`

행운의 감다살, 바로 뽑아보세요!
