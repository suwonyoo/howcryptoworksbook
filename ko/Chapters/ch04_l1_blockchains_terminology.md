# Chapter 4: L1 Blockchains - 용어집

## 핵심 개념 (Core Concepts)

| 영어 | 한국어 | 병기 형식 (첫 등장) | 비고 |
|------|--------|---------------------|------|
| Blockchain Trilemma | 블록체인 트릴레마 | 블록체인 트릴레마(Blockchain Trilemma) | 탈중앙화, 보안, 확장성의 동시 최적화 제약 |
| Throughput | 처리량 | 처리량(Throughput) | 초당 트랜잭션 처리 능력 |
| Liquidity | 유동성 | 유동성(Liquidity) | 자산의 거래 가능성 및 시장 깊이 |

## 아키텍처 (Architecture)

| 영어 | 한국어 | 병기 형식 (첫 등장) | 비고 |
|------|--------|---------------------|------|
| Monolithic Blockchain | 모놀리식 블록체인 | 모놀리식 블록체인(Monolithic Blockchain) | 4가지 기능을 단일 레이어에서 처리 |
| Modular Blockchain | 모듈러 블록체인 | 모듈러 블록체인(Modular Blockchain) | 기능을 분리된 구성요소로 처리 |
| Execution | 실행 | 실행(Execution) | 트랜잭션 처리 레이어 |
| Settlement | 정산 | 정산(Settlement) | 최종 상태 확정 레이어 |
| Consensus | 합의 | 합의(Consensus) | 트랜잭션 순서 동의 메커니즘 |
| Data Availability | 데이터 가용성 | 데이터 가용성(Data Availability) | 데이터 저장 및 검증 가능성 |
| Atomic Composability | 원자적 구성 가능성 | 원자적 구성 가능성(Atomic Composability) | 단일 트랜잭션에서 여러 컨트랙트 원자적 결합 |
| Composability | 구성 가능성 | 구성 가능성(Composability) | 프로토콜 간 결합 능력 |
| Sharding | 샤딩 | 샤딩(Sharding) | 상태와 처리를 병렬 샤드로 분할 |
| Subnet | 서브넷 | 서브넷(Subnet) | Avalanche의 애플리케이션별 블록체인 |

## 합의 메커니즘 (Consensus Mechanisms)

| 영어 | 한국어 | 병기 형식 (첫 등장) | 비고 |
|------|--------|---------------------|------|
| Proof of Work (PoW) | 작업 증명 | 작업 증명(Proof-of-Work, PoW) | 계산 퍼즐 기반 합의 |
| Proof of Stake (PoS) | 지분 증명 | 지분 증명(Proof-of-Stake, PoS) | 경제적 스테이킹 기반 합의 |
| Slashing Penalty | 슬래싱 페널티 | 슬래싱 페널티(Slashing Penalty) | 검증자 잘못된 행동에 대한 처벌 |
| Byzantine Fault Tolerance (BFT) | 비잔틴 장애 허용 | 비잔틴 장애 허용(Byzantine Fault Tolerance, BFT) | 악의적 참여자 존재시에도 합의 도달 |
| Delegated Proof of Stake (DPoS) | 위임 지분 증명 | 위임 지분 증명(Delegated Proof of Stake, DPoS) | 토큰 보유자가 검증자에게 위임 |
| Delegate | 위임 | 위임(Delegate) | 지분을 검증자에게 위탁 |
| Tendermint | 텐더민트 | Tendermint | Cosmos 생태계의 BFT 합의 |
| Proof of History | 역사 증명 | 역사 증명(Proof-of-History) | Solana의 암호학적 시간 기록 |
| Liveness | 라이브니스 | 라이브니스(Liveness) | 네트워크 진행 및 블록 생산 능력 |
| Safety | 안전성 | 안전성(Safety) | 무효/충돌 블록 비생성 보장 |
| Inactivity Leak | 비활성 누수 | 비활성 누수(Inactivity Leak) | 오프라인 검증자 지분 점진적 감소 |

## 최종성 유형 (Finality Types)

| 영어 | 한국어 | 병기 형식 (첫 등장) | 비고 |
|------|--------|---------------------|------|
| Finality | 최종성 | 최종성(Finality) | 트랜잭션 되돌림 불가능 상태 |
| Probabilistic Finality | 확률적 최종성 | 확률적 최종성(Probabilistic Finality) | 시간 경과에 따라 되돌림 확률 감소 |
| Economic Finality | 경제적 최종성 | 경제적 최종성(Economic Finality) | 되돌림이 경제적으로 비합리적 |
| Deterministic Finality | 결정론적 최종성 | 결정론적 최종성(Deterministic Finality) | 수학적으로 보장된 즉각적 최종성 |

## 가상 머신 (Virtual Machines)

| 영어 | 한국어 | 병기 형식 (첫 등장) | 비고 |
|------|--------|---------------------|------|
| EVM (Ethereum Virtual Machine) | 이더리움 가상 머신 | EVM(Ethereum Virtual Machine) | 이더리움 실행 환경 |
| SVM (Solana Virtual Machine) | 솔라나 가상 머신 | SVM(Solana Virtual Machine) | 솔라나 병렬 실행 환경 |
| MoveVM | Move 가상 머신 | MoveVM | Aptos, Sui의 실행 환경 |
| WASM (WebAssembly) | 웹어셈블리 | 웹어셈블리(WebAssembly, WASM) | 다중 언어 컴파일 대상 |
| Resource | 리소스 | 리소스(Resource) | Move의 복사/파괴 불가 객체 타입 |
| Linear Type | 선형 타입 | 선형 타입(Linear Type) | Move의 리소스 안전성 보장 타입 |
| CosmWasm | CosmWasm | CosmWasm | Cosmos 생태계 WASM 컨트랙트 |
| Substrate | 서브스트레이트 | 서브스트레이트(Substrate) | Polkadot의 블록체인 프레임워크 |

## 확장성 (Scalability)

| 영어 | 한국어 | 병기 형식 (첫 등장) | 비고 |
|------|--------|---------------------|------|
| Vertical Scaling | 수직적 확장 | 수직적 확장(Vertical Scaling) | 개별 체인 성능 향상 |
| Horizontal Scaling | 수평적 확장 | 수평적 확장(Horizontal Scaling) | 병렬 체인으로 작업 분배 |
| State | 상태 | 상태(State) | 블록체인의 현재 데이터 스냅샷 |
| State Growth | 상태 성장 | 상태 성장(State Growth) | 상태 데이터의 지속적 증가 |
| State Rent | 상태 렌트 | 상태 렌트(State Rent) | 온체인 데이터 저장 지속 수수료 |
| State Expiry | 상태 만료 | 상태 만료(State Expiry) | 미접근 데이터 자동 제거 |
| Verkle Tree | 버클 트리 | 버클 트리(Verkle Tree) | 작은 증명으로 상태 검증 가능 |
| TPS | TPS | TPS(Transactions Per Second) | 초당 트랜잭션 수 |

## 상호운용성 (Interoperability)

| 영어 | 한국어 | 병기 형식 (첫 등장) | 비고 |
|------|--------|---------------------|------|
| Interoperability | 상호운용성 | 상호운용성(Interoperability) | 체인 간 자산/데이터 이동 |
| Bridge | 브릿지 | 브릿지(Bridge) | 체인 간 자산 전송 메커니즘 |
| Light Client | 라이트 클라이언트 | 라이트 클라이언트(Light Client) | 전체 상태 없이 검증 가능 노드 |
| IBC (Inter-Blockchain Communication) | IBC | IBC(Inter-Blockchain Communication) | Cosmos 크로스 체인 통신 프로토콜 |
| Fraud Proof | 사기 증명 | 사기 증명(Fraud Proof) | 무효 메시지 챌린지 증명 |
| Optimistic Bridge | 낙관적 브릿지 | 낙관적 브릿지(Optimistic Bridge) | 유효성 가정 후 챌린지 허용 |
| Trusted/Multisig Bridge | 신뢰/멀티시그 브릿지 | 신뢰/멀티시그 브릿지(Trusted/Multisig Bridge) | 가디언 그룹 기반 브릿지 |
| Validator Set Bridge | 검증자 세트 브릿지 | 검증자 세트 브릿지(Validator Set Bridge) | 전용 검증자 네트워크 기반 |
| Native Verification | 네이티브 검증 | 네이티브 검증(Native Verification) | 암호학적 증명 기반 직접 검증 |
| External Verification | 외부 검증 | 외부 검증(External Verification) | 제3자 중개자 기반 검증 |
| Zero-Knowledge Light Client Bridge | 영지식 라이트 클라이언트 브릿지 | 영지식 라이트 클라이언트 브릿지(Zero-Knowledge Light Client Bridge) | ZK 증명 압축 검증 |
| Intent-based Architecture | 의도 기반 아키텍처 | 의도 기반 아키텍처(Intent-based Architecture) | 사용자 의도 지정, 솔버 라우팅 처리 |

## 프로젝트 및 프로토콜 (Projects & Protocols)

| 영어 | 한국어 | 비고 |
|------|--------|------|
| Avalanche | 아발란체 | 서브넷 아키텍처 L1 |
| Avalanche Warp Messaging | 아발란체 워프 메시징 | Avalanche 크로스 서브넷 통신 |
| Cosmos | 코스모스 | IBC 기반 블록체인 생태계 |
| Aptos | 앱토스 | Move 기반 L1 |
| Sui | 수이 | Move 기반 객체 중심 L1 |
| Monad | 모나드 | EVM 호환 고성능 L1 |
| NEAR Protocol | 니어 프로토콜 | WASM 기반 L1 |
| Polkadot | 폴카닷 | 멀티체인 프레임워크 |
| Fogo | 포고 | SVM 기반 L1 |
| Solayer | 솔레이어 | SVM 기반 L1 |
| LayerZero | 레이어제로 | 크로스 체인 메시징 프로토콜 |
| Wormhole | 웜홀 | 가디언 기반 브릿지 |
| Axelar | 액셀러 | 검증자 세트 브릿지 |
| Chainlink CCIP | 체인링크 CCIP | 오라클 기반 크로스 체인 |
| Circle CCTP | 써클 CCTP | USDC 전용 크로스 체인 |
| Stargate | 스타게이트 | LayerZero 기반 유동성 브릿지 |
| Across Protocol | 어크로스 프로토콜 | 낙관적 모델 브릿지 |
| Ronin Bridge | 로닌 브릿지 | Axie Infinity 브릿지 |
| Rainbow Bridge | 레인보우 브릿지 | NEAR 브릿지 |
| Nomad | 노마드 | 낙관적 브릿지 |
| Poly Network | 폴리 네트워크 | 크로스 체인 브릿지 |
| Harmony Horizon | 하모니 호라이즌 | Harmony 브릿지 |

## 기술 용어 (Technical Terms)

| 영어 | 한국어 | 병기 형식 (첫 등장) | 비고 |
|------|--------|---------------------|------|
| Flash Loan | 플래시 론 | 플래시 론(Flash Loan) | 단일 트랜잭션 무담보 대출 |
| Reentrancy Attack | 재진입 공격 | 재진입 공격(Reentrancy Attack) | 컨트랙트 재호출 취약점 |
| Gas | 가스 | 가스(Gas) | 트랜잭션 연산 비용 단위 |
| Block Gas Limit | 블록 가스 리밋 | 블록 가스 리밋(Block Gas Limit) | 블록당 최대 가스 |
| Uncle/Orphan Block | 엉클/고아 블록 | 엉클 블록(Uncle Block) | 채택되지 않은 유효 블록 |
| Oracle | 오라클 | 오라클(Oracle) | 외부 데이터 온체인 전달 |
| Forkless Upgrade | 포크리스 업그레이드 | 포크리스 업그레이드(Forkless Upgrade) | 하드포크 없는 런타임 변경 |
| Pipelining | 파이프라이닝 | 파이프라이닝(Pipelining) | 병렬 처리 최적화 기법 |

---

## 번역 규칙 적용 예시

### 첫 등장 시
- "블록체인 설계에서 **블록체인 트릴레마(Blockchain Trilemma)**는 핵심 제약이다."
- "**비잔틴 장애 허용(Byzantine Fault Tolerance, BFT)** 합의 알고리즘을 사용한다."

### 이후 등장 시
- "Blockchain Trilemma로 인해 모든 체인은 타협해야 한다."
- "BFT 체인은 안전성을 우선시한다."

### 고유명사
- 프로젝트명(Avalanche, Cosmos, Monad 등)은 첫 등장 시 한국어 음역 후 영어 사용
- 예: "아발란체(Avalanche)는...", 이후 "Avalanche"

### 약어
- 약어는 첫 등장 시 전체 명칭과 함께 표기
- 예: "지분 증명(Proof-of-Stake, PoS)"
- 이후: "PoS 시스템"
