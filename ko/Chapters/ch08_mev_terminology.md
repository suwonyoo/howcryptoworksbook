# Chapter 8: MEV - 신규 용어 목록

이 문서는 Chapter 8에서 새롭게 등장한 기술 용어들을 정리합니다. 용어집(glossary.md)에 이미 정의된 용어는 제외되었습니다.

---

## MEV 핵심 개념 (MEV Core Concepts)

| English | Korean | 번역 근거 |
|---------|--------|-----------|
| Maximal Extractable Value (MEV) | 최대 추출 가능 가치 (MEV) | 트랜잭션 순서화로 추출되는 가치. glossary에 등재 |
| Miner Extractable Value | 채굴자 추출 가능 가치 | MEV의 PoW 시대 원래 명칭 |
| Dark Forest | 다크 포레스트 | 류츠신 SF 소설에서 차용한 멤풀 환경 비유 |
| Mempool | 멤풀 | 미확인 거래 대기열. glossary에 등재 |
| Transaction Ordering | 트랜잭션 순서화 | 블록 내 트랜잭션 배치 순서 결정 |

## MEV 참여자 (MEV Participants)

| English | Korean | 번역 근거 |
|---------|--------|-----------|
| Searcher | 서처 | MEV 기회를 탐색하는 참여자. 업계 통용 음차 |
| Builder | 빌더 | 블록을 구성하고 입찰하는 참여자. 업계 통용 음차 |
| Proposer | 프로포저 | 블록을 제안하는 검증자. 업계 통용 음차 |
| Relay | 릴레이 | 빌더와 프로포저 사이의 신뢰받는 중개자 |
| Validator | 검증자 | PoS에서 블록 제안 및 검증 수행. glossary에 등재 |

## MEV 유형 (MEV Types)

| English | Korean | 번역 근거 |
|---------|--------|-----------|
| Benevolent MEV | 선의적 MEV | 시장에 이로운 기능을 수행하는 MEV |
| Malignant MEV | 악의적 MEV | 순수 가치 이전만 일으키는 해로운 MEV |
| CEX-DEX Arbitrage | CEX-DEX 차익 거래 | 중앙화/탈중앙화 거래소 간 가격 차이 활용 |
| Cross-Domain MEV | 크로스 도메인 MEV | 여러 블록체인에 걸친 MEV 추출 |

## MEV 추출 전략 (MEV Extraction Strategies)

| English | Korean | 번역 근거 |
|---------|--------|-----------|
| Front-running | 프런트러닝 | 타인의 거래 앞에 자신의 거래 삽입. 업계 통용어 |
| Back-running | 백러닝 | 타인의 거래 바로 뒤에 자신의 거래 배치 |
| Sandwich Attack | 샌드위치 공격 | 피해자 거래 전후에 거래를 배치하여 가치 추출 |
| Just-In-Time Liquidity (JIT) | 적시 유동성 (JIT) | 특정 블록에서만 유동성을 제공하고 제거하는 전략 |
| Liquidation | 청산 | 담보 부족 포지션 강제 청산. Ch06/Ch07에서 상세 설명 |
| Priority Gas Auction (PGA) | 우선순위 가스 경매 | 트랜잭션 우선순위를 위한 가스비 입찰 경쟁 |
| Time-Bandit Attack | 타임밴딧 공격 | 최근 블록을 재구성하여 MEV 캡처 시도 |

## 사용자 보호 (User Protection)

| English | Korean | 번역 근거 |
|---------|--------|-----------|
| Slippage Tolerance | 슬리피지 허용치 | 수용 가능한 가격 변동 범위 설정 |
| Private Transaction Routing | 프라이빗 트랜잭션 라우팅 | 공개 멤풀을 우회하는 트랜잭션 전송 |
| Batch Auction | 배치 옥션 | 여러 주문을 동시에 정산하는 경매 방식. Ch07에서 소개 |
| Encrypted Mempool | 암호화된 멤풀 | 순서화 전까지 트랜잭션 내용을 암호화 |
| Order Flow Auction | 주문 흐름 경매 | 사용자 트랜잭션 흐름을 최고 입찰자에게 경매 |
| MEV Rebate | MEV 리베이트 | 피한 MEV의 일부를 사용자에게 반환 |

## Flashbots 생태계 (Flashbots Ecosystem)

| English | Korean | 번역 근거 |
|---------|--------|-----------|
| Flashbots | Flashbots | MEV 인프라 연구 조직. 고유명사 |
| MEV-Geth | MEV-Geth | PoW 시대 Flashbots의 수정된 이더리움 클라이언트 |
| MEV-Boost | MEV-Boost | PoS 이더리움용 PBS 미들웨어. 고유명사 |
| Flashbots Protect | Flashbots Protect | 사용자 대상 프라이빗 트랜잭션 서비스 |
| Bundle | 번들 | 원자적으로 실행되는 트랜잭션 묶음 |

## PBS (Proposer-Builder Separation)

| English | Korean | 번역 근거 |
|---------|--------|-----------|
| Proposer-Builder Separation (PBS) | 제안자-빌더 분리 (PBS) | 빌더와 프로포저 역할을 분리하는 설계 |
| Enshrined PBS | 내장 PBS | 프로토콜 레벨에 내장된 PBS |
| Block Header | 블록 헤더 | 블록 내용 없이 메타데이터만 포함하는 헤더 |
| Block Bid | 블록 입찰 | 빌더가 프로포저에게 제시하는 블록 가치 |

## 중앙화 및 탈중앙화 (Centralization and Decentralization)

| English | Korean | 번역 근거 |
|---------|--------|-----------|
| Builder Concentration | 빌더 집중 | 소수 빌더에게 블록 생산이 집중되는 현상 |
| Relay Dominance | 릴레이 지배 | 소수 릴레이가 시장을 지배하는 현상 |
| OFAC Compliance | OFAC 컴플라이언스 | 미국 해외자산통제국 제재 준수 |
| Censorship Resistance | 검열 저항 | 트랜잭션 검열에 저항하는 능력. glossary에 등재 |
| BuilderNet | BuilderNet | 탈중앙화 블록 빌딩 네트워크. 고유명사 |
| Secure Enclave | 보안 엔클레이브 | 격리된 하드웨어 실행 환경. glossary에 등재 |

## 기타 관련 용어 (Other Related Terms)

| English | Korean | 번역 근거 |
|---------|--------|-----------|
| Oracle Update | 오라클 업데이트 | 가격 피드의 온체인 가격 갱신 |
| Deterministic Pricing Curve | 결정론적 가격 곡선 | AMM의 예측 가능한 가격 책정 공식 |
| Atomic Execution | 원자적 실행 | 완전 성공 또는 완전 실패만 가능한 실행 |
| Price Impact | 가격 영향 | 거래가 풀 가격에 미치는 영향. Ch07에서 상세 설명 |
| Unbundling | 언번들링 | 프라이빗 번들을 분해하는 익스플로잇 |
| Wire Fraud | 와이어 사기 | 전신 통신을 이용한 사기 (미국 법률 용어) |
| Money Laundering | 자금 세탁 | 불법 자금의 출처 은폐 |

---

## 프로젝트명 및 고유명사 (Projects and Proper Nouns)

| English | Korean | 번역 근거 |
|---------|--------|-----------|
| Flashbots | Flashbots | MEV 인프라 연구 조직 |
| Beaverbuild | Beaverbuild | 빌더 운영자 |
| Nethermind | Nethermind | 이더리움 클라이언트 개발팀 |
| Shutter Network | Shutter Network | 암호화된 멤풀 프로젝트 |
| CoW Swap | CoW Swap | 배치 옥션 기반 DEX. Ch07에서 소개 |
| UniswapX | UniswapX | 더치 옥션 기반 인텐트 DEX. Ch07에서 소개 |
| Uniswap v4 | Uniswap v4 | Uniswap의 최신 버전 |
| Chainlink | Chainlink | 오라클 네트워크. Ch07에서 상세 설명 |
| Aave | Aave | 대출 프로토콜. Ch07에서 상세 설명 |

---

## 번역 원칙 요약

1. **프로젝트명 보존**: Flashbots, MEV-Boost, BuilderNet 등 프로젝트명은 고유명사로 유지

2. **업계 통용 음차어**: 한국 암호화폐 커뮤니티에서 정착된 음차 사용
   - 예: 서처, 빌더, 프로포저, 릴레이, 프런트러닝, 백러닝

3. **기술적 약어 병기**: 첫 등장 시 한국어(English, ABBR) 형식으로 병기
   - 예: "최대 추출 가능 가치(Maximal Extractable Value, MEV)"
   - 예: "제안자-빌더 분리(Proposer-Builder Separation, PBS)"

4. **금융/법률 용어 표준 번역**: 금융업계에서 이미 사용되는 번역 채택
   - 예: 차익 거래, 청산, 자금 세탁

5. **이전 챕터와 일관성**: Ch01의 Mempool, Ch07의 슬리피지/AMM/오라클 등 일관되게 사용

6. **문학적 비유 보존**: "다크 포레스트"는 SF 소설 참조로 음차 유지

---

## 용어집 업데이트 권장 사항

다음 용어들을 `/Users/yoo/howcryptoworksbook/ko/glossary.md`에 추가할 것을 권장합니다:

### B 섹션
| 영어 | 한국어 | 첫 등장 챕터 | 비고 |
|------|--------|-------------|------|
| Builder | 빌더 | ch08 | 블록 구성 및 입찰 참여자 |
| Back-running | 백러닝 | ch08 | 타 거래 직후 자신의 거래 배치 |

### F 섹션
| 영어 | 한국어 | 첫 등장 챕터 | 비고 |
|------|--------|-------------|------|
| Front-running | 프런트러닝 | ch08 | 타 거래 앞에 자신의 거래 삽입 |
| Flashbots | Flashbots | ch08 | MEV 인프라 연구 조직 |

### J 섹션
| 영어 | 한국어 | 첫 등장 챕터 | 비고 |
|------|--------|-------------|------|
| JIT Liquidity | 적시 유동성 | ch08 | Just-In-Time Liquidity |

### P 섹션
| 영어 | 한국어 | 첫 등장 챕터 | 비고 |
|------|--------|-------------|------|
| PBS | 제안자-빌더 분리 | ch08 | Proposer-Builder Separation |
| Proposer | 프로포저 | ch08 | 블록을 제안하는 검증자 |

### R 섹션
| 영어 | 한국어 | 첫 등장 챕터 | 비고 |
|------|--------|-------------|------|
| Relay | 릴레이 | ch08 | 빌더-프로포저 간 중개자 |

### S 섹션
| 영어 | 한국어 | 첫 등장 챕터 | 비고 |
|------|--------|-------------|------|
| Searcher | 서처 | ch08 | MEV 기회 탐색 참여자 |
| Sandwich Attack | 샌드위치 공격 | ch08 | 피해자 거래 전후 가치 추출 |
