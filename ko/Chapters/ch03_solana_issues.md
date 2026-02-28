# ch03_solana 번역 이슈

## 원문 오류/모호함

| 위치 | 원문 | 이슈 | 심각도 |
|------|------|------|--------|
| - | - | 특별한 이슈 없음 | - |

## 번역 해석 논의

### 1. "Proof of History" 번역
- **원문**: "Proof of History (PoH)"
- **번역 선택**: "역사 증명(Proof of History, PoH)"
- **이유**: "이력 증명"도 가능하나 "역사 증명"이 더 직관적.

### 2. "Lamports" 번역
- **원문**: "lamports" (Solana 최소 단위)
- **번역 선택**: "램포트(Lamports)"
- **이유**: Leslie Lamport의 이름에서 유래. 고유명사로 음차.

### 3. "Program Derived Addresses" 번역
- **원문**: "Program Derived Addresses (PDAs)"
- **번역 선택**: "프로그램 파생 주소(PDAs)"
- **이유**: Solana 핵심 개념. "파생"이 derived를 정확히 표현.

### 4. Solana 고유 컴포넌트명
- **원문**: Gulf Stream, Turbine, Sealevel 등
- **번역 선택**: 원문 유지
- **이유**: Solana 아키텍처의 고유명사. 음차하면 의미 손실.

### 5. "Account Model" vs "UTXO Model"
- **원문**: "account model" (Solana/Ethereum)
- **번역 선택**: "계정 모델(Account Model)"
- **이유**: Bitcoin의 UTXO 모델과 대비되는 개념.

## 잠재적 GitHub Issue

없음

## 번역 노트

- Solana는 독특한 아키텍처로 고유 용어가 많음
- 기술 컴포넌트 이름은 대부분 고유명사로 유지
- MEV, validator 등은 이전 챕터와 일관성 유지
