# 감다살 첼린지

감다살 셀 구성원들이 촬영한 첼린지 영상을 모아 보는 웹 페이지입니다. 영상 제목을 입력하고 파일을 드래그&드롭(또는 파일 선택 버튼)으로 올리면 file.io를 통해 공유 링크가 생성되고 목록에 자동 추가됩니다. 목록은 브라우저 `localStorage`에 저장되어 다음 접속에도 유지됩니다.

## 사용 방법
1. 페이지에 접속하면 기본 샘플 영상 10개가 보입니다.
2. 하단 업로드 폼에서 **영상 제목**을 입력한 뒤 파일을 끌어다 놓거나 `파일 선택` 버튼으로 mp4 영상을 고릅니다.
3. `업로드` 버튼을 누르면 file.io에 업로드되고, 생성된 링크가 목록에 추가됩니다. (file.io 정책상 1회 다운로드 또는 1주 후 만료)
4. 영상 카드 오른쪽의 `삭제` 버튼으로 목록에서 제거할 수 있습니다.

## 커스터마이징 포인트
- 샘플 영상 변경: `index.html`의 `DEFAULT_UPLOADS` 배열을 원하는 링크로 수정하세요.
- 저장 키 변경: `STORAGE_KEY`/`STORAGE_VERSION`을 수정하면 다른 페이지와 저장소를 분리할 수 있습니다.
- 스타일 조정: CSS 색상과 섹션 레이아웃을 페이지 톤에 맞게 변경하세요.

## 배포 순서
```bash
git add .
git commit -m "update: 감다살 첼린지"
git push origin main
netlify deploy --prod
```

GitHub Pages 주소: https://chosundeveloper.github.io/netlify-text-banner/

## THANKS 페이지
- https://chosundeveloper.github.io/netlify-text-banner/thanks/