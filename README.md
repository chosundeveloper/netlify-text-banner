# Netlify 문자 출력 예제

아주 간단한 정적 페이지를 Netlify에 배포하기 위한 예제입니다. `index.html`의 내용을 원하는 문구로 바꾸고 GitHub 저장소에 올린 뒤 Netlify와 연동하면 자동으로 배포됩니다.

## 사용 방법

1. 이 디렉터리에서 Git 초기화 및 커밋을 준비합니다.
   ```bash
   git init
   git add .
   git commit -m "초기 커밋: Netlify 데모"
   ```
2. GitHub에 새 저장소를 만든 후 원격을 등록하고 푸시합니다.
   ```bash
   git remote add origin https://github.com/<your-id>/<repo-name>.git
   git push -u origin main
   ```
3. [Netlify](https://app.netlify.com/)에 접속하여 **Add new site → Import an existing project → GitHub**를 선택합니다.
4. 방금 만든 GitHub 저장소를 선택하고 다음 설정을 적용합니다.
   - **Build command:** (빈 칸으로 두기)
   - **Publish directory:** `.`
5. **Deploy site** 버튼을 누르면 몇 초 내로 배포가 완료됩니다.
6. 배포 URL을 확인하고, 필요하다면 `Site settings → Domain management`에서 사용자 지정 도메인을 연결할 수 있습니다.

## 수정 포인트

- 문구를 바꾸고 싶으면 `index.html`의 `<h1>`나 `<p>` 내용을 수정하세요.
- 정적 파일을 추가하려면 같은 디렉터리에 이미지를 넣거나, 하위 폴더를 만들어 링크하면 됩니다.

즐거운 배포 되세요!
