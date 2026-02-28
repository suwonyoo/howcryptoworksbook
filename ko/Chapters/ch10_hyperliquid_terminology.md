# Chapter 10: Hyperliquid - 신규 용어 목록

이 문서는 Chapter 10에서 새롭게 등장한 기술 용어들을 정리합니다. 용어집(glossary.md)에 이미 정의된 용어는 제외되었습니다.

---

## Hyperliquid 핵심 개념 (Hyperliquid Core Concepts)

| English | Korean | 번역 근거 |
|---------|--------|-----------|
| Hyperliquid | Hyperliquid | 고성능 무기한 선물 앱체인. 고유명사 |
| HyperCore | HyperCore | Hyperliquid의 고성능 L1 블록체인. 고유명사 |
| HyperBFT | HyperBFT | Hyperliquid의 커스텀 비잔틴 장애 허용 합의 메커니즘. 고유명사 |
| HyperEVM | HyperEVM | Hyperliquid의 EVM 호환 실행 레이어. 고유명사 |
| HYPE | HYPE | Hyperliquid의 네이티브 토큰. 고유명사 |
| Perp DEX | 무기한 선물 DEX (Perp DEX) | 무기한 선물을 거래하는 탈중앙화 거래소 |

## 무기한 선물 관련 (Perpetual Futures Related)

| English | Korean | 번역 근거 |
|---------|--------|-----------|
| Hyperps | 하이퍼프 (Hyperps) | Hyperliquid의 사전 출시 무기한 선물. 고유명사 |
| Pre-launch Trading | 사전 출시 거래 | 토큰 출시 전 무기한 선물 거래 |
| Central Limit Order Book (CLOB) | 중앙 지정가 호가창 (CLOB) | 가격-시간 우선순위 매칭 주문장 |
| On-chain Order Book | 온체인 오더북 | 블록체인에 기록되는 주문장 |
| Auto-deleveraging | 자동 디레버리징 | 극단적 상황에서 수익 포지션 강제 청산 |

## HLP 및 유동성 (HLP and Liquidity)

| English | Korean | 번역 근거 |
|---------|--------|-----------|
| Hyperliquidity Provider (HLP) | 하이퍼리퀴디티 공급자 (HLP) | Hyperliquid의 커뮤니티 소유 시장조성 볼트 |
| User-owned Vaults | 사용자 소유 볼트 | 누구나 생성할 수 있는 공개/비공개 볼트 |
| Liquidation Cascade | 청산 캐스케이드 | 연쇄적으로 발생하는 청산 |
| Child Vault | 차일드 볼트 | HLP 내 격리된 위험 한도를 가진 하위 볼트 |
| Backstop Liquidator | 백스톱 청산자 | 최후의 청산 수단으로 작동하는 주체 |
| Cold-start Liquidity Problem | 콜드 스타트 유동성 문제 | 신규 거래소의 초기 유동성 부족 문제 |

## 인프라 및 아키텍처 (Infrastructure and Architecture)

| English | Korean | 번역 근거 |
|---------|--------|-----------|
| Dual Block Architecture | 이중 블록 아키텍처 | HyperEVM의 두 종류 블록 구조 |
| Session Keys | 세션 키 | 임시 서명 권한을 가진 로컬 키 |
| Asset Linking | 자산 연결 | HyperCore와 HyperEVM 간 자산 동기화 |
| Builder Codes | 빌더 코드 | 제3자 프론트엔드 개발자 수수료 시스템 |
| Validator Jailing | 검증자 제일링 | 검증자의 블록 생성 자격 일시 정지 |

## 브릿지 및 자산 (Bridges and Assets)

| English | Korean | 번역 근거 |
|---------|--------|-----------|
| Lock-and-mint | 락앤민트 | 원본 자산 잠금 후 대응 토큰 발행 방식 |
| Unit | Unit | Hyperliquid의 토큰화 레이어 파트너. 고유명사 |
| Guardian Network | 가디언 네트워크 | 브릿지 보안을 담당하는 서명자 네트워크 |
| HIP-1 Token | HIP-1 토큰 | HyperCore의 네이티브 토큰 표준 |
| UBTC | UBTC | Unit 브릿지를 통한 비트코인 표현. 고유명사 |
| Native USDC | 네이티브 USDC | Circle이 직접 발행하는 Hyperliquid USDC |
| USDH | USDH | Hyperliquid 네이티브 스테이블코인. 고유명사 |

## 거버넌스 (Governance)

| English | Korean | 번역 근거 |
|---------|--------|-----------|
| Hyperliquid Improvement Proposals (HIPs) | Hyperliquid 개선 제안 (HIPs) | 플랫폼 진화를 위한 거버넌스 제안 |
| HIP-1 | HIP-1 | 네이티브 토큰 표준 및 더치 경매 메커니즘 |
| HIP-2 | HIP-2 | 스팟 페어에 대한 자동 Hyperliquidity 제공 |
| HIP-3 | HIP-3 | 무허가 무기한 선물 시장 배포 |
| HIP-4 | HIP-4 | 결과 시장 (옵션 및 예측 시장) |
| Dutch Auction | 더치 옥션 | 높은 가격에서 시작해 낮아지는 경매 방식 |
| Stake Slashing | 스테이크 슬래싱 | 악의적 행위에 대한 스테이크 몰수 |

## 탈중앙화 및 검증자 (Decentralization and Validators)

| English | Korean | 번역 근거 |
|---------|--------|-----------|
| Hyper Foundation | 하이퍼 파운데이션 | Hyperliquid 프로토콜의 주요 관리 주체 |
| Validator Delegation | 검증자 위임 | 토큰 보유자가 검증자에게 스테이킹 위임 |
| Commission | 커미션 | 검증자가 위임자에게 부과하는 수수료 |
| Blind Signing | 블라인드 서명 | 코드 검사 없이 서명하는 상황 |
| Closed-source Node Software | 비공개 소스 노드 소프트웨어 | 소스 코드가 공개되지 않은 노드 소프트웨어 |

## 경쟁사 (Competitors)

| English | Korean | 번역 근거 |
|---------|--------|-----------|
| dYdX | dYdX | 탈중앙화 무기한 선물 거래소. 고유명사 |
| Lighter | Lighter | 검증 가능한 매칭 및 청산을 제공하는 DEX. 고유명사 |
| Aster | Aster | CZ 자문 역할의 무기한 선물 플랫폼. 고유명사 |
| LLP | LLP | Lighter의 유동성 공급자 볼트. 고유명사 |
| Verifiable Matching | 검증 가능한 매칭 | 암호학적으로 증명 가능한 주문 매칭 |
| Cryptographic Proofs | 암호학적 증명 | 정확한 실행을 수학적으로 검증하는 증명 |

## 리퀴드 스테이킹 (Liquid Staking)

| English | Korean | 번역 근거 |
|---------|--------|-----------|
| Native Liquid Staking | 네이티브 리퀴드 스테이킹 | 블록체인 내장 리퀴드 스테이킹 |
| Kinetiq | Kinetiq | Hyperliquid 리퀴드 스테이킹 프로토콜. 고유명사 |
| kHYPE | kHYPE | Kinetiq의 리퀴드 스테이킹 토큰. 고유명사 |

## 시장 조작 및 위험 (Market Manipulation and Risks)

| English | Korean | 번역 근거 |
|---------|--------|-----------|
| JELLY Manipulation | JELLY 조작 | 저유동성 토큰을 이용한 볼트 공격 사례 |
| Price Cap | 가격 상한선 | 급격한 가격 변동 방지를 위한 제한 |
| Oracle Override | 오라클 오버라이드 | 긴급 상황에서 오라클 가격 수동 조정 |
| Liquidation Threshold Clustering | 청산 임계값 군집화 | 유사한 청산 가격에 포지션이 집중되는 현상 |

## 기타 용어 (Other Terms)

| English | Korean | 번역 근거 |
|---------|--------|-----------|
| Airdrop | 에어드롭 | 토큰 무상 배포. 업계 통용어 |
| Token Buyback | 토큰 바이백 | 프로토콜 수익으로 토큰 재매입 |
| Fee Capture | 수수료 캡처 | 프로토콜 수수료의 토큰 가치 전환 |
| Flywheel Effect | 플라이휠 효과 | 자기 강화 성장 사이클 |
| TVL (Total Value Locked) | 총 예치금 (TVL) | 프로토콜에 예치된 자산의 총 가치 |
| Points Farming | 포인트 파밍 | 미래 에어드롭을 위한 프로토콜 참여 |
| OFT (Omnichain Fungible Token) | 옴니체인 대체 가능 토큰 (OFT) | 체인 간 이동 가능한 토큰 표준 |

---

## 번역 원칙 요약

1. **프로젝트명 보존**: Hyperliquid, HyperBFT, HyperEVM, dYdX, Lighter, Aster 등 고유명사 유지

2. **기술적 약어 병기**: 첫 등장 시 한국어(English, ABBR) 형식으로 병기
   - 예: "하이퍼리퀴디티 공급자(Hyperliquidity Provider, HLP)"
   - 예: "중앙 지정가 호가창(Central Limit Order Book, CLOB)"

3. **금융 용어 통용 번역**: 금융업계에서 이미 사용되는 번역 채택
   - 예: 청산, 레버리지, 유동성, 담보

4. **업계 통용 음차어**: 한국 암호화폐 커뮤니티에서 정착된 음차 사용
   - 예: 에어드롭, 바이백, 볼트, 스테이킹

5. **Chapter VI 연계**: 무기한 선물 관련 용어는 Chapter VI와 일관성 유지
   - 예: 펀딩 비율, 마크 가격, 청산

6. **이전 챕터와 일관성**:
   - Ch02: EVM, 검증자, 스테이킹
   - Ch04: BFT, 합의 메커니즘, 앱체인
   - Ch07: DEX, 유동성 풀, TVL

---

## 용어집 업데이트 권장 사항

다음 용어들을 `/Users/yoo/howcryptoworksbook/ko/glossary.md`에 추가할 것을 권장합니다:

### H 섹션
| 영어 | 한국어 | 첫 등장 챕터 | 비고 |
|------|--------|-------------|------|
| HLP | 하이퍼리퀴디티 공급자 | ch10 | Hyperliquidity Provider |
| Hyperps | 하이퍼프 | ch10 | 사전 출시 무기한 선물 |

### C 섹션
| 영어 | 한국어 | 첫 등장 챕터 | 비고 |
|------|--------|-------------|------|
| CLOB | 중앙 지정가 호가창 | ch10 | Central Limit Order Book |

### A 섹션
| 영어 | 한국어 | 첫 등장 챕터 | 비고 |
|------|--------|-------------|------|
| Auto-deleveraging | 자동 디레버리징 | ch10 | 극단적 청산 백스톱 메커니즘 |
| Appchain | 앱체인 | ch10 | 특정 애플리케이션 최적화 블록체인 |

### B 섹션
| 영어 | 한국어 | 첫 등장 챕터 | 비고 |
|------|--------|-------------|------|
| Builder Codes | 빌더 코드 | ch10 | 제3자 프론트엔드 수수료 시스템 |
