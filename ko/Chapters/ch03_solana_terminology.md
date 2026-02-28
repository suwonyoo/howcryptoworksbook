# Chapter 3: Solana - 신규 용어 목록

이 문서는 Chapter 3에서 새롭게 등장한 기술 용어들을 정리합니다. 용어집(glossary.md)에 이미 정의된 용어는 제외되었습니다.

---

## 솔라나 핵심 아키텍처

| English | Korean | 번역 근거 |
|---------|--------|-----------|
| Solana | 솔라나 | 고유명사 음차. 한국 커뮤니티에서 통용 |
| SOL | SOL | 네이티브 토큰 티커. 영어 그대로 사용 |
| Parallel Execution | 병렬 실행 | 여러 거래를 동시에 처리하는 실행 모델 |
| Account Model | 계정 모델 | 솔라나의 상태 관리 방식. 직역이 명확 |
| Program | 프로그램 | 솔라나의 스마트 컨트랙트. 솔라나에서는 "Program"으로 지칭 |
| Cross-Program Invocations (CPIs) | 교차 프로그램 호출 (CPIs) | 프로그램 간 상호 호출 |
| Program Derived Addresses (PDAs) | 프로그램 파생 주소 (PDAs) | Private Key 없는 프로그램 제어 주소 |
| Lamports | 램포트 | SOL의 최소 단위 (1 SOL = 10억 램포트). 창시자 이름에서 유래 |
| Rent-exempt | 임대 면제 | 계정 유지를 위한 최소 잔액 조건 |

## 거래 및 수수료

| English | Korean | 번역 근거 |
|---------|--------|-----------|
| Ed25519 | Ed25519 | 암호학 알고리즘. 영어 그대로 사용 |
| Priority Fees | 우선 수수료 | 더 빠른 처리를 위한 추가 수수료 |
| Compute Unit | 연산 단위 | 거래 처리에 필요한 연산 리소스 |
| Local Fee Markets | 로컬 수수료 시장 | 계정별 수수료 책정 메커니즘 |
| Preflight Simulation | 사전 비행 시뮬레이션 | 거래 제출 전 결과 미리보기 |
| Dropped Transaction | 누락된 거래 | 블록에 포함되지 못한 거래 |
| Failed Transaction | 실패한 거래 | 블록에 포함되었으나 되돌려진 거래 |
| Atomic Composability | 원자적 조합성 | 여러 작업이 전부 성공하거나 전부 실패하는 특성 |

## 합의 및 네트워킹

| English | Korean | 번역 근거 |
|---------|--------|-----------|
| Proof of History (PoH) | 역사 증명 (Proof of History, PoH) | 솔라나의 암호학적 시간 기록 메커니즘 |
| Tower BFT | Tower BFT | 솔라나의 합의 프로토콜. 고유명사 |
| Slot | 슬롯 | 약 400ms의 블록 생성 단위 |
| Epoch | 에포크 | 약 2일 단위의 검증자 스케줄 기간 |
| Gulf Stream | Gulf Stream | 솔라나의 거래 전달 프로토콜. 고유명사 |
| Turbine | Turbine | 솔라나의 블록 전파 프로토콜. 고유명사 |
| Shreds | 슈레드 | Turbine에서 사용하는 블록 조각 |
| QUIC | QUIC | 현대적 네트워크 전송 프로토콜. 약어 그대로 사용 |
| Quality of Service (QoS) | 서비스 품질 (QoS) | 네트워크 품질 보장 메커니즘 |
| DoubleZero | DoubleZero | 전용 광섬유 네트워크 인프라. 고유명사 |

## Alpenglow 업그레이드

| English | Korean | 번역 근거 |
|---------|--------|-----------|
| Alpenglow | Alpenglow | 솔라나의 합의 업그레이드. 고유명사 |
| Votor | Votor | Alpenglow의 새로운 투표 메커니즘. 고유명사 |
| Rotor | Rotor | Alpenglow의 블록 전파 개선. 고유명사 |
| 20+20 Resilience Model | 20+20 회복 모델 | 안전성 20% + 활성 20% 허용 모델 |

## MEV 및 블록 빌딩

| English | Korean | 번역 근거 |
|---------|--------|-----------|
| Jito-Solana | Jito-Solana | MEV 번들 경매 클라이언트. 고유명사 |
| Bundle | 번들 | 패키징된 거래 세트 |
| Searchers | 검색자 | MEV 추출을 위해 거래를 찾는 주체 |
| BAM (Block Assembly Marketplace) | BAM (Block Assembly Marketplace) | Jito의 블록 조립 마켓플레이스. 고유명사 |
| Trusted Execution Environments (TEEs) | 신뢰 실행 환경 (TEEs) | 안전한 코드 실행을 위한 격리 환경 |
| Harmonic | Harmonic | 블록 빌더 집계 계층. 고유명사 |
| Raiku | Raiku | 결정론적 실행 보장 인프라. 고유명사 |
| CLOB (Central Limit Order Book) | CLOB (중앙 지정가 주문서) | 전통적인 거래소 오더북 방식 |
| Ahead-of-Time (AOT) | 사전 예약 (AOT) | Raiku의 사전 커밋 거래 유형 |
| Just-in-Time (JIT) | 즉시 실행 (JIT) | Raiku의 실시간 실행 거래 유형 |

## 경제학 및 스테이킹

| English | Korean | 번역 근거 |
|---------|--------|-----------|
| Disinflationary | 디스인플레이션 | 인플레이션율이 감소하는 특성 |
| Terminal Inflation Rate | 최종 인플레이션율 | 영구적으로 안정화되는 인플레이션율 |
| Delegation | 위임 | 스테이킹 권한 위임 |
| Commission Rate | 수수료율 | 검증자가 부과하는 보상 수수료 비율 |
| Stake Activation/Deactivation | 지분 활성화/비활성화 | 스테이킹 상태 변경 |
| Vote Transaction | 투표 거래 | 검증자의 합의 투표에 사용되는 거래 |
| Solana Foundation Delegation Program (SFDP) | 솔라나 파운데이션 위임 프로그램 (SFDP) | 검증자 부트스트랩 프로그램 |
| Superminority Threshold | 슈퍼마이너리티 임계값 | 네트워크 중단에 필요한 지분 비율 (~1/3) |
| Slashing | 슬래싱 | 부정행위에 대한 지분 몰수 페널티 |

## 거버넌스

| English | Korean | 번역 근거 |
|---------|--------|-----------|
| SIMD (Solana Improvement Document) | SIMD (솔라나 개선 문서) | 솔라나 프로토콜 변경 제안 표준 |
| Feature Gates | 기능 게이트 | 기본 비활성화된 프로토콜 변경 기능 |
| Agave | Agave | 솔라나의 주요 검증자 클라이언트. 고유명사 |
| Anza | Anza | Agave 클라이언트 유지 관리 팀. 고유명사 |

## 개발자 스택

| English | Korean | 번역 근거 |
|---------|--------|-----------|
| SVM (Solana Virtual Machine) | SVM (솔라나 가상 머신) | 솔라나의 실행 환경 |
| Sealevel | Sealevel | SVM의 병렬 스케줄러. 고유명사 |
| Register-based VM | 레지스터 기반 가상 머신 | 스택 대신 레지스터 사용하는 VM |
| Sysvars | 시스바 | 시스템 상태 접근을 위한 읽기 전용 계정 |
| Anchor | Anchor | 솔라나 개발 프레임워크. 고유명사 |
| IDL (Interface Definition Language) | IDL (인터페이스 정의 언어) | 프로그램 인터페이스의 기계 판독 가능 설명 |
| SPL Tokens | SPL 토큰 | 솔라나 프로그램 라이브러리 토큰 표준 |
| Mint Account | 민트 계정 | 토큰 속성을 정의하는 계정 |
| Associated Token Accounts | 연관 토큰 계정 | 자동 유도되는 표준 토큰 계정 |
| Token-2022 | Token-2022 | 확장 기능을 가진 새로운 토큰 표준 |
| Transfer Hooks | 전송 후크 | Token-2022의 전송 시 커스텀 로직 실행 기능 |
| Confidential Transfers | 기밀 전송 | Token-2022의 프라이버시 전송 기능 |
| Upgradeable Loader | 업그레이드 가능 로더 | 프로그램 업그레이드를 가능하게 하는 로더 |
| Upgrade Authority | 업그레이드 권한 | 프로그램 업그레이드 권한을 가진 주체 |

## 상태 압축 및 NFT

| English | Korean | 번역 근거 |
|---------|--------|-----------|
| State Compression | 상태 압축 | 머클 트리 기반 데이터 압축 기술 |
| Concurrent Merkle Tree | 동시 머클 트리 | 동시 업데이트를 지원하는 머클 트리 |
| Compressed NFTs | 압축된 NFT | 상태 압축을 사용하는 NFT |
| Metaplex | Metaplex | 솔라나 NFT 표준 및 도구. 고유명사 |

## 인프라 및 클라이언트

| English | Korean | 번역 근거 |
|---------|--------|-----------|
| RPC Node | RPC 노드 | 쿼리에 응답하는 서버 |
| Archive Node | 아카이브 노드 | 전체 역사 데이터를 저장하는 노드 |
| Pruning | 정리 | 오래된 데이터 삭제 |
| Ledger Retention | 원장 보존 | 저장되는 원장 데이터 양 |
| Snapshot | 스냅샷 | 특정 시점의 상태 저장본 |
| Firedancer | Firedancer | Jump Crypto의 솔라나 검증자 재구현. 고유명사 |
| Frankendancer | Frankendancer | Firedancer의 하이브리드 구현. 고유명사 |
| Client Diversity | 클라이언트 다양성 | 여러 독립적 클라이언트 구현의 존재 |

## 사용 사례

| English | Korean | 번역 근거 |
|---------|--------|-----------|
| Memecoin | 밈코인 | 밈 기반 암호화폐. 음차 |
| DEX Aggregator | DEX 애그리게이터 | 여러 DEX의 유동성을 집계하는 서비스 |
| Jupiter | Jupiter | 솔라나의 대표 DEX 애그리게이터. 고유명사 |
| Pump.fun | Pump.fun | 토큰 출시 플랫폼. 고유명사 |
| Phantom | Phantom | 솔라나 지갑. 고유명사 |
| Moonshot | Moonshot | 솔라나 모바일 앱. 고유명사 |
| AMM (Automated Market Maker) | AMM (자동화된 시장 메이커) | 유동성 풀 기반 거래 메커니즘 |
| Proactive AMM / Prop AMM | 프로액티브 AMM | 능동적으로 가격을 조정하는 AMM |
| Hyperliquid | Hyperliquid | 영구 선물 거래 플랫폼. 고유명사 |
| xStocks | xStocks | 토큰화된 주식 제품. 고유명사 |

---

## 번역 원칙 요약

1. **고유명사 보존**: 프로토콜 이름, 제품명, 회사명 등은 영어 그대로 사용 (예: Alpenglow, Firedancer, Jupiter)

2. **약어 병기**: 기술적 약어는 영어와 풀네임을 병기 (예: PoH → 역사 증명 (Proof of History, PoH))

3. **솔라나 특화 용어**: 솔라나 생태계에서 독자적으로 사용되는 용어는 최대한 정확하게 번역 (예: Lamports → 램포트)

4. **기존 표준 준수**: 이전 챕터에서 사용된 번역과 일관성 유지 (예: MEV, DeFi, 검증자 등)

5. **기술적 정확성**: 기술적 의미가 정확히 전달되도록 번역 (예: Parallel Execution → 병렬 실행)

6. **첫 등장 시 병기**: 기술 용어의 첫 등장 시 한국어(English) 형식으로 병기하고, 이후에는 영어만 사용

---

## Glossary 업데이트 필요 항목

다음 용어들은 용어집(glossary.md)에 추가가 필요합니다:

| 영어 | 한국어 | 첫 등장 챕터 | 비고 |
|------|--------|-------------|------|
| Solana | 솔라나 | ch03 | Layer 1 블록체인 |
| SOL | SOL | ch03 | 솔라나 네이티브 토큰 |
| Proof of History (PoH) | 역사 증명 | ch03 | 솔라나의 시간 기록 메커니즘 |
| Program Derived Addresses (PDAs) | 프로그램 파생 주소 | ch03 | Private Key 없는 주소 |
| SPL Tokens | SPL 토큰 | ch03 | 솔라나 토큰 표준 |
| Parallel Execution | 병렬 실행 | ch03 | 동시 거래 처리 |
| Atomic Composability | 원자적 조합성 | ch03 | 전부 성공 또는 전부 실패 |
| State Compression | 상태 압축 | ch03 | 머클 트리 기반 압축 |
| Firedancer | Firedancer | ch03 | 솔라나 검증자 재구현 |
| Slashing | 슬래싱 | ch03 | 부정행위 페널티 |
