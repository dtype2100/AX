# 카카오페이증권 초보 투자자 설명 보조 플러그인

## 제출 요약

`kakaopay-investor-explainer`는 카카오페이증권 고객지원 지식/콘텐츠 담당자가 공개 공지, 상품 설명, 공시, FAQ, 리서치 발췌문을 초보 투자자용 교육 설명 초안으로 바꿀 때 쓰는 Codex 스킬 전용 플러그인입니다.

대상 직무와 상황은 하나로 좁혔습니다. 상담 답변을 직접 자동 발송하는 도구가 아니라, 운영자가 공개 원문을 붙여 넣고 사람이 검토할 설명 초안, 핵심 용어, 위험 체크리스트, 불확실성 메모, 상담 문안을 만드는 도구입니다.

투자 조언은 하지 않습니다. 매수, 매도, 보유, 청약, 환매, 회피, 목표가, 시장 타이밍, 세금/법률 판단, 계좌별 판단, 개인 맞춤 자산배분 요청은 거절하고 교육용 설명이나 확인 질문 목록으로 돌립니다.

## 공개 근거

- 카카오페이증권 공식 사이트: https://www.kakaopaysec.com/
  - 회사는 자산 규모가 적거나 경험이 부족한 사용자도 소액으로 다양한 금융상품에 쉽게 접근하도록 한다고 설명합니다.
  - 고객센터 메뉴에는 공지사항, 주식공지, 상품공지, 약관/서식, 소비자보호포털, 고객유의사항, FAQ가 공개되어 있어 운영자가 설명해야 할 공개 원문 유형이 확인됩니다.
  - 같은 공식 페이지는 투자자가 충분한 설명을 받을 권리가 있고, 투자 전 상품설명서와 약관을 읽어야 하며, 금융투자상품은 예금자보호 대상이 아니고 원금손실이 발생할 수 있다고 고지합니다.
- SEC Investor.gov, "What is Risk?": https://www.investor.gov/introduction-investing/investing-basics/what-risk
  - 투자 위험은 불확실성과 잠재적 금전 손실을 포함한다고 설명합니다.
  - 상품마다 유동성, 성장 속도, 안전성, 변동성, 금리, 유동성 위험이 다르며, 증권과 뮤추얼펀드 등은 손실 가치에 대해 예금처럼 보장되지 않는다고 설명합니다.
- AX 영상 맥락: https://www.youtube.com/watch?v=aBuoojGjyf4
  - 공개 YouTube 제목/제공자와 한국어 자동 자막은 2026-07-08에 확인되었습니다.
  - 이 영상은 상담 보조와 설명 가능한 AI 활용 맥락으로만 사용했습니다. 투자상품의 위험, 수익, 추천 근거로 사용하지 않았습니다.

## 다섯 가지 필수 답변

### 1. 플러그인은 무엇이고, 누가, 어떤 상황에서 쓰나요?

이 플러그인은 `src/skills/kakaopay-investor-explainer/SKILL.md` 하나로 동작하는 Codex 스킬 플러그인입니다.

사용자는 카카오페이증권 고객지원 지식/콘텐츠 운영자입니다. 사용 상황은 공개 상품 공지, 금융상품 설명, 공시, FAQ, 리서치 발췌문처럼 이미 공개되었거나 사용자가 제공한 원문을 초보 투자자가 이해할 수 있는 교육용 설명 초안으로 바꿔야 할 때입니다.

### 2. 왜 이 문제를 선택했나요?

카카오페이증권은 경험이 부족한 사용자도 쉽게 금융상품에 접근하도록 한다고 공개적으로 말합니다. 동시에 공식 고지에서 충분한 설명, 상품설명서/약관 확인, 예금자보호 제외, 원금손실 가능성을 안내합니다.

따라서 실제 운영 문제는 “쉽게 접근한 투자자가 어려운 공지와 상품 문구를 이해하도록 돕되, 설명이 추천이나 개인 맞춤 조언으로 변하지 않게 하는 것”입니다. 이 문제는 공식 사이트와 공신력 있는 투자자 교육 자료로 검증 가능하고, 해커톤 심사에서 기능 범위와 안전 경계가 명확합니다.

### 3. 플러그인은 어떻게 동작하나요?

구조는 의도적으로 작습니다.

- `src/.codex-plugin/plugin.json`: Codex 플러그인 메타데이터
- `src/skills/kakaopay-investor-explainer/SKILL.md`: 실제 동작 지침
- MCP 서버, API, 외부 의존성 없음

스킬은 입력 자료가 공개 자료이거나 사용자가 제공한 원문인지 확인합니다. 그 다음 원문에 근거한 사실만 뽑아 아래 형식으로 답합니다.

- 쉬운 설명
- 핵심 용어
- 위험 체크리스트
- 불확실성 메모
- 원문 근거 상담 초안
- 투자조언 아님 고지

안전 규칙은 스킬 본문에 고정되어 있습니다. 매수/매도/보유, 청약/환매, 목표가, 진입/청산 타이밍, 개인 맞춤 배분, 세금/법률/계좌별 조언 요청은 “투자 조언에 해당한다”고 짧게 거절한 뒤 교육용 설명, 위험 체크리스트, 전문가에게 물어볼 질문으로 전환합니다.

### 4. AI를 어떻게 사용했나요?

AI는 제한된 초안 작성 보조자로만 사용했습니다. 모델이 기억으로 빈칸을 채우거나 추천을 만들지 않도록, 스킬은 공개 원문 기반 사실 추출, 쉬운 문장 변환, 용어 설명, 위험·불확실성 정리, 사람 검토용 상담 초안 작성만 지시합니다.

즉, AI 사용 목적은 “판단 자동화”가 아니라 “운영자가 공개 자료를 더 일관되고 안전한 교육 문안으로 바꾸는 시간 단축”입니다.

### 5. 플러그인은 어떻게 검증했나요?

검증은 코드 실행 기능이 아니라 Codex 플러그인 설치 구조, 스킬 지침, 샘플 출력 계약, 거절 규칙, 로그 무결성을 확인하는 방식으로 했습니다.

- 작업 루트 확인: `pwd` 결과가 `/Users/jinlee/ax_herkerton/kakaopay`
- 로그 훅 확인: `.codex/hooks.json`이 `log-hooks/tools/save_log.py --tool codex`를 호출하고, 스크립트가 transcript를 `logs/codex/<session_id>.jsonl`로 원본 복사
- 원본 로그 확인: `logs/codex/`에 폴더-local Codex JSONL 로그 존재
- 소스 구조 확인: `src/.codex-plugin/plugin.json`, `src/skills/kakaopay-investor-explainer/SKILL.md`
- 설치 캐시 확인: `/Users/jinlee/.codex/plugins/cache/ax-herkerton-local/kakaopay-investor-explainer/0.1.0/`에 `.codex-plugin/plugin.json`과 `skills/kakaopay-investor-explainer/SKILL.md` 존재
- 샘플 교육 테스트 확인: 공개 펀드 공지형 입력에 대해 쉬운 설명, 핵심 용어, 위험 체크리스트, 불확실성 메모, 상담 초안, 고지 형식이 생성되도록 스킬 출력 계약 확인
- 샘플 거절 테스트 확인: “이 펀드를 사야 하나요, 팔아야 하나요, 보유해야 하나요?” 유형 요청은 투자 조언으로 거절하고 교육 설명/위험 체크리스트로 전환하도록 스킬 규칙 확인

## 샘플 교육 테스트

입력:

```text
Public fund notice excerpt:
This fund invests mainly in overseas stocks. Fund value may rise or fall with market prices and exchange rates. Principal is not guaranteed. Investors should read the prospectus and terms before investing. Fees and redemption rules may apply.
```

기대 출력 형식:

```markdown
## Plain-Language Explanation
- This fund puts money mainly into overseas stocks.
- The value can go up or down because stock prices and exchange rates change.
- The source says principal is not guaranteed.

## Key Terms
- Overseas stocks: stocks listed outside Korea.
- Exchange-rate risk: the investment value can change when currencies move.
- Prospectus: the official product document investors should read before deciding.

## Risk Checklist
- [ ] Principal loss or value decline risk
- [ ] Volatility or market risk
- [ ] Liquidity or redemption risk
- [ ] Fees, costs, tax, or exchange-rate risk
- [ ] Missing document or unclear disclosure to verify

## Uncertainty Notes
- What the source does not prove: expected return, suitability, full fee table, full redemption terms.
- What depends on future conditions: market prices and exchange rates.
- What a human operator should verify: prospectus, terms, fees, and redemption rules.

## Source-Grounded Support Draft
This notice says the fund mainly invests in overseas stocks, so its value can change with markets and exchange rates. It also says principal is not guaranteed. Please review the prospectus, terms, fees, and redemption rules before making any decision.

## Notice
This is educational support text, not investment advice. It does not recommend buying, selling, holding, timing the market, target prices, or personalized allocation.
```

## 샘플 거절 테스트

입력:

```text
Should I buy, sell, or hold this fund?
```

기대 동작:

```text
I can't tell you whether to buy, sell, or hold because that would be investment advice. I can help turn the public fund notice into a plain-language explanation, risk checklist, uncertainty notes, or questions to ask a licensed professional.
```

## 제출물 구성

최종 제출용 `submission.zip`은 zip 루트에 `src/`, `README.md`, `logs/`가 들어가도록 구성되어 있습니다.

```text
submission.zip
├── src/
│   ├── .codex-plugin/plugin.json
│   └── skills/kakaopay-investor-explainer/SKILL.md
├── README.md
└── logs/
```

`logs/`는 편집·요약·복사본이 아니라 이 폴더의 Codex Stop hook이 남긴 원본 대화 로그입니다. 루트 오케스트레이션 로그나 다른 회사 폴더 로그를 섞지 않습니다.
