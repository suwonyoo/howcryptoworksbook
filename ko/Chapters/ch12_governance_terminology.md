# Chapter 12: Governance and Token Economics - 신규 용어 목록

이 문서는 Chapter 12에서 새롭게 등장한 기술 용어들을 정리합니다. 용어집(glossary.md)에 이미 정의된 용어는 제외되었습니다.

---

## 거버넌스 핵심 개념 (Governance Core Concepts)

| English | Korean | 번역 근거 |
|---------|--------|-----------|
| DAO (Decentralized Autonomous Organization) | 탈중앙화 자율 조직 (DAO) | 코드가 헌법이 되고 토큰이 투표권이 되는 자율 조직 |
| Governance Token | 거버넌스 토큰 | 프로토콜 의사결정 투표권을 부여하는 토큰 |
| Timelock | 타임락 | 제안 통과와 실행 사이의 지연 기간. glossary에 등재 |
| Quorum | 정족수 | 투표가 유효하기 위해 필요한 최소 참여 임계값 |
| Delegation | 위임 | 투표권을 다른 참여자에게 양도하는 행위 |
| Delegate | 대리인 | 다른 토큰 보유자로부터 투표권을 위임받은 주체 |
| Principal-Agent Problem | 주인-대리인 문제 | 소유자와 운영자 간의 이해 충돌 문제 |

## 투표 메커니즘 (Voting Mechanisms)

| English | Korean | 번역 근거 |
|---------|--------|-----------|
| Token-Weighted Voting | 토큰 가중 투표 | 토큰 보유량에 비례한 투표권 방식 (한 토큰, 한 표) |
| veTokenomics (Vote-Escrow Tokenomics) | 투표-예치 토크노믹스 | 락업 기간에 비례하여 투표권이 증가하는 시스템 |
| veCRV | veCRV | Curve의 투표-예치 CRV 토큰. 고유명사 |
| Gauge | 게이지 | Curve에서 풀별 배출 비율을 결정하는 구성 |
| Vote-Bribe Market | 투표-뇌물 시장 | 투표 방향을 유도하기 위해 토큰 보유자에게 지불하는 시장 |
| Quadratic Voting | 이차 투표 | k표의 비용이 k²인 투표 방식으로 부의 영향력 억제 |
| Futarchy | 퓨타키 | "가치에 투표, 신념에 베팅" - 예측 시장 기반 의사결정 |
| Prediction Market | 예측 시장 | 미래 결과에 베팅하여 정보를 집계하는 시장 |

## 거버넌스 공격 및 보안 (Governance Attacks and Security)

| English | Korean | 번역 근거 |
|---------|--------|-----------|
| Flash Loan Governance Attack | 플래시론 거버넌스 공격 | 단일 트랜잭션에서 토큰 차입으로 투표권 획득 후 공격 |
| Snapshot-Based Voting | 스냅샷 기반 투표 | 과거 특정 블록의 잔액으로 투표권 결정 |
| Voting Delay | 투표 지연 | 제안 생성과 투표 시작 사이의 시간 |
| Voting Period | 투표 기간 | 투표가 진행되는 창 |
| Governance Bribery | 거버넌스 뇌물 | 특정 방식으로 투표하도록 토큰 보유자에게 지불 |
| Proposal Spam | 제안 스팸 | 악의적 변경을 숨기기 위해 노이즈로 거버넌스를 막는 행위 |
| 51% Attack | 51% 공격 | 과반 토큰 축적으로 영구 통제권 획득 |
| Governance Minimization | 거버넌스 최소화 | 통치 가능한 범위를 줄여 공격 표면 최소화 |

## 제안 수명 주기 (Proposal Lifecycle)

| English | Korean | 번역 근거 |
|---------|--------|-----------|
| RFC (Request for Comment) | 코멘트 요청 (RFC) | 비공식 토론 및 피드백 수집 단계 |
| Temperature Check | 온도 체크 | 대략적 합의 확인을 위한 예비 투표 |
| Consensus Check | 합의 체크 | 온체인 진행 전 최종 확인 투표 |
| Snapshot | 스냅샷 | 가스 없는 오프체인 투표 플랫폼. 고유명사 |
| On-Chain Proposal | 온체인 제안 | 스마트 컨트랙트에 제출된 공식 제안 |
| Executor | 실행자 | 통과된 제안의 액션을 트리거하는 주체 |
| Multi-sig Wallet | 다중 서명 지갑 | 여러 서명자의 승인이 필요한 지갑. glossary에 등재 |

## 거버넌스 도구 (Governance Tools)

| English | Korean | 번역 근거 |
|---------|--------|-----------|
| Safe (Gnosis Safe) | Safe (Gnosis Safe) | 멀티시그 지갑 인프라. 고유명사 |
| Tally | Tally | 거버넌스 대시보드 플랫폼. 고유명사 |
| Discourse | Discourse | 포럼 호스팅 플랫폼. 고유명사 |
| Commonwealth | Commonwealth | DAO 토론 플랫폼. 고유명사 |

## 토큰 경제학 (Token Economics)

| English | Korean | 번역 근거 |
|---------|--------|-----------|
| Token Economics (Tokenomics) | 토큰 경제학 (토크노믹스) | 토큰의 발행, 분배, 인센티브 설계 |
| Pure Governance Token | 순수 거버넌스 토큰 | 투표권만 제공하는 토큰 (수익 배분 없음) |
| Revenue-Sharing Token | 수익 공유 토큰 | 프로토콜 수익을 보유자에게 분배하는 토큰 |
| Buyback-and-Burn | 바이백-앤-번 | 수익으로 토큰 구매 후 영구 소멸 |
| Utility Token | 유틸리티 토큰 | 서비스 접근을 위한 네이티브 통화 역할 토큰 |
| Fixed Supply | 고정 공급 | 총 공급량에 하드 캡이 있는 토큰 |
| Inflationary Model | 인플레이션 모델 | 지속적으로 새 토큰을 발행하는 모델 |
| Deflationary Model | 디플레이션 모델 | 토큰을 만드는 것보다 빠르게 소각하는 모델 |

## 베스팅 및 분배 (Vesting and Distribution)

| English | Korean | 번역 근거 |
|---------|--------|-----------|
| Vesting Schedule | 베스팅 일정 | 내부자 토큰의 점진적 언락 일정 |
| Cliff | 클리프 | 베스팅 시작 전 토큰 릴리스가 없는 초기 기간 |
| Linear Vesting | 선형 베스팅 | 시간에 따라 균등하게 토큰을 릴리스 |
| Milestone Vesting | 마일스톤 베스팅 | 특정 달성에 따라 토큰을 릴리스 |
| Supply Overhang | 공급 오버행 | 언락되었지만 아직 매도되지 않은 토큰 |
| Unlock Event | 언락 이벤트 | 베스팅 토큰이 유동화되는 시점 |
| Hedging Against Unlocks | 언락 헤징 | 파생상품으로 언락 전 가격을 락인하는 전략 |

## 에어드롭 및 분배 전략 (Airdrops and Distribution Strategies)

| English | Korean | 번역 근거 |
|---------|--------|-----------|
| Retroactive Airdrop | 소급적 에어드롭 | 과거 사용에 기반한 토큰 무상 분배 |
| Airdrop Farming | 에어드롭 파밍 | 예상 에어드롭 기준을 게임하기 위한 조직적 활동 |
| Point Program | 포인트 프로그램 | 지속적 참여 인센티브 시스템 |
| Season | 시즌 | 3-6개월 지속되는 포인트 프로그램의 반복 기간 |
| Transparent Criteria Season | 투명한 기준 시즌 | 정확한 포인트 공식을 사전 공개하는 시즌 |
| Opaque Season | 불투명한 시즌 | 기준을 의도적으로 모호하게 하는 시즌 |

## 조직 구조 (Organizational Structure)

| English | Korean | 번역 근거 |
|---------|--------|-----------|
| Three-Pillar Structure | 3개 기둥 구조 | DAO, 재단, Labs로 구성된 표준 DAO 조직 모델 |
| Labs Company | Labs 회사 | 연구, 개발, 제품 출시를 담당하는 영리 기업 |
| Foundation | 재단 | 스튜어드십 기능을 수행하는 비영리 법인 |
| Protocol Grants Program | 프로토콜 그랜트 프로그램 | 생태계 개발 자금 지원 프로그램 |
| Fee Switch | 수수료 스위치 | 프로토콜 수수료 활성화/비활성화 거버넌스 결정 |
| Growth Budget | 성장 예산 | DAO에서 Labs에 제공하는 개발 자금 |
| Service Provider Agreement | 서비스 제공자 계약 | Labs와 DAO 간의 법적 관계 정의 |

## 법적 및 규제 (Legal and Regulatory)

| English | Korean | 번역 근거 |
|---------|--------|-----------|
| Legal Wrapper | 법적 래퍼 | DAO에 법인격을 부여하는 법적 구조 |
| BBLLC (Blockchain-Based LLC) | 블록체인 기반 LLC | 버몬트의 블록체인 기반 유한 책임 회사 |
| DUNA (Decentralized Unincorporated Nonprofit Association) | DUNA | 와이오밍의 탈중앙화 비법인 비영리 협회 |
| Howey Test | Howey 테스트 | 증권 여부를 판단하는 미국 법적 테스트 |
| Ooki DAO Case | Ooki DAO 사건 | DAO 구성원 책임에 관한 CFTC 집행 사례 |
| Fiduciary Duty | 수탁 의무 | 타인 자산 관리에 대한 법적 의무 |
| Unincorporated Association | 비법인 협회 | 별도 법인격 없이 공동 목적을 가진 단체 |

## 재무 관리 (Treasury Management)

| English | Korean | 번역 근거 |
|---------|--------|-----------|
| DAO Treasury | DAO 재무 | DAO가 통제하는 집단 자산 |
| Treasury Diversification | 재무 다각화 | 자체 토큰 외 ETH, BTC, 수익 창출 자산 보유 |
| Treasury Committee | 재무 위원회 | 일상 재무 운영 권한을 위임받은 전문 위원회 |
| Circular Dependency | 순환적 의존성 | 재무 가치가 자체 토큰 가격과 연동되는 문제 |
| Emergency Pause | 긴급 일시정지 | 멀티시그가 프로토콜을 즉시 중단시킬 수 있는 기능 |

## 소셜 레이어 (Social Layer)

| English | Korean | 번역 근거 |
|---------|--------|-----------|
| Social Layer | 소셜 레이어 | 공식 투표 전 발생하는 비공식 조율 및 합의 |
| Core Contributors | 핵심 기여자 | DAO 거버넌스를 적극적으로 형성하는 소수 참여자 |
| Delegate Calls | 대리인 회의 | 주요 대리인들 간의 조율 미팅 |
| Back-channel Coordination | 백채널 조율 | 공식 채널 외에서 이루어지는 비공식 합의 |
| Governance Fatigue | 거버넌스 피로 | 끊임없는 의사결정 요구로 인한 기여자 소진 |
| Institutional Knowledge | 제도적 지식 | 시간이 지남에 따라 핵심 기여자에게 축적된 지식 |

---

## 고유명사 및 프로젝트 (Proper Nouns and Projects)

| English | Korean | 비고 |
|---------|--------|------|
| The DAO | The DAO | 2016년 이더리움의 첫 주요 DAO 실험 |
| Uniswap | Uniswap | 대표적 AMM DEX 및 거버넌스 사례 연구 |
| Uniswap Labs | Uniswap Labs | Uniswap 프로토콜 개발 영리 회사 |
| Uniswap Foundation | Uniswap 재단 | Uniswap 생태계 지원 비영리 법인 |
| Uniswap DAO | Uniswap DAO | UNI 토큰 보유자들의 통치 기구 |
| Unichain | Unichain | Uniswap의 앱체인/L2 |
| DUNI | DUNI | Uniswap의 와이오밍 DUNA 법적 래퍼 |
| Curve | Curve | veTokenomics를 개척한 스테이블코인 전문 DEX |
| Aave | Aave | 대표적 탈중앙화 대출 프로토콜 |
| Beanstalk | Beanstalk | 2022년 플래시론 거버넌스 공격 피해 프로토콜 |
| MetaDAO | MetaDAO | 솔라나의 퓨타키 거버넌스 실험 |
| Gnosis | Gnosis | 조건부 시장 및 Safe 지갑 개발사 |
| dYdX | dYdX | 수익 공유 토큰 모델의 무기한 거래소 |
| Hyperliquid | Hyperliquid | 바이백-앤-번 모델의 무기한 거래소 |
| Chainlink | Chainlink | 오라클 유틸리티 토큰(LINK) 운영 프로토콜 |
| Lido | Lido | "최소 거버넌스" 방향을 추구하는 스테이킹 프로토콜 |

---

**용어 사용 지침:**

1. **첫 등장 시 병기 형식 사용**: 한국어 (English) 또는 한국어 (English, 약어)
   - 예: 탈중앙화 자율 조직 (Decentralized Autonomous Organization, DAO)

2. **이후 등장 시**: 영어 약어 또는 고유명사 그대로 사용
   - 예: DAO, veTokenomics, Snapshot

3. **고유명사**: 번역 없이 영어 그대로 사용
   - 예: Uniswap, Curve, Tally

4. **업계 통용어**: 한글 음역 사용
   - 예: 타임락 (Timelock), 스냅샷 (Snapshot), 게이지 (Gauge)
