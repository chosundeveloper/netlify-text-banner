# 감다살 영상 아카이브

한 페이지에서 감다살 **첼린지**와 **THANKS** 영상을 함께 관리할 수 있는 단순 웹 앱입니다. 영상 제목을 입력하고 파일을 드래그&드롭(또는 `파일 선택`)으로 올리면 file.io를 통해 공유 링크가 생성되고, 해당 섹션 목록에 즉시 추가됩니다. 목록은 브라우저 `localStorage`에 저장되어 같은 기기에서는 다음 접속에도 유지됩니다.

## 사용 방법
1. 페이지 상단에서 원하는 섹션(첼린지/THANKS)을 확인합니다.
2. 업로드 폼에 **영상 제목**을 적고, mp4 영상을 끌어다 놓거나 `파일 선택`을 눌러 등록합니다.
3. `업로드` 버튼을 누르면 file.io에 업로드되며, 생성된 링크가 목록에 추가됩니다. (file.io 정책상 1회 다운로드 또는 1주 후 만료)
4. 각 영상 카드 오른쪽의 `삭제` 버튼으로 목록에서 제거할 수 있습니다.

## 커스터마이징 포인트
- 샘플 영상: `index.html` 상단의 `sections` 배열에서 `defaults` 값을 원하는 링크로 수정하세요.
- 저장 키: `storageKey`/`storageVersion`을 수정하면 다른 프로젝트와 저장소 충돌을 막을 수 있습니다.
- 스타일: CSS 색상과 레이아웃을 필요에 맞게 변경하세요.

## 배포 순서
```bash
git add .
git commit -m "update: 감다살 영상 아카이브"
git push origin main
netlify deploy --prod
```

GitHub Pages 주소: https://chosundeveloper.github.io/netlify-text-banner/
