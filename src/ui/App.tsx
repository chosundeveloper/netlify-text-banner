import React from 'react';

export const App: React.FC = () => {
	return (
		<div className="container">
			<header>
				<h1>감다살 첼린지</h1>
				<p>감다살 셀의 미션/첼린지 영상을 등록하고 시청하세요.</p>
			</header>

			<section className="cards">
				<div className="card">
					<h2>💝 감사, 하루의 발견</h2>
					<p>매일 작은 감사한 순간들을 발견하고 기록하는 특별한 여정을 시작해보세요</p>
				</div>
			</section>

			<section className="features">
				<div>📝 매일 기록</div>
				<div>🤝 함께 공유</div>
				<div>🌟 행복 발견</div>
			</section>

			<section className="logs">
				<h3>업로드 로그</h3>
				<p>최근 업로드 시도와 응답을 확인할 수 있습니다.</p>
				<div className="actions">
					<button>클라우드 동기화</button>
					<button>로그 복사</button>
					<button>로그 초기화</button>
				</div>
				<p><strong>✅ 자동 동기화 활성화:</strong><br />
				 • 어느 기기에서든 업로드하면 모든 기기에서 자동으로 보입니다<br />
				 • 별도 설정 불필요 - 바로 사용 가능<br />
				 • 폰에서 업로드 → 컴퓨터에서 즉시 확인 가능</p>
				<p><strong>🧪 Supabase 연결 테스트:</strong> Database 테스트 · Storage 테스트</p>
				<p><strong>⚠️ Supabase 설정 필요:</strong><br />
				 1. Storage → Buckets → "videos" 버킷 생성 (Public)<br />
				 2. Authentication → Policies → video_uploads RLS 비활성화<br />
				 3. Storage → Policies → videos 버킷 정책 설정</p>
			</section>

			<section className="upload">
				<h3>영상 제목</h3>
				<p><strong>영상 또는 이미지 파일을 끌어다 놓거나 아래 버튼을 눌러 선택하세요.</strong></p>
				<button>파일 선택</button>
				<p>Supabase 클라우드에 저장되어 모든 기기에서 즉시 확인할 수 있습니다.</p>
				<button>업로드</button>
			</section>
		</div>
	);
};
