# 감다살 첼린지 영상 아카이브

감다살 셀 구성원들이 촬영한 첼린지 영상을 모아 보는 단순한 웹 페이지입니다. 영상 제목과 MP4 주소만 입력하면 목록에 추가되고, 브라우저 `localStorage`에 저장되어 다음 접속에도 그대로 유지됩니다.

## 사용 방법
1. 페이지에 접속하면 기본 샘플 영상 두 개가 보입니다.
2. 하단 입력 폼에 **영상 제목**과 **MP4 링크**를 적고 `업로드` 버튼을 누르면 목록이 갱신됩니다.
3. 각 영상 카드 오른쪽의 `삭제` 버튼으로 목록에서 제거할 수 있습니다.
4. 저장은 브라우저마다 독립적으로 이뤄지므로, 여러 명이 같은 데이터를 공유하려면 별도의 데이터베이스를 연동해야 합니다.

## 커스터마이징 포인트
- 샘플 영상 변경: `index.html`의 `DEFAULT_UPLOADS` 배열을 원하는 링크로 수정하세요.
- 저장 키 변경: `STORAGE_KEY`를 수정하면 다른 페이지와 저장소를 분리할 수 있습니다.
- 스타일 조정: CSS 색상과 섹션 레이아웃을 페이지 톤에 맞게 변경하세요.

## 배포 순서
```bash
git add .
git commit -m "update: 감다살 첼린지 영상 아카이브"
git push origin main
netlify deploy --prod
```

GitHub Pages 주소: https://chosundeveloper.github.io/netlify-text-banner/

## THANKS 전용 페이지
- https://chosundeveloper.github.io/netlify-text-banner/thanks/
- `thanks/index.html`을 수정하면 THANKS 테마 전용 영상 목록을 따로 관리할 수 있습니다.
