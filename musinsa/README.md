# Musinsa MD Brief

## 1. 플러그인은 무엇이고, 누가, 어떤 상황에서 쓰나?

`musinsa-md-brief`는 무신사 카테고리 MD가 트렌드, 브랜드, 상품, 검색/거래/CTR/재고 지표 조각을 받아 머천다이징 의사결정 브리프로 정리하는 skill-only Codex 플러그인입니다.

사용자는 트렌드 민감 카테고리를 맡은 무신사 MD입니다. 사용 상황은 다음 주 시즌 기획전, 카테고리 큐레이션, 프로모션 슬롯, 노출 우선순위, 재고 강조 여부를 결정하기 전입니다. 플러그인은 일부 신호만 있는 상태에서 사실, 누락 입력, MD 질문, 가설, 선택지, 브랜드/고객 리스크, 검증 항목을 분리합니다.

## 2. 왜 이 문제를 선택했나?

무신사 공개 자료는 이 문제가 실제 회사/산업 문제임을 보여줍니다. 무신사는 파트너 브랜드 성장과 고객의 스타일 발견을 회사 방향으로 제시합니다. 뉴스룸은 AI 트렌드 큐레이션이 플랫폼 밖 실시간 패션/뷰티 트렌드를 분석해 상품과 연결한다고 설명합니다. 또 바캉스 품목 검색 증가, 29CM 새틴 스커트 수요 증가처럼 시즌·검색·거래 신호가 실제 기획전과 상품 운영에 연결되는 사례를 공개했습니다.

그래서 이 제출물은 추천 엔진이나 내부 API를 새로 만들지 않습니다. 해커톤에서 검증 가능한 가장 좁은 문제, 즉 MD가 실행 전에 흩어진 신호를 의사결정 가능한 브리프로 바꾸는 일을 해결합니다.

공개 근거:

- 무신사 기업 사이트: 파트너 브랜드 성장과 고객 스타일 발견 미션, https://corp.musinsa.com/ko/
- 무신사 뉴스룸, AI 트렌드 큐레이션, 2026-06-03, https://newsroom.musinsa.com/newsroom-menu/2026-0603
- 무신사 뉴스룸, ChatGPT 무신사 앱과 대화형 상품 발견, 2026-06-09, https://newsroom.musinsa.com/newsroom-menu/2026-0609-01
- 무신사 뉴스룸, 바캉스 용품 검색 증가와 기획전 실행, 2026-07-06, https://newsroom.musinsa.com/newsroom-menu/2026-0706
- 무신사 뉴스룸, 29CM 새틴 스커트 수요 사례, 2026-07-02, https://newsroom.musinsa.com/newsroom-menu/2026-0702
- AX 영상 맥락 확인, 2026-07-08: "무신사의 AI 시대 전략과 인재상 | AX 인재전쟁 3화 무신사", https://www.youtube.com/watch?v=OLAWeIuiD5Y. 공개 YouTube 메타데이터와 한국어 자동 생성 자막을 확인했고, 활용한 맥락은 상품/회원/데이터 시스템 파편화, one-core multi-platform 운영, 브랜드와 고객을 더 명확히 연결하는 의사결정입니다.

## 3. 플러그인은 어떻게 동작하나?

구조는 의도적으로 단순합니다.

- `src/.codex-plugin/plugin.json`: Codex 플러그인 메타데이터
- `src/skills/musinsa-md-brief/SKILL.md`: 실제 동작하는 단일 스킬
- MCP 서버 없음
- 외부 API 없음
- 신규 의존성 없음
- 비공개 무신사 데이터 접근 없음

MD가 입력한 신호를 기반으로 스킬은 항상 아래 섹션을 반환합니다.

- Facts
- Missing Inputs
- MD Questions
- Hypotheses
- Decision Options
- Brand And Customer Risks
- Verification Checks

중요한 가드레일은 사실과 가설을 분리하고, 사용자가 준 수치와 기간을 그대로 보존하며, 근거가 없는 값은 만들지 않는 것입니다.

## 4. AI는 어떻게 사용했나?

AI는 공개 근거와 AX 영상 맥락을 MD 업무 흐름으로 압축하는 데 사용했습니다. 실행 시 AI는 애매한 머천다이징 입력을 구조화하고, 근거 없는 추정을 가설로 표시하며, 실행 전에 확인해야 할 누락 근거를 드러냅니다.

이 플러그인의 AI 사용 범위는 의사결정 보조입니다. 최종 재고, 프로모션, 노출 결정은 사람이 검증 항목을 확인한 뒤 내립니다.

## 5. 플러그인은 어떻게 검증했나?

검증한 항목:

- 작업 루트가 `/Users/jinlee/ax_herkerton/musinsa`임을 확인했습니다.
- `.codex/hooks.json`, `log-hooks/tools/save_log.py`, `logs/codex/`가 폴더 안에 있음을 확인했습니다.
- `../.agents/plugins/marketplace.json`에서 `ax-herkerton-local` 마켓플레이스가 `musinsa-md-brief`를 `./musinsa/src`에서 설치 가능하게 노출하는 것을 확인했습니다.
- 설치 캐시 `~/.codex/plugins/cache/ax-herkerton-local/musinsa-md-brief/0.1.0/`가 존재하고, 캐시 안에 `.codex-plugin/plugin.json`과 `skills/musinsa-md-brief/SKILL.md`가 있음을 확인했습니다.
- 아래 시즌 트렌드/브랜드 지표 샘플로 스킬 출력 형식과 가드레일을 확인했습니다.
- `logs/codex/`에는 폴더-local Stop hook이 원본 그대로 복사한 Codex 대화 로그가 들어 있습니다. 제출용 로그를 편집, 요약, 복사, 후처리하지 않았습니다.

마켓플레이스 확인 근거:

```json
{
  "name": "musinsa-md-brief",
  "source": { "source": "local", "path": "./musinsa/src" },
  "policy": { "installation": "AVAILABLE", "authentication": "ON_INSTALL" }
}
```

설치 캐시 확인 근거:

```text
~/.codex/plugins/cache/ax-herkerton-local/musinsa-md-brief/0.1.0/
├── .codex-plugin/plugin.json
└── skills/musinsa-md-brief/SKILL.md
```

샘플 입력:

```text
Create a Musinsa category MD brief.
Context: summer sandals and linen shirts are rising before peak vacation season.
Brand A has high summer sandal stock and can support a one-week promotion.
Brand B linen shirts have CTR 2.1% vs category average 1.3%, but only limited sizes remain.
We need a low-risk curation decision for next week's summer edit.
```

검증된 출력 형태:

```markdown
## Musinsa MD Brief

### Facts
- The decision is for next week's summer edit.
- Summer sandals and linen shirts are described as rising before peak vacation season.
- Brand A has high summer sandal stock and can support a one-week promotion.
- Brand B linen shirts have CTR 2.1% versus a category average of 1.3%.
- Brand B linen shirts have limited size availability.

### Missing Inputs
- Time window and source for the summer sandals and linen shirts trend signal.
- Brand A sell-through, margin, return rate, price band, and customer segment.
- Brand B stock by size, conversion rate, return rate, replenishment plan, and price band.
- Category-level traffic, search lift, transaction lift, and promotion calendar conflicts.
- Customer fit, styling, and review signals for sandals and linen shirts.

### MD Questions
- Is Brand A's sandal stock matched to the rising search or purchase demand, or just overstock?
- Does Brand B's higher CTR convert after customers see limited size availability?
- Should the summer edit prioritize breadth with Brand A sandals, demand proof with Brand B linen shirts, or a mixed vacation look?
- Which customer segment is most likely to respond: vacation shoppers, office-casual shoppers, or value seekers?

### Hypotheses
- Brand A sandals are a lower operational risk for a one-week promotion because stock support is available.
- Brand B linen shirts may be better for selective editorial placement than broad promotion because CTR is strong but size depth is weak.
- A combined summer edit could work if sandals anchor availability and linen shirts provide trend credibility.

### Decision Options
- Lead with Brand A sandals in the promotion module and use Brand B linen shirts in a smaller styling/editorial slot.
- Run a mixed vacation edit with sandals as shoppable inventory depth and linen shirts as limited-quantity styling support.
- Hold Brand B out of paid promotion until size-depth and replenishment checks pass.

### Brand And Customer Risks
- Brand A risk: broad promotion may feel like stock clearance if styling and trend evidence are weak.
- Brand B risk: high CTR with limited sizes can frustrate customers and waste traffic.
- Customer risk: sandals and linen shirts may serve different occasions unless the edit makes the summer-use case clear.
- Ecosystem risk: over-weighting one brand can reduce partner-brand fairness if category evidence is incomplete.

### Verification Checks
- Confirm trend-source, date range, and search/transaction lift for sandals and linen shirts.
- Compare Brand A promotion inventory to expected sell-through for one week.
- Check Brand B size availability, conversion after click, and replenishment status.
- Review return/review signals for fit, comfort, fabric, and vacation-use language.
- Monitor CTR, conversion, stockout, cancellation, and customer complaint signals during the edit.
```
