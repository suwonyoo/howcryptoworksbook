# Chapter 7: DeFi - 신규 용어 목록

이 문서는 Chapter 7에서 새롭게 등장한 기술 용어들을 정리합니다. 용어집(glossary.md)에 이미 정의된 용어는 제외되었습니다.

---

## DeFi 핵심 개념 (DeFi Core Concepts)

| English | Korean | 번역 근거 |
|---------|--------|-----------|
| Decentralized Finance (DeFi) | 탈중앙화 금융 (DeFi) | 은행/중개자 없이 운영되는 금융 시스템. glossary에 등재 |
| Atomic Composability | 원자적 조합 가능성 | 트랜잭션 내에서 완전한 성공 또는 완전한 실패만 가능한 조합 가능성 |
| MEV (Maximal Extractable Value) | 최대 추출 가능 가치 (MEV) | 트랜잭션 순서에서 추출되는 가치. Ch08에서 상세 설명 |
| Impermanent Loss | 비영구적 손실 | LP가 자산 가격 비율 변화로 겪는 기회비용. 업계 표준 번역 |
| Slippage | 슬리피지 | 거래 규모에 따른 가격 영향. 업계 통용어 |
| TVL (Total Value Locked) | 총 예치금 (TVL) | 프로토콜에 예치된 자산의 총 가치 |
| Permissionless Access | 무허가 접근 | 누구나 참여 가능한 시스템 특성 |
| Over-collateralization | 초과 담보 | 대출액보다 많은 담보를 요구하는 방식 |

## AMM 및 DEX (AMM and DEX)

| English | Korean | 번역 근거 |
|---------|--------|-----------|
| Automated Market Maker (AMM) | 자동화된 시장 조성자 (AMM) | 풀 잔액에서 가격을 산출하는 시스템. 업계 표준 |
| Liquidity Pool | 유동성 풀 | 토큰 쌍이 예치된 스마트 컨트랙트 |
| Liquidity Provider (LP) | 유동성 공급자 (LP) | 유동성 풀에 자산을 예치하는 참여자 |
| Constant Product Formula | 상수곱 공식 | x × y = k 공식. Uniswap의 핵심 수학 |
| Price Impact | 가격 영향 | 거래가 풀 가격에 미치는 영향 |
| Pool Depth | 풀 깊이 | 유동성 풀의 총 자산 규모 |
| Concentrated Liquidity | 집중 유동성 | Uniswap v3에서 LP가 특정 가격 범위에 유동성 집중 |
| Tick | 틱 | Uniswap v3에서 집중 유동성의 가격 범위 단위 |
| Range Order | 범위 주문 | 가격 범위 내에서 실행되는 LP 포지션 기반 주문 |
| TWAP (Time-Weighted Average Price) | 시간 가중 평균 가격 (TWAP) | 시간에 따른 평균 가격 계산 방식 |
| Flash Swap | 플래시 스왑 | 담보 없이 자산을 빌려 사용 후 같은 트랜잭션 내 반환 |

## Uniswap 관련 (Uniswap Related)

| English | Korean | 번역 근거 |
|---------|--------|-----------|
| Uniswap | Uniswap | 대표적 AMM DEX. 고유명사 |
| Router | 라우터 | 최적 경로를 통해 스왑을 실행하는 컨트랙트 |
| Multi-hop Routing | 다중 홉 라우팅 | 여러 풀을 경유하는 스왑 경로 |
| Singleton Contract | 싱글톤 컨트랙트 | v4에서 모든 풀을 담는 단일 컨트랙트 |
| Hooks | 훅 | v4에서 프로그래밍 가능한 AMM 동작 확장 기능 |

## Curve Finance 관련 (Curve Finance Related)

| English | Korean | 번역 근거 |
|---------|--------|-----------|
| Curve Finance | Curve Finance | 스테이블코인 전문 DEX. 고유명사 |
| StableSwap | StableSwap | Curve의 하이브리드 가격 곡선. 고유명사 |
| Amplification Factor (A) | 증폭 계수 (A) | StableSwap에서 페그 근처의 곡선 평탄도 제어 |
| 3pool | 3pool | USDC/USDT/DAI 유동성 풀. 고유명사 |
| Meta-pool | 메타풀 | 3pool LP 토큰과 쌍을 이루는 풀 |

## 본딩 커브 및 런치패드 (Bonding Curves and Launchpads)

| English | Korean | 번역 근거 |
|---------|--------|-----------|
| Bonding Curve | 본딩 커브 | 토큰 가격을 공급량에 연동시키는 수학적 곡선 |
| Launchpad | 런치패드 | 토큰 초기 발행 플랫폼 |
| Pump.fun | Pump.fun | Solana 기반 본딩 커브 런치패드. 고유명사 |
| Graduation | 졸업 | 본딩 커브에서 AMM으로의 전환 |
| LP Token Burning | LP 토큰 소각 | 유동성 인출 방지를 위한 LP 토큰 영구 제거 |
| Rug Pull | 러그 풀 | 개발자가 유동성을 인출하여 투자자를 손해보게 하는 행위 |
| Soft Rug | 소프트 러그 | 보유 토큰 공격적 매도 또는 프로젝트 방치 |

## 인텐트 기반 시스템 (Intent-Based Systems)

| English | Korean | 번역 근거 |
|---------|--------|-----------|
| Intent | 인텐트 | 사용자가 서명하는 원하는 결과 명세 |
| Solver | 솔버 | 인텐트를 이행하기 위해 경쟁하는 오프체인 주체 |
| Filler | 필러 | UniswapX에서 인텐트를 이행하는 주체 |
| CoW Swap | CoW Swap | 배치 옥션 기반 인텐트 DEX. 고유명사 |
| UniswapX | UniswapX | 더치 옥션 기반 인텐트 DEX. 고유명사 |
| Coincidence of Wants (CoW) | 우연의 일치 (CoW) | 주문이 직접 매칭되는 상황 |
| Batch Auction | 배치 옥션 | 여러 주문을 동시에 정산하는 경매 방식 |
| Dutch Auction | 더치 옥션 | 가격이 점진적으로 개선되는 경매 방식 |

## RFQ 시스템 (RFQ Systems)

| English | Korean | 번역 근거 |
|---------|--------|-----------|
| Request-for-Quote (RFQ) | 호가 요청 (RFQ) | 시장 조성자에게 확정 가격을 요청하는 시스템 |
| Hashflow | Hashflow | RFQ 기반 DEX. 고유명사 |
| 0x RFQ | 0x RFQ | 0x 프로토콜의 RFQ 시스템. 고유명사 |

## 탈중앙화 무기한 거래소 (Decentralized Perpetual Exchanges)

| English | Korean | 번역 근거 |
|---------|--------|-----------|
| Decentralized Perpetual Exchange | 탈중앙화 무기한 거래소 | 온체인 레버리지 거래 플랫폼 |
| GMX | GMX | LP 풀 기반 무기한 거래소. 고유명사 |
| dYdX | dYdX | StarkEx에서 시작, 앱체인으로 이전. 고유명사 |
| Hyperliquid | Hyperliquid | 거래 최적화 앱체인. 고유명사, Ch10에서 상세 |
| Application-Specific Chain | 앱 전용 체인 | 특정 용도에 최적화된 블록체인 |

## 대출 프로토콜 (Lending Protocols)

| English | Korean | 번역 근거 |
|---------|--------|-----------|
| Health Factor (HF) | 건강 계수 (HF) | 포지션의 청산 근접도를 측정하는 지표 |
| Loan-to-Value (LTV) | 담보 대출 비율 (LTV) | 담보 대비 최대 대출 가능 비율 |
| Liquidation Threshold | 청산 임계값 | 포지션이 청산 가능해지는 지점 |
| Liquidation Bonus | 청산 보너스 | 청산인에게 제공되는 담보 할인 |
| aToken | aToken | Aave의 이자 수익 토큰. 고유명사 |
| Debt Tokenization | 부채 토큰화 | 부채를 토큰으로 표현하는 방식 |
| Credit Delegation | 신용 위임 | 타인의 담보로 대출하는 기능 |
| Collateral Swap | 담보 교환 | 담보 자산을 변경하는 기능 |
| Isolation Mode | 격리 모드 | 롱테일 자산의 위험을 격리하는 기능 |
| Efficiency Mode (E-Mode) | 효율 모드 (E-Mode) | 상관 자산 쌍에 대한 향상된 조건 |
| Unified Liquidity Layer | 통합 유동성 레이어 | Aave v4의 중앙집중식 유동성 관리 아키텍처 |
| Looping | 루핑 | 예치-대출-재예치를 반복하는 레버리지 전략 |

## 대출 프로토콜 - 프로젝트명 (Lending Protocols - Projects)

| English | Korean | 번역 근거 |
|---------|--------|-----------|
| Aave | Aave | 대표적 대출 프로토콜. 고유명사 |
| Compound | Compound | 대출 프로토콜. 고유명사 |
| Euler | Euler | 모듈형 대출 프로토콜. 고유명사 |
| Morpho | Morpho | P2P 최적화 및 최소 신뢰 대출. 고유명사 |
| Morpho Blue | Morpho Blue | Morpho의 최소 신뢰 대출 프리미티브. 고유명사 |
| MetaMorpho | MetaMorpho | Morpho Blue 위의 볼트 프로토콜. 고유명사 |
| Euler Vault Kit (EVK) | Euler Vault Kit (EVK) | Euler v2의 크레딧 볼트 프레임워크. 고유명사 |
| Euler Vault Connector (EVC) | Euler Vault Connector (EVC) | 볼트 연결 도구. 고유명사 |
| GHO | GHO | Aave의 초과담보 스테이블코인. 고유명사 |

## 위험 관리 및 큐레이터 (Risk Management and Curators)

| English | Korean | 번역 근거 |
|---------|--------|-----------|
| Risk Curator | 위험 큐레이터 | 볼트 설계 및 위험 관리를 담당하는 주체 |
| Vault | 볼트 | 특정 전략에 따라 자산을 관리하는 컨트랙트 |
| Risk Service Provider | 위험 서비스 제공자 | Aave DAO에 조언하는 위험 분석 회사 |
| Gauntlet | Gauntlet | 위험 관리 회사. 고유명사 |
| Chaos Labs | Chaos Labs | 위험 관리 회사. 고유명사 |

## Sky (구 MakerDAO) 관련

| English | Korean | 번역 근거 |
|---------|--------|-----------|
| Sky | Sky | MakerDAO의 리브랜딩명. 고유명사 |
| MakerDAO | MakerDAO | 탈중앙화 스테이블코인 프로토콜. 고유명사 |
| USDS | USDS | Sky의 스테이블코인. 고유명사 |
| DAI | DAI | MakerDAO의 원래 스테이블코인. 고유명사 |
| sUSDS | sUSDS | 스테이킹된 USDS. 고유명사 |
| Sky Savings Rate (SSR) | Sky Savings Rate (SSR) | USDS 저축 이율. 고유명사 |
| LitePSM | LitePSM | USDS/DAI와 타 스테이블코인 간 고정 환율 스왑 모듈 |
| Stars | Stars | Sky의 프로토콜 할당자 |

## Wildcat 관련

| English | Korean | 번역 근거 |
|---------|--------|-----------|
| Wildcat | Wildcat | 저담보 기관 대출 프로토콜. 고유명사 |
| Under-collateralized Lending | 저담보 대출 | 담보가 대출액보다 적은 대출 |
| Reserve Ratio | 준비금 비율 | 유동성 버퍼 비율 |
| Delinquent | 연체 | 준비금이 요구 수준 이하로 하락한 상태 |
| Default | 채무 불이행 | 차입자가 상환하지 못하는 상황 |
| Counterparty Credit Risk | 거래 상대방 신용 위험 | 상대방이 의무를 이행하지 못할 위험 |

## 수익 전략 (Yield Strategies)

| English | Korean | 번역 근거 |
|---------|--------|-----------|
| Delta-Neutral | 델타 중립 | 가격 변동에 중립적인 포지션 |
| Hedging | 헤징 | 가격 위험을 상쇄하는 전략 |
| Funding Rate | 펀딩 비율 | 무기한 선물에서 롱/숏 간 주기적 지급 |
| Carry Trade | 캐리 트레이드 | 금리 차이를 활용한 차익 거래 |
| Basis | 베이시스 | 현물과 선물 가격 간의 차이 |

## Ethena 관련

| English | Korean | 번역 근거 |
|---------|--------|-----------|
| Ethena | Ethena | 델타 중립 합성 달러 프로토콜. 고유명사 |
| USDe | USDe | Ethena의 합성 달러. 고유명사 |
| sUSDe | sUSDe | 스테이킹된 USDe. 고유명사 |
| Off-Exchange Settlement (OES) | 장외 정산 (OES) | 담보 자산 보관 제공자 |
| Custody Risk | 커스터디 위험 | 자산 보관 관련 위험 |
| Peg Stability | 페그 안정성 | 고정 가격 유지 능력 |

## Pendle 관련

| English | Korean | 번역 근거 |
|---------|--------|-----------|
| Pendle | Pendle | 수익 토큰화 프로토콜. 고유명사 |
| Principal Token (PT) | 원금 토큰 (PT) | 만기 시 기초 자산 청구권 |
| Yield Token (YT) | 수익 토큰 (YT) | 만기까지의 수익 청구권 |
| Zero-Coupon Bond | 무이표 채권 | 할인 발행 후 만기에 액면가 지급 |
| Fixed Yield | 고정 수익률 | 확정된 수익률 |
| Maturity | 만기 | 토큰이 기초 자산으로 전환되는 시점 |
| PT Looping | PT 루핑 | PT를 담보로 대출 후 더 많은 PT 구매 반복 |
| Implied Yield | 내재 수익률 | PT 가격에서 도출되는 수익률 |
| LTV Killswitch | LTV 킬스위치 | 급격한 가격 변동 시 보호 장치 |

## 포인트 파밍 (Points Farming)

| English | Korean | 번역 근거 |
|---------|--------|-----------|
| Points Farming | 포인트 파밍 | 미래 에어드롭을 위한 프로토콜 참여 |
| Airdrop | 에어드롭 | 토큰 무상 배포 |
| Sybil Detection | 시빌 탐지 | 다중 계정 필터링 |
| Program Risk | 프로그램 위험 | 포인트 조건 변경 또는 취소 위험 |

## 옵션 볼트 (Options Vaults)

| English | Korean | 번역 근거 |
|---------|--------|-----------|
| Options Vault | 옵션 볼트 | 체계적 옵션 전략을 실행하는 볼트 |
| Covered Call | 커버드 콜 | 기초 자산 보유 상태에서 콜옵션 매도 |
| Cash-Secured Put | 현금 담보 풋 | 현금 보유 상태에서 풋옵션 매도 |
| Strike Price | 행사가 | 옵션 행사 가격 |
| Option Premium | 옵션 프리미엄 | 옵션 매도로 받는 수익 |
| Assignment | 배정 | 옵션 행사 시 기초 자산 인수/인도 |
| Volatility Crush | 변동성 붕괴 | 내재 변동성 급락 |
| Upside Capping | 상승 제한 | 커버드 콜에서 이익 상한 발생 |

## 인프라 의존성 (Infrastructure Dependencies)

| English | Korean | 번역 근거 |
|---------|--------|-----------|
| Oracle | 오라클 | 외부 데이터를 온체인에 제공하는 시스템 |
| Oracle Problem | 오라클 문제 | 오프체인 데이터를 신뢰할 수 있게 온체인화하는 과제 |
| Price Feed | 가격 피드 | 자산 가격 정보 제공 |
| Off-Chain Reporting | 오프체인 보고 | Chainlink의 오프체인 데이터 집계 시스템 |
| Deviation Threshold | 편차 임계값 | 가격 업데이트를 트리거하는 변동 비율 |
| Heartbeat | 하트비트 | 정기 업데이트 간격 |
| Pull Model | 풀 모델 | 애플리케이션이 필요시 가격을 가져오는 방식 |
| Push Model | 푸시 모델 | 지속적으로 가격을 게시하는 방식 |
| Medianization | 중앙값 처리 | 여러 소스의 중앙값 사용 |

## 오라클 네트워크 - 프로젝트명 (Oracle Networks - Projects)

| English | Korean | 번역 근거 |
|---------|--------|-----------|
| Chainlink | Chainlink | 대표적 오라클 네트워크. 고유명사 |
| Pyth Network | Pyth Network | 풀 기반 오라클. 고유명사 |
| RedStone | RedStone | 대안적 오라클 네트워크. 고유명사 |
| Band Protocol | Band Protocol | 대안적 오라클 네트워크. 고유명사 |

## 오라클 구성 유형 (Oracle Configuration Types)

| English | Korean | 번역 근거 |
|---------|--------|-----------|
| Fundamental Oracle | 기본 오라클 | 내부 환율/온체인 회계 기반 가격 산출 |
| Hardcoded Oracle | 하드코딩 오라클 | 고정 가격 관계 설정 (예: 1:1) |
| Market-Reliant Oracle | 시장 의존 오라클 | 실제 거래 가격 기반 |
| Hybrid Risk Oracle | 하이브리드 위험 오라클 | 여러 접근법을 결합한 오라클 |
| Exchange Rate | 환율 | 볼트의 기초 자산 대비 비율 |
| Bad Debt | 부실 채권 | 청산 불가능한 미상환 부채 |
| Circuit Breaker | 서킷 브레이커 | 극단적 이벤트 시 운영 중단 메커니즘 |
| Freeze Guardian | 동결 가디언 | 긴급 상황 시 운영을 중지할 수 있는 주체 |

## 오라클 공격 및 방어 (Oracle Attacks and Defenses)

| English | Korean | 번역 근거 |
|---------|--------|-----------|
| Flash Loan Price Manipulation | 플래시론 가격 조작 | 플래시론으로 풀 가격을 조작하는 공격 |
| Stale Price | 부실 가격 | 오래된 업데이트되지 않은 가격 |
| Staleness Check | 부실성 검사 | 가격 데이터의 최신성 확인 |
| Reentrancy Guard | 재진입 가드 | 콜백을 통한 조작 방지 |
| Read-Only Reentrancy | 읽기 전용 재진입 | 읽기 함수를 통한 재진입 공격 |

## 플래시론 (Flash Loans)

| English | Korean | 번역 근거 |
|---------|--------|-----------|
| Flash Loan | 플래시론 | 같은 트랜잭션 내 대출 및 상환. 업계 통용어 |
| Atomic Transaction | 원자적 트랜잭션 | 완전 성공 또는 완전 실패만 가능한 트랜잭션 |
| Flash Minting | 플래시 발행 | 같은 트랜잭션 내 발행 및 소각 |
| Checks-Effects-Interactions Pattern | 검사-효과-상호작용 패턴 | 스마트 컨트랙트 보안 패턴 |
| Arbitrage | 차익 거래 | 가격 차이를 이용한 무위험 이익 |
| Collateral Swap | 담보 교환 | 담보 자산을 원자적으로 변경 |
| Refinancing | 재융자 | 부채를 다른 프로토콜로 이전 |

---

## 번역 원칙 요약

1. **프로젝트명 보존**: Uniswap, Aave, Curve, Pendle, Ethena 등 프로젝트명은 고유명사로 유지

2. **프로토콜 버전 표기**: Uniswap v1/v2/v3/v4, Aave v1/v2/v3/v4 등 버전 표기 유지

3. **기술적 약어 병기**: 첫 등장 시 한국어(English, ABBR) 형식으로 병기
   - 예: "자동화된 시장 조성자(Automated Market Maker, AMM)"

4. **금융 용어 통용 번역**: 금융업계에서 이미 사용되는 번역 채택
   - 예: 담보, 청산, 레버리지, 헤징

5. **업계 통용 음차어**: 한국 암호화폐 커뮤니티에서 정착된 음차 사용
   - 예: 슬리피지, 플래시론, 루핑, 볼트

6. **DeFi 전문 용어**: DeFi 고유 개념은 의미 전달 중심 번역
   - 예: Impermanent Loss → 비영구적 손실

7. **이전 챕터와 일관성**: Ch02에서 정의된 용어(검증자, 롤업, EVM 등) 일관되게 사용

---

## 용어집 업데이트 권장 사항

다음 용어들을 `/Users/yoo/howcryptoworksbook/ko/glossary.md`에 추가할 것을 권장합니다:

### A 섹션
| 영어 | 한국어 | 첫 등장 챕터 | 비고 |
|------|--------|-------------|------|
| AMM | 자동화된 시장 조성자 | ch07 | Automated Market Maker |
| Atomic Composability | 원자적 조합 가능성 | ch07 | 완전 성공/실패 트랜잭션 |

### F 섹션
| 영어 | 한국어 | 첫 등장 챕터 | 비고 |
|------|--------|-------------|------|
| Flash Loan | 플래시론 | ch07 | 무담보 단일 트랜잭션 대출 |

### H 섹션
| 영어 | 한국어 | 첫 등장 챕터 | 비고 |
|------|--------|-------------|------|
| Health Factor | 건강 계수 | ch07 | 청산 근접도 지표 |

### I 섹션
| 영어 | 한국어 | 첫 등장 챕터 | 비고 |
|------|--------|-------------|------|
| Impermanent Loss | 비영구적 손실 | ch07 | LP의 기회비용 |

### L 섹션
| 영어 | 한국어 | 첫 등장 챕터 | 비고 |
|------|--------|-------------|------|
| Liquidity Pool | 유동성 풀 | ch07 | 토큰 쌍 예치 컨트랙트 |
| LTV | 담보 대출 비율 | ch07 | Loan-to-Value |

### O 섹션
| 영어 | 한국어 | 첫 등장 챕터 | 비고 |
|------|--------|-------------|------|
| Oracle | 오라클 | ch07 | 외부 데이터 제공 시스템 |
| Over-collateralization | 초과 담보 | ch07 | 대출액 초과 담보 요구 |

### S 섹션
| 영어 | 한국어 | 첫 등장 챕터 | 비고 |
|------|--------|-------------|------|
| Slippage | 슬리피지 | ch07 | 거래 규모에 따른 가격 영향 |

### T 섹션
| 영어 | 한국어 | 첫 등장 챕터 | 비고 |
|------|--------|-------------|------|
| TVL | 총 예치금 | ch07 | Total Value Locked |
