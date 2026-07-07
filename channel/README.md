# Channel ALF Planner

Channel ALF Planner는 채널톡 ALF 도입을 준비하는 이커머스 CX 운영 매니저를 위한 skill-only Codex 플러그인입니다. API, MCP 서버, 외부 의존성 없이 `src/skills/channel-alf-planner/SKILL.md` 하나가 Codex의 작업 절차를 정의합니다.

## 1. 플러그인은 무엇이고, 누가 어떤 상황에서 쓰나요?

대상 직무는 이커머스 CX 운영 매니저입니다. 이 사용자는 채널톡 ALF를 실제 운영에 넣기 전에 FAQ, 배송/교환/환불 정책, 상담 매크로, 상품 메모, 익명화된 고객 문의를 정리해야 합니다.

이 플러그인은 붙여 넣은 자료를 다음 ALF 준비 산출물로 바꿉니다.

- Inquiry Taxonomy
- FAQ Gaps
- ALF Rule Candidates
- ALF Task Candidates
- Answer-Quality Risks
- Escalation Triggers
- Next Channel Talk Setup Actions

## 2. 왜 이 문제를 선택했나요?

채널톡의 공개 자료가 같은 준비 업무를 직접 설명합니다. 채널톡 AI 문서는 AI 기능이 반복 문의를 줄이고 팀이 중요한 일에 집중하도록 돕는다고 설명합니다: https://docs.channel.io/help/en/categories/AI-d5340000

FAQ 문서는 ALF가 등록된 FAQ 답변을 바탕으로 응답할 수 있고, AI 추천이 진행 중인 상담을 분석해 자주 들어오는 FAQ 추가를 제안한다고 설명합니다: https://docs.channel.io/help/en/articles/FAQ--db21218c

Rule 문서는 문의 유형, 고객 정보, 상황별로 ALF 지시문을 작성하는 방식을 설명하며 배송 지연 태그, 파손 상품 라우팅 같은 예시를 듭니다: https://docs.channel.io/help/en/articles/Rule-b43e19a1

Knowledge 문서는 ALF가 문서, FAQ, 웹사이트, Excel, PDF 같은 지식 소스를 참조할 수 있고, 참조 설명과 필터로 사용 범위를 제어한다고 설명합니다: https://docs.channel.io/help/en/articles/Knowledge--803f6ac9

Task 문서는 ALF Task가 단순 Q&A를 넘어 주문 취소, 주소 변경, 교환/반품/환불, 사이즈/재고 확인 같은 이커머스 업무를 처리할 수 있다고 설명합니다: https://docs.channel.io/help/en/articles/Task--2a16be8b

따라서 선정한 문제는 "챗봇을 새로 만드는 일"이 아닙니다. 이미 있는 채널톡 ALF 기능을 설정하기 전에, CX 운영 매니저가 어떤 지식을 정리하고, 어떤 FAQ를 보강하고, 어떤 Rule/Task 후보를 만들고, 어떤 케이스를 상담원 검토로 남길지 판단하는 일입니다.

보조 근거로, 채널톡 홈페이지도 AI 해결을 위해 명확한 규칙, 구조화된 지식, 실행 가능한 업무, 지속 개선을 강조합니다: https://channel.io/us

AX 영상 맥락은 많은 AI 도구를 나열하는 것보다 실제 고객/회사 커뮤니케이션 문제에서 왜 이 문제와 도구를 골랐는지 설명하는 역량을 강조합니다: https://www.youtube.com/watch?v=5iRf37Z8Wd4

## 3. 플러그인은 어떻게 작동하나요?

구조는 의도적으로 작습니다.

- `src/.codex-plugin/plugin.json`: 플러그인 이름, 설명, 스킬 경로, 기본 프롬프트를 선언합니다.
- `src/skills/channel-alf-planner/SKILL.md`: Codex가 따라야 할 입력 조건, 개인정보 차단, 분석 절차, 출력 형식을 정의합니다.
- MCP 서버, Channel Talk API 호출, 새 패키지, 런타임 코드는 없습니다.

실행 흐름은 다음과 같습니다.

1. 사용자가 자료를 붙여 넣지 않으면 Codex가 자료를 요청합니다.
2. 개인정보가 보이면 제거를 요청하고 진행하지 않습니다.
3. 사실, 정책, 처리 절차, 불명확한 주장, 문의 예시를 나눕니다.
4. 지저분한 고객 문의를 짧은 표준 질문으로 바꿉니다.
5. 질문과 정책 근거를 문의 분류표로 묶습니다.
6. 고객에게 안전하게 답할 수 없는 FAQ 공백을 찾습니다.
7. 반복 답변, 태그, 라우팅, 상황별 응대에 맞는 ALF Rule 후보를 냅니다.
8. 주문 취소, 주소 변경, 환불, 교환, 재고 확인, 주문/배송 조회처럼 시스템 확인이나 실행이 필요한 경우만 ALF Task 후보로 분리합니다.
9. 답변 품질 리스크, 상담원 이관 기준, 다음 설정 순서를 끝에 둡니다.

정책 근거가 부족하면 추측하지 않고 `not enough evidence`로 표시하도록 스킬에 명시했습니다.

## 4. AI를 어떻게 사용했나요?

AI는 고객 응대 자료를 대신 실행하는 자동화가 아니라, ALF 설정 전 기획 보조자로 사용했습니다. Codex가 비정형 정책/문의 텍스트를 읽고 고객 질문을 표준화하며, 반복 주제를 묶고, FAQ/Rule/Task 후보와 리스크를 초안화합니다.

이 방식은 고객지원 AI가 의도나 개인 맥락을 놓칠 수 있으므로 사람 검토와 이관 조건이 필요하다는 Human-AI support 연구 방향과도 맞습니다: https://arxiv.org/abs/2301.12158

또한 이커머스 메시지를 짧은 질문으로 바꾸는 접근은 buyer-seller messaging 연구의 message-to-question reformulation 방식과 맞습니다: https://arxiv.org/abs/2401.09785

## 5. 플러그인은 어떻게 검증했나요?

검증은 `/Users/jinlee/ax_herkerton/channel` 안에서만 했고, 제출용 로그는 수정하지 않았습니다. `logs/codex/*.jsonl` 파일은 `.codex/hooks.json`의 Stop hook이 `log-hooks/tools/save_log.py`로 원본 transcript를 `logs/` 아래에 그대로 복사한 원본 hook 로그입니다.

설치 확인:

```text
$ pwd
/Users/jinlee/ax_herkerton/channel

$ codex plugin list | rg -n "ax-herkerton|channel-alf"
485:Marketplace `ax-herkerton-local`
489:channel-alf-planner@ax-herkerton-local          installed, enabled  0.1.0    /Users/jinlee/ax_herkerton/channel/src
```

구조 확인:

```text
$ find src -maxdepth 4 -type f | sort
src/.codex-plugin/plugin.json
src/skills/channel-alf-planner/SKILL.md

$ python3 -m json.tool src/.codex-plugin/plugin.json >/dev/null && echo plugin-json-ok
plugin-json-ok
```

로그 훅 확인: `logs/codex`에는 폴더 로컬 Stop hook이 저장한 원본 Codex JSONL 로그가 들어 있음을 확인했습니다.

사용 테스트 입력:

```text
Shipping: standard delivery takes 2-4 business days after payment confirmation. Tracking appears after carrier pickup. Do not promise a delivery date if tracking is missing.
Cancellation: customers may cancel before shipment starts. After shipment starts, guide return process instead.
Returns/exchanges: exchanges and returns are accepted within 7 days of delivery for unused items. Damaged items need photos and order number.
Stock: size restock dates are not guaranteed. Agents can check the product page and internal stock memo.
Payment: failed card payments may be retried; bank approval status cannot be confirmed by support.
Sample inquiries: Where is my package? Can I cancel now? The item arrived damaged. When will size M restock? My card was charged twice. I am a VIP and angry about a delayed gift order.
```

사용 테스트에서 확인한 출력:

- Inquiry Taxonomy: 배송 상태, 취소, 교환/반품/환불, 파손 상품, 재고, 결제, VIP/불만 이관 분류를 확인했습니다.
- FAQ Gaps: 환불 소요 기간, 파손 사진 기준, 재입고 안내 문구, 중복 결제 처리, 배송 지연 약속 금지처럼 입력에 부족한 답변 근거를 확인했습니다.
- ALF Rule Candidates: 배송 태그/라우팅, 파손 상품 접수 라우팅, 결제 불확실성 가드레일, VIP/분노 고객 이관 규칙을 확인했습니다.
- ALF Task Candidates: 취소 가능 여부 확인, 주문/배송 조회, 교환/반품 접수, 파손 상품 접수, 재고 확인처럼 실행 또는 시스템 확인이 필요한 후보만 분리되는 것을 확인했습니다.
- Answer-Quality Risks: 환불 SLA 부재, 재고 정보 최신성, 결제/은행 승인 불확실성, 배송과 취소 정책 충돌 가능성을 확인했습니다.
- Escalation Triggers: VIP 불만, 파손 상품, 중복 결제, 고가 선물 배송 지연, 모호한 주문 상태, 법적/결제 주장, 정책 예외 요청을 확인했습니다.
- Next Channel Talk Setup Actions: 지식 정리, FAQ 추가, 태그/Rule 설정, Task 후보 검토, 상담 태그/분석 확인, 사람 QA 순서를 확인했습니다.
