# Chapter 11: NFTs - 신규 용어 목록

이 문서는 Chapter 11에서 새롭게 등장한 기술 용어들을 정리합니다. 용어집(glossary.md)에 이미 정의된 용어는 제외되었습니다.

---

## NFT 핵심 개념 (NFT Core Concepts)

| English | Korean | 번역 근거 |
|---------|--------|-----------|
| Non-Fungible Token (NFT) | 대체 불가능 토큰 (NFT) | 각 토큰이 고유한 디지털 자산. 업계 표준 번역 |
| Fungible Token | 대체 가능 토큰 | 모든 단위가 동일한 토큰. NFT와 대비 개념 |
| Metadata | 메타데이터 | 토큰에 첨부된 이름, 설명, 이미지 등의 정보 |
| tokenURI | tokenURI | 메타데이터 파일을 가리키는 URI. 기술 용어 유지 |
| Provenance | 출처 증명 | 토큰의 원본성과 이력 증명 |
| Token-gated | 토큰 게이트 | 토큰 보유에 기반한 접근 제한 기능 |
| Royalty | 로열티 | 2차 판매 시 창작자에게 지급되는 수수료 |

## 토큰 표준 (Token Standards)

| English | Korean | 번역 근거 |
|---------|--------|-----------|
| ERC-721 | ERC-721 | 이더리움 대체 불가능 토큰 표준. 고유명사 유지 |
| ERC-1155 | ERC-1155 | 이더리움 다중 토큰 표준. 고유명사 유지 |
| ERC-2981 | ERC-2981 | NFT 로열티 표준. 고유명사 유지 |
| ownerOf | ownerOf | ERC-721 함수명. 기술 용어 유지 |
| transferFrom | transferFrom | ERC-721 함수명. 기술 용어 유지 |
| approve | approve | ERC-721 함수명. 기술 용어 유지 |
| setApprovalForAll | setApprovalForAll | ERC-721 함수명. 기술 용어 유지 |
| Batch Operations | 배치 작업 | 다수 토큰을 단일 트랜잭션으로 처리 |

## NFT 유형 (NFT Types)

| English | Korean | 번역 근거 |
|---------|--------|-----------|
| Dynamic NFT | 다이나믹 NFT | 시간에 따라 진화하는 NFT |
| Composable NFT | 조합 가능한 NFT | 다른 토큰을 포함할 수 있는 NFT |
| Semi-fungible Token | 반대체 가능 토큰 | 대체 가능과 고유 사이의 토큰 |
| Soulbound Token (SBT) | 소울바운드 토큰 (SBT) | 전송 불가능한 신원/자격증 NFT. Vitalik Buterin 제안 용어 |
| Profile Picture Project (PFP) | 프로필 사진 프로젝트 (PFP) | 소셜 미디어 아바타용 NFT 컬렉션 |
| Generative Art | 제너레이티브 아트 | 알고리즘에 의해 생성된 아트 |

## 스토리지 솔루션 (Storage Solutions)

| English | Korean | 번역 근거 |
|---------|--------|-----------|
| IPFS (InterPlanetary File System) | IPFS (행성간 파일 시스템) | 콘텐츠 주소 지정 분산 스토리지 |
| Arweave | Arweave | 영구 스토리지 블록체인. 고유명사 유지 |
| Permaweb | 영구 웹 | Arweave의 영구 저장 레이어 |
| Pinning | 피닝 | IPFS에서 파일을 사용 가능하게 유지하는 행위 |
| Content-addressed | 콘텐츠 주소 지정 | 콘텐츠 해시로 파일을 식별하는 방식 |
| On-chain Storage | 온체인 스토리지 | 블록체인에 직접 데이터 저장 |

## 저작권 및 라이선스 (Copyright and Licensing)

| English | Korean | 번역 근거 |
|---------|--------|-----------|
| Creative Commons Zero (CC0) | 크리에이티브 커먼즈 제로 (CC0) | 퍼블릭 도메인 헌정 라이선스 |
| Public Domain | 퍼블릭 도메인 | 저작권 없이 자유롭게 사용 가능한 상태 |
| Commercial Rights | 상업적 권리 | 아트워크의 상업적 사용 권한 |
| Intellectual Property | 지적 재산 | 창작물에 대한 법적 권리 |
| Usage Rights | 사용권 | 콘텐츠 사용에 대한 정의된 권한 |

## 가격 책정 및 시장 (Pricing and Market)

| English | Korean | 번역 근거 |
|---------|--------|-----------|
| Floor Price | 바닥 가격 | 컬렉션 내 가장 저렴한 NFT 가격. 업계 통용어 |
| Trait-based Pricing | 특성 기반 가격 책정 | NFT의 개별 특성을 고려한 가격 산정 |
| Collection-wide Bidding | 컬렉션 전체 입찰 | 특정 기준 충족하는 모든 NFT에 입찰 |
| Trait-level Bidding | 특성 수준 입찰 | 특정 특성을 가진 NFT에 입찰 |
| Floor Sweep | 바닥 스윕 | 바닥 가격의 NFT를 대량 구매 |
| Price Discovery | 가격 발견 | 시장에서 적정 가격을 찾는 과정 |

## 공급 메커니즘 (Supply Mechanics)

| English | Korean | 번역 근거 |
|---------|--------|-----------|
| Fixed Supply | 고정 공급 | 절대 증가하지 않는 토큰 수량 |
| Bonding Curve | 본딩 커브 | 공급에 따라 가격이 변하는 수학적 곡선. Ch07에서 상세 설명 |
| Burning Mechanism | 소각 메커니즘 | 토큰을 영구 파괴하는 기능 |
| Deflationary Pressure | 디플레이션 압력 | 공급 감소로 인한 가치 상승 압력 |
| Minting | 민팅 | 새로운 NFT 생성 |

## 런칭 전략 (Launch Strategies)

| English | Korean | 번역 근거 |
|---------|--------|-----------|
| Fair Launch | 공정 출시 | 선착순 동일 가격 판매 |
| Dutch Auction | 더치 옥션 | 높은 가격에서 하락하는 경매. Ch07에서 소개 |
| Allowlist | 허용 목록 | 사전 승인된 지갑에 조기 접근 부여 |
| Whitelist | 화이트리스트 | Allowlist의 대체 용어 |
| Public Sale | 퍼블릭 세일 | 일반 대중 대상 판매 |

## 마켓플레이스 (Marketplaces)

| English | Korean | 번역 근거 |
|---------|--------|-----------|
| OpenSea | OpenSea | 최대 이더리움 NFT 마켓플레이스. 고유명사 |
| Blur | Blur | 전문 트레이더 대상 NFT 마켓플레이스. 고유명사 |
| Magic Eden | Magic Eden | 솔라나 주요 NFT 마켓플레이스. 고유명사 |
| Tensor | Tensor | 솔라나 전문 트레이더 마켓플레이스. 고유명사 |
| Aggregator | 애그리게이터 | 여러 마켓플레이스 가격 비교 플랫폼 |
| Gem | Gem | NFT 애그리게이터 (OpenSea 인수). 고유명사 |
| Genie | Genie | NFT 애그리게이터 (Uniswap 인수). 고유명사 |
| Operator Filter | 운영자 필터 | OpenSea의 로열티 강제 메커니즘 |

## 솔라나 NFT (Solana NFTs)

| English | Korean | 번역 근거 |
|---------|--------|-----------|
| Metaplex | Metaplex | 솔라나 NFT 표준 프레임워크. 고유명사 |
| Compressed NFT | 압축 NFT | 상태 압축을 사용한 저비용 NFT |
| State Compression | 상태 압축 | 온체인 요약만 저장하는 기술. Ch03에서 소개 |

## 보안 (Security)

| English | Korean | 번역 근거 |
|---------|--------|-----------|
| Wallet Drainer | 지갑 드레이너 | 지갑 자산을 빼내는 악성 컨트랙트 |
| Phishing Attack | 피싱 공격 | 가짜 웹사이트로 속이는 공격 |
| Burner Wallet | 버너 지갑 | 위험한 상호작용용 일회용 지갑 |
| Approval | 승인 | 다른 컨트랙트에 토큰 전송 권한 부여 |

## NFT 컬렉션 및 프로젝트명 (NFT Collections and Projects)

| English | Korean | 번역 근거 |
|---------|--------|-----------|
| CryptoPunks | CryptoPunks | 최초의 NFT PFP 프로젝트. 고유명사 |
| Bored Ape Yacht Club | Bored Ape Yacht Club | 대표적 PFP 프로젝트. 고유명사 |
| Pudgy Penguins | Pudgy Penguins | PFP 프로젝트. 고유명사 |
| Nouns DAO | Nouns DAO | CC0 채택 프로젝트. 고유명사 |
| CrypToadz | CrypToadz | CC0 채택 프로젝트. 고유명사 |
| Art Blocks | Art Blocks | 제너레이티브 아트 플랫폼. 고유명사 |
| Fidenzas | Fidenzas | Tyler Hobbs의 제너레이티브 아트. 고유명사 |
| Chromie Squiggles | Chromie Squiggles | Snowfro의 제너레이티브 아트. 고유명사 |
| Autoglyphs | Autoglyphs | 온체인 제너레이티브 아트. 고유명사 |
| Axie Infinity | Axie Infinity | P2E 게임 NFT 프로젝트. 고유명사 |
| The Sandbox | The Sandbox | 가상 세계 NFT 프로젝트. 고유명사 |
| Solana Monkey Business | Solana Monkey Business | 솔라나 NFT 컬렉션. 고유명사 |
| Mad Lads | Mad Lads | 솔라나 NFT 컬렉션. 고유명사 |
| Claynosaurz | Claynosaurz | 솔라나 NFT 컬렉션. 고유명사 |

## 기타 개념 (Other Concepts)

| English | Korean | 번역 근거 |
|---------|--------|-----------|
| Digital Tribal Signaling | 디지털 부족 신호 | 온라인 정체성과 소속을 나타내는 행위 |
| Network Effects | 네트워크 효과 | 사용자 증가에 따른 가치 상승 |
| Blue-chip | 블루칩 | 가치가 인정된 대표 컬렉션 |
| Long Tail | 롱테일 | 주류 외의 다수의 소규모 프로젝트 |
| Play-to-Earn (P2E) | 플레이-투-언 (P2E) | 게임으로 수익을 얻는 모델 |

---

## 번역 원칙 요약

1. **프로젝트명 보존**: CryptoPunks, OpenSea, Blur, Art Blocks 등 프로젝트명은 고유명사로 유지

2. **토큰 표준 유지**: ERC-721, ERC-1155, ERC-2981 등 표준명은 원어 유지

3. **기술적 약어 병기**: 첫 등장 시 한국어(English, ABBR) 형식으로 병기
   - 예: "대체 불가능 토큰(Non-Fungible Token, NFT)"
   - 예: "소울바운드 토큰(Soulbound Token, SBT)"

4. **업계 통용 음차어**: 한국 암호화폐 커뮤니티에서 정착된 음차 사용
   - 예: 메타데이터, 민팅, 로열티, 피닝

5. **스토리지 관련 용어**: 기술적 특성을 반영한 번역
   - 예: IPFS → 행성간 파일 시스템 (첫 등장 시 병기)

6. **이전 챕터와 일관성**: Ch07에서 정의된 용어(본딩 커브, 더치 옥션 등) 일관되게 사용

7. **마켓플레이스 고유명사**: OpenSea, Blur, Magic Eden 등 마켓플레이스명 유지

---

## 용어집 업데이트 권장 사항

다음 용어들을 `/Users/yoo/howcryptoworksbook/ko/glossary.md`에 추가할 것을 권장합니다:

### A 섹션
| 영어 | 한국어 | 첫 등장 챕터 | 비고 |
|------|--------|-------------|------|
| Allowlist | 허용 목록 | ch11 | NFT 민팅 사전 승인 목록 |
| Arweave | Arweave | ch11 | 영구 스토리지 블록체인 |

### C 섹션
| 영어 | 한국어 | 첫 등장 챕터 | 비고 |
|------|--------|-------------|------|
| CC0 | 크리에이티브 커먼즈 제로 | ch11 | Creative Commons Zero |
| Compressed NFT | 압축 NFT | ch11 | 상태 압축 기반 저비용 NFT |

### D 섹션
| 영어 | 한국어 | 첫 등장 챕터 | 비고 |
|------|--------|-------------|------|
| Dynamic NFT | 다이나믹 NFT | ch11 | 시간에 따라 변화하는 NFT |

### E 섹션
| 영어 | 한국어 | 첫 등장 챕터 | 비고 |
|------|--------|-------------|------|
| ERC-721 | ERC-721 | ch11 | 이더리움 NFT 표준 |
| ERC-1155 | ERC-1155 | ch11 | 이더리움 다중 토큰 표준 |
| ERC-2981 | ERC-2981 | ch11 | NFT 로열티 표준 |

### F 섹션
| 영어 | 한국어 | 첫 등장 챕터 | 비고 |
|------|--------|-------------|------|
| Floor Price | 바닥 가격 | ch11 | 컬렉션 최저가 |

### I 섹션
| 영어 | 한국어 | 첫 등장 챕터 | 비고 |
|------|--------|-------------|------|
| IPFS | 행성간 파일 시스템 | ch11 | InterPlanetary File System |

### M 섹션
| 영어 | 한국어 | 첫 등장 챕터 | 비고 |
|------|--------|-------------|------|
| Metadata | 메타데이터 | ch11 | NFT 속성 정보 |
| Minting | 민팅 | ch11 | NFT 생성 |

### N 섹션
| 영어 | 한국어 | 첫 등장 챕터 | 비고 |
|------|--------|-------------|------|
| NFT | 대체 불가능 토큰 | ch11 | Non-Fungible Token |

### R 섹션
| 영어 | 한국어 | 첫 등장 챕터 | 비고 |
|------|--------|-------------|------|
| Royalty | 로열티 | ch11 | NFT 2차 판매 수수료 |

### S 섹션
| 영어 | 한국어 | 첫 등장 챕터 | 비고 |
|------|--------|-------------|------|
| Soulbound Token (SBT) | 소울바운드 토큰 | ch11 | 전송 불가능한 신원 NFT |

### W 섹션
| 영어 | 한국어 | 첫 등장 챕터 | 비고 |
|------|--------|-------------|------|
| Wallet Drainer | 지갑 드레이너 | ch11 | 자산 탈취 악성 컨트랙트 |
