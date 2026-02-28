# Chapter 5: Custody - 용어집

## 핵심 개념별 용어

### 암호학적 기반 (Cryptographic Foundations)

| 영어 | 한국어 | 병기 표현 | 비고 |
|------|--------|----------|------|
| Custody | 수탁 | 수탁(Custody) | 자산 보관 및 관리 |
| Self-sovereignty | 자기 주권 | 자기 주권(Self-sovereignty) | 자산에 대한 개인적 통제권 |
| Private Key | 개인키 | 개인키(Private Key) | glossary 기존 용어 |
| Public Key | 공개키 | 공개키(Public Key) | glossary 기존 용어 |
| Entropy | 엔트로피 | 엔트로피(Entropy) | 무작위성의 측정치 |
| Seed Phrase | 시드 구문 | 시드 구문(Seed Phrase) | glossary 기존 용어 |
| Digital Signature | 디지털 서명 | 디지털 서명(Digital Signature) | 거래 승인 서명 |
| Non-repudiation | 부인 방지 | 부인 방지(Non-repudiation) | 서명 후 부인 불가 |
| ECDSA | 타원 곡선 디지털 서명 알고리즘 | ECDSA(타원 곡선 디지털 서명 알고리즘, Elliptic Curve Digital Signature Algorithm) | 비트코인/이더리움 사용 |
| EdDSA | 에드워즈 곡선 디지털 서명 알고리즘 | EdDSA(에드워즈 곡선 디지털 서명 알고리즘, Edwards-curve Digital Signature Algorithm) | 솔라나 사용 |
| Schnorr Signatures | 슈노르 서명 | 슈노르 서명(Schnorr Signatures) | glossary 기존 용어 |
| Address | 주소 | 주소(Address) | 암호화폐 수신 식별자 |

### 시드 구문 및 HD 지갑 (Seed Phrases and HD Wallets)

| 영어 | 한국어 | 병기 표현 | 비고 |
|------|--------|----------|------|
| Mnemonic | 니모닉 | 니모닉(Mnemonic) | 기억 보조 단어 목록 |
| BIP-39 | BIP-39 | BIP-39(비트코인 개선 제안 39) | 니모닉 구문 표준 |
| BIP-32 | BIP-32 | BIP-32 | HD 지갑 파생 방법 |
| BIP-44 | BIP-44 | BIP-44 | 경로 구조 표준화 |
| Key Stretching | 키 스트레칭 | 키 스트레칭(Key Stretching) | 암호학적 해싱 반복 |
| Brute-force Attack | 무차별 대입 공격 | 무차별 대입 공격(Brute-force Attack) | 모든 경우의 수 시도 공격 |
| Hierarchical Deterministic (HD) Wallet | 계층적 결정론적 지갑 | 계층적 결정론적(HD, Hierarchical Deterministic) 지갑 | 하나의 시드로 다중 주소 생성 |
| Derivation Path | 파생 경로 | 파생 경로(Derivation Path) | 시드에서 주소 생성 방법 |
| Deterministic | 결정론적 | 결정론적(Deterministic) | 동일 입력 = 동일 출력 |
| Plausible Deniability | 부인 가능성 | 부인 가능성(Plausible Deniability) | 25번째 단어 관련 |
| Passphrase | 암호문 | 암호문(Passphrase) | 선택적 추가 보안 계층 |

### 개인 자기 수탁 (Individual Self-Custody)

| 영어 | 한국어 | 병기 표현 | 비고 |
|------|--------|----------|------|
| Software Wallet | 소프트웨어 지갑 | 소프트웨어 지갑(Software Wallet) | 범용 기기에 저장 |
| Hardware Wallet | 하드웨어 지갑 | 하드웨어 지갑(Hardware Wallet) | 전문 보안 기기 |
| Supply Chain Attack | 공급망 공격 | 공급망 공격(Supply Chain Attack) | 배송/생산 중 손상 |
| Clipboard Hijacker | 클립보드 하이재커 | 클립보드 하이재커(Clipboard Hijacker) | 복사 주소 대체 공격 |
| Man-in-the-middle Attack | 중간자 공격 | 중간자 공격(Man-in-the-middle Attack) | 통신 가로채기 공격 |
| Secure Element | 보안 요소 | 보안 요소(Secure Element) | 변조 방지 하드웨어 칩 |
| Wipe Code | 삭제 코드 | 삭제 코드(Wipe Code) | 자체 파괴 PIN |

### 기관 수탁 모델 (Institutional Custody Models)

| 영어 | 한국어 | 병기 표현 | 비고 |
|------|--------|----------|------|
| Insider Risk | 내부자 위험 | 내부자 위험(Insider Risk) | 권한 있는 접근자 위험 |
| Multisig (Multisignature) | 멀티시그 | 멀티시그(Multisig, 다중 서명) | glossary 기존 용어 |
| Multi-Party Computation (MPC) | 다자간 연산 | 다자간 연산(MPC, Multi-Party Computation) | 분산 암호학적 작업 |
| Threshold Signatures | 임계값 서명 | 임계값 서명(Threshold Signatures) | 정족수 기반 서명 |
| Shamir's Secret Sharing (SSS) | 샤미르의 비밀 공유 | 샤미르의 비밀 공유(SSS, Shamir's Secret Sharing) | 키 분할 방식 |
| Shard / Share | 샤드 | 샤드(Share) | 분할된 키 조각 |
| Hardware Security Module (HSM) | 하드웨어 보안 모듈 | 하드웨어 보안 모듈(HSM, Hardware Security Module) | 기업용 보안 장치 |
| Secure Enclave | 보안 엔클레이브 | 보안 엔클레이브(Secure Enclave) | 프로세서 내 격리 환경 |
| Qualified Custodian | 적격 수탁기관 | 적격 수탁기관(Qualified Custodian) | 규제 받는 은행/신탁 |
| Bankruptcy Remoteness | 도산 격리 | 도산 격리(Bankruptcy Remoteness) | 파산 시 자산 보호 구조 |

### 거래소 수탁 (Exchange Custody)

| 영어 | 한국어 | 병기 표현 | 비고 |
|------|--------|----------|------|
| Hot Storage | 핫 스토리지 | 핫 스토리지(Hot Storage) | 온라인 접근 가능 저장 |
| Warm Storage | 웜 스토리지 | 웜 스토리지(Warm Storage) | 부분적 온라인 저장 |
| Cold Storage | 콜드 스토리지 | 콜드 스토리지(Cold Storage) | 오프라인 저장 |
| Proof-of-Reserves (PoR) | 준비금 증명 | 준비금 증명(PoR, Proof-of-Reserves) | 거래소 지급 능력 증명 |
| Merkle Tree | 머클 트리 | 머클 트리(Merkle Tree) | 해시 기반 데이터 구조 |

### 역사적 사례 관련 용어

| 영어 | 한국어 | 병기 표현 | 비고 |
|------|--------|----------|------|
| Segregation | 분리 | 분리(Segregation) | 자산 구분 보관 |
| Reconciliation | 조정 | 조정(Reconciliation) | 잔액 대조 확인 |
| Formal Verification | 형식 검증 | 형식 검증(Formal Verification) | 수학적 정확성 증명 |
| Dependency Management | 의존성 관리 | 의존성 관리(Dependency Management) | 라이브러리 관리 |
| Validator | 검증자 | 검증자(Validator) | 블록/거래 검증 노드 |
| Bridge | 브릿지 | 브릿지(Bridge) | 체인 간 자산 이동 |

---

## 번역 원칙

1. **첫 등장 시 병기**: 모든 기술 용어는 첫 등장 시 한국어(영어) 형식으로 병기
2. **이후 일관성**: 첫 등장 이후에는 상황에 따라 한국어 또는 영어 약어 사용
3. **glossary 참조**: 기존 glossary에 있는 용어는 해당 번역 준수
4. **맥락 유지**: 원문의 기술적 정확성 유지

## 참고: 주요 기업/제품명

| 영어 | 처리 방식 | 비고 |
|------|----------|------|
| Ledger | Ledger | 고유명사 유지 |
| Trezor | Trezor | 고유명사 유지 |
| MetaMask | MetaMask | 고유명사 유지 |
| Trust Wallet | Trust Wallet | 고유명사 유지 |
| Phantom | Phantom | 고유명사 유지 |
| Fireblocks | Fireblocks | 고유명사 유지 |
| Copper | Copper | 고유명사 유지 |
| Coinbase Custody | Coinbase Custody | 고유명사 유지 |
| Anchorage Digital | Anchorage Digital | 고유명사 유지 |
| BitGo | BitGo | 고유명사 유지 |
| Safe (Gnosis Safe) | Safe (이전의 Gnosis Safe) | 고유명사 유지 |
| Mt. Gox | Mt. Gox | 고유명사 유지 |
| Parity | Parity | 고유명사 유지 |
| Ronin | Ronin | 고유명사 유지 |
| Axie Infinity | Axie Infinity | 고유명사 유지 |
| FTX | FTX | 고유명사 유지 |

## glossary 업데이트 필요 항목

다음 용어들은 ch05에서 처음 등장하여 glossary에 추가가 필요함:

| 영어 | 한국어 | 비고 |
|------|--------|------|
| Custody | 수탁 | 자산 보관 |
| Digital Signature | 디지털 서명 | 전자 서명 |
| ECDSA | 타원 곡선 디지털 서명 알고리즘 | Elliptic Curve Digital Signature Algorithm |
| EdDSA | 에드워즈 곡선 디지털 서명 알고리즘 | Edwards-curve Digital Signature Algorithm |
| Mnemonic | 니모닉 | 기억 보조 단어 |
| BIP-39 | BIP-39 | 니모닉 표준 |
| HD Wallet | 계층적 결정론적 지갑 | Hierarchical Deterministic Wallet |
| Hardware Wallet | 하드웨어 지갑 | 전용 보안 기기 |
| Software Wallet | 소프트웨어 지갑 | 범용 기기 지갑 |
| Secure Element | 보안 요소 | 변조 방지 칩 |
| HSM | 하드웨어 보안 모듈 | Hardware Security Module |
| Secure Enclave | 보안 엔클레이브 | 격리 실행 환경 |
| MPC | 다자간 연산 | Multi-Party Computation |
| Shamir's Secret Sharing | 샤미르의 비밀 공유 | SSS |
| Cold Storage | 콜드 스토리지 | 오프라인 저장 |
| Proof-of-Reserves | 준비금 증명 | PoR |
| Bankruptcy Remoteness | 도산 격리 | 파산 보호 구조 |
