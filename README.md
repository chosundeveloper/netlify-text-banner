# 감다살 공 뽑기

한 번의 클릭으로 오늘의 감다살 주인공을 뽑는 미니 게임입니다. 화면에는 반짝이는 공 버튼과 실시간으로 반짝이는 연출이 들어가 있어 파티 게임 느낌을 줍니다. 기본 후보는 `이하연셀 정요한`, `강민욱`, `이하연` 세 명입니다.

## 커스터마이징
- 후보 변경: `index.html` 하단의 `names` 배열을 수정하세요.
- 연출 조정: CSS 섹션에서 색상, 글로우, 배경을 자유롭게 변형할 수 있습니다.

## 배포 순서
```bash
git add .
git commit -m "update: 감다살 게임 연출"
git push origin main
netlify deploy --prod
```

배포 후 `https://netlify-text-banner.netlify.app`에서 곧바로 게임을 즐길 수 있습니다.
