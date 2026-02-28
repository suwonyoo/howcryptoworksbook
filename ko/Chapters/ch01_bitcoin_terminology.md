# Chapter 1: Bitcoin - 신규 용어 목록

이 문서는 Chapter 1에서 새롭게 등장한 기술 용어들을 정리합니다. 용어집(glossary.md)에 이미 정의된 용어는 제외되었습니다.

---

## 핵심 합의 메커니즘

| English | Korean | 번역 근거 |
|---------|--------|-----------|
| Proof of Work (PoW) | 작업 증명 | 국내 암호화폐 커뮤니티에서 널리 사용되는 표준 번역. "작업"이 computational work를 의미 |
| Nakamoto Consensus | 나카모토 합의 | 사토시 나카모토의 이름을 딴 합의 알고리즘. 고유명사로 음차 사용 |
| Genesis Block | 제네시스 블록 | 최초 블록을 의미하는 고유명사적 용어. "창세 블록"보다 업계에서 "제네시스 블록" 통용 |
| Difficulty Retarget | 난이도 재조정 | 채굴 난이도가 주기적으로 재조정되는 메커니즘. "재조정"이 retarget의 의미를 정확히 전달 |

## 채굴 관련 용어

| English | Korean | 번역 근거 |
|---------|--------|-----------|
| Mining | 채굴 | 국내 표준 번역. 금 채굴에서 유래한 비유를 유지 |
| Miner | 채굴자 | Mining을 수행하는 주체 |
| Block Reward | 블록 보상 | 블록 생성에 대한 보상. 직역이 명확 |
| Halving | 반감기 | 보상이 절반으로 줄어드는 이벤트. 한국 암호화폐 커뮤니티 표준 용어 |
| Hash Function | 해시 함수 | 암호학 표준 용어. "해시"는 음차로 통용 |
| Hash Rate | 해시레이트 | 채굴 성능 지표. 영어 그대로 사용이 일반적 |
| Nonce | 논스 | Number used once의 약자. 음차로 통용 |
| ASIC (Application-Specific Integrated Circuit) | ASIC (주문형 반도체) | 약어는 영어 그대로, 풀네임은 한국어로 병기 |
| Mining Pool | 마이닝 풀 | 채굴자들의 연합. "채굴 풀"보다 "마이닝 풀"이 업계에서 더 통용 |
| Coinbase Transaction | 코인베이스 트랜잭션 | 블록의 첫 번째 거래. 거래소 이름과 구별 필요 |
| Stale (block) | 스테일 (블록) | 폐기된 블록. "고아 블록"이라고도 하나 원문에서 stale 사용 |
| Subsidy | 보조금 | 새로 발행되는 비트코인. Block reward의 구성 요소 |

## UTXO 및 거래 구조

| English | Korean | 번역 근거 |
|---------|--------|-----------|
| UTXO (Unspent Transaction Output) | UTXO (미사용 트랜잭션 출력) | 비트코인 핵심 개념. 약어와 풀네임 병기 |
| Coin Selection | 코인 선택 | UTXO 선택 과정. 직역이 명확 |
| Bitcoin Script | 비트코인 스크립트 | 비트코인의 프로그래밍 언어 |
| Timelock | 타임락 | 시간 기반 잠금. 영어 그대로 사용이 일반적 |
| Mempool | 멤풀 | Memory pool의 약자. 미확인 거래 대기열 |
| Fee Rate | 수수료율 | 단위 크기당 수수료 |
| Replace by Fee (RBF) | 수수료 대체 (RBF) | 수수료를 높여 거래를 대체하는 기능 |
| Child Pays for Parent (CPFP) | 자식이 부모를 지불 (CPFP) | 자식 거래로 부모 거래 수수료를 보충 |
| Satoshi | 사토시 | 비트코인의 최소 단위 (1억분의 1 BTC). 창시자 이름에서 유래 |

## 주소 및 암호학

| English | Korean | 번역 근거 |
|---------|--------|-----------|
| Elliptic Curve Cryptography | 타원 곡선 암호 | 암호학 표준 번역 |
| Public Key | 공개키 | 암호학 표준 번역 |
| Legacy Address | 레거시 주소 | 구형 주소 형식 |
| P2SH (Pay to Script Hash) | P2SH | 기술적 약어는 영어 그대로 사용 |
| Native SegWit | 네이티브 SegWit | SegWit 주소의 네이티브 형식 |
| Transaction Malleability | 거래 가변성 | 거래 ID가 변경될 수 있는 취약점 |
| Block Weight | 블록 가중치 | SegWit 도입 이후의 블록 크기 측정 단위 |

## 프라이버시 관련

| English | Korean | 번역 근거 |
|---------|--------|-----------|
| CoinJoin | 코인조인 | 프라이버시 기술. 고유명사로 음차 |
| Address Reuse | 주소 재사용 | 같은 주소를 반복 사용하는 것 |
| Transaction Graph Analysis | 거래 그래프 분석 | 온체인 분석 기법 |

## 프로토콜 업그레이드

| English | Korean | 번역 근거 |
|---------|--------|-----------|
| BIP (Bitcoin Improvement Proposal) | BIP (비트코인 개선 제안) | 비트코인 변경 제안 표준 |
| Consensus Rules | 합의 규칙 | 블록체인 유효성 검증 규칙 |
| Policy Rules | 정책 규칙 | 노드의 선택적 필터링 규칙 |
| Soft Fork | 소프트 포크 | 역호환적 프로토콜 변경 |
| Hard Fork | 하드 포크 | 비호환적 프로토콜 변경 |
| MASF (Miner Activated Soft Fork) | MASF (채굴자 활성화 소프트 포크) | 채굴자 시그널링 기반 활성화 |
| UASF (User Activated Soft Fork) | UASF (사용자 활성화 소프트 포크) | 사용자/노드 주도 활성화 |
| Speedy Trial | 스피디 트라이얼 | Taproot 활성화에 사용된 메커니즘 |
| Protocol Ossification | 프로토콜 경직화 | 변화에 저항하는 경향 |

## SegWit 및 Taproot

| English | Korean | 번역 근거 |
|---------|--------|-----------|
| SegWit (Segregated Witness) | SegWit (세그윗) | 분리된 증인. "세그윗"은 한국에서 통용되는 음차 |
| Witness | 증인 | 서명 데이터를 분리 저장하는 구조 |
| Taproot | Taproot (탭루트) | 2021년 활성화된 업그레이드. 고유명사 |
| Schnorr Signatures | 슈노르 서명 | Taproot에서 도입된 서명 방식 |
| MAST (Merkleized Abstract Syntax Trees) | MAST (머클화된 추상 구문 트리) | 복잡한 스크립트 조건 구조화 기술 |

## 네트워크 운영

| English | Korean | 번역 근거 |
|---------|--------|-----------|
| Full Node | 풀 노드 | 전체 블록체인을 검증하는 노드 |
| Pruned Node | 가지치기 노드 | 오래된 데이터를 삭제하는 노드 |
| SPV (Simplified Payment Verification) | SPV (간이 결제 검증) | 경량 검증 방식 |
| Initial Block Download (IBD) | 초기 블록 다운로드 | 신규 노드의 동기화 과정 |
| Compact Block Relay | 컴팩트 블록 릴레이 | 효율적인 블록 전파 프로토콜 |
| 51% Attack | 51% 공격 | 과반수 해시파워를 이용한 공격 |
| Security Budget | 보안 예산 | 블록 보조금 + 거래 수수료 |
| Eclipse Attack | 이클립스 공격 | 노드 격리 공격 |
| Selfish Mining | 이기적 채굴 | 블록 보류 전략 |
| Chain Reorganization (Reorg) | 체인 재구성 (Reorg) | 체인 분기 해결 과정 |
| Confirmation | 컨펌 | 블록에 포함된 후의 확인 수 |
| Fork | 포크 | 체인 분기 |

## Layer 2 및 확장

| English | Korean | 번역 근거 |
|---------|--------|-----------|
| Lightning Network | 라이트닝 네트워크 | 비트코인 L2 결제 네트워크 |
| Payment Channel | 결제 채널 | 오프체인 결제 경로 |
| Inbound Capacity | 인바운드 용량 | 받을 수 있는 최대 금액 |
| Outbound Capacity | 아웃바운드 용량 | 보낼 수 있는 최대 금액 |
| Covenant | 코버넌트 | 미래 지출 조건을 제한하는 기능 |
| BitVM | BitVM | 비트코인 가상 머신. 고유명사 |
| Sidechain | 사이드체인 | 비트코인에 연결된 별도 체인 |
| Federation | 연합 | 다중 서명 관리 그룹 |

## Ordinals 및 인스크립션

| English | Korean | 번역 근거 |
|---------|--------|-----------|
| Ordinal Theory | 오디널 이론 | 사토시 번호 매기기 체계 |
| Ordinals | 오디널스 | 서수 기반 자산 시스템 |
| Inscription | 인스크립션 | 사토시에 데이터를 새기는 것 |
| BRC-20 | BRC-20 | 비트코인 대체 가능 토큰 표준 |

## 기타

| English | Korean | 번역 근거 |
|---------|--------|-----------|
| Cypherpunk | 사이퍼펑크 | 암호학 기반 프라이버시 운동 |
| Fiat Currency | 법정화폐 | 정부 발행 화폐 |
| Disinflationary | 디스인플레이션 | 인플레이션율이 감소하는 특성 |
| Antifragile | 안티프래질 | 스트레스로부터 강해지는 특성 (탈레브 용어) |
| Schelling Point | 쉘링 포인트 | 자연스러운 조정점 (게임 이론) |

---

## 번역 원칙 요약

1. **업계 통용 용어 우선**: 한국 암호화폐 커뮤니티에서 이미 널리 사용되는 번역이 있으면 해당 번역을 채택 (예: 반감기, 채굴)

2. **고유명사 음차**: 프로토콜 이름, 기술 명칭 등 고유명사는 음차 처리 (예: Taproot → 탭루트, SegWit → 세그윗)

3. **약어 보존**: 기술적 약어는 영어 그대로 유지하고 풀네임을 병기 (예: UTXO, BIP, MASF)

4. **첫 등장 시 병기**: 기술 용어의 첫 등장 시 한국어(English) 형식으로 병기하고, 이후에는 영어만 사용

5. **직역 가능한 경우 직역**: 의미가 명확히 전달되는 경우 직역 선호 (예: Block Reward → 블록 보상)

6. **맥락 고려**: 같은 단어라도 맥락에 따라 다르게 번역 가능 (예: node가 그래프 이론에서는 "노드", 네트워크에서는 "노드")
