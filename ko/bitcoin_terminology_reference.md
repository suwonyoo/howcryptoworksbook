# Bitcoin 용어 번역 참고 가이드

## 출처 및 참고 자료

본 가이드는 다음 출처들을 기반으로 작성되었습니다:

### 공식 문서 및 표준
- [Bitcoin.org 한국어 용어집](https://bitcoin.org/ko/vocabulary) - 공식 비트코인 용어 번역
- [Bitcoin.org 한국어 백서](https://bitcoin.org/files/bitcoin-paper/bitcoin_ko.pdf) - 사토시 나카모토 백서 공식 번역
- [Bitcoin 백서 한국어 번역 v2.0](https://mincheol.im/bitcoin) - 개선된 번역본

### 한국 거래소 및 미디어
- [업비트 투자자보호센터](https://m.upbitcare.com/academy) - 국내 최대 거래소 교육 자료
- [코인데스크 코리아](https://www.coindesk.com/) - 블록체인 전문 언론
- [디센터](https://www.decenter.kr/) - 블록체인 뉴스 미디어

### 학술 및 커뮤니티 자료
- [나무위키 비트코인](https://namu.wiki/w/%EB%B9%84%ED%8A%B8%EC%BD%BD%EC%9D%B8) - 한국어 커뮤니티 설명
- [BIP 한글화 프로젝트](https://powbitcoiner.com/posts/61) - 비트코인 개선안 번역 작업

---

## 핵심 용어 번역 가이드

### A. 기본 개념 (Core Concepts)

| 영문 | 한국어 | 병기 형식 | 사용 지침 |
|------|--------|-----------|-----------|
| Bitcoin | 비트코인 | 비트코인(Bitcoin) | 첫 언급 시 병기, 이후 비트코인만 사용 |
| blockchain | 블록체인 | 블록체인 | 한국어로 정착된 용어, 병기 불필요 |
| cryptocurrency | 암호화폐 | 암호화폐 | 가상자산, 가상화폐보다 암호화폐 권장 |
| peer-to-peer (P2P) | 개인 대 개인 / 피어투피어 | 피어투피어(P2P) | 백서에서는 "개인 대 개인", 기술 문서에서는 P2P |
| satoshi | 사토시 | 사토시 | 가장 작은 비트코인 단위 (0.00000001 BTC) |

### B. 채굴 및 합의 (Mining and Consensus)

| 영문 | 한국어 | 병기 형식 | 사용 지침 |
|------|--------|-----------|-----------|
| Proof of Work (PoW) | 작업 증명 | 작업 증명(Proof of Work, PoW) | 첫 언급 시 전체 병기, 이후 작업 증명 또는 PoW |
| mining | 채굴 | 채굴 | 마이닝보다 채굴 권장 |
| miner | 채굴자 | 채굴자 | 마이너보다 채굴자 권장 |
| hash rate / hashrate | 해시레이트 / 해시율 | 해시레이트 | 해시율보다 해시레이트가 더 일반적 |
| hash function | 해시 함수 | 해시 함수 | - |
| nonce | 논스 | 논스(nonce) | 기술 용어, 첫 언급 시 병기 |
| difficulty adjustment | 난이도 조정 | 난이도 조정 | - |
| difficulty retarget | 난이도 재조정 | 난이도 재조정 | - |
| block reward | 블록 보상 | 블록 보상 | 채굴 보상과 혼용 가능 |
| halving | 반감기 | 반감기 | 할빙보다 반감기 권장 |
| coinbase transaction | 코인베이스 거래 | 코인베이스 거래 | 거래소 Coinbase와 구별 필요 시 설명 추가 |
| ASIC | 에이식 / 주문형 반도체 | 에이식(ASIC) | Application-Specific Integrated Circuit |
| mining pool | 채굴 풀 | 채굴 풀 | - |
| Nakamoto Consensus | 나카모토 합의 / 나카모토 컨센서스 | 나카모토 합의(Nakamoto Consensus) | 합의가 컨센서스보다 자연스러움 |
| longest chain rule | 최장 체인 규칙 | 최장 체인 규칙 | - |

### C. 트랜잭션 및 UTXO (Transactions and UTXO)

| 영문 | 한국어 | 병기 형식 | 사용 지침 |
|------|--------|-----------|-----------|
| UTXO (Unspent Transaction Output) | 미사용 출력 / 미사용 출력값 | 미사용 출력(UTXO, Unspent Transaction Output) | 첫 언급 시 전체 병기, 이후 UTXO 또는 미사용 출력 |
| transaction | 거래 / 트랜잭션 | 거래 | 일반 문맥에서는 거래, 기술 문맥에서는 트랜잭션 |
| input | 입력 | 입력 | - |
| output | 출력 | 출력 | - |
| private key | 개인 키 | 개인 키 | 비밀 키보다 개인 키 권장 |
| public key | 공개 키 | 공개 키 | - |
| address | 주소 | 주소 | - |
| wallet | 지갑 | 지갑 | - |
| signature | 서명 | 서명 | - |
| digital signature | 디지털 서명 | 디지털 서명 | - |
| Bitcoin Script | 비트코인 스크립트 | 비트코인 스크립트(Bitcoin Script) | - |
| locking script | 잠금 스크립트 | 잠금 스크립트 | - |
| unlocking script | 잠금 해제 스크립트 | 잠금 해제 스크립트 | - |
| timelock | 타임락 / 시간 잠금 | 타임락 | - |
| multisig | 다중 서명 | 다중 서명(multisig) | - |

### D. 주소 형식 (Address Types)

| 영문 | 한국어 | 병기 형식 | 사용 지침 |
|------|--------|-----------|-----------|
| legacy address | 레거시 주소 | 레거시 주소 | - |
| P2SH (Pay to Script Hash) | P2SH | P2SH(Pay to Script Hash) | 약어 유지 권장 |
| Native SegWit | 네이티브 세그윗 | 네이티브 세그윗 | - |
| Taproot address | 탭루트 주소 | 탭루트 주소 | - |
| elliptic curve cryptography | 타원곡선 암호화 | 타원곡선 암호화 | - |

### E. 네트워크 및 노드 (Network and Nodes)

| 영문 | 한국어 | 병기 형식 | 사용 지침 |
|------|--------|-----------|-----------|
| node | 노드 | 노드 | - |
| full node | 풀 노드 / 전체 노드 | 풀 노드 | 전체 노드보다 풀 노드가 더 일반적 |
| mempool | 멤풀 | 멤풀(mempool) | memory pool의 축약어 |
| fee rate | 수수료율 | 수수료율 | - |
| satoshis per virtual byte (sats/vB) | 가상 바이트당 사토시 | 가상 바이트당 사토시(sats/vB) | - |
| Replace by Fee (RBF) | RBF | RBF(Replace by Fee) | 약어 유지, 필요 시 "수수료 대체" 설명 |
| Child Pays for Parent (CPFP) | CPFP | CPFP(Child Pays for Parent) | 약어 유지, 필요 시 "자식이 부모 비용 지불" 설명 |
| fork | 포크 | 포크 | - |
| chain reorganization (reorg) | 체인 재구성 | 체인 재구성(reorg) | - |
| confirmation | 승인 / 컨펌 | 승인 | 컨펌보다 승인 권장 |
| genesis block | 제네시스 블록 | 제네시스 블록 | 창세 블록보다 제네시스 블록 권장 |

### F. 프라이버시 (Privacy)

| 영문 | 한국어 | 병기 형식 | 사용 지침 |
|------|--------|-----------|-----------|
| pseudonymous | 가명성 | 가명성 | - |
| anonymous | 익명성 | 익명성 | - |
| KYC/AML | KYC/AML | KYC/AML | Know Your Customer / Anti-Money Laundering |
| address reuse | 주소 재사용 | 주소 재사용 | - |
| coin selection | 코인 선택 | 코인 선택 | - |
| CoinJoin | 코인조인 | 코인조인(CoinJoin) | - |
| anonymity set | 익명 집합 | 익명 집합 | - |

### G. 프로토콜 업그레이드 (Protocol Upgrades)

| 영문 | 한국어 | 병기 형식 | 사용 지침 |
|------|--------|-----------|-----------|
| BIP (Bitcoin Improvement Proposal) | BIP / 비트코인 개선 제안 | BIP(Bitcoin Improvement Proposal) | 첫 언급 시 병기, 이후 BIP 사용 |
| consensus rules | 합의 규칙 | 합의 규칙 | - |
| policy rules | 정책 규칙 | 정책 규칙 | - |
| hard fork | 하드 포크 | 하드 포크 | - |
| soft fork | 소프트 포크 | 소프트 포크 | - |
| Segregated Witness (SegWit) | 세그윗 / 분리된 증인 | 세그윗(Segregated Witness, SegWit) | 분리된 증인보다 세그윗 권장 |
| transaction malleability | 거래 가변성 | 거래 가변성 | - |
| block weight | 블록 가중치 | 블록 가중치 | - |
| Taproot | 탭루트 | 탭루트(Taproot) | - |
| Schnorr Signatures | 슈노르 서명 | 슈노르 서명(Schnorr Signatures) | - |
| MAST (Merkleized Abstract Syntax Trees) | MAST | MAST(Merkleized Abstract Syntax Trees) | 약어 유지, 필요 시 머클화된 추상 구문 트리 설명 |
| protocol ossification | 프로토콜 경화 | 프로토콜 경화 | ossification = 경화, 화석화 |

### H. 포크 활성화 메커니즘 (Activation Mechanisms)

| 영문 | 한국어 | 병기 형식 | 사용 지침 |
|------|--------|-----------|-----------|
| Miner Activated Soft Fork (MASF) | MASF / 채굴자 활성화 소프트 포크 | MASF(Miner Activated Soft Fork) | - |
| User Activated Soft Fork (UASF) | UASF / 사용자 활성화 소프트 포크 | UASF(User Activated Soft Fork) | - |
| Speedy Trial | 신속 시험 | 신속 시험(Speedy Trial) | - |
| signaling | 시그널링 / 신호 전송 | 시그널링 | - |
| lock-in | 락인 / 확정 | 락인 | - |
| activation | 활성화 | 활성화 | - |

### I. 레이어2 및 확장성 (Layer 2 and Scaling)

| 영문 | 한국어 | 병기 형식 | 사용 지침 |
|------|--------|-----------|-----------|
| Lightning Network | 라이트닝 네트워크 | 라이트닝 네트워크(Lightning Network) | - |
| payment channel | 지불 채널 | 지불 채널 | 결제 채널과 혼용 가능 |
| off-chain | 오프체인 | 오프체인 | - |
| on-chain | 온체인 | 온체인 | - |
| second layer / Layer 2 | 2차 레이어 / 레이어2 | 레이어2 | - |
| multisig wallet | 다중 서명 지갑 | 다중 서명 지갑 | - |

### J. 최신 기술 (Recent Innovations)

| 영문 | 한국어 | 병기 형식 | 사용 지침 |
|------|--------|-----------|-----------|
| Ordinals | 오디널스 | 오디널스(Ordinals) | - |
| inscriptions | 인스크립션 | 인스크립션 | "새김" 또는 "각인"보다 인스크립션 권장 |
| BRC-20 | BRC-20 | BRC-20 | 비트코인의 토큰 표준, ERC-20에서 영감 |

### K. 보안 및 공격 (Security and Attacks)

| 영문 | 한국어 | 병기 형식 | 사용 지침 |
|------|--------|-----------|-----------|
| double-spend | 이중 지불 | 이중 지불 | - |
| 51% attack | 51% 공격 | 51% 공격 | - |
| eclipse attack | 이클립스 공격 | 이클립스 공격 | - |
| selfish mining | 이기적 채굴 | 이기적 채굴 | - |
| security budget | 보안 예산 | 보안 예산 | - |

### L. 기타 기술 용어 (Other Technical Terms)

| 영문 | 한국어 | 병기 형식 | 사용 지침 |
|------|--------|-----------|-----------|
| SHA-256 | SHA-256 | SHA-256 | 암호화 해시 함수, 번역 불필요 |
| cryptography | 암호학 / 암호 작성술 | 암호학 | 암호 작성술보다 암호학이 더 일반적 |
| timestamp | 타임스탬프 / 시간 기록 | 타임스탬프 | - |
| Stratum | 스트라텀 | 스트라텀(Stratum) | 채굴 풀 통신 프로토콜 |
| version bit | 버전 비트 | 버전 비트 | - |
| Bitcoin Core | 비트코인 코어 | 비트코인 코어(Bitcoin Core) | - |
| reference implementation | 참조 구현 | 참조 구현 | - |

---

## 번역 원칙 및 가이드라인

### 1. 병기 사용 규칙

**첫 언급 시 병기 형식:**
- 중요 기술 용어는 첫 등장 시 한국어(영문) 형식으로 병기
- 예: "작업 증명(Proof of Work, PoW)"
- 이후에는 한국어 또는 약어만 사용

**병기가 불필요한 경우:**
- 이미 한국어로 정착된 용어: 블록체인, 채굴, 지갑
- 일반적인 개념: 거래, 주소, 네트워크

### 2. 용어 선택 기준

**한국어 번역 우선:**
- 독자 친화적이고 이해하기 쉬운 용어 선택
- 예: "마이너" → "채굴자", "컨펌" → "승인"

**영문/음차 유지:**
- 기술적으로 정착된 용어: UTXO, SegWit, Taproot
- 고유 명사: Bitcoin Core, Lightning Network

**일관성 유지:**
- 동일한 개념에 대해 일관된 용어 사용
- 예: transaction을 거래/트랜잭션 중 문맥에 따라 선택하되, 같은 섹션 내에서는 통일

### 3. 문체 가이드

**전문성과 접근성의 균형:**
- 기술 문서이므로 정확성 우선
- 그러나 불필요하게 어려운 용어는 피하고 설명 추가

**번역 vs 음차:**
- 의미가 명확한 경우: 번역 (예: mining → 채굴)
- 번역이 부자연스러운 경우: 음차 (예: Taproot → 탭루트)
- 이미 커뮤니티에서 정착된 용어는 그대로 사용

### 4. 특수한 경우

**약어 처리:**
- BIP, UTXO, RBF, CPFP 등은 약어 유지
- 첫 언급 시 전체 명칭 병기
- 이후 약어만 사용

**기술 표준 및 프로토콜:**
- SHA-256, P2SH, MAST 등은 원문 유지
- 필요 시 설명 추가

**수치 및 단위:**
- sats/vB, TH/s, EH/s 등 기술 단위는 원문 유지
- 필요 시 한국어 설명 추가

---

## 문맥별 사용 예시

### 기술 문서 작성 시:
```
비트코인(Bitcoin)은 작업 증명(Proof of Work, PoW) 합의 알고리즘을 사용합니다.
채굴자들은 블록 보상과 거래 수수료를 받으며, 약 4년마다 반감기가 발생합니다.
```

### 일반 독자용 설명 시:
```
비트코인 네트워크에서 거래가 승인되기까지는 평균 10분이 걸립니다.
이는 채굴자들이 복잡한 수학 문제를 풀어 새로운 블록을 생성하기 때문입니다.
```

### 기술 세부사항 설명 시:
```
UTXO(Unspent Transaction Output, 미사용 출력) 모델은 각 거래의 입력과 출력을
명확하게 추적합니다. 개인 키로 서명된 거래만이 해당 UTXO를 사용할 수 있습니다.
```

---

## 참고 자료별 용어 비교

### Bitcoin.org vs 커뮤니티 용어

| 개념 | Bitcoin.org | 커뮤니티 일반 | 권장 |
|------|-------------|---------------|------|
| Mining | 채굴 | 마이닝/채굴 | 채굴 |
| Confirmation | 승인 | 컨펌/확인 | 승인 |
| Wallet | 지갑 | 월렛/지갑 | 지갑 |
| Hash rate | 해시 속도 | 해시레이트 | 해시레이트 |

### 법규 및 공식 문서 vs 기술 문서

| 개념 | 법규/공식 | 기술 문서 | 사용 지침 |
|------|-----------|-----------|-----------|
| Cryptocurrency | 가상자산 | 암호화폐 | 법률 문맥: 가상자산, 기술 문맥: 암호화폐 |
| P2P | 개인 대 개인 | 피어투피어 | 백서: 개인 대 개인, 기술: P2P |

---

## 주의사항

1. **거래소 Coinbase와 coinbase transaction 구별:**
   - coinbase transaction = 코인베이스 거래 (채굴 보상 거래)
   - Coinbase exchange = 코인베이스 거래소
   - 문맥상 혼동 가능성이 있을 경우 명확히 설명

2. **비트코인 vs 비트코인:**
   - 네트워크/프로토콜: 비트코인 (Bitcoin)
   - 화폐 단위: 비트코인 (bitcoin, BTC)
   - 영문에서는 대소문자로 구별하나 한국어에서는 문맥으로 구분

3. **합의 vs 컨센서스:**
   - Nakamoto Consensus = 나카모토 합의 (컨센서스보다 자연스러움)
   - consensus rules = 합의 규칙

4. **레이어 vs 계층:**
   - Layer 2 = 레이어2 (계층보다 레이어가 더 일반적)

---

## 버전 정보

- **작성일:** 2026-02-28
- **기반 리서치:** Bitcoin.org, 국내 거래소, 커뮤니티 표준
- **적용 대상:** How Crypto Works 책 ch01_bitcoin.md 번역

---

## 추가 참고 링크

### 공식 문서
- [Bitcoin.org 한국어](https://bitcoin.org/ko/)
- [Bitcoin 백서 한국어 PDF](https://bitcoin.org/files/bitcoin-paper/bitcoin_ko.pdf)

### 용어 사전
- [Bitcoin.org 용어집](https://bitcoin.org/ko/vocabulary)
- [코인픽 용어 사전](https://coinpick.com/term)

### 기술 리소스
- [BIP 한글화](https://powbitcoiner.com/posts/61)
- [디센터 - UTXO 설명](https://www.decenter.kr/NewsView/1RZJK9SEOA)
- [나카모토 컨센서스 설명 (DSRV)](https://medium.com/dsrv/classic-one-%EB%82%98%EC%B9%B4%EB%AA%A8%ED%86%A0-%EC%BB%A8%EC%84%BC%EC%84%9C%EC%8A%A4-150a54d33a18)
- [세그윗 설명 (위키원)](https://wiki1.kr/index.php/%EC%84%B8%EA%B7%B8%EC%9C%97)
- [탭루트 설명 (GOPAX)](https://academy.gopax.co.kr/taebruteuran-mueosimyeo-biteukoine-eoddeohge-doumi-doelggayo/)
- [라이트닝 네트워크 설명 (Phemex)](https://phemex.com/ko/academy/%EB%B9%84%ED%8A%B8%EC%BD%94%EC%9D%B8-%EB%9D%BC%EC%9D%B4%ED%8A%B8%EB%8B%9D-%EB%84%A4%ED%8A%B8%EC%9B%8C%ED%81%AClightning-network%EB%8A%94-%EB%AC%B4%EC%97%87%EC%9D%BC%EA%B9%8C)
- [오디널스 및 BRC-20 설명](https://research.despread.io/ko/ordinals/)

---

**이 가이드는 ch01_bitcoin.md 번역 시 일관성과 정확성을 유지하기 위한 참고 자료입니다.**
