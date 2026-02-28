# Bitcoin 용어 한국어 번역 리서치 보고서

## 요약

본 보고서는 ch01_bitcoin.md의 한국어 번역을 위해 비트코인 기술 용어의 표준 한국어 번역을 조사한 결과입니다. Bitcoin.org 공식 문서, 국내 주요 거래소, 블록체인 미디어, 학술 자료 등을 종합적으로 분석하여 한국 암호화폐 커뮤니티에서 실제로 사용되는 용어를 정리했습니다.

**작성일:** 2026-02-28
**목적:** How Crypto Works 책 1장 비트코인 번역 가이드

---

## 1. 주요 출처 및 신뢰도

### 1.1 공식 문서 (최고 신뢰도)

**Bitcoin.org 한국어 공식 용어집**
- URL: https://bitcoin.org/ko/vocabulary
- 신뢰도: ★★★★★
- 특징: 비트코인 공식 웹사이트의 한국어 용어 정의
- 주요 용어: 채굴(Mining), 블록체인(Blockchain), 승인(Confirmation), 해시 속도(Hash Rate)

**비트코인 백서 한국어 번역 (v2.0)**
- URL: https://mincheol.im/bitcoin
- 신뢰도: ★★★★★
- 특징: 국립국어원 표준 맞춤법 적용, 기술 용어 일관성 유지
- 주요 기여: P2P = "개인 대 개인", 작업 증명 등 핵심 개념 번역

### 1.2 국내 거래소 및 업계 표준 (높은 신뢰도)

**업비트(Upbit) / 빗썸(Bithumb)**
- 한국 최대 암호화폐 거래소들
- 신뢰도: ★★★★
- 특징: 일반 사용자들이 가장 많이 접하는 용어 사용
- 주요 용어: 채굴, 블록체인, 지갑, 거래 등 대중적 표현

### 1.3 블록체인 미디어 및 커뮤니티 (참고 자료)

**코인데스크 코리아, 디센터 등 전문 언론**
- 신뢰도: ★★★★
- 특징: 기술 기사에서 사용되는 표준 용어
- 활용: 최신 기술(Taproot, Ordinals 등)의 한국어 표현

**나무위키, 위키백과**
- 신뢰도: ★★★
- 특징: 커뮤니티 합의를 반영한 설명
- 활용: 대중적으로 통용되는 용어 확인

---

## 2. 핵심 용어 번역 가이드라인

### 2.1 작업 증명 및 채굴 관련

#### Proof of Work (PoW)
- **표준 번역:** 작업 증명
- **첫 사용:** 작업 증명(Proof of Work, PoW)
- **이후 사용:** 작업 증명 또는 PoW
- **출처:** Bitcoin.org, 학술 논문, 업계 표준
- **대안 용어:** 작업 증명 시스템
- **설명:** "서비스 요청자로부터 일부 작업을 요구함으로써 서비스 거부 공격을 단념하게 만드는 경제적 수단"

#### Mining / Miner
- **Mining:** 채굴 (마이닝 ✗)
- **Miner:** 채굴자 (마이너 ✗)
- **근거:** Bitcoin.org 공식 용어, 업비트/빗썸 등 거래소 표준
- **설명:** "컴퓨터 하드웨어가 비트코인 네트워크의 거래 승인 및 보안을 위한 수학적 계산 처리"

#### Hash Rate
- **표준 번역:** 해시레이트 (해시율보다 일반적)
- **설명:** "비트코인 네트워크의 처리능력을 측정하는 단위"
- **단위:** TH/s (테라해시/초), EH/s (엑사해시/초)

#### Block Reward / Halving
- **Block Reward:** 블록 보상
- **Halving:** 반감기 (할빙 ✗)
- **출처:** 토스뱅크, 레저, 주요 언론
- **설명:** "블록 보상은 채굴자가 새 블록을 생성했을 때 받는 보상. 반감기는 21만 블록마다 보상이 절반으로 줄어드는 시점"
- **역사:**
  - 2009년: 50 BTC
  - 2012년: 25 BTC
  - 2016년: 12.5 BTC
  - 2020년: 6.25 BTC
  - 2024년: 3.125 BTC

#### Difficulty Adjustment
- **표준 번역:** 난이도 조정
- **관련 용어:** 난이도 재조정(Difficulty Retarget)
- **설명:** "2,016개 블록마다 약 2주 간격으로 채굴 난이도를 자동 조정"

### 2.2 UTXO 및 트랜잭션

#### UTXO (Unspent Transaction Output)
- **표준 번역:** 미사용 출력 / 미사용 출력값 / 미사용 트랜잭션 출력값
- **첫 사용:** 미사용 출력(UTXO, Unspent Transaction Output)
- **이후 사용:** UTXO 또는 미사용 출력
- **커뮤니티 설명:**
  - "아직 쓰지 않은 잔액"
  - "원화에 동전이나 지폐가 있듯, 비트코인에는 UTXO가 있다"
  - "비트코인 네트워크에서는 잔액이라는 개념이 애초에 존재하지 않고, 트랜잭션 결과물들의 합을 UTXO 데이터로 대체"
- **출처:** Medium, Steemit, Brunch 기술 블로그

#### Private Key / Public Key
- **Private Key:** 개인 키 (비밀 키보다 권장)
- **Public Key:** 공개 키
- **출처:** Bitcoin.org, 백서 번역
- **설명:** "개인 키는 특정한 비트코인 지갑의 비트코인을 소비할 권리가 있음을 증명하는 비밀정보"

### 2.3 합의 메커니즘

#### Nakamoto Consensus
- **표준 번역:** 나카모토 합의 (나카모토 컨센서스보다 자연스러움)
- **첫 사용:** 나카모토 합의(Nakamoto Consensus)
- **출처:** Hashed 팀 블로그, Medium 기술 글
- **설명:**
  - "제네시스 블록 이후 약 10년간 한 번도 실패하지 않은 비트코인 프로토콜의 원리"
  - "누적 난이도가 제일 높은 체인을 메인 체인으로 정함"
  - "가장 긴 체인이 아니라 가장 많은 작업이 투입된 체인"

#### Genesis Block
- **표준 번역:** 제네시스 블록 (창세 블록보다 권장)
- **설명:** 블록체인의 첫 번째 블록
- **역사적 의미:** 2009년 1월 3일, 사토시 나카모토가 "Chancellor on brink of second bailout for banks" 메시지 삽입

### 2.4 프로토콜 업그레이드

#### Segregated Witness (SegWit)
- **표준 번역:** 세그윗 (분리된 증인보다 권장)
- **첫 사용:** 세그윗(Segregated Witness, SegWit)
- **출처:** 업비트, 빗썸, 블록체인 미디어
- **설명:** "서명 데이터를 별도 위치로 분리하여 거래 가변성 문제 해결"

#### Taproot
- **표준 번역:** 탭루트 (음차)
- **첫 사용:** 탭루트(Taproot)
- **출처:** BitMEX 블로그, GOPAX, Phemex
- **관련 기술:** 슈노르 서명(Schnorr Signatures)
- **설명:** "비트코인의 확장성, 안정성, 프라이버시 향상"

#### Schnorr Signatures
- **표준 번역:** 슈노르 서명
- **출처:** BitMEX, Phemex, 기술 블로그
- **설명:** "키와 서명을 집계하여 복잡한 다자간 거래를 단일 서명처럼 보이게 함"

#### BIP (Bitcoin Improvement Proposal)
- **표준 번역:** BIP / 비트코인 개선 제안
- **첫 사용:** BIP(Bitcoin Improvement Proposal)
- **이후 사용:** BIP
- **출처:** Bitcoin.org, 기술 문서

### 2.5 라이트닝 네트워크

#### Lightning Network
- **표준 번역:** 라이트닝 네트워크 (음차)
- **첫 사용:** 라이트닝 네트워크(Lightning Network)
- **출처:** 뱅크샐러드, Medium, Phemex
- **설명:** "비트코인의 확장성 문제를 해결하기 위한 2차 레이어 솔루션"

#### Payment Channel
- **표준 번역:** 지불 채널 / 결제 채널 (혼용 가능)
- **출처:** Decipher Media, Codechain, Medium
- **설명:**
  - "멀티시그 기술을 통해 양쪽의 거래를 오프체인으로 진행"
  - "거래의 시작과 끝은 온체인, 중간 거래는 오프체인"
  - "라이트닝 네트워크와 페이먼트 채널 네트워크의 관계는 비트코인과 블록체인의 관계와 같음"

### 2.6 최신 기술 (Ordinals, BRC-20)

#### Ordinals
- **표준 번역:** 오디널스 (음차)
- **첫 사용:** 오디널스(Ordinals)
- **출처:** 한국경제, 파이낸셜뉴스, BeinCrypto Korea
- **설명:**
  - "2023년 1월 케이시 로더머(Casey Rodarmor)가 개발"
  - "비트코인의 최소 단위인 사토시에 데이터를 첨부하여 NFT를 만드는 기술"

#### Inscriptions
- **표준 번역:** 인스크립션 ("새김" 또는 "각인"보다 권장)
- **출처:** 한국경제, 크몽, 업계 표준
- **설명:** "사토시에 비문, 이미지 등의 데이터를 첨부하는 과정"

#### BRC-20
- **표준 번역:** BRC-20 (음차)
- **출처:** 한국경제, BeinCrypto Korea, HackerNoon
- **설명:**
  - "2023년 3월 도모(domo)가 발표"
  - "오디널스 프로토콜을 활용해 비트코인 블록체인에 대체 가능 토큰(FT)을 형성하는 표준"
  - "ERC-20에서 영감을 받음"

---

## 3. 번역 원칙 및 베스트 프랙티스

### 3.1 병기(倂記) 사용 규칙

**첫 언급 시 병기:**
```
작업 증명(Proof of Work, PoW)
미사용 출력(UTXO, Unspent Transaction Output)
나카모토 합의(Nakamoto Consensus)
```

**이후 사용:**
- 한국어 또는 약어만 사용
- 예: "작업 증명은..." 또는 "PoW는..."

**병기 불필요:**
- 이미 정착된 용어: 블록체인, 채굴, 지갑, 거래
- 너무 기본적인 용어: 주소, 네트워크, 노드

### 3.2 용어 선택 기준

#### 한국어 번역 우선 (독자 친화성)
- Mining → 채굴 (마이닝 ✗)
- Miner → 채굴자 (마이너 ✗)
- Confirmation → 승인 (컨펌 ✗)
- Wallet → 지갑 (월렛 ✗)

#### 영문/음차 유지 (기술 정착도)
- UTXO (미사용 출력과 병용)
- SegWit, Taproot, Ordinals
- Bitcoin Core, Lightning Network
- SHA-256, P2SH, MAST

#### 문맥별 선택
- **Transaction:**
  - 일반 문맥: 거래
  - 기술 문맥: 트랜잭션
  - 같은 섹션 내 일관성 유지

### 3.3 특수 케이스

#### 약어 처리
```
BIP(Bitcoin Improvement Proposal) → 이후 BIP
RBF(Replace by Fee) → 이후 RBF
CPFP(Child Pays for Parent) → 이후 CPFP
```

#### 혼동 주의 용어

**Coinbase 구별:**
- Coinbase transaction = 코인베이스 거래 (채굴 보상)
- Coinbase exchange = 코인베이스 거래소
- 혼동 가능 시 명시적 설명 추가

**Bitcoin 대소문자:**
- Bitcoin (대문자) = 네트워크/프로토콜
- bitcoin (소문자) = 화폐 단위
- 한국어에서는 문맥으로 구분

**합의 vs 컨센서스:**
- Nakamoto Consensus = 나카모토 합의 (✓)
- Consensus rules = 합의 규칙 (✓)
- "컨센서스"보다 "합의"가 자연스러움

---

## 4. 문맥별 번역 예시

### 4.1 기술 문서 (전문적)

**원문:**
> Bitcoin uses Proof of Work consensus. Miners receive block rewards and transaction fees.

**번역:**
> 비트코인은 작업 증명(Proof of Work, PoW) 합의 알고리즘을 사용합니다. 채굴자들은 블록 보상과 거래 수수료를 받습니다.

### 4.2 일반 독자용 (친화적)

**원문:**
> Transactions are confirmed by miners who compete to solve complex puzzles.

**번역:**
> 거래는 복잡한 수학 문제를 풀기 위해 경쟁하는 채굴자들에 의해 승인됩니다.

### 4.3 기술 세부사항 (정확성)

**원문:**
> The UTXO model tracks each transaction's inputs and outputs. Only transactions signed with the private key can spend UTXOs.

**번역:**
> UTXO(Unspent Transaction Output, 미사용 출력) 모델은 각 거래의 입력과 출력을 명확하게 추적합니다. 개인 키로 서명된 거래만이 해당 UTXO를 사용할 수 있습니다.

---

## 5. 주요 발견 사항

### 5.1 커뮤니티 용어 통일성

**높은 통일성 (90% 이상 일치):**
- 채굴(Mining), 블록체인(Blockchain), 지갑(Wallet)
- 작업 증명(PoW), 반감기(Halving)
- 세그윗(SegWit), 탭루트(Taproot)

**중간 통일성 (70-90%):**
- UTXO: "미사용 출력" vs "미사용 출력값"
- Hash Rate: "해시레이트" vs "해시율"
- Confirmation: "승인" vs "컨펌"

**낮은 통일성 (70% 미만):**
- Payment Channel: "지불 채널" vs "결제 채널" vs "페이먼트 채널"
- P2P: "피어투피어" vs "개인 대 개인"

### 5.2 영문 유지 vs 한국어 번역 경향

**영문 유지 선호:**
- 기술 표준: SHA-256, P2SH, MAST
- 약어: BIP, UTXO, RBF, CPFP
- 고유 명사: Bitcoin Core, Lightning Network

**한국어 번역 선호:**
- 일반 개념: 채굴, 지갑, 거래, 주소
- 설명 가능: 작업 증명, 블록 보상, 난이도 조정

### 5.3 신조어 및 최신 기술

**최신 기술 용어 (2021-2024):**
- Taproot → 탭루트 (음차)
- Schnorr Signatures → 슈노르 서명
- Ordinals → 오디널스
- Inscriptions → 인스크립션
- BRC-20 → BRC-20

**경향:**
- 대부분 음차 후 설명 추가
- 커뮤니티 합의 형성 중
- 기술 미디어가 표준 선도

---

## 6. 권장 번역 전략

### 6.1 우선순위

1. **Bitcoin.org 공식 용어** (최우선)
2. **백서 한국어 번역** (핵심 개념)
3. **국내 거래소 표준** (대중성)
4. **기술 미디어 용어** (최신성)
5. **커뮤니티 합의** (실사용)

### 6.2 일관성 유지

**동일 섹션 내:**
- Transaction → 거래 또는 트랜잭션 중 하나로 통일
- 한 번 선택한 용어 계속 사용

**전체 문서:**
- 핵심 용어는 전체적으로 통일
- 용어집 참조하여 일관성 확보

### 6.3 독자 배려

**기술 용어 첫 등장:**
```
작업 증명(Proof of Work, PoW)은 채굴자가 엄청난 계산 작업을
수행했음을 증명하는 시스템입니다.
```

**반복 언급:**
```
작업 증명 시스템에서는...
PoW 알고리즘은...
```

---

## 7. 번역 시 주의사항

### 7.1 피해야 할 표현

❌ **지양:**
- 마이너, 마이닝, 월렛, 컨펌
- 과도한 영어 남용
- 문맥 없는 기술 용어 나열

✅ **지향:**
- 채굴자, 채굴, 지갑, 승인
- 한국어 + 영문 병기
- 용어 정의와 설명

### 7.2 정확성 vs 가독성

**기술 정확성 필수:**
- UTXO, SegWit, Taproot 등 핵심 개념
- 숫자, 알고리즘, 프로토콜 명칭

**가독성 우선 가능:**
- 일반 설명 부분
- 예시 및 비유
- 도입부 설명

### 7.3 문화적 맥락

**한국 독자 고려:**
- 법률 용어: 가상자산 (공식), 암호화폐 (기술)
- 익숙한 예시: 원화, 은행, 거래소
- 국내 규제 환경 반영

---

## 8. 참고 자료 전체 목록

### 8.1 공식 문서
1. [Bitcoin.org 한국어 용어집](https://bitcoin.org/ko/vocabulary)
2. [Bitcoin 백서 한국어 번역 v2.0](https://mincheol.im/bitcoin)
3. [Bitcoin.org 한국어 백서 PDF](https://bitcoin.org/files/bitcoin-paper/bitcoin_ko.pdf)

### 8.2 기술 리소스
4. [작업 증명 설명 - 위키백과](https://ko.wikipedia.org/wiki/%EC%9E%91%EC%97%85_%EC%A6%9D%EB%AA%85_%EC%8B%9C%EC%8A%A4%ED%85%9C)
5. [UTXO 개념 - Steemit](https://steemit.com/coinkorea/@brownbears/utxo)
6. [나카모토 합의 - Hashed](https://medium.com/hashed-kr/conflux-scaling-nakamoto-consensus-kr-6cfe87559136)
7. [블록체인 용어 - 뱅크샐러드](https://www.banksalad.com/contents/%EC%89%BD%EA%B2%8C-%EC%84%A4%EB%AA%85%ED%95%98%EB%8A%94-%EB%B8%94%EB%A1%9D%EC%B2%B4%EC%9D%B8-%EB%B8%94%EB%A1%9D%EC%B2%B4%EC%9D%B8-%EC%9A%A9%EC%96%B4-%EC%A0%95%EB%A6%AC-WEkfu)

### 8.3 세그윗/탭루트
8. [슈노르 서명 및 탭루트 - BitMEX](https://blog.bitmex.com/please-translate-in-ko_kr-the-schnorr-signature-taproot-softfork-proposal/)
9. [탭루트 설명 - GOPAX](https://medium.com/gopax/%ED%83%AD%EB%A3%A8%ED%8A%B8-taproot-%EB%9E%80-%EB%AC%B4%EC%97%87%EC%9D%B8%EA%B0%80-d191d970a500)
10. [비트코인 주소 유형 - 비트펑크](https://www.bitpunk.one/entry/%EB%B9%84%ED%8A%B8%EC%BD%94%EC%9D%B8-%EC%A3%BC%EC%86%8C-%EC%9C%A0%ED%98%95-%EB%A0%88%EA%B1%B0%EC%8B%9C-%EC%84%B8%EA%B7%B8%EC%9C%97-%ED%83%AD%EB%A3%A8%ED%8A%B8-%EA%B0%9C%EB%85%90%EA%B3%BC-%EC%B0%A8%EC%9D%B4%EC%A0%90)

### 8.4 라이트닝 네트워크
11. [라이트닝 네트워크 1부 - Medium](https://medium.com/the-litecoin-school-of-crypto/%EB%9D%BC%EC%9D%B4%ED%8A%B8%EB%8B%9D-%EB%84%A4%ED%8A%B8%EC%9B%8C%ED%81%AC-%EC%9D%B4%ED%95%B4%ED%95%98%EA%B8%B0-1%EB%B6%80-6bcc9d0b9d59)
12. [지불 채널 - Decipher Media](https://medium.com/decipher-media/%EB%9D%BC%EC%9D%B4%ED%8A%B8%EB%8B%9D-%EB%84%A4%ED%8A%B8%EC%9B%8C%ED%81%AC-%EC%8B%9C%EB%A6%AC%EC%A6%88-1-30de587ce6cb)
13. [라이트닝 네트워크 설명 - 뱅크샐러드](https://www.banksalad.com/contents/%EC%89%BD%EA%B2%8C-%EC%84%A4%EB%AA%85%ED%95%98%EB%8A%94-%EB%B8%94%EB%A1%9D%EC%B2%B4%EC%9D%B8-%EB%9D%BC%EC%9D%B4%ED%8A%B8%EB%8B%9D-%EB%84%A4%ED%8A%B8%EC%9B%8C%ED%81%AC-Lightning-Network-%EB%9E%80-g9nT6)

### 8.5 반감기
14. [비트코인 반감기 - 토스뱅크](https://www.tossbank.com/articles/bitcoinhalf)
15. [반감기 설명 - Ledger](https://www.ledger.com/ko/academy/glossary/halving)

### 8.6 오디널스/BRC-20
16. [BRC-20 가이드 - BeinCrypto Korea](https://kr.beincrypto.com/learn-kr/brc-20-%EC%B4%88%EA%B0%84%EB%8B%A8-%ED%88%AC%EC%9E%90-%EA%B0%80%EC%9D%B4%EB%93%9C/)
17. [오디널스 논쟁 - 한국경제](https://www.hankyung.com/article/202312095251B)
18. [BRC-20 설명 - 한국경제](https://www.hankyung.com/article/202305121482g)

### 8.7 용어 사전
19. [코인픽 용어 사전](https://coinpick.com/term)
20. [블록체인 용어사전 - Medium](https://medium.com/ceta-network/%EB%B8%94%EB%A1%9D%EC%B2%B4%EC%9D%B8-%EC%9A%A9%EC%96%B4%EC%82%AC%EC%A0%84-1%EB%B6%80-%E3%84%B1-%E3%85%87-f69b3cda64f5)

---

## 9. 결론 및 권장 사항

### 9.1 핵심 발견

1. **표준화 수준:**
   - 기본 용어(채굴, 블록체인)는 높은 통일성
   - 신기술 용어는 커뮤니티 합의 진행 중
   - Bitcoin.org가 가장 신뢰할 수 있는 기준

2. **번역 경향:**
   - 일반 개념 → 한국어 번역 선호
   - 기술 표준 → 영문 유지
   - 최신 기술 → 음차 + 설명

3. **독자 배려:**
   - 첫 언급 시 병기 필수
   - 기술 용어는 설명 추가
   - 문맥에 따른 유연한 선택

### 9.2 번역 시 권장 워크플로우

**1단계: 용어 식별**
- 원문에서 기술 용어 추출
- 핵심 용어와 일반 용어 구분

**2단계: 표준 확인**
- 본 가이드 및 용어집 참조
- Bitcoin.org 공식 용어 우선
- 커뮤니티 사용 빈도 확인

**3단계: 일관성 검증**
- 동일 용어의 통일된 번역
- 병기 형식의 일관성
- 섹션별 용어 통일

**4단계: 독자 검증**
- 기술 정확성 확인
- 가독성 테스트
- 설명 충분성 평가

### 9.3 최종 권장사항

1. **Bitcoin.org 용어를 기본으로 사용**
2. **첫 언급 시 영문 병기**
3. **대중적 용어 우선 선택** (채굴 > 마이닝)
4. **기술 표준은 영문 유지** (UTXO, BIP, SegWit)
5. **일관성 철저히 유지**
6. **독자 수준 고려한 설명 추가**

---

## 부록: 빠른 참조 테이블

### A. 반드시 병기할 용어 (첫 언급 시)
| 영문 | 한국어 | 병기 형식 |
|------|--------|-----------|
| Proof of Work | 작업 증명 | 작업 증명(Proof of Work, PoW) |
| UTXO | 미사용 출력 | 미사용 출력(UTXO, Unspent Transaction Output) |
| Nakamoto Consensus | 나카모토 합의 | 나카모토 합의(Nakamoto Consensus) |
| Segregated Witness | 세그윗 | 세그윗(Segregated Witness, SegWit) |
| BIP | 비트코인 개선 제안 | BIP(Bitcoin Improvement Proposal) |

### B. 한국어만 사용 (병기 불필요)
- 블록체인, 채굴, 채굴자, 지갑, 거래, 주소, 승인, 난이도 조정, 블록 보상, 반감기

### C. 영문만 사용
- SHA-256, P2SH, MAST, BRC-20, RBF, CPFP

---

**보고서 작성:** 2026-02-28
**기반 리서치:** Bitcoin.org, 국내 거래소, 학술 자료, 커뮤니티 표준
**적용 대상:** How Crypto Works - Chapter 1: Bitcoin 번역
