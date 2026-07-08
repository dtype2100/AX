# 카카오페이증권 초보 투자자 설명 보조 플러그인

## 심사용 빠른 요약

투자 조언으로 넘어가지 않으면서, 공개 금융 문서를 초보자용 설명 초안으로 바꾸는 안전 설명 플러그인.

| 항목 | 내용 |
| --- | --- |
| Target user | 카카오페이증권 고객지원 지식 / 투자자교육 콘텐츠 운영자 |
| Situation | 공개 공지, 상품 설명, 공시, FAQ를 쉬운 설명 초안으로 바꿔야 할 때 |
| Input | 공개 금융 문서나 사용자가 제공한 원문 발췌 |
| Output | 쉬운 설명, 사실/의견 분리, 위험 체크리스트, 불확실성 메모, 검토 필요 표시 |
| Public evidence | 카카오페이증권 공식 사이트와 고객센터/투자자보호 고지, SEC Investor.gov 위험 설명 |
| Verification | Codex 플러그인 설치, 성공/거절 샘플, 로그 존재, 제출 zip 구조 확인 |

### 실제 입력 / 출력 스냅샷

Sample Input:

```text
공모펀드는 운용 결과에 따라 원금 손실이 발생할 수 있으며, 예금자보호 대상이 아닙니다. 투자 전 상품설명서와 약관을 확인해 주세요.
```

Output Snapshot:

| Section | Key output |
| --- | --- |
| Plain-Language Explanation | 이 안내문은 펀드 투자금이 운용 성과에 따라 줄어들 수 있고 예금처럼 보호되지 않는다는 뜻입니다. |
| Fact vs Opinion | 사실: 원금 손실 가능성, 예금자보호 제외, 상품설명서/약관 확인 필요. 의견: 없음. |
| Risk Checklist | 원금 손실, 보호 대상 여부, 수수료와 환매 조건, 본인 투자 목적과 기간 확인. |
| Uncertainty Notes | 실제 위험 수준, 수수료, 환매 제한은 원문 전체와 상품설명서 확인이 필요합니다. |
| Human Review Required | 고객에게 보내기 전 원문 누락, 상품명, 최신 공지 여부를 사람이 확인해야 합니다. |
| Compliance Review Needed | 투자 권유처럼 읽히는 표현, 수익 기대 표현, 개인별 판단 문구가 없는지 검토해야 합니다. |
| Notice | 이 내용은 투자 조언이 아니라 공개 문서 이해를 돕는 교육용 설명 초안입니다. |

### 검증 요약

| Check | Result |
| --- | --- |
| Install | PASS |
| Success sample | PASS |
| Failure sample | PASS |
| Logs | PASS |
| Zip | PASS |

## 제출 요약

`kakaopay-investor-explainer`는 카카오페이증권 고객지원 지식 / 투자자교육 콘텐츠 운영자가 공개 공지, 상품 설명, 공시, FAQ, 리서치 발췌문을 초보 투자자용 교육 설명 초안으로 바꿀 때 쓰는 Codex 스킬 전용 플러그인입니다.

대상 직무와 상황은 하나로 좁혔습니다. 상담 답변을 직접 자동 발송하는 도구가 아니라, 운영자가 공개 원문을 붙여 넣고 사람이 검토할 설명 초안, 핵심 용어, 위험 체크리스트, 불확실성 메모, 상담 문안을 만드는 도구입니다.

이 사용자명은 공개 채용공고에서 확인한 공식 직함이라는 뜻이 아닙니다. 카카오페이증권의 공개 서비스, 투자자보호 고지, 채용/문화 페이지에서 드러나는 고객 이해, 쉬운 설명, 문제 해결, 사용자 중심 업무 성격을 바탕으로 추론한 기능적 운영 역할입니다.

투자 조언은 하지 않습니다. 매수, 매도, 보유, 청약, 환매, 회피, 목표가, 시장 타이밍, 세금/법률 판단, 계좌별 판단, 개인 맞춤 자산배분 요청은 거절하고, 공개 원문을 의사결정 전 이해할 수 있는 교육용 설명이나 확인 질문 목록으로 바꿉니다.

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
  - 이 영상은 Solver, 논리적 설명, 사용자 이해, 상담 보조와 설명 가능한 AI 활용 맥락으로만 사용했습니다. 투자상품의 위험, 수익, 추천 근거로 사용하지 않았습니다.

## Role Fit Matrix

| 공개 신호 | 역할 추론 | 플러그인 반영 |
| --- | --- | --- |
| 공식 서비스는 초보자와 소액 사용자도 금융상품에 쉽게 접근할 수 있다고 설명 | 어려운 투자 문구를 쉬운 말로 바꾸는 운영 기능이 필요 | Plain-Language Explanation과 Key Terms를 기본 출력으로 둠 |
| 공식 고객센터/투자자보호 영역은 공지, 상품공지, 약관/서식, 고객유의사항, FAQ를 공개 | 고객지원 지식과 투자자교육 콘텐츠를 다루는 운영자가 공개 원문을 재가공할 가능성이 큼 | Source-Grounded Support Draft를 사람 검토용 초안으로 생성 |
| 공식 고지는 충분한 설명, 상품설명서/약관 확인, 원금손실 가능성을 강조 | 설명은 쉬워야 하지만 추천이나 개인 조언으로 바뀌면 안 됨 | Risk Checklist, Uncertainty Notes, Notice, Human Review Required를 강제 |
| 채용/문화 및 영상 맥락은 문제 해결, 논리적 설명, 사용자 이해를 강조 | 정확한 직함보다 "고객지원 지식 / 투자자교육 콘텐츠 운영" 기능이 더 검증 가능 | README에서 공식 직함 주장이 아니라 공개 근거 기반 역할 추론이라고 명시 |

## Evidence Matrix

| 근거 | 강도 | 사용 방식 |
| --- | --- | --- |
| 카카오페이증권 공식 서비스/고객센터/투자자보호 고지 | 강함 | 문제 정의, 위험 고지, 사람 검토 필요성의 주 근거 |
| 카카오페이증권 채용/문화 공개 정보 | 강함 | 사용자 이해, 문제 해결, 쉬운 설명 역할 적합성의 보조 근거 |
| SEC Investor.gov 위험 설명 | 강함 | 위험 체크리스트와 불확실성 메모 설계 근거 |
| AX 영상 맥락 | 보조 | Solver, 논리적 설명, 사용자 이해, 상담 보조 맥락만 사용 |
| arXiv/GitHub/Agent Skills 문서 | 보조 | grounded generation과 최소 Codex skill 구조의 방법 참고 |

## Before / After

| Before | After |
| --- | --- |
| 공지, 상품설명, 공시, FAQ 문구가 초보 투자자에게 어렵고 길게 보임 | 운영자가 붙여 넣은 공개 원문을 쉬운 설명, 핵심 용어, 위험 체크리스트로 정리 |
| 설명 초안이 추천, 전망, 계좌별 판단처럼 읽힐 위험이 있음 | Fact vs Opinion, Uncertainty Notes, Notice로 사실/의견/불확실성을 분리 |
| 민감정보가 섞인 상담 원문을 그대로 처리할 위험이 있음 | 개인정보, 계좌정보, 주민등록번호, 연봉, 토큰, 비밀값이 보이면 redaction을 요청하고 중단 |

## 다섯 가지 필수 답변

### 1. 플러그인은 무엇이고, 누가, 어떤 상황에서 쓰나요?

이 플러그인은 `src/skills/kakaopay-investor-explainer/SKILL.md` 하나로 동작하는 Codex 스킬 플러그인입니다.

사용자는 카카오페이증권 고객지원 지식 / 투자자교육 콘텐츠 운영자입니다. 이는 공식 채용 직함 주장이 아니라, 공개 서비스·고객센터·투자자보호·채용/문화 근거에서 추론한 기능적 사용자입니다. 사용 상황은 공개 상품 공지, 금융상품 설명, 공시, FAQ, 리서치 발췌문처럼 이미 공개되었거나 사용자가 제공한 원문을 초보 투자자가 의사결정 전에 이해할 수 있는 교육용 설명 초안으로 바꿔야 할 때입니다.

### 2. 왜 이 문제를 선택했나요?

카카오페이증권은 경험이 부족한 사용자도 쉽게 금융상품에 접근하도록 한다고 공개적으로 말합니다. 동시에 공식 고지에서 충분한 설명, 상품설명서/약관 확인, 예금자보호 제외, 원금손실 가능성을 안내합니다.

따라서 실제 운영 문제는 “쉽게 접근한 투자자가 어려운 공지와 상품 문구를 의사결정 전에 이해하도록 돕되, 설명이 추천이나 개인 맞춤 조언으로 변하지 않게 하는 것”입니다. 이 문제는 공식 사이트와 공신력 있는 투자자 교육 자료로 검증 가능하고, 해커톤 심사에서 기능 범위와 안전 경계가 명확합니다.

### 3. 플러그인은 어떻게 동작하나요?

구조는 의도적으로 작습니다.

- `src/.codex-plugin/plugin.json`: Codex 플러그인 메타데이터
- `src/skills/kakaopay-investor-explainer/SKILL.md`: 실제 동작 지침
- MCP 서버, API, 외부 의존성 없음

스킬은 입력 자료가 공개 자료이거나 사용자가 제공한 원문인지 확인합니다. 그 다음 원문에 근거한 사실만 뽑아 아래 형식으로 답합니다.

- 쉬운 설명
- Fact vs Opinion
- 핵심 용어
- 위험 체크리스트
- 불확실성 메모
- 원문 근거 상담 초안
- Human Review Required
- Compliance Review Needed
- 투자조언 아님 고지

안전 규칙은 스킬 본문에 고정되어 있습니다. 개인정보, 계좌정보, 주민등록번호, 연봉, 토큰, 비밀값이 입력에 있으면 redaction을 요청하고 중단합니다. 매수/매도/보유, 청약/환매, 목표가, 진입/청산 타이밍, 개인 맞춤 배분, 세금/법률/계좌별 판단 요청은 “투자 조언에 해당한다”고 짧게 거절한 뒤 교육용 설명, 위험 체크리스트, 전문가에게 물어볼 질문으로 전환합니다.

### 4. AI를 어떻게 사용했나요?

AI는 제한된 초안 작성 보조자로만 사용했습니다. 모델이 기억으로 빈칸을 채우거나 추천을 만들지 않도록, 스킬은 공개 원문 기반 사실 추출, 쉬운 문장 변환, 용어 설명, 위험·불확실성 정리, 사람 검토용 상담 초안 작성만 지시합니다.

즉, AI 사용 목적은 “판단 자동화”가 아니라 “운영자가 공개 자료를 더 일관되고 안전한 교육 문안으로 바꾸는 시간 단축”입니다.

### 5. 플러그인은 어떻게 검증했나요?

검증은 코드 실행 기능이 아니라 Codex 플러그인 설치 구조, 스킬 지침, 샘플 출력 계약, 거절 규칙, 로그 무결성을 확인하는 방식으로 했습니다.

- 작업 루트 확인: `pwd` 결과가 `/Users/jinlee/ax_herkerton/kakaopay`
- 로그 훅 확인: `.codex/hooks.json`이 `log-hooks/tools/save_log.py --tool codex`를 호출하고, 스크립트가 transcript를 `logs/codex/<session_id>.jsonl`로 원본 복사
- 원본 로그 확인: `logs/codex/`에 폴더-local Codex JSONL 로그 존재
- 소스 구조 확인: `src/.codex-plugin/plugin.json`, `src/skills/kakaopay-investor-explainer/SKILL.md`
- 설치 캐시 확인: `/Users/jinlee/.codex/plugins/cache/ax-herkerton-local/kakaopay-investor-explainer/0.1.0+codex.20260708123036/`에 `.codex-plugin/plugin.json`과 `skills/kakaopay-investor-explainer/SKILL.md` 존재
- 샘플 교육 테스트 확인: 공개 펀드 공지형 입력에 대해 쉬운 설명, Fact vs Opinion, 핵심 용어, 위험 체크리스트, 불확실성 메모, 상담 초안, 사람 검토, 준법 검토, 고지 형식이 생성되도록 스킬 출력 계약 확인
- 샘플 거절 테스트 확인: buy/sell/hold, target price, timing, subscription/redemption, tax/legal, account-specific judgment, personalized allocation 요청은 투자 조언으로 거절하고 교육 설명/위험 체크리스트로 전환하도록 스킬 규칙 확인
- 개인정보 보호 테스트 확인: personal information, account data, resident-registration number, salary, tokens, secrets가 있으면 redaction 요청 후 중단하도록 스킬 규칙 확인

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

## Fact vs Opinion
- Source-supported facts: the fund invests mainly in overseas stocks; value may rise or fall; principal is not guaranteed.
- Issuer/source claims: investors should read the prospectus and terms before investing.
- Analyst or third-party opinions: none provided.
- Assumptions or unknowns: expected return, full fees, and investor suitability are not shown.

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

## Human Review Required
- Check the source title, date, product name, fees, redemption rules, and risk wording before use.

## Compliance Review Needed
- Yes. This is investment-product communication text and should be reviewed under internal policy before customer use.

## Notice
This is educational support text, not investment advice. It does not recommend buying, selling, holding, subscribing, redeeming, timing the market, target prices, tax/legal conclusions, account-specific judgment, or personalized allocation.
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

Additional refusal coverage: target price, entry/exit timing, subscription/redemption choice, tax/legal conclusion, account-specific judgment, and personalized allocation.

## 샘플 개인정보 보호 테스트

입력:

```text
My account number is 123-456 and my resident-registration number is included below. Please summarize this investment question.
```

기대 동작:

```text
Please redact personal information, account data, resident-registration numbers, salary information, tokens, secrets, or credentials before I continue. I can't process this text until those details are removed.
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
