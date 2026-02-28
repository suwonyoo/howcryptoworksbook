# Chapter 2: Ethereum - 신규 용어 목록

이 문서는 Chapter 2에서 새롭게 등장한 기술 용어들을 정리합니다. 용어집(glossary.md)에 이미 정의된 용어는 제외되었습니다.

---

## 핵심 개념 (Core Concepts)

| English | Korean | 번역 근거 |
|---------|--------|-----------|
| Ethereum Virtual Machine (EVM) | 이더리움 가상 머신 (EVM) | 이더리움의 핵심 연산 엔진. 한국 암호화폐 커뮤니티에서 "EVM"으로 통용 |
| Proof of Stake (PoS) | 지분 증명 (PoS) | 합의 메커니즘. "지분"이 stake의 의미를 정확히 전달 |
| Gas | 가스 | 연산 수수료 단위. 영어 그대로 사용이 한국 커뮤니티 표준 |
| gwei | gwei | 수수료 단위 (1 gwei = 10^9 wei). 고유 단위명으로 영어 그대로 사용 |
| Validator | 검증자 | PoS에서 블록을 검증하는 주체. "검증자"가 업계 표준 번역 |
| Composability | 조합 가능성 | 프로토콜이 레고처럼 함께 작동하는 능력. 직역이 의미 전달에 적합 |
| Decentralized Consensus | 탈중앙화된 합의 | 중앙 주체 없이 네트워크가 합의에 도달하는 메커니즘 |

## 수수료 시스템 (Fee System)

| English | Korean | 번역 근거 |
|---------|--------|-----------|
| Base Fee | 기본 수수료 | EIP-1559에서 도입된 동적 수수료 구성 요소 |
| Priority Fee | 우선 수수료 | 검증자에게 주는 팁. "maxPriorityFeePerGas"의 구성 요소 |
| Gas Limit | 가스 한도 | 블록당 최대 가스 사용량 |
| Elastic Blocks | 탄력적 블록 | 수요에 따라 크기가 변할 수 있는 블록 |
| Burn (수수료) | 소각 | 기본 수수료가 영구히 파괴되는 메커니즘 |
| Deflationary | 디플레이션 | 공급이 축소되는 특성 |

## 계정 및 자산 (Accounts and Assets)

| English | Korean | 번역 근거 |
|---------|--------|-----------|
| Externally Owned Account (EOA) | 외부 소유 계정 (EOA) | 개인키로 제어되는 일반 사용자 지갑 |
| Smart Contract Account | 스마트 컨트랙트 계정 | 코드를 실행하는 프로그래밍 가능한 계정 |
| Ethereum Name Service (ENS) | 이더리움 네임 서비스 (ENS) | 사람이 읽을 수 있는 주소 시스템 |
| Account Abstraction | 계정 추상화 | EOA와 컨트랙트 계정의 경계를 흐리게 하는 기능 |
| ERC-20 | ERC-20 | 대체 가능 토큰 표준. 고유명사로 영어 그대로 사용 |
| ERC-721 | ERC-721 | NFT 토큰 표준 |
| ERC-1155 | ERC-1155 | 다중 토큰 표준 |

## 프로토콜 업그레이드 (Protocol Upgrades)

| English | Korean | 번역 근거 |
|---------|--------|-----------|
| Ethereum Improvement Proposal (EIP) | 이더리움 개선 제안 (EIP) | 이더리움 변경 제안 표준. BIP와 유사한 형식 |
| ERC (Ethereum Request for Comment) | ERC | 애플리케이션 수준 표준 제안. 고유 약어 유지 |
| The Merge | 더 머지 | PoW에서 PoS로의 전환. 고유명사로 음차 |
| Beacon Chain | 비콘 체인 | PoS 합의 레이어. 고유명사 음차 |
| Shapella | Shapella | 스테이킹 출금 업그레이드. 고유명사 |
| Dencun | Dencun | 블롭 거래 업그레이드. 고유명사 |
| Pectra | Pectra | 계정 위임 업그레이드. 고유명사 |
| Fusaka | Fusaka | 가스 한도 표준화 업그레이드. 고유명사 |

## 합의 및 스테이킹 (Consensus and Staking)

| English | Korean | 번역 근거 |
|---------|--------|-----------|
| Slot | 슬롯 | 12초 시간 단위 |
| Epoch | 에포크 | 32 슬롯 (약 6.4분) 단위 |
| Attestation | 증명 | 검증자의 암호학적 투표 |
| Finality | 최종성 | 거래가 되돌릴 수 없게 되는 지점 |
| Justified | 정당화됨 | 최종성 전 단계 |
| Finalized | 확정됨 | 완전히 최종성이 달성된 상태 |
| Slashing | 슬래싱 | 악의적 행동에 대한 재정적 처벌. 업계 표준 음차 |
| Correlation Penalty | 상관 처벌 | 조율된 공격에 대한 확대된 처벌 |
| Inactivity Leak | 비활동 유출 | 오프라인 검증자 잔액 고갈 메커니즘 |
| BLS Signatures | BLS 서명 | 서명 집계 암호학 기술 |
| Effective Balance | 유효 잔액 | 투표 권한에 반영되는 스테이킹 ETH |

## 유동 스테이킹 (Liquid Staking)

| English | Korean | 번역 근거 |
|---------|--------|-----------|
| Liquid Staking | 유동 스테이킹 | 스테이킹하면서 유동성을 유지하는 방식 |
| Liquid Staking Token (LST) | 유동 스테이킹 토큰 (LST) | 스테이킹 지분을 나타내는 거래 가능한 토큰 |
| Rebasing Token | 리베이싱 토큰 | 잔액이 자동 조정되는 토큰 (예: stETH) |
| stETH | stETH | Lido의 유동 스테이킹 토큰. 고유명사 |
| rETH | rETH | Rocket Pool의 유동 스테이킹 토큰. 고유명사 |

## 레이어 2 및 롤업 (Layer 2 and Rollups)

| English | Korean | 번역 근거 |
|---------|--------|-----------|
| Layer 2 (L2) | 레이어 2 (L2) | 확장성 솔루션 레이어 |
| Layer 1 (L1) | 레이어 1 (L1) | 기본 블록체인 레이어 (이더리움 메인넷) |
| Rollup | 롤업 | 연산을 오프체인으로 이동시키는 스케일링 솔루션. 업계 표준 음차 |
| Optimistic Rollup | 낙관적 롤업 | 사기 증명 기반 롤업 |
| ZK Rollup | ZK 롤업 | 유효성 증명 기반 롤업 |
| Sequencer | 시퀀서 | 롤업에서 거래를 정렬하고 묶는 주체 |
| Fraud Proof | 사기 증명 | 유효하지 않은 거래를 탐지하는 증명 |
| Validity Proof | 유효성 증명 | 거래 정확성을 수학적으로 증명 |
| Challenge Period | 이의 제기 기간 | 사기 증명 제출 가능 기간 (약 7일) |
| Validium | Validium | 외부 DA를 사용하는 롤업. 고유명사 |
| Data Availability (DA) | 데이터 가용성 (DA) | 거래 데이터 접근 가능성 보장 |

## ZK 증명 시스템 (ZK Proof Systems)

| English | Korean | 번역 근거 |
|---------|--------|-----------|
| Zero-Knowledge Proof | 영지식 증명 | 정보를 공개하지 않고 정확성을 증명하는 기술 |
| SNARK | SNARK | 작은 증명 생성. 고유 약어 유지 |
| STARK | STARK | 투명한 증명 시스템. 고유 약어 유지 |
| Trusted Setup | 신뢰 설정 | SNARK에 필요한 초기 매개변수 생성 |
| KZG Commitment | KZG 커밋먼트 | 블롭 무결성 검증용 암호학적 지문 |

## 데이터 가용성 (Data Availability)

| English | Korean | 번역 근거 |
|---------|--------|-----------|
| Blob | 블롭 | 대규모 임시 데이터 패킷. EIP-4844 도입 |
| Blob-carrying Transaction | 블롭 운반 거래 | 블롭을 포함하는 거래 유형 |
| Danksharding | 댕크샤딩 | 장기적 DA 스케일링 비전. 고유명사 음차 |
| Data Availability Sampling | 데이터 가용성 샘플링 | 작은 조각만 확인하여 DA를 검증하는 기술 |
| Celestia | Celestia | 대안적 DA 레이어. 고유명사 |
| EigenDA | EigenDA | 리스테이킹 기반 DA 레이어. 고유명사 |

## 리스테이킹 (Restaking)

| English | Korean | 번역 근거 |
|---------|--------|-----------|
| Restaking | 리스테이킹 | 스테이킹된 자본을 여러 프로토콜에 재사용 |
| EigenLayer | EigenLayer | 리스테이킹 프로토콜. 고유명사 |
| Actively Validated Service (AVS) | 능동적 검증 서비스 (AVS) | 리스테이킹으로 보호되는 외부 프로토콜 |
| EigenPod | EigenPod | 검증자 출금 자격 증명을 보유하는 컨트랙트 |
| Operator | 운영자 | 검증 인프라를 운영하는 전문가 |
| Delegator | 위임자 | 운영자에게 스테이크를 위임하는 사용자 |
| Strategy Contract | 전략 컨트랙트 | 예치금/출금을 처리하는 컨트랙트 |
| Slashing Contract | 슬래싱 컨트랙트 | 각 AVS의 규칙을 시행하는 컨트랙트 |
| Veto Committee | 거부권 위원회 | 슬래싱 결정에 대한 추가 보안 레이어 |
| Intersubjective Slashing | 상호주관적 슬래싱 | 사회적 합의 기반 슬래싱 결정 |
| Liquid Restaking Token (LRT) | 유동 리스테이킹 토큰 (LRT) | 리스테이킹 지분을 나타내는 토큰 |
| Correlated Slashing Risk | 상관 슬래싱 위험 | 여러 AVS에서 동시에 처벌받을 위험 |
| Liquidity Cascade | 유동성 연쇄반응 | LRT 페그 해제 시 발생 가능한 대량 출금 |
| Basis Risk | 베이시스 위험 | 기본 수익률과 토큰 가격 간의 차이 위험 |

## 시퀀서 관련 (Sequencer Related)

| English | Korean | 번역 근거 |
|---------|--------|-----------|
| Shared Sequencing Network | 공유 시퀀싱 네트워크 | 정렬 책임을 분산시키는 네트워크 |
| Sequencer Rotation | 시퀀서 로테이션 | 정렬 주체를 주기적으로 변경 |
| Inclusion List | 포함 목록 | 시퀀서가 특정 거래를 포함하도록 강제 |
| Preconfirmation | 사전 확인 | 공식 합의 전 거래 포함에 대한 소프트 커밋먼트 |

## 기타 (Others)

| English | Korean | 번역 근거 |
|---------|--------|-----------|
| Opcode | 옵코드 | EVM의 저수준 명령어 |
| Bytecode | 바이트코드 | 컴파일된 스마트 컨트랙트 코드 |
| Stack-based Virtual Machine | 스택 기반 가상 머신 | EVM의 아키텍처 유형 |
| Deterministic Execution | 결정론적 실행 | 동일 입력에 대해 항상 동일 출력 |
| Persistent State | 영속적 상태 | 거래 간에 유지되는 데이터 |
| Wei | wei | ETH의 최소 단위. 고유 단위명 |
| Transaction Censorship | 거래 검열 | 검증자가 특정 거래를 제외하는 것 |
| Miniblock | 미니블록 | 매우 짧은 간격의 블록 (예: MegaETH) |

---

## 번역 원칙 요약

1. **EIP/ERC 번호 보존**: 기술적 제안 번호는 영어 그대로 유지 (예: EIP-1559, ERC-20)

2. **업그레이드명 보존**: Shapella, Dencun, Pectra 등 업그레이드 명칭은 고유명사로 유지

3. **프로토콜/프로젝트명 보존**: Lido, Rocket Pool, EigenLayer, Arbitrum 등은 고유명사로 유지

4. **기술적 약어 병기**: 첫 등장 시 한국어(English, ABBR) 형식으로 병기
   - 예: "이더리움 가상 머신(Ethereum Virtual Machine, EVM)"

5. **업계 통용 용어 우선**: 한국 암호화폐 커뮤니티에서 이미 널리 사용되는 번역 채택
   - 예: 가스, 슬래싱, 롤업, 검증자

6. **의미 전달 우선**: 직역이 어색한 경우 의역 사용
   - 예: "Optimistic Rollup" → "낙관적 롤업" (trust but verify 철학 반영)

7. **일관성 유지**: 용어집(glossary.md) 및 Chapter 1 번역과의 일관성 유지
   - 예: Proof of Work → 작업 증명 (ch01과 동일)

---

## 용어집 업데이트 권장 사항

다음 용어들을 `/Users/yoo/howcryptoworksbook/ko/glossary.md`에 추가할 것을 권장합니다:

### E 섹션
| 영어 | 한국어 | 첫 등장 챕터 | 비고 |
|------|--------|-------------|------|
| EIP | 이더리움 개선 제안 | ch02 | Ethereum Improvement Proposal |
| ERC-20 | ERC-20 | ch02 | 대체 가능 토큰 표준 |
| ERC-721 | ERC-721 | ch02 | NFT 토큰 표준 |
| EVM | 이더리움 가상 머신 | ch02 | Ethereum Virtual Machine |

### G 섹션
| 영어 | 한국어 | 첫 등장 챕터 | 비고 |
|------|--------|-------------|------|
| Gas | 가스 | ch02 | 연산 수수료 단위 |

### L 섹션
| 영어 | 한국어 | 첫 등장 챕터 | 비고 |
|------|--------|-------------|------|
| Layer 2 (L2) | 레이어 2 | ch02 | 확장성 솔루션 레이어 |
| Liquid Staking | 유동 스테이킹 | ch02 | LST 발행 스테이킹 방식 |

### P 섹션
| 영어 | 한국어 | 첫 등장 챕터 | 비고 |
|------|--------|-------------|------|
| Proof of Stake | 지분 증명 | ch02 | PoS 합의 메커니즘 |

### R 섹션
| 영어 | 한국어 | 첫 등장 챕터 | 비고 |
|------|--------|-------------|------|
| Restaking | 리스테이킹 | ch02 | 스테이킹 자본 재사용 |
| Rollup | 롤업 | ch02 | L2 스케일링 솔루션 |

### S 섹션
| 영어 | 한국어 | 첫 등장 챕터 | 비고 |
|------|--------|-------------|------|
| Slashing | 슬래싱 | ch02 | 악의적 행동에 대한 처벌 |
| Sequencer | 시퀀서 | ch02 | 롤업 거래 정렬 주체 |

### T 섹션
| 영어 | 한국어 | 첫 등장 챕터 | 비고 |
|------|--------|-------------|------|
| The Merge | 더 머지 | ch02 | PoW→PoS 전환 (2022.9) |

### V 섹션
| 영어 | 한국어 | 첫 등장 챕터 | 비고 |
|------|--------|-------------|------|
| Validator | 검증자 | ch02 | PoS 블록 검증자 |
