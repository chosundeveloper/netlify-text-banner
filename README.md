# 감다살 공 뽑기

버튼 하나로 감다살 멤버 중 한 명을 뽑는 가벼운 페이지입니다. 후보는 기본으로 `이하연셀 정요한`, `강민욱`, `이하연`이 들어 있습니다.

## 바꾸고 싶다면
- 후보 이름은 `index.html` 최하단의 `names` 배열을 수정하세요.
- 색감이나 연출을 조정하려면 같은 파일의 CSS를 손보면 됩니다.

## 배포
```bash
git add .
git commit -m "update: 감다살 공 뽑기"
git push origin main
netlify deploy --prod
```

배포 후에는 `https://netlify-text-banner.netlify.app`에서 바로 확인할 수 있어요.
