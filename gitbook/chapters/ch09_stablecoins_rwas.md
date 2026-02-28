# Chapter IX: Stablecoins and RWAs

=== "EN"

    The promise of cryptocurrency was always bigger than speculation, it was about rebuilding financial infrastructure from first principles. Nowhere is this transformation more visible than in the evolution of stablecoins and tokenized real-world assets. What began as experimental attempts to create "digital dollars" has matured into institutional-grade infrastructure handling trillions in annual volume and attracting Wall Street giants like BlackRock.

=== "KO"

    암호화폐의 약속은 항상 투기 그 이상이었다. 그것은 금융 인프라를 처음부터 다시 구축하는 것이었다. 이 변화가 가장 명확하게 나타나는 곳은 스테이블코인(Stablecoin)과 토큰화된 실물 자산(Real World Assets)의 진화다. "디지털 달러"를 만들려는 실험적 시도로 시작된 것이 이제는 연간 수조 달러의 거래량을 처리하고 BlackRock과 같은 월가 대기업의 관심을 끄는 기관급 인프라로 성숙했다.

## Section I: Types of Stablecoins

=== "EN"

    Stablecoins maintain their value through four distinct mechanisms, each offering different trade-offs between security, yield generation, and decentralization. The most established approach involves **fiat-backed stablecoins** (such as USDT and USDC), which maintain their **peg** by holding cash or cash equivalents such as treasuries and short-term government bonds in 1:1 proportion to circulating supply. Traditional fiat-backed stablecoins like USDT and USDC do not pass the interest they earn down to holders and instead keep it as revenue.

    A second category, crypto-backed stablecoins like USDS from Sky (examined in detail in Chapter VII), uses other cryptocurrencies as collateral. These systems typically require **overcollateralization** where crypto holdings exceed the stablecoin's value to account for inherent asset volatility. This approach trades capital efficiency for the benefit of remaining within the cryptocurrency ecosystem.

    More sophisticated synthetic stablecoins have emerged, exemplified by USDe from Ethena (discussed in Chapter VII's yield generation section). These maintain stability through automated hedging strategies using perpetual futures (detailed in Chapter VI) to offset the price movements of their underlying crypto assets. By holding crypto collateral while simultaneously taking short positions that profit when prices fall, these stablecoins neutralize volatility. They can also generate yield from funding rates, the periodic payments that flow between traders holding long and short positions in derivatives markets.

    A new type of stablecoins, sometimes called "yieldcoins" (such as USDY from Ondo), uses the same backing mechanism as fiat-backed stablecoins but passes earned interest to holders, effectively creating tokenized money market funds that combine blockchain accessibility with traditional fixed-income returns. The distinction here is business model, not the mechanism for maintaining the peg.

    Finally, **algorithmic stablecoins** represent perhaps the most ambitious but ultimately failed experiment in the space. These systems attempted to maintain stability through programmed mechanisms that automatically adjust token supply based on market demand, with no asset reserves. The fatal flaw emerged during confidence shocks: when users rushed to exit, the algorithms minted more of the backing token to maintain the peg, but this dilution crashed the backing token's value, further undermining confidence in the stablecoin and creating a reflexive death spiral where the stabilization mechanism itself accelerated collapse. While worth mentioning from a historical perspective, all major algorithmic stablecoins have failed, with the UST (Luna) collapse serving as the most prominent cautionary tale.

    The remainder of this chapter focuses primarily on fiat-backed stablecoins, which dominate the market with over 95% of total stablecoin circulation and have proven most viable for institutional adoption.

=== "KO"

    스테이블코인은 네 가지 뚜렷한 메커니즘을 통해 가치를 유지하며, 각각 보안, 수익 창출, 탈중앙화 간의 다양한 절충점을 제공한다. 가장 확립된 접근 방식은 **법정화폐 담보 스테이블코인(Fiat-backed Stablecoin)**(USDT, USDC 등)으로, 유통 공급량과 1:1 비율로 현금 또는 국채, 단기 정부채권과 같은 현금 등가물을 보유함으로써 **페그(Peg)**를 유지한다. USDT와 USDC 같은 전통적인 법정화폐 담보 스테이블코인은 자신들이 벌어들인 이자를 보유자에게 전달하지 않고 수익으로 보유한다.

    두 번째 범주인 암호화폐 담보 스테이블코인(Crypto-backed Stablecoin)은 Sky의 USDS(제7장에서 자세히 검토)와 같이 다른 암호화폐를 담보로 사용한다. 이러한 시스템은 일반적으로 **초과 담보(Overcollateralization)**를 요구하는데, 이는 내재적인 자산 변동성을 설명하기 위해 암호화폐 보유량이 스테이블코인의 가치를 초과해야 함을 의미한다. 이 접근 방식은 암호화폐 생태계 내에 머무르는 이점을 위해 자본 효율성을 희생한다.

    더 정교한 합성 스테이블코인(Synthetic Stablecoin)이 등장했는데, Ethena의 USDe(제7장의 수익 창출 섹션에서 논의)가 대표적이다. 이들은 기초 암호화폐 자산의 가격 변동을 상쇄하기 위해 무기한 선물(제6장에서 자세히 설명)을 사용하는 자동화된 헤지 전략을 통해 안정성을 유지한다. 암호화폐 담보를 보유하면서 동시에 가격 하락 시 수익을 내는 숏 포지션을 취함으로써, 이러한 스테이블코인은 변동성을 중화한다. 또한 파생상품 시장에서 롱 포지션과 숏 포지션을 보유한 트레이더 간에 주기적으로 이동하는 지불금인 펀딩 비율에서 수익을 창출할 수 있다.

    새로운 유형의 스테이블코인인, 때때로 "일드코인(Yieldcoin)"이라 불리는 것(Ondo의 USDY 등)은 법정화폐 담보 스테이블코인과 동일한 담보 메커니즘을 사용하지만 획득한 이자를 보유자에게 전달하여, 블록체인 접근성과 전통적인 고정 수익을 결합한 토큰화된 머니마켓 펀드를 효과적으로 만들어낸다. 여기서 차이점은 페그를 유지하는 메커니즘이 아닌 비즈니스 모델이다.

    마지막으로, **알고리즘 스테이블코인(Algorithmic Stablecoin)**은 아마도 이 분야에서 가장 야심 차지만 궁극적으로 실패한 실험을 대표한다. 이 시스템들은 자산 준비금 없이 시장 수요에 따라 자동으로 토큰 공급을 조정하는 프로그래밍된 메커니즘을 통해 안정성을 유지하려 했다. 치명적인 결함은 신뢰 충격 중에 드러났다: 사용자들이 급히 빠져나갈 때, 알고리즘은 페그를 유지하기 위해 더 많은 담보 토큰을 발행했지만, 이 희석은 담보 토큰의 가치를 폭락시켜 스테이블코인에 대한 신뢰를 더욱 약화시키고, 안정화 메커니즘 자체가 붕괴를 가속화하는 반사적 죽음의 나선을 만들어냈다. 역사적 관점에서 언급할 가치가 있지만, 모든 주요 알고리즘 스테이블코인은 실패했으며, UST(Luna) 붕괴가 가장 대표적인 경고 사례로 남아 있다.

    이 장의 나머지 부분은 주로 법정화폐 담보 스테이블코인에 초점을 맞추는데, 이는 총 스테이블코인 유통량의 95% 이상을 차지하며 기관 채택에 가장 적합한 것으로 입증되었기 때문이다.

## Section II: Fiat Stablecoins

=== "EN"

    The dominant stablecoin model emerged from brutal market selection. USDT and USDC, which currently have about a quarter of a trillion dollars in circulation, survived multiple crypto winters by embracing a simple truth: stability requires tangible assets, not algorithmic promises.

    These stablecoins maintain their peg through **arbitrage** mechanisms that create profit opportunities whenever price deviates from $1. When a stablecoin trades below $1, arbitrageurs buy the discounted tokens and redeem them from the issuer for exactly $1 worth of backing assets, pocketing the difference. Conversely, when price rises above $1, authorized participants can mint new tokens by depositing $1 of collateral with the issuer, then sell these tokens at a premium. This continuous arbitrage activity pulls the price back toward parity, but only if the underlying reserves and redemption mechanisms remain credible. Combined with strong reserve management, this mechanism has proven to be the winning formula for achieving both scale and institutional adoption.

=== "KO"

    지배적인 스테이블코인 모델은 가혹한 시장 선택에서 나타났다. 현재 약 2,500억 달러의 유통량을 가진 USDT와 USDC는 단순한 진실을 수용함으로써 여러 번의 크립토 윈터를 생존했다: 안정성은 알고리즘적 약속이 아닌 유형의 자산을 필요로 한다.

    이러한 스테이블코인은 가격이 1달러에서 벗어날 때마다 이익 기회를 창출하는 **차익거래(Arbitrage)** 메커니즘을 통해 페그를 유지한다. 스테이블코인이 1달러 아래에서 거래될 때, 차익거래자들은 할인된 토큰을 사들여 발행자로부터 정확히 1달러 상당의 담보 자산으로 상환하고 그 차이를 수익으로 챙긴다. 반대로 가격이 1달러 위로 오르면, 승인된 참여자들은 발행자에게 1달러의 담보를 예치하여 새 토큰을 발행한 후, 이 토큰을 프리미엄 가격에 판매할 수 있다. 이 지속적인 차익거래 활동이 가격을 등가로 끌어당기지만, 기초 준비금과 상환 메커니즘이 신뢰성을 유지해야만 한다. 강력한 준비금 관리와 결합되어, 이 메커니즘은 규모와 기관 채택 모두를 달성하기 위한 성공 공식으로 입증되었다.

### USDT

=== "EN"

    USDT is a stablecoin issued by Tether and the most widely adopted stablecoin globally, with $187 billion in circulation as of early 2026. Since its 2014 launch, Tether faced early challenges around transparency and banking relationships, but the company has since achieved much better compliance and publishes quarterly attestations, which are third-party verifications of its reserves conducted by accounting firm BDO Italia.

    Tether generates most of its revenue from yield earned on U.S. Treasury bills, reverse repos, and money market funds. This business model proved highly profitable in 2024, delivering $13 billion in net profit. The company has been reinvesting these profits into long-term growth areas including AI, renewable energy, and communications infrastructure. Tether also maintains approximately $10 billion each in Bitcoin and gold reserves on its balance sheet.

=== "KO"

    USDT는 Tether가 발행하는 스테이블코인으로, 2026년 초 기준 유통량 1,870억 달러로 전 세계적으로 가장 널리 채택된 스테이블코인이다. 2014년 출시 이후, Tether는 투명성과 은행 관계와 관련한 초기 도전에 직면했지만, 이후 회사는 훨씬 더 나은 규정 준수를 달성하고 회계 법인 BDO Italia가 수행하는 준비금에 대한 제3자 검증인 분기별 증명(Attestation)을 발행하고 있다.

    Tether는 대부분의 수익을 미국 재무부 채권, 역환매계약, 머니마켓 펀드에서 얻은 수익으로 생성한다. 이 비즈니스 모델은 2024년에 매우 수익성 있는 것으로 입증되어 130억 달러의 순이익을 달성했다. 회사는 이러한 이익을 AI, 재생에너지, 통신 인프라를 포함한 장기 성장 분야에 재투자하고 있다. Tether는 또한 대차대조표에 각각 약 100억 달러 상당의 비트코인과 금 준비금을 유지하고 있다.

### USDC

=== "EN"

    USDC is a stablecoin issued by Circle, a publicly traded company on the NYSE (CRCL). As the second most widely used stablecoin, USDC has $75 billion in circulation and Circle has established a strong reputation for transparency and regulatory compliance in the U.S.

    Circle maintains its reserves primarily in the BlackRock-managed Circle Reserve Fund, a government money market fund, along with cash holdings. The company has demonstrated its commitment to transparency by publishing monthly assurance reports conducted by Deloitte since 2022.

    Unlike Tether, Circle reported relatively modest profits of $156 million in 2024. This is partly explained by the revenue-sharing arrangement between Circle and Coinbase for USDC interest income: each platform retains 100% of the interest generated by USDC held on its own platform, while they split the interest from off-platform USDC holdings equally.

=== "KO"

    USDC는 NYSE(CRCL)에 상장된 상장 기업인 Circle이 발행하는 스테이블코인이다. 두 번째로 널리 사용되는 스테이블코인으로서, USDC는 750억 달러의 유통량을 보유하고 있으며 Circle은 미국에서 투명성과 규정 준수에 대한 강력한 평판을 구축했다.

    Circle은 BlackRock이 관리하는 Circle Reserve Fund(정부 머니마켓 펀드)와 현금 보유에 주로 준비금을 유지한다. 회사는 2022년 이후 Deloitte가 수행하는 월간 보증 보고서를 발행함으로써 투명성에 대한 약속을 보여주었다.

    Tether와 달리, Circle은 2024년에 1억 5,600만 달러의 상대적으로 적은 이익을 보고했다. 이는 부분적으로 USDC 이자 수익에 대한 Circle과 Coinbase 간의 수익 공유 약정으로 설명된다: 각 플랫폼은 자체 플랫폼에서 보유한 USDC에서 생성된 이자의 100%를 유지하고, 플랫폼 외부의 USDC 보유에서 생성된 이자는 균등하게 나눈다.

### PYUSD

=== "EN"

    PayPal USD (PYUSD) is a stablecoin issued in collaboration between PayPal and Paxos. PYUSD can be used on PayPal or Venmo, and it is issued on Ethereum, Solana, and Arbitrum. There are no fees for transactions within PayPal. PYUSD is much smaller than USDT and USDC and currently has $1.4 billion in circulation.

=== "KO"

    PayPal USD(PYUSD)는 PayPal과 Paxos 간의 협력으로 발행되는 스테이블코인이다. PYUSD는 PayPal이나 Venmo에서 사용할 수 있으며, 이더리움, 솔라나, Arbitrum에서 발행된다. PayPal 내의 거래에는 수수료가 없다. PYUSD는 USDT와 USDC보다 훨씬 작으며 현재 14억 달러의 유통량을 보유하고 있다.

### EUR Stablecoins

=== "EN"

    EUR stablecoins remain negligible compared to their USD counterparts, representing less than 1% of the total stablecoin market. The two largest EUR stablecoins are EURC (Circle) with approximately $220 million in circulation and EURS (Stasis) with around $120 million. This disparity stems from the U.S. dollar's global dominance in international trade and finance, which naturally extends to crypto where USD-denominated assets have broader acceptance across centralized exchanges, decentralized exchanges, and DeFi protocols. The EU's MiCA regulation, discussed below, has compounded this structural advantage by creating additional compliance barriers that deter both issuers and users.

=== "KO"

    EUR 스테이블코인은 USD에 비해 미미한 수준으로, 총 스테이블코인 시장의 1% 미만을 차지한다. 두 개의 가장 큰 EUR 스테이블코인은 약 2억 2,000만 달러 유통량의 EURC(Circle)와 약 1억 2,000만 달러의 EURS(Stasis)이다. 이러한 불균형은 국제 무역과 금융에서의 미국 달러의 글로벌 지배력에서 비롯되며, 이는 자연스럽게 USD 표시 자산이 중앙화 거래소, 탈중앙화 거래소, DeFi 프로토콜 전반에서 더 넓은 수용을 받는 암호화폐로 확장된다. 아래에서 논의되는 EU의 MiCA 규정은 발행자와 사용자 모두를 저해하는 추가적인 규정 준수 장벽을 만들어 이 구조적 우위를 강화했다.

### Regulations

=== "EN"

    While fiat-backed stablecoins are issued on permissionless blockchains, the assets themselves operate under existing financial regulations. They can be frozen if illegal activity is suspected, and Know Your Customer (KYC) protocols are required for both redemptions and new issuances. This hybrid model, combining blockchain efficiency with regulatory compliance, has enabled stablecoins to achieve both scale and institutional adoption while remaining subject to evolving regulatory frameworks across different jurisdictions.

=== "KO"

    법정화폐 담보 스테이블코인은 무허가 블록체인에서 발행되지만, 자산 자체는 기존 금융 규제 하에 운영된다. 불법 활동이 의심되면 동결될 수 있으며, 상환과 새로운 발행 모두에 대해 고객확인의무(Know Your Customer, KYC) 프로토콜이 필요하다. 블록체인 효율성과 규정 준수를 결합한 이 하이브리드 모델은 스테이블코인이 다양한 관할권의 진화하는 규제 프레임워크에 종속되면서 규모와 기관 채택 모두를 달성할 수 있게 했다.

#### United States

=== "EN"

    In the U.S., stablecoins are now governed by The GENIUS Act, which was signed into law in July 2025 and establishes a comprehensive regulatory framework for USD stablecoins. Only "permitted issuers" may issue stablecoins to U.S. people, specifically subsidiaries of insured banks, federally qualified issuers supervised by the Office of the Comptroller of the Currency, or state-qualified issuers (capped at $10 billion outstanding). Issuers must maintain strict 1:1 reserves in approved assets (USD cash, bank deposits, short-term Treasuries, and similar instruments), publish monthly reserve reports with independent accounting examinations, and comply with tailored Bank Secrecy Act and anti-money laundering obligations including customer identification and sanctions compliance.

    The law requires issuers to maintain technical capabilities to block or freeze tokens pursuant to lawful orders, prohibits paying interest on the stablecoins themselves, and bars marketing that implies U.S. government backing. Foreign-issued stablecoins are generally prohibited unless Treasury deems the home country's regulatory regime comparable and the issuer meets additional U.S. requirements. The framework becomes effective by January 18, 2027 (or 120 days after final regulations), with a three-year phase-out period after which U.S. digital asset service providers cannot offer non-compliant payment stablecoins. Importantly, compliant stablecoins are not classified as securities or commodities, and stablecoin holders receive priority claims on reserves in issuer insolvency proceedings.

    In September 2025, Tether announced the launch of USAT, a new U.S.-regulated stablecoin designed to comply with GENIUS Act. USAT will leverage Anchorage Digital as the federally regulated issuer and Cantor Fitzgerald as the reserve custodian.

=== "KO"

    미국에서 스테이블코인은 현재 2025년 7월 법률로 서명된 GENIUS Act에 의해 규제되며, USD 스테이블코인에 대한 포괄적인 규제 프레임워크를 수립한다. "허가된 발행자"만이 미국인에게 스테이블코인을 발행할 수 있는데, 구체적으로 예금보험에 가입된 은행의 자회사, 통화감독청이 감독하는 연방 자격 발행자, 또는 주 자격 발행자(미결제 잔액 100억 달러 상한)이다. 발행자는 승인된 자산(USD 현금, 은행 예금, 단기 재무부 채권 및 유사 상품)에서 엄격한 1:1 준비금을 유지하고, 독립적인 회계 심사와 함께 월간 준비금 보고서를 발행하며, 고객 식별 및 제재 준수를 포함한 맞춤형 은행비밀법 및 자금세탁방지 의무를 준수해야 한다.

    법률은 발행자가 합법적 명령에 따라 토큰을 차단하거나 동결하는 기술적 능력을 유지하도록 요구하고, 스테이블코인 자체에 대한 이자 지급을 금지하며, 미국 정부 보증을 암시하는 마케팅을 금지한다. 외국 발행 스테이블코인은 재무부가 본국의 규제 체제가 비교 가능하다고 판단하고 발행자가 추가적인 미국 요건을 충족하지 않는 한 일반적으로 금지된다. 프레임워크는 2027년 1월 18일(또는 최종 규정 이후 120일)까지 발효되며, 이후 3년간의 단계적 폐지 기간이 있으며 그 이후에는 미국 디지털 자산 서비스 제공자가 비준수 결제 스테이블코인을 제공할 수 없다. 중요하게도, 준수 스테이블코인은 증권 또는 상품으로 분류되지 않으며, 스테이블코인 보유자는 발행자 지급 불능 시 준비금에 대한 우선권을 받는다.

    2025년 9월, Tether는 GENIUS Act에 준수하도록 설계된 새로운 미국 규제 스테이블코인 USAT의 출시를 발표했다. USAT는 Anchorage Digital을 연방 규제 발행자로, Cantor Fitzgerald를 준비금 수탁자로 활용할 것이다.

#### European Union

=== "EN"

    Under the EU Markets in Crypto-Assets (MiCA) regulation, single-currency stablecoins are classified as e-money tokens (EMT) and subject to stringent reserve requirements designed to ensure liquidity and systemic stability. Standard EMT issuers must hold at least 30% of their reserves as deposits with EU-authorized credit institutions, with the remainder in high-quality liquid assets. However, "significant" tokens, those with higher systemic risk and potential monetary policy impact, face elevated requirements, including a 60% deposit floor and enhanced supervision by the European Banking Authority. This tiered approach reflects regulators' concern about redemption runs and contagion effects from larger stablecoin operations.

    The framework also incorporates operational safeguards and concentration limits to prevent over-reliance on single institutions. Issuers must distribute deposits across multiple EU banks (often requiring six or more banking partners for significant EMTs), maintain formal liquidity management policies, conduct regular stress testing, and keep reserves segregated with detailed reporting to supervisors. Notably, while euro-denominated EMTs face no usage restrictions, non-EUR stablecoins are subject to means-of-exchange caps, if their daily transaction volume exceeds 1 million transactions or €200 million in any EU currency area, issuers must halt new issuance until compliance is restored. This regulatory architecture effectively anchors stablecoin liquidity to the EU banking system while maintaining supervisory control and limiting systemic exposure.

    Circle achieved full MiCA compliance in July 2024 through a French Electronic Money Institution license, allowing both USDC and EURC to operate in the EU. Circle chose to comply to gain mainstream acceptance and regulatory clarity. Despite complying, Circle has also critiqued certain MiCA reserve requirements, particularly high bank deposit mandates, as introducing unnecessary bank risk, showing Circle supports the framework's clarity and market access while advocating for refinements to specific prudential details.

    Tether chose not to comply with MiCA and exchanges had to delist or restrict USDT in the EU. The company said that it wouldn't comply primarily because the requirements for stablecoins to hold at least 60% of reserves in EU bank deposits creates "systemic risk" and makes both stablecoins and banks less safe than holding short-term U.S. Treasuries. Tether believes that bank deposits are inherently more fragile since banks re-lend them (citing the SVB/USDC incident as evidence), while Treasuries offer superior safety and liquidity as reserve assets. Additionally, Tether views MiCA's bank concentration limits and operational requirements as adding unnecessary complexity and risk, while the broader EU restrictions on non-euro stablecoin usage are seen as hostile to dollar-denominated stablecoins' everyday use in Europe.

=== "KO"

    EU 암호자산시장규제법(Markets in Crypto-Assets, MiCA) 하에서, 단일 통화 스테이블코인은 전자화폐 토큰(e-money token, EMT)으로 분류되며 유동성과 시스템적 안정성을 보장하기 위해 설계된 엄격한 준비금 요건의 대상이 된다. 표준 EMT 발행자는 준비금의 최소 30%를 EU 인가 신용기관에 예금으로 보유해야 하며, 나머지는 고품질 유동자산으로 보유해야 한다. 그러나 "중요한" 토큰, 즉 더 높은 시스템적 위험과 잠재적 통화 정책 영향을 가진 토큰은 60% 예금 하한과 유럽은행감독청(European Banking Authority)의 강화된 감독을 포함한 높은 요건에 직면한다. 이 계층적 접근 방식은 대규모 스테이블코인 운영에서의 상환 쇄도와 전염 효과에 대한 규제 기관의 우려를 반영한다.

    프레임워크는 또한 단일 기관에 대한 과도한 의존을 방지하기 위한 운영 안전장치와 집중 한도를 포함한다. 발행자는 여러 EU 은행에 예금을 분산해야 하며(중요한 EMT의 경우 종종 6개 이상의 은행 파트너 필요), 공식적인 유동성 관리 정책을 유지하고, 정기적인 스트레스 테스트를 수행하며, 준비금을 분리하여 감독자에게 상세한 보고를 유지해야 한다. 특히 유로화 표시 EMT는 사용 제한이 없지만, 비EUR 스테이블코인은 교환 수단 제한을 받는다. 일일 거래량이 EU 통화권에서 100만 건의 거래 또는 2억 유로를 초과하면, 발행자는 준수가 회복될 때까지 새로운 발행을 중단해야 한다. 이 규제 구조는 스테이블코인 유동성을 EU 은행 시스템에 고정하면서 감독 통제를 유지하고 시스템적 노출을 제한한다.

    Circle은 2024년 7월 프랑스 전자화폐 기관 라이선스를 통해 완전한 MiCA 준수를 달성하여 USDC와 EURC 모두 EU에서 운영될 수 있게 했다. Circle은 주류 수용과 규제 명확성을 얻기 위해 준수하기로 선택했다. 준수하면서도, Circle은 특정 MiCA 준비금 요건, 특히 높은 은행 예금 의무가 불필요한 은행 리스크를 도입한다고 비판하며, Circle이 프레임워크의 명확성과 시장 접근을 지지하면서 특정 건전성 세부 사항에 대한 개선을 옹호하고 있음을 보여주었다.

    Tether는 MiCA에 준수하지 않기로 선택했고 거래소들은 EU에서 USDT를 상장 폐지하거나 제한해야 했다. 회사는 스테이블코인이 준비금의 최소 60%를 EU 은행 예금으로 보유해야 한다는 요건이 "시스템적 위험"을 만들고 단기 미국 재무부 채권을 보유하는 것보다 스테이블코인과 은행 모두를 덜 안전하게 만든다는 이유로 주로 준수하지 않겠다고 말했다. Tether는 은행 예금이 은행이 재대출하기 때문에 본질적으로 더 취약하다고 믿으며(SVB/USDC 사건을 증거로 인용), 재무부 채권이 준비금 자산으로서 우수한 안전성과 유동성을 제공한다고 본다. 추가로, Tether는 MiCA의 은행 집중 한도와 운영 요건이 불필요한 복잡성과 위험을 추가한다고 보며, 비유로 스테이블코인 사용에 대한 더 넓은 EU 제한은 유럽에서 달러 표시 스테이블코인의 일상적 사용에 적대적인 것으로 본다.

### De-pegging risks

=== "EN"

    Despite their robust stabilization mechanisms, fiat-backed stablecoins still face de-pegging risk, the failure to maintain 1:1 parity with the underlying asset. This risk is fundamentally tied to reserve-confidence shocks, where doubts about reserve quality or accessibility can trigger a crisis of confidence. When users lose faith in a stablecoin's backing, they rush to sell their holdings for BTC, ETH, or fiat currencies, creating intense selling pressure that pushes the token's market price below $1 until redemptions and arbitrage activities restore parity.

    The March 2023 U.S. banking crisis (also discussed in Chapter VII's Curve section) provided a clear example of this dynamic. After Circle disclosed that approximately $3.3 billion of USDC's cash reserves was held at the failing Silicon Valley Bank, the stablecoin fell as low as $0.87 on March 11, 2023. This episode demonstrated how interconnected stablecoins are with legacy banking infrastructure and how external banking issues can directly impact stablecoin stability. The price recovered after the joint Treasury/Fed/FDIC statement on March 12, 2023 backstopped deposits and Circle resumed redemptions on March 13.

    USDT experienced its most severe de-pegging crisis in October 2018 with intraday lows as low as $0.86 amid a perfect storm of banking and confidence issues. The crisis was precipitated by reports that Noble Bank, a key banking partner that had serviced Tether and Bitfinex in Puerto Rico, was seeking a buyer and had lost clients, with both Tether and Bitfinex reportedly looking elsewhere for banking support.

    These episodes illustrate how banking infrastructure problems create feedback loops. Concerns about redemption capacity can fuel panic selling, effectively creating digital bank runs. These crises only resolve once normal banking relationships and redemption processes are restored. The interconnected nature of stablecoin reserves with incumbent banking systems means that external financial sector stress can directly threaten the stability mechanisms these tokens rely upon.

=== "KO"

    강력한 안정화 메커니즘에도 불구하고, 법정화폐 담보 스테이블코인은 여전히 디페깅 위험(De-pegging Risk), 즉 기초 자산과의 1:1 등가를 유지하지 못하는 실패에 직면한다. 이 위험은 근본적으로 준비금-신뢰 충격과 연결되어 있으며, 준비금 품질이나 접근성에 대한 의심이 신뢰 위기를 촉발할 수 있다. 사용자들이 스테이블코인의 담보에 대한 믿음을 잃으면, 그들은 보유량을 BTC, ETH 또는 법정화폐로 급히 판매하여 상환과 차익거래 활동이 등가를 회복할 때까지 토큰의 시장 가격을 1달러 아래로 밀어내는 강렬한 매도 압력을 만든다.

    2023년 3월 미국 은행 위기(제7장 Curve 섹션에서도 논의됨)는 이 역학의 명확한 예를 제공했다. Circle이 USDC 현금 준비금의 약 33억 달러가 파산한 Silicon Valley Bank에 예치되어 있다고 공개한 후, 스테이블코인은 2023년 3월 11일 최저 0.87달러까지 떨어졌다. 이 사건은 스테이블코인이 레거시 은행 인프라와 얼마나 밀접하게 연결되어 있는지, 그리고 외부 은행 문제가 스테이블코인 안정성에 직접적으로 영향을 미칠 수 있는지를 보여주었다. 가격은 2023년 3월 12일 재무부/연준/FDIC의 공동 성명이 예금을 보장하고 Circle이 3월 13일 상환을 재개한 후 회복되었다.

    USDT는 2018년 10월 은행 및 신뢰 문제의 완벽한 폭풍 속에서 장중 최저 0.86달러까지 떨어지는 가장 심각한 디페깅 위기를 경험했다. 위기는 푸에르토리코에서 Tether와 Bitfinex를 서비스하던 주요 은행 파트너인 Noble Bank가 매수자를 찾고 있고 고객을 잃었다는 보도, 그리고 Tether와 Bitfinex 모두 다른 곳에서 은행 지원을 찾고 있다는 보도에 의해 촉발되었다.

    이러한 사건들은 은행 인프라 문제가 어떻게 피드백 루프를 만드는지를 보여준다. 상환 능력에 대한 우려는 패닉 매도를 부추길 수 있으며, 효과적으로 디지털 뱅크런을 만든다. 이러한 위기는 정상적인 은행 관계와 상환 프로세스가 회복되어야만 해결된다. 스테이블코인 준비금이 기존 은행 시스템과 상호 연결된 특성은 외부 금융 부문 스트레스가 이 토큰들이 의존하는 안정화 메커니즘을 직접적으로 위협할 수 있음을 의미한다.

### Use Cases

=== "EN"

    Stablecoins have become core crypto plumbing, accounting for more than 50% of global crypto transaction value each year. Visa estimates approximately $5.7 trillion in stablecoin settlement volume in 2024, after adjusting for artificial volume from bots and fake trades designed to inflate activity metrics. This massive scale demonstrates that stablecoins have evolved far beyond their origins as trading instruments to become genuine payment and transfer infrastructure. They have proven especially valuable in regions where legacy financial systems are inadequate, restricted, or unreliable.

=== "KO"

    스테이블코인은 핵심 암호화폐 배관이 되어, 매년 글로벌 암호화폐 거래 가치의 50% 이상을 차지한다. Visa는 봇과 활동 지표를 부풀리기 위해 설계된 가짜 거래로 인한 인위적 거래량을 조정한 후 2024년 스테이블코인 결제량을 약 5조 7천억 달러로 추정한다. 이 대규모 규모는 스테이블코인이 거래 수단으로서의 기원을 넘어 진정한 결제 및 송금 인프라가 되었음을 보여준다. 스테이블코인은 레거시 금융 시스템이 부적절하거나, 제한되거나, 신뢰할 수 없는 지역에서 특히 가치가 있는 것으로 입증되었다.

#### Trading and Arbitrage

=== "EN"

    Trading and arbitrage remain the dominant applications, with arbitrage activity highly concentrated among a small set of professional firms. Market makers maintain capital reserves in USDT and USDC, positioning themselves to quickly capitalize on price differences across centralized exchanges, decentralized exchanges, and different geographic regions.

=== "KO"

    트레이딩과 차익거래는 여전히 지배적인 응용 분야로 남아 있으며, 차익거래 활동은 소수의 전문 회사에 고도로 집중되어 있다. 시장 조성자들은 USDT와 USDC로 자본 준비금을 유지하며, 중앙화 거래소, 탈중앙화 거래소, 다양한 지리적 지역 간의 가격 차이를 신속하게 활용할 수 있는 위치에 있다.

#### Cross-Border Payments and Remittances

=== "EN"

    Beyond trading, cross-border payments and remittances represent one of stablecoins' most transformative applications. The cost advantages are substantial: sending a $200 remittance from Sub-Saharan Africa costs approximately 60% less using stablecoins compared to traditional fiat-based methods. This dramatic cost reduction makes stablecoins attractive to migrant workers and underbanked populations. Strong adoption has followed in Latin America and Sub-Saharan Africa, where stablecoins provide both a hedge against local currency volatility and practical access to USD-denominated value. Geographic adoption data shows these regions experiencing over 40% year-over-year growth in retail and professional-sized stablecoin transfers.

=== "KO"

    트레이딩 외에도, 국경 간 결제와 송금은 스테이블코인의 가장 변혁적인 응용 중 하나를 대표한다. 비용 이점은 상당하다: 사하라 이남 아프리카에서 200달러 송금을 보내는 비용은 스테이블코인을 사용하면 전통적인 법정화폐 기반 방법에 비해 약 60% 더 저렴하다. 이 극적인 비용 절감은 스테이블코인을 이주 노동자와 은행 서비스 미접근 인구에게 매력적으로 만든다. 라틴 아메리카와 사하라 이남 아프리카에서 강력한 채택이 이어졌으며, 여기서 스테이블코인은 현지 통화 변동성에 대한 헤지와 USD 표시 가치에 대한 실질적인 접근을 모두 제공한다. 지리적 채택 데이터는 이 지역에서 소매 및 전문 규모의 스테이블코인 송금이 연간 40% 이상 성장하고 있음을 보여준다.

#### Store of Value in High-Inflation Regions

=== "EN"

    Stablecoins also serve as a critical store of value in regions facing economic instability or high inflation. They allow individuals and businesses to preserve purchasing power when local currencies become unreliable. This use case has proven especially significant in countries experiencing monetary instability, where stablecoins often trade at premiums reflecting users' willingness to pay for stability and faster money movement. Turkey leads the world in stablecoin trading volume as a percentage of GDP. Meanwhile, countries across the Middle East and North Africa are seeing stablecoins capture larger market shares than traditionally dominant cryptocurrencies like Bitcoin and Ethereum.

=== "KO"

    스테이블코인은 또한 경제 불안정이나 높은 인플레이션에 직면한 지역에서 중요한 가치 저장 수단으로 기능한다. 스테이블코인은 현지 통화가 신뢰할 수 없게 될 때 개인과 기업이 구매력을 보존할 수 있게 한다. 이 사용 사례는 통화 불안정을 경험하는 국가에서 특히 중요한 것으로 입증되었으며, 스테이블코인은 종종 안정성과 더 빠른 자금 이동에 대해 지불하려는 사용자의 의지를 반영하는 프리미엄에 거래된다. 터키는 GDP 대비 스테이블코인 거래량에서 세계를 선도한다. 한편 중동과 북아프리카 전역의 국가들은 스테이블코인이 비트코인과 이더리움과 같은 전통적으로 지배적인 암호화폐보다 더 큰 시장 점유율을 차지하는 것을 보고 있다.

#### Institutional Adoption

=== "EN"

    The institutional adoption of stablecoins has reached new heights. Banks and financial institutions increasingly integrate them into operations for liquidity management, settlement mechanisms, and as entry points into cryptocurrency markets. Major payment processors including Stripe, Mastercard, and Visa have launched products enabling users to spend stablecoins through conventional payment rails. This infrastructure has enabled cross-border investment applications through tokenized assets. Investors now swap into stablecoins to access tokenized U.S. Treasury funds like Franklin's BENJI, BlackRock's BUIDL, and Ondo's OUSG, enabling 24/7 settlement capabilities. (These tokenized treasuries are discussed in more detail in Section II of this chapter.)

=== "KO"

    스테이블코인의 기관 채택은 새로운 고점에 도달했다. 은행과 금융 기관은 유동성 관리, 결제 메커니즘, 암호화폐 시장 진입점으로 점점 더 스테이블코인을 운영에 통합하고 있다. Stripe, Mastercard, Visa를 포함한 주요 결제 처리업체는 사용자가 기존 결제 레일을 통해 스테이블코인을 사용할 수 있도록 하는 제품을 출시했다. 이 인프라는 토큰화된 자산을 통한 국경 간 투자 응용을 가능하게 했다. 투자자들은 이제 스테이블코인으로 교환하여 Franklin의 BENJI, BlackRock의 BUIDL, Ondo의 OUSG와 같은 토큰화된 미국 재무부 펀드에 접근하여 연중무휴 결제 기능을 가능하게 한다. (이러한 토큰화된 재무부 채권은 이 장의 제2절에서 더 자세히 논의된다.)

#### Looking Forward

=== "EN"

    While trading and arbitrage continue to dominate global stablecoin flows, the infrastructure is expanding into broader economic applications. The significant growth in retail usage across high-inflation economies, combined with emerging institutional applications through tokenized assets, signals an important shift. Stablecoins are transitioning from primarily serving sophisticated financial players toward becoming genuine alternatives to incumbent banking systems, especially in regions where legacy infrastructure fails to meet local needs.

=== "KO"

    트레이딩과 차익거래가 글로벌 스테이블코인 흐름을 계속 지배하지만, 인프라는 더 넓은 경제적 응용으로 확장되고 있다. 고인플레이션 경제에서의 상당한 소매 사용 증가와 토큰화된 자산을 통한 새로운 기관 응용의 결합은 중요한 변화를 시사한다. 스테이블코인은 주로 정교한 금융 플레이어를 위한 서비스에서 기존 은행 시스템에 대한 진정한 대안으로 전환하고 있으며, 특히 레거시 인프라가 현지 필요를 충족하지 못하는 지역에서 그러하다.

## Section III: Real World Assets

=== "EN"

    While stablecoins proved that blockchains could handle money, Real World Asset (RWA) **tokenization** represents the next step: moving conventional financial assets on-chain to provide greater efficiency, transparency, and global accessibility than off-chain rails.

    The shift is already underway. Incumbent financial giants like BlackRock, Franklin Templeton, and JPMorgan have launched tokenized products that now handle billions in assets and daily volumes. JPMorgan's Kinexys platform processes daily volumes exceeding $2 billion, powering short-term collateralized lending between institutions and tokenized settlement processes. What began as crypto-native experiments has now attracted the world's largest asset managers.

    RWA tokenization spans the full spectrum of established markets, ranging from U.S. Treasury bills to complex private credit arrangements, with real estate, stocks, and commodities bridging the gap between these extremes.

    The tokenization process requires four critical components that work together to create a functional system. The legal structure forms the foundation through legal wrappers, typically **Special Purpose Vehicles (SPVs)** or trusts, that hold the underlying assets while protecting them from bankruptcy risks. On-chain management utilizes smart contracts to manage ownership records and handle distributions automatically, replacing traditional back-office processes. Data bridges play a crucial role as oracles (the verification infrastructure detailed in Chapter VII) bring real-world asset prices and performance data into blockchain systems. Finally, regulatory compliance infrastructure enforces regulatory requirements while preserving the programmable nature of blockchain transactions.

    Additionally, U.S. registered investment funds must maintain a dedicated transfer agent. This agent keeps official shareholder records and processes all distributions and redemptions according to regulatory standards.

    As of early 2026, approximately $21 billion worth of RWAs (excluding stablecoins) have been issued on-chain, with participation from more than 200 different issuers. The market breakdown shows about $9 billion in U.S. Treasury Debt, $4 billion in commodities and another $2.5 billion in private credit. The majority of these RWAs are issued on Ethereum.

=== "KO"

    스테이블코인이 블록체인이 화폐를 처리할 수 있다는 것을 증명했다면, 실물 자산(Real World Asset, RWA) **토큰화(Tokenization)**는 다음 단계를 대표한다: 오프체인 레일보다 더 큰 효율성, 투명성, 글로벌 접근성을 제공하기 위해 전통적인 금융 자산을 온체인으로 이동하는 것이다.

    이 변화는 이미 진행 중이다. BlackRock, Franklin Templeton, JPMorgan과 같은 기존 금융 대기업들이 이제 수십억 달러의 자산과 일일 거래량을 처리하는 토큰화된 제품을 출시했다. JPMorgan의 Kinexys 플랫폼은 20억 달러를 초과하는 일일 거래량을 처리하며, 기관 간 단기 담보 대출과 토큰화된 결제 프로세스를 지원한다. 암호화폐 네이티브 실험으로 시작된 것이 이제 세계 최대 자산 운용사들을 끌어들이고 있다.

    RWA 토큰화는 미국 재무부 채권에서 복잡한 사모 신용 거래에 이르기까지 기존 시장의 전체 스펙트럼에 걸쳐 있으며, 부동산, 주식, 상품이 이 양극단 사이의 간격을 메운다.

    토큰화 프로세스에는 함께 작동하여 기능적 시스템을 만드는 네 가지 중요한 구성 요소가 필요하다. 법적 구조는 파산 위험으로부터 자산을 보호하면서 기초 자산을 보유하는 법적 래퍼, 일반적으로 **특수목적회사(Special Purpose Vehicle, SPV)** 또는 신탁을 통해 기반을 형성한다. 온체인 관리는 스마트 컨트랙트를 사용하여 소유권 기록을 관리하고 분배를 자동으로 처리하여 전통적인 백오피스 프로세스를 대체한다. 데이터 브릿지는 오라클(제7장에서 자세히 설명된 검증 인프라)이 실세계 자산 가격과 성과 데이터를 블록체인 시스템으로 가져오는 중요한 역할을 한다. 마지막으로, 규제 준수 인프라는 블록체인 거래의 프로그래머블 특성을 유지하면서 규제 요건을 시행한다.

    추가로, 미국 등록 투자 펀드는 전담 양도 대리인(Transfer Agent)을 유지해야 한다. 이 대리인은 공식 주주 기록을 유지하고 규제 기준에 따라 모든 분배와 상환을 처리한다.

    2026년 초 기준, 약 210억 달러 상당의 RWA(스테이블코인 제외)가 온체인에서 발행되었으며, 200개 이상의 다양한 발행자가 참여하고 있다. 시장 분석에 따르면 미국 재무부 채무에 약 90억 달러, 상품에 40억 달러, 사모 신용에 25억 달러가 있다. 이러한 RWA의 대부분은 이더리움에서 발행된다.

### Regulatory Framework

=== "EN"

    RWA tokenization operates at the complex intersection of securities law and digital assets. Most RWA tokens qualify as securities under U.S. law, but rather than pursue expensive public registrations, protocols use regulatory workarounds that enable innovation while limiting mainstream adoption.

    The most common approach is Regulation D private placements (limited to accredited investors) or Regulation S offshore offerings (excluding U.S. persons). This regulatory arbitrage creates both opportunities and constraints that shape how protocols operate in practice.

    Most protocols implement compliance as code: a comprehensive infrastructure stack that embeds regulatory requirements across multiple layers rather than relying on manual oversight. This multi-layered compliance architecture represents the invisible regulatory plumbing that makes tokenization legally viable while attempting to preserve programmability.

    At the token level, standardized smart contract frameworks encode transfer restrictions and compliance checks directly into the tokens themselves. These tokens can programmatically enforce whitelisting (only approved addresses), lock-up periods, and accredited investor requirements. At the platform level, services like Securitize provide the operational infrastructure, handling KYC/AML verification, investor accreditation, ongoing regulatory reporting, and automatic transaction monitoring. Increasingly, compliance portability operates at the wallet level through verifiable credentials and attestations, enabling investors to reuse KYC/AML proofs across venues without fragmenting liquidity.

=== "KO"

    RWA 토큰화는 증권법과 디지털 자산의 복잡한 교차점에서 운영된다. 대부분의 RWA 토큰은 미국 법률상 증권으로 자격이 부여되지만, 비용이 많이 드는 공개 등록을 추구하기보다 프로토콜은 혁신을 가능하게 하면서 주류 채택을 제한하는 규제적 우회책을 사용한다.

    가장 일반적인 접근 방식은 Regulation D 사모발행(적격 투자자에게 제한) 또는 Regulation S 역외 공모(미국인 제외)이다. 이 규제 차익거래는 프로토콜이 실제로 운영되는 방식을 형성하는 기회와 제약 모두를 만들어낸다.

    대부분의 프로토콜은 수동적 감독에 의존하기보다 여러 레이어에 걸쳐 규제 요건을 내장하는 포괄적인 인프라 스택인 코드로서의 규정 준수를 구현한다. 이 다층 규정 준수 아키텍처는 프로그래머빌리티를 유지하려고 시도하면서 토큰화를 법적으로 실행 가능하게 만드는 보이지 않는 규제 배관을 나타낸다.

    토큰 수준에서, 표준화된 스마트 컨트랙트 프레임워크는 이전 제한과 규정 준수 검사를 토큰 자체에 직접 인코딩한다. 이러한 토큰은 화이트리스팅(승인된 주소만), 락업 기간, 적격 투자자 요건을 프로그래밍 방식으로 시행할 수 있다. 플랫폼 수준에서, Securitize와 같은 서비스는 운영 인프라를 제공하며, KYC/AML 검증, 투자자 자격 인증, 지속적인 규제 보고, 자동 거래 모니터링을 처리한다. 점점 더 규정 준수 이식성은 검증 가능한 자격 증명과 증명(Attestation)을 통해 지갑 수준에서 작동하여, 투자자가 유동성을 분산시키지 않고 여러 장소에서 KYC/AML 증명을 재사용할 수 있게 한다.

### Treasury and Fixed Income

=== "EN"

    Tokenized Treasuries became RWA's first major success story because they solve a clear problem: DeFi protocols needed high-quality, yield-bearing collateral that wasn't subject to crypto volatility. U.S. Treasury bills offer the perfect combination of safety, liquidity, and yield, but legacy financial systems made them difficult to access programmatically.

    BlackRock's BUIDL fund represents a watershed moment: the world's largest asset manager offering a tokenized money market fund that accrues income daily and pays distributions in-kind as additional BUIDL tokens. The fund surpassed $2 billion in assets under management by April 2025, demonstrating institutional demand for tokenized Treasury exposure. Franklin Templeton's FOBXX went further, becoming the first U.S.-registered mutual fund to record transactions and share ownership on a public blockchain rather than just tokenizing claims.

    The mechanics vary but follow similar patterns. Some protocols use daily net asset value updates with redemption windows, while others employ continuous pricing through authorized market makers. Ondo Finance pioneered widely-used tokenized Treasuries (OUSG for institutional investors meeting high net worth thresholds) and yield-bearing cash equivalents (USDY/rUSDY for broader access), bridging institutional and retail markets with around-the-clock on- and off-ramping capabilities.

    Other notable issuers/operators include Superstate (tokenized short-term government funds), Backed (tokenized ETFs and bonds), and Hashnote.

    Because RWA tokens are programmable, they can be reused across DeFi protocols, posted as collateral while still earning underlying yield. New institutional venues like Aave Horizon allow qualified users to borrow against tokenized Treasuries and other debt instruments, improving capital efficiency compared to traditional finance workflows.

    Corporate bonds and private credit represent the next frontier for fixed income tokenization. Platforms like Centrifuge and Maple Finance facilitate on-chain lending to real-world borrowers, but must navigate complex credit assessment, legal documentation, and default resolution processes. The challenge isn't technical but rather operational, requiring traditional finance expertise alongside blockchain integration.

=== "KO"

    토큰화된 재무부 채권은 RWA의 첫 번째 주요 성공 사례가 되었는데, 이는 명확한 문제를 해결하기 때문이다: DeFi 프로토콜은 암호화폐 변동성의 영향을 받지 않는 고품질 수익 창출 담보를 필요로 했다. 미국 재무부 채권은 안전성, 유동성, 수익의 완벽한 조합을 제공하지만, 레거시 금융 시스템은 프로그래밍 방식으로 접근하기 어렵게 만들었다.

    BlackRock의 BUIDL 펀드는 획기적인 순간을 대표한다: 세계 최대 자산 운용사가 매일 수익이 발생하고 추가 BUIDL 토큰으로 현물 분배를 지급하는 토큰화된 머니마켓 펀드를 제공한 것이다. 펀드는 2025년 4월까지 운용 자산 20억 달러를 넘어서며 토큰화된 재무부 채권 노출에 대한 기관 수요를 보여주었다. Franklin Templeton의 FOBXX는 더 나아가 단순히 청구권을 토큰화하는 것이 아니라 거래와 주식 소유권을 공개 블록체인에 기록하는 미국 최초의 등록 뮤추얼 펀드가 되었다.

    메커니즘은 다양하지만 유사한 패턴을 따른다. 일부 프로토콜은 상환 창구와 함께 일일 순자산 가치 업데이트를 사용하고, 다른 프로토콜은 승인된 시장 조성자를 통한 연속 가격 책정을 사용한다. Ondo Finance는 널리 사용되는 토큰화된 재무부 채권(고액 자산 기준을 충족하는 기관 투자자를 위한 OUSG)과 수익 창출 현금 등가물(더 넓은 접근을 위한 USDY/rUSDY)을 개척하여, 연중무휴 온/오프램핑 기능으로 기관과 소매 시장을 연결했다.

    다른 주목할 만한 발행자/운영자로는 Superstate(토큰화된 단기 정부 펀드), Backed(토큰화된 ETF와 채권), Hashnote가 있다.

    RWA 토큰이 프로그래머블하기 때문에, 기초 수익을 계속 얻으면서 담보로 게시되어 DeFi 프로토콜 전반에서 재사용될 수 있다. Aave Horizon과 같은 새로운 기관 장소는 자격을 갖춘 사용자가 토큰화된 재무부 채권 및 기타 채무 상품에 대해 대출받을 수 있게 하여, 전통 금융 워크플로우에 비해 자본 효율성을 개선한다.

    회사채와 사모 신용은 고정 수익 토큰화의 다음 개척지를 대표한다. Centrifuge와 Maple Finance와 같은 플랫폼은 실물 차입자에 대한 온체인 대출을 촉진하지만, 복잡한 신용 평가, 법적 문서화, 부도 해결 프로세스를 탐색해야 한다. 과제는 기술적인 것이 아니라 운영적인 것으로, 블록체인 통합과 함께 전통 금융 전문성을 필요로 한다.

### Tokenized Stocks

=== "EN"

    While fixed income tokenization focuses on debt instruments, equity markets represent another major category of conventional assets moving on-chain. The technical implementation, however, varies dramatically depending on how issuers bridge the gap between blockchain records and traditional securities infrastructure.

    Tokenized stocks and ETFs are emerging through three distinct architectural approaches. The key distinction lies in whether the token represents a claim on shares held by someone else, or whether the token itself is the actual security. Each approach offers different trade-offs between ease of implementation, regulatory complexity, and integration with existing markets.

    The first model, wrapper tokenization (issuer- or SPV-backed), operates similarly to fiat-backed stablecoins but for equities. A non-broker issuer acquires a basket of underlying securities, such as 100 stocks or an ETF, and issues tokens representing claims on the pooled assets. These tokens are economically linked to the underlying securities but are not the same security themselves. Investors redeem tokens with the issuer rather than holding native shares at a brokerage. This structure typically relies on Reg D/Reg S or other jurisdictional exemptions and includes transfer restrictions and whitelisting. Operators like Backed and WisdomTree use this approach, offering on-chain claims on traditional funds. The advantage is speed to market, but the limitation is clear: tokens exist as claims on the wrapper entity rather than direct ownership of the underlying security.

    The second approach, wrapper via broker-dealer (brokerage receipts), places a regulated broker-dealer or custody platform at the center of the architecture. The broker maintains the canonical brokerage record and issues on-chain receipts representing customers' brokerage balances. These tokens function as transferable claims inside the broker's ledger, typically limited to eligible, often non-U.S., users and whitelisted wallets. Settlement and finality depend on the broker's books, with the on-chain balance mapping to the broker's internal account structure. Think brokerage-led programs where investors can move balances on-chain, but the underlying asset remains a brokerage entitlement, not a standalone, depositable share. This model inherits broker protections and regulatory infrastructure but constrains composability to the broker's ecosystem.

    The third and most ambitious model, canonical tokenization, attempts to make the on-chain instrument the same security as the off-chain share. The token carries the same official security identifier as traditional shares, requiring coordination with the issuer, transfer agent, and market infrastructure. Investors can theoretically bridge positions between their brokerage account and an on-chain wallet, with the transfer agent maintaining authoritative records across both environments. Superstate exemplifies this approach, pursuing true security tokenization rather than wrapper claims. This model leverages standardized compliance-focused token frameworks and transfer-agent integration, unlocking fungibility with traditional markets. However, it requires deep integration with issuers, transfer agents, and venue rules, making it the most operationally complex path.

    Each model represents different compromises. Wrappers ship fastest but create new securities that are merely claims on underlying assets. Broker-led receipts inherit existing regulatory frameworks and investor protections but remain confined to brokerage ecosystems. Canonical tokens promise true interoperability between traditional and blockchain markets but demand infrastructure integration that most issuers aren't prepared to undertake.

    Adoption remains limited across all three models, with BlackRock's reported interest in tokenizing ETFs representing perhaps the most significant validation. Current use cases focus on institutional portfolio rebalancing, collateralization, and programmable settlement rather than retail trading, constrained by the secondary market liquidity challenges discussed below.

=== "KO"

    고정 수익 토큰화가 채무 상품에 초점을 맞추는 반면, 주식 시장은 온체인으로 이동하는 전통 자산의 또 다른 주요 범주를 대표한다. 그러나 기술적 구현은 발행자가 블록체인 기록과 전통적인 증권 인프라 간의 간격을 어떻게 메우는지에 따라 극적으로 달라진다.

    토큰화된 주식과 ETF는 세 가지 뚜렷한 아키텍처 접근 방식을 통해 나타나고 있다. 핵심적인 차이점은 토큰이 다른 누군가가 보유한 주식에 대한 청구권을 나타내는지, 아니면 토큰 자체가 실제 증권인지에 있다. 각 접근 방식은 구현 용이성, 규제 복잡성, 기존 시장과의 통합 간에 다양한 절충점을 제공한다.

    첫 번째 모델인 래퍼 토큰화(발행자 또는 SPV 지원)는 법정화폐 담보 스테이블코인과 유사하게 작동하지만 주식에 적용된다. 비중개인 발행자가 100개 주식이나 ETF와 같은 기초 증권 바스켓을 취득하고 풀링된 자산에 대한 청구권을 나타내는 토큰을 발행한다. 이러한 토큰은 기초 증권과 경제적으로 연결되어 있지만 동일한 증권 자체는 아니다. 투자자는 증권사에서 네이티브 주식을 보유하는 것이 아니라 발행자와 함께 토큰을 상환한다. 이 구조는 일반적으로 Reg D/Reg S 또는 다른 관할권 면제에 의존하며 이전 제한과 화이트리스팅을 포함한다. Backed와 WisdomTree와 같은 운영자가 이 접근 방식을 사용하여 전통 펀드에 대한 온체인 청구권을 제공한다. 장점은 시장 출시 속도이지만, 한계는 분명하다: 토큰은 기초 증권의 직접 소유권이 아닌 래퍼 기업에 대한 청구권으로 존재한다.

    두 번째 접근 방식인 증권사를 통한 래퍼(증권사 영수증)는 규제된 증권사 또는 수탁 플랫폼을 아키텍처의 중심에 둔다. 증권사는 공식 증권사 기록을 유지하고 고객의 증권사 잔액을 나타내는 온체인 영수증을 발행한다. 이러한 토큰은 증권사 원장 내에서 양도 가능한 청구권으로 기능하며, 일반적으로 자격이 있는, 종종 비미국인 사용자와 화이트리스트된 지갑으로 제한된다. 정산과 최종성은 증권사의 장부에 의존하며, 온체인 잔액은 증권사의 내부 계정 구조에 매핑된다. 투자자가 잔액을 온체인으로 이동할 수 있지만 기초 자산은 독립적이고 예탁 가능한 주식이 아닌 증권사 수령권으로 남아 있는 증권사 주도 프로그램을 생각해보라. 이 모델은 증권사 보호와 규제 인프라를 상속하지만 구성 가능성을 증권사 생태계로 제한한다.

    세 번째이자 가장 야심찬 모델인 정식 토큰화는 온체인 상품을 오프체인 주식과 동일한 증권으로 만들려 한다. 토큰은 전통적인 주식과 동일한 공식 증권 식별자를 갖고 있어 발행자, 양도 대리인, 시장 인프라와의 조율이 필요하다. 투자자는 이론적으로 증권사 계좌와 온체인 지갑 사이에서 포지션을 브릿지할 수 있으며, 양도 대리인은 두 환경 모두에서 권위 있는 기록을 유지한다. Superstate는 래퍼 청구권이 아닌 진정한 증권 토큰화를 추구하며 이 접근 방식을 예시한다. 이 모델은 표준화된 규정 준수 중심 토큰 프레임워크와 양도 대리인 통합을 활용하여 전통 시장과의 대체 가능성을 해제한다. 그러나 발행자, 양도 대리인, 장소 규칙과의 깊은 통합이 필요하여 운영적으로 가장 복잡한 경로가 된다.

    각 모델은 다른 타협을 나타낸다. 래퍼는 가장 빨리 출시되지만 단순히 기초 자산에 대한 청구권인 새로운 증권을 만든다. 증권사 주도 영수증은 기존 규제 프레임워크와 투자자 보호를 상속하지만 증권사 생태계에 국한된다. 정식 토큰은 전통적 시장과 블록체인 시장 간의 진정한 상호운용성을 약속하지만 대부분의 발행자가 착수할 준비가 되어 있지 않은 인프라 통합을 요구한다.

    세 가지 모델 모두에서 채택은 제한적으로 남아 있으며, ETF 토큰화에 대한 BlackRock의 관심 보도가 아마도 가장 중요한 검증을 대표한다. 현재 사용 사례는 아래에서 논의되는 2차 시장 유동성 과제로 인해 소매 거래보다는 기관 포트폴리오 리밸런싱, 담보화, 프로그래밍 가능한 결제에 초점을 맞추고 있다.

### Physical Assets

=== "EN"

    While tokenized financial instruments have gained traction, physical asset tokenization remains largely experimental. Real estate and commodities represent the most prominent categories, but both face fundamental challenges that limit their practical adoption.

    Real estate tokenization promises to democratize property investment. Instead of needing hundreds of thousands to buy a rental property, investors could own $1,000 worth of a diversified portfolio and receive proportional rental income. Early platforms tokenize individual properties, with each token representing LLC shares in the underlying asset. However, three critical hurdles limit real estate tokenization in practice. First, properties require regular appraisals to maintain accurate valuations, creating ongoing costs and potential disputes. Second, operational management remains complex: someone must handle property maintenance, tenant relations, and local regulatory compliance. Third, the liquidity challenges discussed below have prevented meaningful secondary markets from developing. These obstacles have prevented real estate tokenization from scaling beyond niche applications.

    Commodity tokenization confronts similar bridging problems between physical and digital worlds. Pax Gold (PAXG) represents actual gold bars stored in Brink's vaults, with each token backed by one troy ounce of investment-grade gold. Tether Gold (XAUT) offers similar exposure through different custody arrangements. These products must navigate storage costs, insurance, audit verification, and redemption logistics. Holding PAXG theoretically represents ownership of real gold, but accessing that gold requires navigating complex custody and shipping arrangements. The result is that commodity tokens primarily serve as a way to gain price exposure without the complexities of physical ownership.

    Across both categories, a fundamental tension emerges: tokenization can improve record-keeping and fractional ownership, but it cannot eliminate the operational complexity of managing physical assets. The technology provides better rails for tracking ownership, yet the underlying assets remain subject to the same liquidity constraints, management requirements, and coordination challenges that have always made physical assets difficult to securitize. Until these operational hurdles are addressed through new business models or regulatory frameworks, physical asset tokenization will likely remain a niche application rather than a mainstream investment category.

=== "KO"

    토큰화된 금융 상품이 견인력을 얻은 반면, 실물 자산 토큰화는 여전히 대체로 실험적이다. 부동산과 상품이 가장 두드러진 범주를 대표하지만, 둘 다 실질적인 채택을 제한하는 근본적인 과제에 직면해 있다.

    부동산 토큰화는 부동산 투자를 민주화하겠다고 약속한다. 임대 부동산을 구매하기 위해 수십만 달러가 필요한 대신, 투자자는 다양한 포트폴리오의 1,000달러 상당을 소유하고 비례적인 임대 수익을 받을 수 있다. 초기 플랫폼은 개별 부동산을 토큰화하며, 각 토큰은 기초 자산의 LLC 지분을 나타낸다. 그러나 세 가지 중요한 장애물이 실제로 부동산 토큰화를 제한한다. 첫째, 부동산은 정확한 가치 평가를 유지하기 위해 정기적인 감정이 필요하여 지속적인 비용과 잠재적 분쟁을 만든다. 둘째, 운영 관리는 복잡하게 남아 있다: 누군가가 부동산 유지보수, 임차인 관계, 현지 규제 준수를 처리해야 한다. 셋째, 아래에서 논의되는 유동성 과제가 의미 있는 2차 시장이 발전하는 것을 막았다. 이러한 장애물은 부동산 토큰화가 틈새 응용을 넘어 확장되는 것을 막았다.

    상품 토큰화는 물리적 세계와 디지털 세계 사이의 유사한 브릿지 문제에 직면한다. Pax Gold(PAXG)는 Brink's 금고에 저장된 실제 금괴를 나타내며, 각 토큰은 투자 등급 금 1트로이온스로 뒷받침된다. Tether Gold(XAUT)는 다른 수탁 방식을 통해 유사한 노출을 제공한다. 이러한 제품은 보관 비용, 보험, 감사 검증, 상환 물류를 탐색해야 한다. PAXG를 보유하는 것은 이론적으로 실제 금의 소유권을 나타내지만, 그 금에 접근하려면 복잡한 수탁 및 배송 절차를 탐색해야 한다. 결과적으로 상품 토큰은 주로 실물 소유의 복잡성 없이 가격 노출을 얻는 방법으로 기능한다.

    두 범주 모두에서 근본적인 긴장이 나타난다: 토큰화는 기록 유지와 분할 소유권을 개선할 수 있지만, 실물 자산 관리의 운영적 복잡성을 제거할 수는 없다. 기술은 소유권 추적을 위한 더 나은 레일을 제공하지만, 기초 자산은 실물 자산을 증권화하기 어렵게 만들어온 동일한 유동성 제약, 관리 요건, 조율 과제의 대상으로 남아 있다. 새로운 비즈니스 모델이나 규제 프레임워크를 통해 이러한 운영적 장애물이 해결될 때까지, 실물 자산 토큰화는 주류 투자 범주가 아닌 틈새 응용으로 남을 가능성이 높다.

### Market Infrastructure

=== "EN"

    Tokenization promises improved liquidity for conventionally illiquid assets, but this promise hasn't materialized. The result is a paradox: tokens designed to make illiquid assets more tradeable often lack meaningful secondary markets themselves.

    Established securities benefit from mature exchanges, professional market makers, and deep institutional participation. Tokenized RWAs often trade on decentralized exchanges with minimal liquidity or private markets with restricted access. The problem manifests differently across asset classes but with consistent results: tokenized real estate properties might trade only a few times per month, commodity tokens serve primarily as price exposure instruments rather than facilitating physical delivery, and tokenized stocks see activity focused on institutional portfolio rebalancing rather than retail participation.

    The fundamental challenge is that tokenization solves record-keeping but not price discovery or market coordination. A building cannot be instantly converted to cash regardless of whether ownership is recorded on-chain or in a county registry. Gold bars still require custody, insurance, and shipping logistics. Regulatory restrictions on equity trading persist whether shares exist as tokens or traditional securities.

    This liquidity challenge means that many RWA tokens function more like conventional private placements than the liquid, tradeable assets their proponents envision. Secondary market liquidity remains the Achilles' heel of RWA tokenization, suggesting that improved infrastructure alone cannot manufacture the network effects and institutional participation that create deep markets.

=== "KO"

    토큰화는 전통적으로 비유동적인 자산의 유동성 개선을 약속하지만, 이 약속은 실현되지 않았다. 결과는 역설이다: 비유동적인 자산을 더 거래 가능하게 만들도록 설계된 토큰이 종종 그 자체로 의미 있는 2차 시장을 갖지 못한다.

    기존 증권은 성숙한 거래소, 전문 시장 조성자, 깊은 기관 참여의 혜택을 받는다. 토큰화된 RWA는 종종 유동성이 최소화된 탈중앙화 거래소나 접근이 제한된 사모 시장에서 거래된다. 문제는 자산 클래스에 따라 다르게 나타나지만 일관된 결과를 보인다: 토큰화된 부동산 자산은 월에 몇 번만 거래될 수 있고, 상품 토큰은 실물 인도를 촉진하기보다는 주로 가격 노출 수단으로 기능하며, 토큰화된 주식은 소매 참여보다는 기관 포트폴리오 리밸런싱에 초점을 맞춘 활동을 본다.

    근본적인 과제는 토큰화가 기록 유지는 해결하지만 가격 발견이나 시장 조율은 해결하지 못한다는 것이다. 건물은 소유권이 온체인에 기록되든 카운티 등기소에 기록되든 관계없이 즉시 현금으로 전환될 수 없다. 금괴는 여전히 수탁, 보험, 배송 물류가 필요하다. 주식 거래에 대한 규제 제한은 주식이 토큰으로 존재하든 전통 증권으로 존재하든 지속된다.

    이 유동성 과제는 많은 RWA 토큰이 지지자들이 상상하는 유동적이고 거래 가능한 자산이 아닌 전통적인 사모발행처럼 더 많이 기능한다는 것을 의미한다. 2차 시장 유동성은 RWA 토큰화의 아킬레스건으로 남아 있으며, 개선된 인프라만으로는 깊은 시장을 만드는 네트워크 효과와 기관 참여를 제조할 수 없음을 시사한다.
