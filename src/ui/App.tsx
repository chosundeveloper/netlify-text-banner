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

			{/* 업로드 로그 섹션 제거 */}

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
