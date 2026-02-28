# Chapter VII: DeFi

## Section I: DeFi Core Concepts and Philosophy

=== "EN"

    ### The Genesis of Decentralized Finance

    While Bitcoin focuses on creating sound money that relies on no authorities, DeFi tackles an even broader question: what if we could create a parallel financial system without banks, brokers, or clearinghouses?

    Imagine a financial system that never sleeps, operates with broad permissionless access, and enables global participation. DeFi delivers financial services built on permissionless blockchains that anyone can use, audit, and build upon. While fees can be exclusionary, front-ends may geo-block users, and some assets face blacklisting risks, DeFi remains far more accessible than traditional systems.

    Traditional finance relies on intermediaries at every layer, each adding costs, delays, and points of failure. DeFi protocols minimize traditional intermediaries by encoding financial logic directly into smart contracts.

    Markets operate continuously without closing hours, with settlements happening atomically within the same chain or rollup. Every transaction and protocol rule remains visible and verifiable, while protocols snap together like "money legos," enabling innovations impossible in siloed systems. For example, a user can borrow funds, swap them on an exchange, and deposit the result into a savings protocol, all within a single transaction that either succeeds completely or fails completely with no partial execution. This **atomic composability** is enabled by Ethereum's transaction model (Chapter II), where complex multi-step operations execute as indivisible units.

    Throughout this chapter, we reference MEV (Maximal Extractable Value), which is covered in depth in Chapter VIII. For now, understand it as various ways sophisticated actors profit from transaction ordering, typically resulting in users paying more through increased slippage or having profitable opportunities extracted by faster actors.

    ### The Economic Drivers

    The demand for decentralized financial services stems from real economic needs that traditional systems often serve poorly. Crypto holders want to earn yield on idle assets, while traders and institutions need leverage for market activities. In DeFi, users can deposit volatile assets and borrow stable dollars without selling their position, preserving upside exposure while accessing liquidity. However, this approach creates liquidation risk.

    Decentralized exchanges (often just called DEXs) address the custody and access problems of centralized platforms. When users trade on a DEX, they never give up control of their assets. Trades settle atomically on the same chain, completely removing custodial exchange risk. DEXs enable permissionless listing of new assets and the bundling of complex transactions like trading plus lending plus staking in a single operation.

    ### The Fundamental Trade-offs

    DeFi comes with significant costs. Users face gas fees, slippage, various forms of MEV extraction, **impermanent loss** (the opportunity cost liquidity providers face when asset price ratios change compared to simply holding those assets), and approval risks from malicious tokens that can drain funds via infinite allowances. Smart contract bugs can drain funds instantly and failures in price data feeds (called **oracles**) can trigger cascading liquidations.

    While sophisticated finance participants often maintain advantages in both traditional and decentralized systems, DeFi uniquely rewards those with deep technical expertise who understand exactly how protocols behave and can identify and exploit market inefficiencies. Professional participation in DeFi markets requires quantitative understanding of these mechanisms. Many MEV opportunities emerge directly from protocol mechanics, making this knowledge valuable for both users and searchers.

=== "KO"

    ### 탈중앙화 금융의 탄생

    비트코인이 어떤 권위에도 의존하지 않는 건전한 화폐를 만드는 데 집중하는 반면, DeFi는 더 광범위한 질문을 다룬다: 은행, 브로커, 청산소 없이 병렬적인 금융 시스템을 만들 수 있다면 어떨까?

    절대 잠들지 않고, 광범위한 무허가 접근(Permissionless Access)으로 운영되며, 전 세계적 참여를 가능하게 하는 금융 시스템을 상상해 보라. DeFi는 누구나 사용하고, 감사하고, 그 위에 구축할 수 있는 무허가 블록체인 위에 구축된 금융 서비스를 제공한다. 수수료가 배제적일 수 있고, 프론트엔드가 지역 차단을 할 수 있으며, 일부 자산은 블랙리스트 위험에 직면할 수 있지만, DeFi는 전통 시스템보다 훨씬 더 접근 가능하다.

    전통 금융은 모든 계층에서 중개자에 의존하며, 각각이 비용, 지연, 장애 지점을 추가한다. DeFi 프로토콜은 금융 로직을 스마트 컨트랙트(Smart Contract)에 직접 인코딩함으로써 전통적인 중개자를 최소화한다.

    시장은 마감 시간 없이 지속적으로 운영되며, 정산은 동일 체인이나 롤업 내에서 원자적으로 이루어진다. 모든 거래와 프로토콜 규칙은 가시적이고 검증 가능하며, 프로토콜들은 "머니 레고"처럼 서로 맞물려 사일로화된 시스템에서는 불가능한 혁신을 가능하게 한다. 예를 들어, 사용자는 자금을 빌리고, 거래소에서 교환하고, 그 결과를 저축 프로토콜에 예치하는 것을 부분 실행 없이 완전히 성공하거나 완전히 실패하는 단일 트랜잭션 내에서 수행할 수 있다. 이러한 **원자적 조합 가능성(Atomic Composability)**은 복잡한 다단계 작업이 분할 불가능한 단위로 실행되는 이더리움의 트랜잭션 모델(Chapter II)에 의해 가능해진다.

    이 챕터 전반에 걸쳐 우리는 **MEV(최대 추출 가능 가치, Maximal Extractable Value)**를 참조하는데, 이는 Chapter VIII에서 심층적으로 다룬다. 지금은 이것을 정교한 행위자들이 트랜잭션 순서에서 이익을 얻는 다양한 방식으로 이해하면 되며, 일반적으로 사용자들은 증가된 슬리피지를 통해 더 많이 지불하거나 더 빠른 행위자들에게 수익 기회를 빼앗기게 된다.

    ### 경제적 동인

    탈중앙화 금융 서비스에 대한 수요는 전통 시스템이 종종 제대로 충족시키지 못하는 실제 경제적 필요에서 비롯된다. 암호화폐 보유자는 유휴 자산에서 수익을 얻고 싶어하고, 트레이더와 기관은 시장 활동을 위한 레버리지가 필요하다. DeFi에서 사용자는 변동성 있는 자산을 예치하고 포지션을 매도하지 않고 안정적인 달러를 빌릴 수 있어, 유동성에 접근하면서 상승 노출을 유지한다. 그러나 이 접근법은 청산 위험을 생성한다.

    탈중앙화 거래소(Decentralized Exchange, DEX)는 중앙화 플랫폼의 커스터디와 접근 문제를 해결한다. 사용자가 DEX에서 거래할 때, 그들은 결코 자산에 대한 통제권을 포기하지 않는다. 거래는 동일 체인에서 원자적으로 정산되어, 커스터디 거래소 위험을 완전히 제거한다. DEX는 새로운 자산의 무허가 상장과 거래 플러스 대출 플러스 스테이킹과 같은 복잡한 트랜잭션의 번들링을 단일 작업으로 가능하게 한다.

    ### 근본적인 트레이드오프

    DeFi에는 상당한 비용이 따른다. 사용자는 가스 수수료, 슬리피지, 다양한 형태의 MEV 추출, **비영구적 손실(Impermanent Loss)**(유동성 공급자가 자산 가격 비율이 변할 때 단순히 그 자산을 보유하는 것에 비해 직면하는 기회비용), 그리고 무한 허용량을 통해 자금을 고갈시킬 수 있는 악의적 토큰의 승인 위험에 직면한다. 스마트 컨트랙트 버그는 즉시 자금을 고갈시킬 수 있고, 가격 데이터 피드(**오라클(Oracle)**이라 불림)의 실패는 연쇄 청산을 유발할 수 있다.

    정교한 금융 참여자들이 전통 시스템과 탈중앙화 시스템 모두에서 종종 우위를 유지하지만, DeFi는 프로토콜이 어떻게 동작하는지 정확히 이해하고 시장 비효율성을 식별하고 활용할 수 있는 깊은 기술적 전문성을 가진 이들에게 독특하게 보상한다. DeFi 시장에서의 전문적 참여는 이러한 메커니즘에 대한 정량적 이해를 필요로 한다. 많은 MEV 기회가 프로토콜 메커니즘에서 직접 발생하여, 이 지식은 사용자와 서처 모두에게 가치가 있다.

## Section II: Decentralized Exchange Architecture

=== "EN"

    Decentralized exchanges solve a fundamental problem: how can users trade assets without trusting a centralized intermediary to hold their funds? In doing so, they establish on-chain price discovery and liquidity that other protocols can build upon.

    ### Uniswap: The AMM Revolution

    Uniswap pioneered a radically different approach to trading that transformed how we think about market making. Instead of maintaining complex order books that require constant updates and millisecond matching, Uniswap uses an **Automated Market Maker (AMM)** that quotes prices from pool balances and settles trades atomically.

    This innovation arose from Ethereum's specific constraints. As discussed in Chapter II, Ethereum has low throughput, variable fees, and roughly twelve-second blocks. A central limit order book requires constant posting and canceling of orders with millisecond matching, making it too transaction-intensive to be feasible and expensive to run fully on-chain. AMMs solve this by replacing the matching engine with a pricing curve that requires only one transaction to update balances and settle immediately.

    The evolution of Uniswap's pricing reveals how DeFi protocols iterate toward better capital utilization. Uniswap v1 used pools pairing every token with ETH, following the constant product invariant where x × y \= k (a fixed value). Any trade between tokens had to route through ETH, requiring two separate swaps and incurring two sets of fees.

    #### Price Impact and Slippage: The Core Mechanics

    Why does buying tokens move the price? This seemingly simple question reveals the core mechanics of AMMs. Consider a constant product pool with token reserves and a fixed invariant. When a trader buys token X with token Y, they add their input amount to the Y reserves and remove output tokens from the X reserves. The constraint that their product must remain constant means larger trades have proportionally larger price impact.

    Two requirements drive this dynamic simultaneously. The pool can never run out of either token, and it must always be able to quote a price for any trade, no matter the size. These constraints working together explain why prices become exponentially steep as reserves shrink: a pool nearly depleted of token X still has to accept your trade, but must price it high enough to mathematically prevent the supply from ever hitting zero.

    To understand this intuitively, imagine a special marketplace with two buckets of red marbles and blue marbles. There's a magical rule that mirrors the AMM's constant product formula: the number of red marbles multiplied by the number of blue marbles must always equal the same number (like 10,000).

    When someone wants to buy red marbles, they have to add blue marbles to the blue bucket. But here's the catch: they can only take out enough red marbles so that the multiplication rule stays true.

    If the buckets start with 100 red marbles and 100 blue marbles (100 × 100 \= 10,000), and someone wants to buy 20 red marbles. They need add 25 blue marbles to the bucket (making it 125 blue and leaving 80 red). This works because 125 × 80 ≈ 10,000.

    The more red marbles someone wants, the exponentially more blue marbles they need to add. The bucket becomes "stingier" with each marble taken, the first marble is cheap, but the 50th costs exponentially more.

    If someone wants to buy 50 red marbles. They need add 100 blue marbles to the bucket (making it 200 blue and leaving 50 red). The math still works because 200 × 50 ≈ 10,000.

    The deeper the buckets (more marbles), the less each individual trade affects the overall balance. Shallow buckets create large price swings; deep buckets maintain price stability.

    In DeFi terms: these buckets are **liquidity pools**, the marbles are token reserves, and the stinginess is **slippage** (the price impact that grows with trade size). Unlike traditional markets where there may not be enough sellers, AMM pools always have liquidity available at a calculable price.

    For small trades, slippage approximates the trading fee. But for larger trades, the curve's shape adds additional price impact that grows with trade size relative to pool depth. Small trades get better execution while large trades pay for their market impact, a natural market mechanism emerging from the mathematical curve.

    This predictability is what makes AMMs powerful. Unlike order book markets where large trades can walk through multiple price levels unpredictably, AMM slippage follows mathematical curves. Traders can calculate their expected execution price before submitting transactions, and arbitrageurs can immediately correct any price deviations between pools.

    #### Uniswap's Evolution: v2, v3, and v4

    With the core mechanics of price impact understood, we can examine how Uniswap evolved to improve capital efficiency while maintaining these fundamental dynamics.

    Uniswap v2 generalized this approach, allowing any ERC-20 pair without forced ETH routing. The router and SDK enable multi-hop routing across pools through off-chain pathfinding, while the contracts execute the supplied path. The protocol also added TWAP (Time-Weighted Average Price) oracles for price tracking and flash swaps for advanced use cases. The core pricing mechanism remained the constant product formula, but the removal of ETH routing significantly improved liquidity utilization.

    Uniswap v3 introduced **concentrated liquidity**, fundamentally changing how AMMs work. Instead of spreading liquidity across all possible prices, liquidity providers can choose specific price ranges called "ticks." Within each active range, the pricing behaves similarly to v2's constant product formula but with higher effective liquidity since capital is concentrated. This reduces slippage for trades within active ranges while maintaining the AMM's simplicity. In practice, this design is especially powerful for highly correlated assets such as stablecoin pairs or liquid staking token pools like stETH/ETH, where most trading happens near a known fair value and LPs are comfortable concentrating around it. It also lets LPs shape how their orders execute over time: by placing liquidity only above or below the current price, they can effectively set up gradual buys or sells (range orders), accumulating or offloading a position while minimizing immediate price impact.

    Uniswap v4, which launched in early 2025, represents the next evolution with a single "singleton" contract holding all pools for gas savings. The major innovation is "hooks" that allow programmable AMM behavior. These hooks can implement dynamic fees, time-weighted average market makers, MEV-aware flows, limit orders, and more. The default pools can still use constant product curves, but the architecture enables entirely new pricing behaviors.

    ### Curve Finance: Math for Stable Trading

    While Uniswap succeeded at enabling trades between volatile assets like ETH and various ERC-20 tokens, an inefficiency emerged when users traded stablecoins on the platform. Stablecoins like USDC and USDT should theoretically trade at nearly identical values, but Uniswap v2's constant product formula spread liquidity across price ranges that rarely occur in stablecoin trading, causing higher slippage for assets that barely fluctuate relative to each other.

    #### The StableSwap Approach

    Curve Finance developed StableSwap, a hybrid mathematical approach that blends two pricing curves to address this inefficiency. Near the peg around the 1:1 ratio, StableSwap behaves like a constant sum formula creating minimal slippage, while gradually transitioning toward constant product behavior as prices drift from the peg to prevent pool failure.

    The key innovation was Curve's amplification factor (A), which controls how flat the pricing curve remains near the 1:1 peg. Higher amplification creates lower slippage for normal trades near $1.00 while maintaining steep protective walls for extreme scenarios. This allowed Curve to charge lower fees (0.01-0.04% versus Uniswap's 0.3%) while providing superior execution for stablecoin swaps.

    #### The Three-Pool Foundation and Ecosystem

    Curve's 3pool containing USDC, USDT, and DAI became a key piece of stablecoin infrastructure. Rather than fragmenting stablecoin liquidity across separate two-asset pools, the 3pool concentrated major stablecoin liquidity in a single venue. Traders could swap between any pair with a single transaction while benefiting from the combined depth of all three assets.

    Building on this foundation, Curve created "meta-pools" that allowed new stablecoins to pair directly against 3pool LP tokens, gaining access to liquidity against all three major stablecoins simultaneously. New projects like FRAX, LUSD, and GUSD could tap into the 3pool's billion-dollar liquidity without fragmenting it across multiple venues, solving the bootstrap problem for new stablecoin launches.

    The architecture extended beyond dollar stablecoins to liquid staking derivatives like stETH/ETH, where the specialized mathematics proved well-suited for assets that should maintain relatively stable ratios. Curve became a major venue for various pegged asset categories including wrapped Bitcoin variants and EUR stablecoins.

    #### Market Evolution and Competition

    Despite these technical innovations and network effects, competitive dynamics have shifted significantly. The March 2023 USDC depegging crisis provided a stress test of Curve's design. As USDC dropped to $0.88, the 3pool became heavily imbalanced toward USDC as traders fled the distressed asset. While the mathematics worked as designed and the pool rebalanced after USDC recovered, the crisis revealed both the resilience and limitations of AMM-based stablecoin trading under extreme market stress.

    Curve's mathematical advantages and established liquidity couldn't prevent market share erosion from Uniswap v3's concentrated liquidity. Uniswap's 0.01% fee tiers matched Curve's pricing while concentrated liquidity allowed sophisticated providers to achieve similar capital efficiency. Combined with Uniswap's more accessible user experience and broader ecosystem integration, this competitive shift has reversed the landscape. Uniswap now processes over $220 million daily in USDC/USDT swaps compared to Curve's approximately $44 million across all its stablecoin pools.

    ### Bonding-Curve Launchpads

    While Uniswap and Curve focus on trading existing tokens, a related innovation applies similar mathematical curves to solve a different problem: how new tokens come into existence and find their initial price. Before bonding-curve launchpads emerged, launching a token typically meant proceeding directly to an AMM like Uniswap or Raydium. Development teams would create their token and seed an initial liquidity pool using their own capital, usually pairing it against ETH, SOL, or a stablecoin. They would often burn or lock the LP tokens to demonstrate they could not later "rug" the pool. This approach made token launches capital-intensive and established a particular set of trust assumptions: users needed to believe the team would neither withdraw liquidity, mint new tokens arbitrarily, nor otherwise abuse their privileged position around the pool.

    Pump.fun fundamentally reframed this pipeline by introducing a distinct "pre-AMM" stage governed by a **bonding curve**. Built on Solana, it functions as a permissionless launchpad where anyone can create a token and watch it trade immediately on a curve-based contract. When someone launches a new token, a fixed supply (commonly one billion units) is minted. Roughly 800 million tokens are made available on the bonding curve, while the remaining 200 million or so are allocated to the creator and typically later recycled into the initial liquidity position once the token graduates.

    The curve sells tokens against SOL, with prices rising non-linearly as more of those 800 million tokens are purchased and falling when they are sold back into the curve. In practice, the creator can also buy from the curve immediately at launch. This gives them a natural opportunity to build an early position at the lowest prices before wider attention arrives.

    Once the bonding curve reaches a defined completion threshold (effectively, once a platform-specified number of tokens have been sold and a target amount of SOL has been accumulated), the token "graduates." At this pivotal moment, the system automatically seeds a liquidity pool on a downstream AMM and transfers the bonded SOL and tokens into it, often burning the resulting LP tokens. Historically, this meant creating a pool on Raydium. More recently, Pump.fun routes graduated tokens into its own AMM, PumpSwap, where they trade like any other Solana token.

    For users, this design compresses issuance, initial price discovery, and AMM listing into a single automated pipeline. Pump.fun's contracts handle pool creation and LP-token burning behind the scenes instead of teams manually setting up a pool and then burning LP. Because PumpSwap is vertically integrated, the platform can also levy protocol fees on secondary trading and share a slice of those fees with token creators. This turns successful graduations into an ongoing fee stream rather than just a one-off bonding-curve event.

    This architecture removes certain trust assumptions while introducing others. Developers no longer control LP tokens during the early phase. The bonding-curve contract enforces pricing and liquidity, while graduation logic automatically seeds the AMM pool. Yet participants now rely on the correctness and governance of a single platform's contracts and backend, along with its off-chain policies governing moderation, regional restrictions, and listing rules.

    The creator still holds a meaningful portion of supply and can buy early on the curve. This means "soft rugs" via aggressive selling or outright abandonment remain common even when classic LP-withdrawal rugs become harder to execute. In practice, only a small fraction of the thousands of daily launches ever graduate off the curve. Lifetime averages sit in the low single digits (around 1-2% of tokens graduating overall), with daily graduation rates typically below 3% and only occasionally spiking above 4% during peak mania. Most tokens die in place as short-lived social experiments.

    Despite these risks, or perhaps because of them, Pump.fun became one of the most influential retail-facing crypto applications of the 2024-2025 cycle. It reduced the cost and friction of token creation to nearly zero, transformed the "token" itself into a disposable social object, and helped catalyze a massive memecoin wave. Many assets began life on a bonding curve before ever touching a conventional AMM. The model proved contagious: bonding-curve launchpads and Pump.fun clones rapidly appeared across other L1s and L2s, cementing this "factory plus curve plus AMM graduation" pipeline as a standard pattern for speculative token issuance.

    Conceptually, bonding-curve launchpads sit upstream of the exchange architectures described throughout the rest of this section. They are not general-purpose DEXs in the way Uniswap or Curve are, but they employ similar mathematical principles to automate primary issuance, early price discovery, and initial liquidity provisioning. AMMs still handle the long-tail trading once a token graduates. Bonding curves simply shifted who must provide seed capital and what users must trust in the earliest, most reflexive phase of a token's existence.

    ### Alternative Exchange Architectures

    The AMM revolution sparked further innovation in exchange design, each solving different aspects of the trading problem.

    #### Intent-Based Systems

    Intent-based platforms like CoW Swap and UniswapX represent a paradigm shift from traditional transaction specification. Instead of users constructing exact swap paths and parameters, they sign high-level "intents" that describe desired outcomes, such as "I want to receive at least 1,000 USDC for my 1 ETH within the next 2 minutes."

    Off-chain solvers (also called "fillers") then compete to fulfill these intents, routing across multiple venues for best execution. CoW Swap uses batch auctions where solvers submit bids to fill multiple orders simultaneously, often finding Coincidence of Wants (CoW) where orders can be settled directly against each other without touching AMM liquidity. UniswapX employs Dutch auctions where the offered price gradually improves until a filler takes it.

    Users often get better prices than direct AMM swaps since solvers can access multiple liquidity sources and internalize trades. UniswapX additionally enables gasless submission where fillers pay the gas fees, improving the user experience. Both systems provide MEV protection since the competitive solver auction makes it difficult for any single actor to extract value.

    #### Request-for-Quote Systems

    Request-for-Quote (RFQ) systems bring professional market making to DeFi by combining off-chain efficiency with on-chain settlement. Platforms like Hashflow and 0x RFQ allow users to request firm quotes from market makers, who provide guaranteed prices based on current conditions.

    Market makers quote prices off-chain, considering their inventory, hedging costs, and desired margins. Once a user accepts a quote, settlement happens on-chain at the guaranteed price with no slippage risk. This approach proves effective for larger trades where AMM price impact would be significant, and for institutional users who value execution certainty over decentralization.

    #### Decentralized Perpetual Exchanges

    Beyond spot trading, decentralized perpetual exchanges have grown rapidly, bringing on-chain leverage and competitive performance. While Chapter VI covered the mechanics of perpetual futures on centralized exchanges, this section focuses on their decentralized counterparts. Platforms like GMX use synthetic pricing with LP pools backing trades, while dYdX originally built on StarkEx for better performance before launching its own application-specific blockchain. These developments demonstrate how DeFi continues expanding the scope of possible financial services.

    Application-specific chains like Hyperliquid run their own blockchains optimized entirely for trading, prioritizing speed and order book efficiency over general-purpose computation. This architecture enables sub-second finality and complex order types that would be impractical on general L1s. Chapter X examines Hyperliquid's approach in depth.

    Each model balances different priorities: AMMs prioritize decentralization and composability, RFQ systems optimize for execution quality, and application-specific chains maximize performance. The optimal choice depends on specific use cases, performance requirements, and risk tolerance.

=== "KO"

    탈중앙화 거래소는 근본적인 문제를 해결한다: 사용자가 자금을 보유할 중앙화된 중개자를 신뢰하지 않고 어떻게 자산을 거래할 수 있을까? 그렇게 함으로써, 그들은 다른 프로토콜이 구축할 수 있는 온체인 가격 발견과 유동성을 확립한다.

    ### Uniswap: AMM 혁명

    Uniswap은 시장 조성에 대한 우리의 생각을 변화시킨 근본적으로 다른 거래 접근법을 개척했다. 지속적인 업데이트와 밀리초 매칭이 필요한 복잡한 오더북을 유지하는 대신, Uniswap은 풀 잔액에서 가격을 산출하고 거래를 원자적으로 정산하는 **자동화된 시장 조성자(Automated Market Maker, AMM)**를 사용한다.

    이 혁신은 이더리움의 특정 제약에서 발생했다. Chapter II에서 논의했듯이, 이더리움은 낮은 처리량, 가변 수수료, 그리고 대략 12초 블록을 가진다. 중앙 지정가 호가창은 밀리초 매칭과 함께 지속적인 주문 게시와 취소를 필요로 하여, 온체인에서 완전히 실행하기에는 너무 트랜잭션 집약적이고 비용이 많이 든다. AMM은 매칭 엔진을 잔액을 업데이트하고 즉시 정산하는 데 단 하나의 트랜잭션만 필요한 가격 곡선으로 대체하여 이를 해결한다.

    Uniswap 가격 책정의 진화는 DeFi 프로토콜이 더 나은 자본 활용을 향해 어떻게 반복하는지를 보여준다. Uniswap v1은 모든 토큰을 ETH와 페어링하는 풀을 사용했으며, x × y = k(고정 값)인 상수곱 불변량을 따랐다. 토큰 간의 모든 거래는 ETH를 통해 라우팅되어야 했고, 두 번의 별도 스왑과 두 세트의 수수료가 필요했다.

    #### 가격 영향과 슬리피지: 핵심 메커니즘

    토큰을 구매하면 왜 가격이 움직일까? 이 겉보기에 단순한 질문이 AMM의 핵심 메커니즘을 드러낸다. 토큰 준비금과 고정된 불변량을 가진 상수곱 풀을 고려하자. 트레이더가 토큰 Y로 토큰 X를 구매할 때, 그들은 입력 금액을 Y 준비금에 추가하고 X 준비금에서 출력 토큰을 제거한다. 그들의 곱이 일정하게 유지되어야 한다는 제약은 더 큰 거래가 비례적으로 더 큰 가격 영향을 가진다는 것을 의미한다.

    두 가지 요구사항이 이 역학을 동시에 구동한다. 풀은 어느 토큰도 고갈될 수 없으며, 규모에 관계없이 항상 모든 거래에 대해 가격을 산출할 수 있어야 한다. 이러한 제약이 함께 작동하면 준비금이 줄어들수록 가격이 기하급수적으로 가파르게 되는 이유를 설명한다: 토큰 X가 거의 고갈된 풀은 여전히 당신의 거래를 받아들여야 하지만, 공급이 결코 0에 도달하지 않도록 수학적으로 방지하기 위해 충분히 높은 가격을 책정해야 한다.

    이것을 직관적으로 이해하기 위해, 빨간 구슬과 파란 구슬 두 버킷이 있는 특별한 시장을 상상해 보라. AMM의 상수곱 공식을 반영하는 마법의 규칙이 있다: 빨간 구슬 수에 파란 구슬 수를 곱한 값은 항상 같은 숫자(예: 10,000)여야 한다.

    누군가가 빨간 구슬을 사고 싶을 때, 그들은 파란 구슬을 파란 버킷에 추가해야 한다. 하지만 여기에 함정이 있다: 그들은 곱셈 규칙이 참으로 유지되도록 충분한 빨간 구슬만 꺼낼 수 있다.

    버킷이 빨간 구슬 100개와 파란 구슬 100개로 시작하면(100 × 100 = 10,000), 누군가가 빨간 구슬 20개를 사고 싶다면. 그들은 버킷에 파란 구슬 25개를 추가해야 한다(파란 125개와 빨간 80개가 남음). 이것이 작동하는 이유는 125 × 80 ≈ 10,000이기 때문이다.

    누군가가 원하는 빨간 구슬이 많을수록, 그들이 추가해야 하는 파란 구슬은 기하급수적으로 많아진다. 버킷은 구슬을 꺼낼 때마다 더 "인색해진다", 첫 번째 구슬은 싸지만, 50번째 구슬은 기하급수적으로 더 비싸다.

    누군가가 빨간 구슬 50개를 사고 싶다면. 그들은 버킷에 파란 구슬 100개를 추가해야 한다(파란 200개와 빨간 50개가 남음). 200 × 50 ≈ 10,000이므로 수학은 여전히 작동한다.

    버킷이 깊을수록(구슬이 많을수록), 각 개별 거래가 전체 균형에 미치는 영향이 적다. 얕은 버킷은 큰 가격 변동을 만들고; 깊은 버킷은 가격 안정성을 유지한다.

    DeFi 용어로: 이 버킷들은 **유동성 풀(Liquidity Pool)**이고, 구슬은 토큰 준비금이며, 인색함은 **슬리피지(Slippage)**(거래 규모에 따라 커지는 가격 영향)이다. 충분한 판매자가 없을 수 있는 전통 시장과 달리, AMM 풀은 항상 계산 가능한 가격에 유동성을 이용 가능하게 한다.

    작은 거래의 경우, 슬리피지는 거래 수수료에 근접한다. 하지만 더 큰 거래의 경우, 곡선의 형태가 풀 깊이 대비 거래 규모에 따라 커지는 추가적인 가격 영향을 더한다. 작은 거래는 더 나은 체결을 얻고 큰 거래는 시장 영향에 대해 지불한다, 이는 수학적 곡선에서 자연스럽게 나타나는 시장 메커니즘이다.

    이 예측 가능성이 AMM을 강력하게 만드는 것이다. 큰 거래가 예측 불가능하게 여러 가격 수준을 통과할 수 있는 오더북 시장과 달리, AMM 슬리피지는 수학적 곡선을 따른다. 트레이더는 트랜잭션을 제출하기 전에 예상 체결 가격을 계산할 수 있고, 차익 거래자는 풀 간의 가격 편차를 즉시 수정할 수 있다.

    #### Uniswap의 진화: v2, v3, v4

    가격 영향의 핵심 메커니즘을 이해했으므로, 이제 Uniswap이 이러한 근본적인 역학을 유지하면서 자본 효율성을 개선하기 위해 어떻게 진화했는지 살펴볼 수 있다.

    Uniswap v2는 이 접근법을 일반화하여 강제 ETH 라우팅 없이 모든 ERC-20 쌍을 허용했다. 라우터와 SDK는 오프체인 경로 탐색을 통해 풀 간 다중 홉 라우팅을 가능하게 하고, 컨트랙트는 제공된 경로를 실행한다. 프로토콜은 또한 가격 추적을 위한 TWAP(시간 가중 평균 가격, Time-Weighted Average Price) 오라클과 고급 사용 사례를 위한 플래시 스왑을 추가했다. 핵심 가격 책정 메커니즘은 상수곱 공식으로 유지되었지만, ETH 라우팅 제거는 유동성 활용을 상당히 개선했다.

    Uniswap v3는 **집중 유동성(Concentrated Liquidity)**을 도입하여 AMM 작동 방식을 근본적으로 변경했다. 모든 가능한 가격에 유동성을 분산시키는 대신, 유동성 공급자는 "틱"이라 불리는 특정 가격 범위를 선택할 수 있다. 각 활성 범위 내에서 가격 책정은 v2의 상수곱 공식과 유사하게 동작하지만, 자본이 집중되어 있으므로 더 높은 유효 유동성을 가진다. 이것은 활성 범위 내 거래의 슬리피지를 줄이면서 AMM의 단순성을 유지한다. 실제로 이 설계는 스테이블코인 쌍이나 stETH/ETH와 같은 리퀴드 스테이킹 토큰 풀처럼 거래가 대부분 알려진 공정 가치 근처에서 발생하고 LP가 그 주변에 집중하는 것이 편안한 고도로 상관된 자산에 특히 강력하다. 또한 LP가 시간에 따라 주문이 어떻게 실행되는지 형성할 수 있게 한다: 현재 가격 위나 아래에만 유동성을 배치함으로써, 그들은 효과적으로 점진적 매수나 매도(범위 주문)를 설정하여 즉각적인 가격 영향을 최소화하면서 포지션을 축적하거나 청산할 수 있다.

    2025년 초에 출시된 Uniswap v4는 가스 절약을 위해 모든 풀을 보유하는 단일 "싱글톤" 컨트랙트로 다음 진화를 나타낸다. 주요 혁신은 프로그래밍 가능한 AMM 동작을 허용하는 "훅"이다. 이 훅은 동적 수수료, 시간 가중 평균 시장 조성자, MEV 인식 흐름, 지정가 주문 등을 구현할 수 있다. 기본 풀은 여전히 상수곱 곡선을 사용할 수 있지만, 아키텍처는 완전히 새로운 가격 책정 동작을 가능하게 한다.

    ### Curve Finance: 안정적 거래를 위한 수학

    Uniswap이 ETH와 다양한 ERC-20 토큰 같은 변동성 자산 간의 거래를 가능하게 하는 데 성공했지만, 사용자가 플랫폼에서 스테이블코인을 거래할 때 비효율성이 나타났다. USDC와 USDT 같은 스테이블코인은 이론적으로 거의 동일한 가치로 거래되어야 하지만, Uniswap v2의 상수곱 공식은 스테이블코인 거래에서 거의 발생하지 않는 가격 범위에 유동성을 분산시켜, 서로 거의 변동하지 않는 자산에 대해 더 높은 슬리피지를 유발했다.

    #### StableSwap 접근법

    Curve Finance는 이 비효율성을 해결하기 위해 두 가격 곡선을 혼합하는 하이브리드 수학적 접근법인 StableSwap을 개발했다. 1:1 비율 주변의 페그 근처에서 StableSwap은 최소한의 슬리피지를 만드는 상수합 공식처럼 동작하고, 풀 실패를 방지하기 위해 가격이 페그에서 벗어날수록 점진적으로 상수곱 동작으로 전환된다.

    핵심 혁신은 Curve의 증폭 계수(A)로, 1:1 페그 근처에서 가격 곡선이 얼마나 평평하게 유지되는지를 제어한다. 더 높은 증폭은 $1.00 근처의 일반 거래에 대해 더 낮은 슬리피지를 만들면서 극단적 시나리오에 대한 가파른 보호벽을 유지한다. 이를 통해 Curve는 스테이블코인 스왑에 대해 우수한 체결을 제공하면서 더 낮은 수수료(Uniswap의 0.3%에 비해 0.01-0.04%)를 부과할 수 있었다.

    #### 3풀 기반과 생태계

    USDC, USDT, DAI를 포함하는 Curve의 3pool은 스테이블코인 인프라의 핵심 조각이 되었다. 스테이블코인 유동성을 별도의 두 자산 풀에 분산시키는 대신, 3pool은 주요 스테이블코인 유동성을 단일 장소에 집중시켰다. 트레이더는 세 자산 모두의 결합된 깊이로부터 혜택을 받으면서 단일 트랜잭션으로 어느 쌍이든 스왑할 수 있었다.

    이 기반 위에 Curve는 새로운 스테이블코인이 3pool LP 토큰과 직접 페어링하여 세 개의 주요 스테이블코인에 대한 유동성에 동시에 접근할 수 있게 하는 "메타풀"을 만들었다. FRAX, LUSD, GUSD와 같은 새로운 프로젝트는 여러 장소에 분산시키지 않고 3pool의 수십억 달러 유동성을 활용할 수 있어, 새로운 스테이블코인 출시의 부트스트랩 문제를 해결했다.

    아키텍처는 달러 스테이블코인을 넘어 stETH/ETH와 같은 리퀴드 스테이킹 파생상품으로 확장되었으며, 여기서 특화된 수학은 상대적으로 안정적인 비율을 유지해야 하는 자산에 적합했다. Curve는 래핑된 비트코인 변종과 EUR 스테이블코인을 포함한 다양한 페깅된 자산 카테고리의 주요 장소가 되었다.

    #### 시장 진화와 경쟁

    이러한 기술적 혁신과 네트워크 효과에도 불구하고, 경쟁 역학은 상당히 변화했다. 2023년 3월 USDC 디페깅 위기는 Curve 설계의 스트레스 테스트를 제공했다. USDC가 $0.88로 떨어지자, 트레이더들이 부실 자산에서 도망치면서 3pool은 USDC 쪽으로 심하게 불균형해졌다. 수학은 설계대로 작동했고 USDC 회복 후 풀이 재균형되었지만, 위기는 극단적 시장 스트레스 하에서 AMM 기반 스테이블코인 거래의 회복력과 한계 모두를 드러냈다.

    Curve의 수학적 이점과 확립된 유동성은 Uniswap v3의 집중 유동성으로부터의 시장 점유율 침식을 막지 못했다. Uniswap의 0.01% 수수료 티어는 Curve의 가격 책정과 맞먹었고, 집중 유동성은 정교한 공급자들이 유사한 자본 효율성을 달성할 수 있게 했다. Uniswap의 더 접근 가능한 사용자 경험과 더 넓은 생태계 통합과 결합되어, 이 경쟁적 변화는 지형을 역전시켰다. Uniswap은 현재 USDC/USDT 스왑에서 일일 2억 2천만 달러 이상을 처리하는 반면, Curve는 모든 스테이블코인 풀에서 약 4천 4백만 달러를 처리한다.

    ### 본딩 커브 런치패드

    Uniswap과 Curve가 기존 토큰 거래에 집중하는 반면, 관련 혁신은 유사한 수학적 곡선을 다른 문제를 해결하는 데 적용한다: 새로운 토큰이 어떻게 존재하게 되고 초기 가격을 찾는가. 본딩 커브 런치패드가 등장하기 전에, 토큰 출시는 일반적으로 Uniswap이나 Raydium과 같은 AMM으로 직접 진행하는 것을 의미했다. 개발팀은 자신의 토큰을 만들고 자체 자본을 사용하여 초기 유동성 풀을 시딩했으며, 보통 ETH, SOL 또는 스테이블코인과 페어링했다. 그들은 나중에 풀을 "러그"할 수 없음을 보여주기 위해 종종 LP 토큰을 소각하거나 잠갔다. 이 접근법은 토큰 출시를 자본 집약적으로 만들고 특정 신뢰 가정을 확립했다: 사용자는 팀이 유동성을 인출하거나, 임의로 새 토큰을 발행하거나, 풀 주변의 특권적 위치를 남용하지 않을 것이라고 믿어야 했다.

    Pump.fun은 **본딩 커브(Bonding Curve)**에 의해 지배되는 별도의 "프리-AMM" 단계를 도입함으로써 이 파이프라인을 근본적으로 재구성했다. Solana에 구축된 이것은 누구나 토큰을 만들고 그것이 즉시 곡선 기반 컨트랙트에서 거래되는 것을 볼 수 있는 무허가 런치패드로 기능한다. 누군가가 새 토큰을 출시하면, 고정 공급량(일반적으로 10억 단위)이 발행된다. 약 8억 개의 토큰이 본딩 커브에서 사용 가능하게 되고, 나머지 약 2억 개는 생성자에게 할당되어 일반적으로 토큰이 졸업한 후 초기 유동성 포지션으로 재활용된다.

    곡선은 SOL에 대해 토큰을 판매하며, 8억 개의 토큰 중 더 많이 구매될수록 가격이 비선형적으로 상승하고 곡선에 다시 판매하면 하락한다. 실제로 생성자도 출시 시 곡선에서 즉시 구매할 수 있다. 이것은 더 넓은 관심이 도착하기 전에 가장 낮은 가격에 초기 포지션을 구축할 자연스러운 기회를 제공한다.

    본딩 커브가 정의된 완료 임계값에 도달하면(효과적으로, 플랫폼이 지정한 수의 토큰이 판매되고 목표 SOL 금액이 축적되면), 토큰은 "졸업"한다. 이 중요한 순간에 시스템은 다운스트림 AMM에 유동성 풀을 자동으로 시딩하고 결합된 SOL과 토큰을 그 안으로 전송하며, 종종 결과로 나온 LP 토큰을 소각한다. 역사적으로 이것은 Raydium에 풀을 만드는 것을 의미했다. 더 최근에 Pump.fun은 졸업한 토큰을 자체 AMM인 PumpSwap으로 라우팅하며, 그곳에서 다른 Solana 토큰처럼 거래된다.

    사용자에게 이 설계는 발행, 초기 가격 발견, AMM 상장을 단일 자동화 파이프라인으로 압축한다. Pump.fun의 컨트랙트는 팀이 풀을 수동으로 설정하고 LP를 소각하는 대신 풀 생성과 LP 토큰 소각을 뒤에서 처리한다. PumpSwap이 수직 통합되어 있기 때문에, 플랫폼은 또한 2차 거래에 프로토콜 수수료를 부과하고 그 수수료의 일부를 토큰 생성자와 공유할 수 있다. 이것은 성공적인 졸업을 일회성 본딩 커브 이벤트가 아닌 지속적인 수수료 흐름으로 바꾼다.

    이 아키텍처는 특정 신뢰 가정을 제거하면서 다른 것을 도입한다. 개발자는 더 이상 초기 단계에서 LP 토큰을 통제하지 않는다. 본딩 커브 컨트랙트는 가격 책정과 유동성을 강제하고, 졸업 로직은 AMM 풀을 자동으로 시딩한다. 그러나 참여자는 이제 단일 플랫폼의 컨트랙트와 백엔드의 정확성과 거버넌스에 의존하며, 중재, 지역 제한, 상장 규칙을 관리하는 오프체인 정책도 마찬가지이다.

    생성자는 여전히 의미 있는 공급 비율을 보유하고 곡선에서 일찍 구매할 수 있다. 이것은 고전적인 LP 인출 러그가 실행하기 어려워지더라도 공격적인 매도를 통한 "소프트 러그"나 완전한 방치가 여전히 흔하다는 것을 의미한다. 실제로 수천 개의 일일 출시 중 극히 일부만이 곡선에서 졸업한다. 평생 평균은 낮은 한 자릿수(전체 토큰의 약 1-2% 졸업)에 머물며, 일일 졸업률은 일반적으로 3% 미만이고 피크 열광 기간에만 가끔 4%를 초과한다. 대부분의 토큰은 단명한 사회적 실험으로 제자리에서 죽는다.

    이러한 위험에도 불구하고, 또는 아마도 그 때문에, Pump.fun은 2024-2025 사이클에서 가장 영향력 있는 소매 대상 암호화폐 애플리케이션 중 하나가 되었다. 토큰 생성의 비용과 마찰을 거의 0으로 줄이고, "토큰" 자체를 일회용 사회적 객체로 변환했으며, 대규모 밈코인 물결을 촉발하는 데 도움을 주었다. 많은 자산이 기존 AMM에 도달하기 전에 본딩 커브에서 시작했다. 이 모델은 전염성이 있음을 증명했다: 본딩 커브 런치패드와 Pump.fun 클론이 다른 L1과 L2에 빠르게 나타났으며, 이 "팩토리 플러스 커브 플러스 AMM 졸업" 파이프라인을 투기적 토큰 발행의 표준 패턴으로 확립했다.

    개념적으로, 본딩 커브 런치패드는 이 섹션의 나머지 부분에서 설명된 거래소 아키텍처의 상류에 위치한다. 그들은 Uniswap이나 Curve가 하는 방식의 범용 DEX는 아니지만, 1차 발행, 초기 가격 발견, 초기 유동성 제공을 자동화하기 위해 유사한 수학적 원리를 사용한다. AMM은 토큰이 졸업한 후에도 여전히 롱테일 거래를 처리한다. 본딩 커브는 단순히 누가 시드 자본을 제공해야 하는지와 토큰 존재의 가장 초기, 가장 반사적인 단계에서 사용자가 무엇을 신뢰해야 하는지를 변화시켰다.

    ### 대안적 거래소 아키텍처

    AMM 혁명은 거래소 설계에서 추가 혁신을 촉발했으며, 각각은 거래 문제의 다른 측면을 해결한다.

    #### 인텐트 기반 시스템

    CoW Swap과 UniswapX와 같은 인텐트 기반 플랫폼은 전통적인 트랜잭션 명세에서의 패러다임 전환을 나타낸다. 사용자가 정확한 스왑 경로와 매개변수를 구성하는 대신, 그들은 "다음 2분 내에 내 1 ETH에 대해 최소 1,000 USDC를 받고 싶다"와 같은 원하는 결과를 설명하는 고수준 "인텐트"에 서명한다.

    오프체인 솔버("필러"라고도 불림)가 이러한 인텐트를 이행하기 위해 경쟁하며, 최상의 체결을 위해 여러 장소에 라우팅한다. CoW Swap은 솔버가 여러 주문을 동시에 이행하기 위해 입찰을 제출하는 배치 옥션을 사용하며, 종종 AMM 유동성을 건드리지 않고 주문이 서로에 대해 직접 정산될 수 있는 우연의 일치(CoW)를 찾는다. UniswapX는 필러가 받을 때까지 제공 가격이 점진적으로 개선되는 더치 옥션을 사용한다.

    솔버가 여러 유동성 소스에 접근하고 거래를 내재화할 수 있으므로, 사용자는 종종 직접 AMM 스왑보다 더 나은 가격을 얻는다. UniswapX는 추가로 필러가 가스 수수료를 지불하는 가스리스 제출을 가능하게 하여 사용자 경험을 개선한다. 경쟁적 솔버 옥션이 단일 행위자가 가치를 추출하기 어렵게 만들므로, 두 시스템 모두 MEV 보호를 제공한다.

    #### 호가 요청 시스템

    호가 요청(Request-for-Quote, RFQ) 시스템은 오프체인 효율성과 온체인 정산을 결합하여 전문 시장 조성을 DeFi에 가져온다. Hashflow와 0x RFQ와 같은 플랫폼은 사용자가 현재 조건에 기반한 보장된 가격을 제공하는 시장 조성자에게 확정 호가를 요청할 수 있게 한다.

    시장 조성자는 재고, 헤징 비용, 원하는 마진을 고려하여 오프체인에서 가격을 호가한다. 사용자가 호가를 수락하면, 정산은 슬리피지 위험 없이 보장된 가격으로 온체인에서 발생한다. 이 접근법은 AMM 가격 영향이 상당한 더 큰 거래와 탈중앙화보다 체결 확실성을 중시하는 기관 사용자에게 효과적이다.

    #### 탈중앙화 무기한 거래소

    현물 거래를 넘어, 탈중앙화 무기한 거래소가 빠르게 성장하여 온체인 레버리지와 경쟁력 있는 성능을 제공한다. Chapter VI가 중앙화 거래소의 무기한 선물 메커니즘을 다루었지만, 이 섹션은 탈중앙화 대응물에 초점을 맞춘다. GMX와 같은 플랫폼은 거래를 뒷받침하는 LP 풀과 함께 합성 가격 책정을 사용하고, dYdX는 원래 더 나은 성능을 위해 StarkEx에 구축했다가 자체 앱 전용 블록체인을 출시했다. 이러한 발전은 DeFi가 어떻게 가능한 금융 서비스의 범위를 계속 확장하는지 보여준다.

    Hyperliquid와 같은 앱 전용 체인은 거래에 완전히 최적화된 자체 블록체인을 운영하며, 범용 연산보다 속도와 오더북 효율성을 우선시한다. 이 아키텍처는 범용 L1에서는 비실용적인 1초 미만의 최종성과 복잡한 주문 유형을 가능하게 한다. Chapter X는 Hyperliquid의 접근법을 심층적으로 검토한다.

    각 모델은 다른 우선순위의 균형을 맞춘다: AMM은 탈중앙화와 조합 가능성을 우선시하고, RFQ 시스템은 체결 품질을 최적화하며, 앱 전용 체인은 성능을 극대화한다. 최적의 선택은 특정 사용 사례, 성능 요구사항, 위험 허용도에 따라 다르다.

## Section III: Lending and Borrowing Fundamentals

=== "EN"

    With on-chain price formation and liquidity established through DEXs, these pricing mechanisms enable the next layer of DeFi infrastructure: lending and borrowing. These protocols form the foundation of the ecosystem, providing the liquidity and leverage that power more complex strategies.

    The most common safety metric for lending protocols is the Health Factor (HF), which measures how close a position is to liquidation. While Chapter VI covered liquidation in the context of centralized exchanges and perpetual futures, DeFi protocols implement similar mechanics entirely on-chain through smart contracts. The Health Factor is calculated based on the ratio of collateral value to debt value, adjusted for liquidation thresholds. An HF above 1 means the position is healthy; below 1 means it can be liquidated.

    ### Aave: Building the Automated Lending Infrastructure

    Aave operates like an automated bank that never closes, using smart contracts to evaluate collateral and approve loans based on pre-defined rules rather than human underwriters. The protocol has evolved significantly since its inception, with each version addressing real limitations users faced in practice.

    For lenders, the process remains straightforward across all versions. A participant deposits assets like ETH, USDC, or other supported tokens into shared liquidity pools and immediately starts earning interest. Deposits are represented by special tokens called aTokens, whose balance in your wallet automatically increases over time as interest accrues. Borrowers must maintain more collateral than they borrow, a design known as **over-collateralization**. For example, depositing $1,000 of ETH might allow borrowing only $800 of USDC, with the $200 buffer protecting lenders from price volatility. This collateral requirement is fundamental to trustless lending, since protocols can't sue defaulters or garnish wages. They need sufficient assets on hand to liquidate when positions become unhealthy.

    #### Who Uses Collateralized Lending

    Aave's lending model serves multiple use cases that explain its popularity, with the protocol having around $60B in total deposits and nearly $25B in active borrows in early 2026\. Many users want liquidity without selling assets they believe will appreciate, an ETH holder may need stablecoins for expenses or new opportunities. Borrowing preserves upside potential while deferring capital gains taxes that selling would trigger immediately.

    Leveraged trades represent another major use case. Users deposit ETH, borrow stablecoins, then buy more ETH through "looping" strategies that amplify exposure, for example, depositing $1,000 of ETH, borrowing $800 USDC, buying more ETH, and repeating until the Health Factor approaches the participant's risk tolerance (e.g., HF ≈ 1.2 for aggressive leverage). Alternatively, staked assets like stETH can serve as collateral to boost yield through measured leverage, combining staking rewards with borrowing strategies.

    Beyond basic lending, these platforms enable shorting and hedging by allowing users to borrow assets they expect to decline and sell them immediately, creating on-chain prime brokerage functionality. Safe shorting requires the borrowed asset to have sufficient liquidity and reliable oracle pricing to prevent manipulation during liquidations. This helps hedge concentrated positions or farming rewards without unwinding entire strategies, maintaining core exposure while managing specific risks.

    Professional traders use the platforms for arbitrage and carry trades, borrowing cheap stablecoins to earn higher yields elsewhere and capturing futures basis, funding rate premiums, or liquid staking token spreads. These strategies exploit rate differentials across DeFi protocols and traditional markets.

    #### Risk Management Through Key Parameters

    Aave manages lending risk through parameters that determine borrowing limits and liquidation triggers. **Loan-to-Value (LTV)** ratios set maximum borrowing power per asset, an 80% LTV means depositing $100 allows borrowing up to $80. Liquidation thresholds define when positions become undercollateralized and eligible for liquidation, always set higher than LTV ratios to create safety buffers. Liquidation bonuses provide incentives for third parties to maintain system solvency by repaying bad debt in exchange for discounted collateral.

    Interest rates adjust automatically based on pool utilization through mathematical curves. High demand increases rates to attract lenders and discourage excessive borrowing. Low utilization decreases rates to encourage borrowing and provide competitive returns. Markets self-balance through these algorithmic adjustments.

    #### Evolution Through Protocol Versions

    Aave v1 introduced the basic concept of pooled lending with interest-bearing tokens and pioneered **flash loans** (see Section V: Infrastructure Dependencies), enabling users to borrow and repay large amounts of capital within a single transaction for arbitrage and liquidations.

    Aave v2 added debt tokenization (non-transferable tokens that represent the borrower's debt), plus credit delegation, collateral swaps, and repay-with-collateral, all of which improved composability and UX. The version also reduced gas costs and improved user experience. Credit delegation allowed trusted parties to borrow against others' collateral without direct access to the underlying assets.

    Aave v3 brought targeted improvements for risk management and liquidity optimization. Isolation modes allowed the protocol to safely list long-tail assets without endangering the broader system, while efficiency modes offered better rates for closely correlated asset pairs like stablecoins. The protocol added variable liquidation close factors, allowing liquidators to close up to 100% of very unhealthy positions to remove bad debt efficiently.

    The forthcoming Aave v4 represents a fundamental architectural shift. Instead of separate pools for each market, the protocol is moving to a Unified Liquidity Layer with a central Liquidity Hub and asset-specific Spokes. This design dramatically improves how markets share liquidity while maintaining safety through compartmentalized risk management per asset type.

    This evolution illustrates DeFi's constant push toward better liquidity utilization while managing risk. Each version solved real problems users faced, from capital fragmentation to gas costs to risk isolation.

    Aave's ecosystem extends beyond lending through GHO, its own over-collateralized stablecoin, transforming the platform from a simple lender into a broader monetary system. When users mint GHO by supplying collateral to Aave, the interest payments flow directly to the Aave DAO treasury, creating a revenue stream for the protocol itself. This makes GHO both a stablecoin and an integral part of Aave's ecosystem, governed entirely by Aave governance.

    ### Euler and Morpho: Isolated Permissionless Markets

    The pooled, blue-chip-focused design that Aave popularized is not the only way to build a lending protocol. Euler and Morpho push further toward isolated, permissionless markets with explicit separation between infrastructure and risk decisions.

    Euler's original design already stood apart through permissionless listing and a tiered risk system that isolated riskier assets. Euler v2 expands this modular approach through the Euler Vault Kit (EVK), a framework for deploying credit vaults. Anyone can launch an isolated lending vault for an ERC-20 asset and configure custom parameters: accepted collateral types, LTVs and caps, interest rate models, and oracle sources. Each vault functions as its own market with its own risk parameters, so issues in one vault don't contaminate others. Tools like the Ethereum Vault Connector and EulerEarn connect vaults, enable cross-collateralization, and aggregate yields. Euler becomes a meta-lending layer that supports everything from conservative blue-chip markets to experimental long-tail configurations while preserving risk isolation.

    Morpho evolved in a parallel direction. The project began as a P2P optimizer on top of Aave and Compound, but Morpho Blue re-architected it as a minimal trustless lending primitive. A Morpho Blue market is extremely simple: one loan asset, one collateral asset, a liquidation LTV, an oracle, and an interest rate model. Markets are permissionlessly created and fully isolated with parameters fixed at creation from governance-approved menus. Above this base layer sits MetaMorpho, a protocol for lending vaults built on Morpho Blue. Anyone can create a vault that allocates deposits across multiple Morpho Blue markets according to a strategy. This is where **risk curators** come in.

    #### Risk Curators and Vault-Based Lending

    A risk curator is an entity (often a specialized risk firm, DAO, or fund) that designs and deploys vaults, chooses which markets the vault supplies liquidity to and in what proportions, sets risk parameters at creation time within protocol constraints, and earns a fee for providing this risk management service. On Morpho, curators use MetaMorpho vaults to route depositor funds into selected markets. They decide which markets a vault can lend into, adjust allocation weights over time, and impose additional vault-level rules like caps and fee structures. Curators include specialist risk firms and DeFi-native asset managers: Gauntlet, Steakhouse, MEV Capital, RE7 Labs, and Moonwell have all launched or managed curated vaults.

    There's an important distinction between risk service providers like Chaos Labs on Aave and risk curators on Morpho and Euler. On Aave, risk firms advise the DAO and publish parameter recommendations, but governance executes changes for all users. Users don't opt into specific risk managers; they use Aave's globally-set parameters. On Morpho and Euler, risk curators own the strategy for a given vault. Users choose a particular vault and thereby opt into that curator's allocation and risk decisions.

    By early 2026, risk-curator-style vaults had grown to nearly $11 billion in deposits, about 10% of all DeFi lending **TVL** (Total Value Locked, the standard measure of assets deposited in a protocol), down from a $13 billion peak after de-risking. Several aggressive vaults that chased yield by accepting riskier stablecoins or thin-liquidity collaterals suffered losses or severe liquidity constraints, with some lenders temporarily stuck or taking haircuts when underlying assets de-pegged or markets froze.

    This highlights both sides of the model. Risk curators can specialize, build sophisticated portfolios across many isolated markets, and offer higher risk-adjusted yields than generic pools. Long-tail assets can be supported without forcing every depositor to bear their risk. However, depositors are exposed not only to protocol-level smart contract and oracle risk, but also to curator behavior: their asset selection, concentration, and reaction speed in stressed conditions. For protocols like Morpho and Euler, the decision of which vault or curator to trust can be just as important as the choice of underlying protocol.

    ### Sky: The Decentralized Central Bank

    While Aave revolutionized peer-to-pool lending, another approach emerged that treats stablecoin issuance fundamentally differently. Sky (formerly MakerDAO) operates like a decentralized central bank that issues USDS stablecoins backed by crypto collateral and real-world assets. (For a broader overview of stablecoin types and mechanisms, see Chapter IX.)

    The Vault system operates through protocol allocators ("Stars") who mint USDS via Vaults and deploy liquidity. Most end users typically upgrade DAI to USDS 1:1 or acquire USDS on markets, then opt into sUSDS to earn the Sky Savings Rate (SSR). Like Aave, the system requires collateral buffers, but the protocol creates newly minted stablecoins rather than lending from existing pools. This distinction matters because it means Sky can create new money supply based on collateral deposits.

    Maintaining the peg requires multiple mechanisms working together. The LitePSM acts like an exchange window, enabling fixed-rate swaps between USDS/DAI and other stablecoins (like USDC) to help maintain the $1 peg. This provides immediate arbitrage opportunities when USDS trades away from $1. The Sky Savings Rate works like a demand lever, governance can adjust the rate to influence demand for holding and saving USDS, which supports the peg by making the stablecoin more attractive to hold.

    Sky represents evolution from its original DAI system to the new USDS framework, with DAI and USDS currently coexisting during the Sky rebrand and voluntary upgrade migration. The protocol increasingly backs stablecoins with real-world assets like Treasury bills alongside crypto collateral, blending DeFi innovation with traditional finance stability.

    ### Wildcat: Institutional Credit On-Chain

    Both Aave and Sky require substantial collateral buffers, but Wildcat brings traditional credit relationships on-chain instead. The protocol connects institutional borrowers like market makers, hedge funds and even protocols with crypto lenders seeking potentially higher yields than fully-collateralized protocols can provide.

    This alternative approach stems from a fundamental difference in collateralization philosophy. Unlike Aave and Sky's asset-backed collateral, Wildcat is intentionally under-collateralized and relies on a reserve-ratio liquidity buffer rather than full asset backing. This fundamental difference explains why Wildcat can offer higher yields while introducing explicit counterparty credit risk.

    Wildcat operates as a marketplace where borrowers set all key parameters including fixed APR rates, lockup periods, and withdrawal windows without any protocol-level underwriting. They can also implement access control through allowlists or enable self-onboarding with OFAC screening via Chainalysis oracle. Additionally, borrowers may require lenders to sign legal agreements off-chain to establish formal credit relationships.

    Risk management mechanics become especially critical when things go wrong. If reserves fall below the required level, the market becomes delinquent and withdrawals are restricted while penalty fees accrue until the borrower replenishes reserves. Actual losses only materialize if the borrower ultimately defaults, which is why Wildcat requires participants to actively manage counterparty risk through due diligence on borrower reputation.

    These risks aren't merely theoretical, they materialized in mid 2025 when Kinto, a DeFi platform that had borrowed through Wildcat's facility following a major hack, announced its shutdown and became Wildcat's first official default. There were more than ten lenders in Kinto's facility and they faced a 24% haircut, recovering 76% of their principal from the borrower's remaining assets. This default demonstrated both the isolation of losses to specific facilities, with no contagion to Wildcat's other $150+ million in outstanding loans, and the real-world implications of Wildcat's undercollateralized lending model.

    The Kinto default illustrates a broader principle about DeFi's evolution: while programmability doesn't eliminate credit risk, it can make it more transparent and controllable through fully on-chain, transparent credit markets with customizable terms. Wildcat represents this philosophy in practice, bringing traditional credit relationships into the programmable, transparent world of DeFi.

=== "KO"

    DEX를 통해 온체인 가격 형성과 유동성이 확립되면서, 이러한 가격 책정 메커니즘은 DeFi 인프라의 다음 레이어인 대출과 차입을 가능하게 한다. 이러한 프로토콜은 생태계의 기반을 형성하며, 더 복잡한 전략을 구동하는 유동성과 레버리지를 제공한다.

    대출 프로토콜의 가장 일반적인 안전 지표는 **건강 계수(Health Factor, HF)**로, 포지션이 청산에 얼마나 가까운지를 측정한다. Chapter VI가 중앙화 거래소와 무기한 선물의 맥락에서 청산을 다루었지만, DeFi 프로토콜은 스마트 컨트랙트를 통해 완전히 온체인에서 유사한 메커니즘을 구현한다. 건강 계수는 청산 임계값으로 조정된 담보 가치 대 부채 가치의 비율을 기반으로 계산된다. HF가 1 이상이면 포지션이 건강하다는 의미이고; 1 미만이면 청산될 수 있다.

    ### Aave: 자동화된 대출 인프라 구축

    Aave는 결코 문을 닫지 않는 자동화된 은행처럼 운영되며, 인간 심사관 대신 스마트 컨트랙트를 사용하여 사전 정의된 규칙에 따라 담보를 평가하고 대출을 승인한다. 프로토콜은 설립 이후 상당히 발전했으며, 각 버전은 사용자가 실제로 직면한 한계를 해결한다.

    대출자에게 프로세스는 모든 버전에서 간단하게 유지된다. 참여자는 ETH, USDC 또는 기타 지원 토큰과 같은 자산을 공유 유동성 풀에 예치하고 즉시 이자를 얻기 시작한다. 예치금은 aToken이라는 특수 토큰으로 표현되며, 지갑에서의 잔액은 이자가 누적됨에 따라 시간이 지나면서 자동으로 증가한다. 차입자는 빌리는 것보다 더 많은 담보를 유지해야 하며, 이 설계는 **초과 담보(Over-collateralization)**로 알려져 있다. 예를 들어, $1,000의 ETH를 예치하면 $800의 USDC만 빌릴 수 있으며, $200의 버퍼가 대출자를 가격 변동성으로부터 보호한다. 이 담보 요구사항은 무신뢰 대출에 근본적이다. 프로토콜은 채무 불이행자를 고소하거나 임금을 압류할 수 없기 때문이다. 포지션이 건강하지 않게 되면 청산하기 위해 충분한 자산을 손에 가지고 있어야 한다.

    #### 담보 대출 사용자

    Aave의 대출 모델은 여러 사용 사례를 충족시키며, 이는 프로토콜이 2026년 초 기준 약 $600억의 총 예치금과 거의 $250억의 활성 대출을 보유한 인기를 설명한다. 많은 사용자는 가치가 상승할 것으로 믿는 자산을 매도하지 않고 유동성을 원한다, ETH 보유자는 비용이나 새로운 기회를 위해 스테이블코인이 필요할 수 있다. 차입은 매도가 즉시 유발할 양도소득세를 연기하면서 상승 잠재력을 보존한다.

    레버리지 거래는 또 다른 주요 사용 사례를 나타낸다. 사용자는 ETH를 예치하고, 스테이블코인을 빌리고, 더 많은 ETH를 구매하는 "루핑" 전략을 통해 노출을 증폭한다, 예를 들어, $1,000의 ETH를 예치하고, $800 USDC를 빌리고, 더 많은 ETH를 사고, 건강 계수가 참여자의 위험 허용도(예: 공격적 레버리지의 경우 HF ≈ 1.2)에 접근할 때까지 반복한다. 대안적으로, stETH와 같은 스테이킹된 자산은 스테이킹 보상과 차입 전략을 결합하여 측정된 레버리지를 통해 수익을 높이는 담보 역할을 할 수 있다.

    기본 대출을 넘어, 이러한 플랫폼은 사용자가 하락할 것으로 예상하는 자산을 빌려 즉시 매도할 수 있게 하여 공매도와 헤징을 가능하게 하며, 온체인 프라임 브로커리지 기능을 만든다. 안전한 공매도는 차입 자산이 충분한 유동성과 청산 중 조작을 방지하기 위한 신뢰할 수 있는 오라클 가격 책정을 갖추어야 한다. 이것은 전체 전략을 풀지 않고 집중된 포지션이나 파밍 보상을 헤지하는 데 도움이 되며, 특정 위험을 관리하면서 핵심 노출을 유지한다.

    전문 트레이더는 플랫폼을 차익 거래와 캐리 트레이드에 사용하며, 저렴한 스테이블코인을 빌려 다른 곳에서 더 높은 수익을 얻고 선물 베이시스, 펀딩 비율 프리미엄 또는 리퀴드 스테이킹 토큰 스프레드를 포착한다. 이러한 전략은 DeFi 프로토콜과 전통 시장 간의 금리 차이를 활용한다.

    #### 핵심 매개변수를 통한 위험 관리

    Aave는 대출 한도와 청산 트리거를 결정하는 매개변수를 통해 대출 위험을 관리한다. **담보 대출 비율(Loan-to-Value, LTV)**은 자산별 최대 대출력을 설정한다, 80% LTV는 $100를 예치하면 최대 $80까지 빌릴 수 있음을 의미한다. 청산 임계값은 포지션이 담보 부족 상태가 되어 청산 대상이 되는 시점을 정의하며, 항상 LTV 비율보다 높게 설정되어 안전 버퍼를 만든다. 청산 보너스는 제3자가 할인된 담보와 교환하여 부실 채권을 상환함으로써 시스템 지급 능력을 유지하도록 인센티브를 제공한다.

    이자율은 수학적 곡선을 통해 풀 활용도에 따라 자동으로 조정된다. 높은 수요는 대출자를 유치하고 과도한 차입을 억제하기 위해 금리를 높인다. 낮은 활용도는 차입을 장려하고 경쟁력 있는 수익을 제공하기 위해 금리를 낮춘다. 시장은 이러한 알고리즘 조정을 통해 자체 균형을 맞춘다.

    #### 프로토콜 버전을 통한 진화

    Aave v1은 이자 수익 토큰을 통한 풀 대출의 기본 개념을 도입하고 **플래시론(Flash Loan)**(Section V: 인프라 의존성 참조)을 개척하여 사용자가 차익 거래와 청산을 위해 단일 트랜잭션 내에서 대량의 자본을 빌리고 상환할 수 있게 했다.

    Aave v2는 부채 토큰화(차입자의 부채를 나타내는 양도 불가능한 토큰), 신용 위임, 담보 스왑, 담보로 상환을 추가하여 조합 가능성과 UX를 개선했다. 이 버전은 또한 가스 비용을 줄이고 사용자 경험을 개선했다. 신용 위임은 신뢰할 수 있는 당사자가 기초 자산에 직접 접근하지 않고 다른 사람의 담보에 대해 빌릴 수 있게 했다.

    Aave v3는 위험 관리와 유동성 최적화를 위한 표적 개선을 가져왔다. 격리 모드는 프로토콜이 더 넓은 시스템을 위험에 빠뜨리지 않고 롱테일 자산을 안전하게 상장할 수 있게 했고, 효율 모드는 스테이블코인과 같이 밀접하게 상관된 자산 쌍에 더 나은 금리를 제공했다. 프로토콜은 가변 청산 종결 비율을 추가하여 청산인이 부실 채권을 효율적으로 제거하기 위해 매우 건강하지 않은 포지션의 최대 100%까지 종결할 수 있게 했다.

    다가오는 Aave v4는 근본적인 아키텍처 전환을 나타낸다. 각 시장에 대한 별도 풀 대신, 프로토콜은 중앙 유동성 허브와 자산별 스포크가 있는 통합 유동성 레이어로 이동하고 있다. 이 설계는 자산 유형별로 구획화된 위험 관리를 유지하면서 시장이 유동성을 공유하는 방식을 극적으로 개선한다.

    이 진화는 위험을 관리하면서 더 나은 유동성 활용을 향한 DeFi의 지속적인 추진을 보여준다. 각 버전은 자본 분산에서 가스 비용, 위험 격리에 이르기까지 사용자가 직면한 실제 문제를 해결했다.

    Aave의 생태계는 자체 초과 담보 스테이블코인인 GHO를 통해 대출을 넘어 확장되어, 플랫폼을 단순한 대출자에서 더 넓은 화폐 시스템으로 변환한다. 사용자가 Aave에 담보를 공급하여 GHO를 발행하면, 이자 지불은 Aave DAO 재무로 직접 흘러가 프로토콜 자체를 위한 수익 흐름을 만든다. 이것은 GHO를 스테이블코인이자 Aave 거버넌스에 의해 완전히 관리되는 Aave 생태계의 필수적인 부분으로 만든다.

    ### Euler와 Morpho: 격리된 무허가 시장

    Aave가 대중화한 풀링된 블루칩 중심 설계는 대출 프로토콜을 구축하는 유일한 방법이 아니다. Euler와 Morpho는 인프라와 위험 결정 사이의 명시적 분리를 가진 격리된 무허가 시장으로 더 나아간다.

    Euler의 원래 설계는 이미 무허가 상장과 더 위험한 자산을 격리하는 계층화된 위험 시스템을 통해 차별화되었다. Euler v2는 크레딧 볼트 배포를 위한 프레임워크인 Euler Vault Kit(EVK)를 통해 이 모듈형 접근법을 확장한다. 누구나 ERC-20 자산에 대한 격리된 대출 볼트를 출시하고 맞춤 매개변수를 구성할 수 있다: 허용되는 담보 유형, LTV 및 상한, 이자율 모델, 오라클 소스. 각 볼트는 자체 위험 매개변수를 가진 자체 시장으로 기능하므로, 한 볼트의 문제가 다른 볼트를 오염시키지 않는다. Ethereum Vault Connector와 EulerEarn과 같은 도구는 볼트를 연결하고, 교차 담보화를 가능하게 하며, 수익을 집계한다. Euler는 위험 격리를 유지하면서 보수적인 블루칩 시장에서 실험적인 롱테일 구성까지 모든 것을 지원하는 메타 대출 레이어가 된다.

    Morpho는 병렬 방향으로 진화했다. 프로젝트는 Aave와 Compound 위의 P2P 최적화기로 시작했지만, Morpho Blue는 최소 신뢰 대출 프리미티브로 재설계했다. Morpho Blue 시장은 매우 단순하다: 하나의 대출 자산, 하나의 담보 자산, 청산 LTV, 오라클, 이자율 모델. 시장은 무허가로 생성되고 완전히 격리되며 매개변수는 거버넌스 승인 메뉴에서 생성 시 고정된다. 이 기본 레이어 위에 Morpho Blue 위에 구축된 대출 볼트를 위한 프로토콜인 MetaMorpho가 있다. 누구나 전략에 따라 여러 Morpho Blue 시장에 예치금을 할당하는 볼트를 만들 수 있다. 여기서 **위험 큐레이터(Risk Curator)**가 등장한다.

    #### 위험 큐레이터와 볼트 기반 대출

    위험 큐레이터는 볼트를 설계하고 배포하는 주체(종종 전문 위험 회사, DAO 또는 펀드)로, 볼트가 어떤 시장에 유동성을 공급하고 어떤 비율로 할지 선택하고, 프로토콜 제약 내에서 생성 시 위험 매개변수를 설정하며, 이 위험 관리 서비스를 제공하는 대가로 수수료를 받는다. Morpho에서 큐레이터는 MetaMorpho 볼트를 사용하여 예치자 자금을 선택된 시장으로 라우팅한다. 그들은 볼트가 어떤 시장에 대출할 수 있는지 결정하고, 시간에 따라 할당 가중치를 조정하며, 상한 및 수수료 구조와 같은 추가적인 볼트 수준 규칙을 부과한다. 큐레이터에는 전문 위험 회사와 DeFi 네이티브 자산 관리자가 포함된다: Gauntlet, Steakhouse, MEV Capital, RE7 Labs, Moonwell이 모두 큐레이팅된 볼트를 출시하거나 관리했다.

    Aave의 Chaos Labs와 같은 위험 서비스 제공자와 Morpho 및 Euler의 위험 큐레이터 사이에는 중요한 구별이 있다. Aave에서 위험 회사는 DAO에 조언하고 매개변수 권장 사항을 발표하지만, 거버넌스는 모든 사용자에 대한 변경을 실행한다. 사용자는 특정 위험 관리자를 선택하지 않는다; 그들은 Aave의 전역적으로 설정된 매개변수를 사용한다. Morpho와 Euler에서 위험 큐레이터는 주어진 볼트에 대한 전략을 소유한다. 사용자는 특정 볼트를 선택하여 그 큐레이터의 할당 및 위험 결정에 참여한다.

    2026년 초까지 위험 큐레이터 스타일 볼트는 약 $110억의 예치금으로 성장했으며, 이는 모든 DeFi 대출 **TVL(총 예치금, Total Value Locked, 프로토콜에 예치된 자산의 표준 측정)** 의 약 10%로, 위험 회피 후 $130억 최고점에서 하락했다. 더 위험한 스테이블코인이나 얇은 유동성 담보를 수용하여 수익을 추구한 여러 공격적 볼트는 손실이나 심각한 유동성 제약을 겪었으며, 일부 대출자는 기초 자산이 디페그되거나 시장이 동결되었을 때 일시적으로 갇히거나 헤어컷을 감수했다.

    이것은 모델의 양면을 부각시킨다. 위험 큐레이터는 전문화하고, 많은 격리된 시장에 걸쳐 정교한 포트폴리오를 구축하고, 일반 풀보다 더 높은 위험 조정 수익을 제공할 수 있다. 롱테일 자산은 모든 예치자가 그 위험을 부담하지 않고도 지원될 수 있다. 그러나 예치자는 프로토콜 수준의 스마트 컨트랙트 및 오라클 위험뿐만 아니라 큐레이터 행동: 자산 선택, 집중도, 스트레스 상황에서의 반응 속도에도 노출된다. Morpho와 Euler 같은 프로토콜의 경우, 어떤 볼트 또는 큐레이터를 신뢰할지에 대한 결정은 기초 프로토콜 선택만큼 중요할 수 있다.

    ### Sky: 탈중앙화 중앙은행

    Aave가 피어 투 풀 대출을 혁신한 반면, 스테이블코인 발행을 근본적으로 다르게 취급하는 또 다른 접근법이 등장했다. Sky(이전 MakerDAO)는 암호화폐 담보와 실물 자산으로 뒷받침되는 USDS 스테이블코인을 발행하는 탈중앙화 중앙은행처럼 운영된다. (스테이블코인 유형과 메커니즘에 대한 더 넓은 개요는 Chapter IX를 참조하라.)

    볼트 시스템은 볼트를 통해 USDS를 발행하고 유동성을 배치하는 프로토콜 할당자("Stars")를 통해 운영된다. 대부분의 최종 사용자는 일반적으로 DAI를 1:1로 USDS로 업그레이드하거나 시장에서 USDS를 취득한 다음, Sky Savings Rate(SSR)을 얻기 위해 sUSDS에 참여한다. Aave와 마찬가지로 시스템은 담보 버퍼를 필요로 하지만, 프로토콜은 기존 풀에서 대출하는 대신 새로 발행된 스테이블코인을 생성한다. 이 구별은 중요하다. Sky가 담보 예치에 기반하여 새로운 화폐 공급을 만들 수 있음을 의미하기 때문이다.

    페그를 유지하려면 여러 메커니즘이 함께 작동해야 한다. LitePSM은 교환 창구처럼 작동하여 USDS/DAI와 다른 스테이블코인(예: USDC) 간의 고정 환율 스왑을 가능하게 하여 $1 페그를 유지하는 데 도움을 준다. 이것은 USDS가 $1에서 벗어나 거래될 때 즉각적인 차익 거래 기회를 제공한다. Sky Savings Rate은 수요 레버처럼 작동하며, 거버넌스는 USDS 보유 및 저축에 대한 수요에 영향을 미치기 위해 금리를 조정할 수 있으며, 이는 스테이블코인을 보유하는 것을 더 매력적으로 만들어 페그를 지원한다.

    Sky는 원래 DAI 시스템에서 새로운 USDS 프레임워크로의 진화를 나타내며, Sky 리브랜딩과 자발적 업그레이드 마이그레이션 동안 DAI와 USDS가 현재 공존한다. 프로토콜은 암호화폐 담보와 함께 국채와 같은 실물 자산으로 스테이블코인을 점점 더 뒷받침하여 DeFi 혁신과 전통 금융 안정성을 혼합한다.

    ### Wildcat: 기관 신용의 온체인화

    Aave와 Sky 모두 상당한 담보 버퍼를 필요로 하지만, Wildcat은 대신 전통적인 신용 관계를 온체인에 가져온다. 프로토콜은 시장 조성자, 헤지펀드, 심지어 프로토콜과 같은 기관 차입자와 완전 담보 프로토콜이 제공할 수 있는 것보다 잠재적으로 더 높은 수익을 추구하는 암호화폐 대출자를 연결한다.

    이 대안적 접근법은 담보화 철학의 근본적인 차이에서 비롯된다. Aave와 Sky의 자산 담보와 달리, Wildcat은 의도적으로 저담보이며 완전한 자산 지원이 아닌 준비금 비율 유동성 버퍼에 의존한다. 이 근본적인 차이는 Wildcat이 명시적인 거래 상대방 신용 위험을 도입하면서 더 높은 수익을 제공할 수 있는 이유를 설명한다.

    Wildcat은 차입자가 고정 APR 금리, 잠금 기간, 인출 기간을 포함한 모든 주요 매개변수를 프로토콜 수준 심사 없이 설정하는 마켓플레이스로 운영된다. 그들은 또한 허용 목록을 통한 접근 제어를 구현하거나 Chainalysis 오라클을 통한 OFAC 스크리닝으로 셀프 온보딩을 가능하게 할 수 있다. 또한 차입자는 공식적인 신용 관계를 수립하기 위해 대출자가 오프체인에서 법적 계약에 서명하도록 요구할 수 있다.

    위험 관리 메커니즘은 상황이 잘못될 때 특히 중요해진다. 준비금이 요구 수준 이하로 떨어지면, 시장은 연체 상태가 되고 차입자가 준비금을 보충할 때까지 인출이 제한되고 위약금 수수료가 발생한다. 실제 손실은 차입자가 궁극적으로 채무 불이행할 경우에만 발생하며, 이것이 Wildcat이 참여자가 차입자 평판에 대한 실사를 통해 거래 상대방 위험을 적극적으로 관리하도록 요구하는 이유이다.

    이러한 위험은 이론적인 것만이 아니며, 2025년 중반 Wildcat의 시설을 통해 차입한 DeFi 플랫폼인 Kinto가 주요 해킹 이후 폐쇄를 발표하고 Wildcat의 첫 공식 채무 불이행이 되면서 현실화되었다. Kinto의 시설에는 10명 이상의 대출자가 있었고 그들은 24% 헤어컷에 직면했으며, 차입자의 남은 자산에서 원금의 76%를 회수했다. 이 채무 불이행은 특정 시설에 대한 손실 격리(Wildcat의 다른 $1.5억 이상의 미상환 대출에 대한 전염 없음)와 Wildcat의 저담보 대출 모델의 실제 영향 모두를 보여주었다.

    Kinto 채무 불이행은 DeFi 진화에 대한 더 넓은 원칙을 보여준다: 프로그래밍 가능성이 신용 위험을 제거하지 않지만, 맞춤형 조건을 가진 완전 온체인의 투명한 신용 시장을 통해 더 투명하고 통제 가능하게 만들 수 있다. Wildcat은 전통적인 신용 관계를 DeFi의 프로그래밍 가능하고 투명한 세계로 가져오는 이 철학을 실천한다.

## Section IV: Yield Generation and Optimization

=== "EN"

    With lending protocols and DEXs providing the foundational infrastructure, DeFi enables a new layer of sophistication: yield optimization strategies that either don't exist or are not available to retail investors in traditional finance. These mechanisms transform how we think about earning returns on capital, creating entirely new categories of financial opportunity.

    Each approach represents a different philosophy toward yield generation. The ecosystem spans from foundational mechanisms like staking and lending to more sophisticated strategies including liquidity provision, real-world asset yields, and complex derivative structures. To illustrate how these mechanisms work in practice, this section examines four innovative approaches that demonstrate DeFi's distinctive capabilities: delta-neutral hedging strategies that create stable returns, time-based derivatives that let traders exchange future yield itself, systematic options strategies that harvest volatility premiums, and speculative farming that bets on future token distributions.

    ### Ethena: Delta-Neutral Yield-Bearing Dollars

    Ethena demonstrates how DeFi can combine multiple financial primitives to create novel yield generation mechanisms. The protocol's USDe represents a new approach to synthetic dollar design through **delta-neutral** hedging, a strategy analogous to owning a stock while simultaneously shorting its futures. The gains and losses cancel out, leaving a stable position that still earns dividends. (For a broader examination of stablecoin categories including synthetic mechanisms like USDe, see Chapter IX.)

    The protocol backs USDe with staked ETH, BTC, other liquid staking tokens, and reserve assets while taking offsetting short positions in perpetual futures markets (Chapter VI). When users mint USDe, their collateral generates staking rewards while the short positions neutralize directional price exposure.

    Three revenue streams emerge. Staking rewards provide baseline yield from the underlying collateral. Funding rate payments from short perpetual positions typically generate additional returns, especially during bull markets when funding rates tend to be positive. Reserve income from T-bill-like assets provides a third yield component. The combination can produce attractive yields on what functions as a stable asset.

    Ethena's innovation lies in transforming stablecoin issuance from a passive backing mechanism into an active yield generation strategy. Users can further compound returns through sUSDe, which stakes their USDe holdings. This demonstrates how DeFi's composability enables financial products impossible in traditional systems.

    However, Ethena introduces unique risks worth noting. Funding rate risk becomes significant during bear markets when negative funding rates could erode yields. To mitigate this, Ethena maintains a reserve fund and dynamically reallocates backing assets into liquid stables earning Treasury-like rates during negative funding periods, protecting users from losses.

    Custody risk emerges from reliance on centralized exchanges for hedging positions. The risk is partially mitigated by relying on Off-Exchange Settlement (OES) providers including Copper, Ceffu, and Fireblocks to hold backing assets. While these providers use bankruptcy-remote trusts or MPC wallets to protect assets, operational issues could temporarily impede minting and redemption functionality. Ethena diversifies this across multiple OES providers and frequent PnL settlement with exchanges.

    Peg stability, while generally maintained through redemption mechanisms, is not absolute. USDe briefly traded as low as $0.62 on October 10th, 2025 during a Binance-specific event before recovering. Binance's yield programs had concentrated substantial leveraged USDe exposure on the exchange through looping opportunities, enabling 4-10x effective leverage. When the market crashed, Binance's internal pricing system triggered a liquidation cascade. Because this system relied primarily on its own spot market rather than broader multi-venue data, the thin USDe orderbook became severely illiquid.

    Critically, on-chain pools remained near $1 throughout this event and USDe stayed over-collateralized, demonstrating that the issue was venue-specific rather than systemic to USDe itself. This episode highlights an important distinction: oracle design and exchange-specific leverage concentration can create severe localized price deviations even when the underlying collateral structure remains sound.

    ### Pendle: Trading Time Itself

    While Ethena demonstrates yield generation through hedging strategies that neutralize price risk, Pendle takes a fundamentally different approach by deconstructing yield itself. Rather than creating stable returns through derivatives, Pendle enables users to separate and trade the time value of money directly.

    By taking yield-bearing assets like staked Ethereum or sUSDe and splitting them into two components, Pendle creates entirely new tradable instruments. The **Principal Token (PT)** represents a claim on the underlying asset at maturity, similar to a zero-coupon bond. The **Yield Token (YT)** represents a claim on all yield generated until maturity. The mathematical relationship ensures that PT price plus YT price tracks the underlying asset price, with small deviations that arbitrage typically closes, creating interesting trading opportunities.

    This separation enables sophisticated strategies. Users seeking fixed rates can sell the YT immediately after depositing, locking in a guaranteed return. Those speculating on higher future yields can buy YT tokens for leveraged exposure to rate changes. Others use various PT and YT combinations to hedge interest rate risk across their portfolios.

    PTs have become core collateral in lending markets like Aave, Euler, and Morpho. PT-sUSDe and PT-USDe markets on Aave grew from low nine figures into roughly low-single-digit billions in total PT supply across maturities, driven by aggressive fixed-yield leverage trades and incentives. For protocols, this became an appealing way to bootstrap TVL: every loop cycle locks more PT on the lending market and more underlying assets inside Pendle.

    The dominant PT use case became looping, a strategy where users deposit PTs as collateral on a lending market, borrow stablecoins against that collateral, use those stablecoins to buy more PT on Pendle, and repeat the cycle. Because PTs trade at a discount to the underlying asset and rise to full value at maturity, this loop effectively creates leveraged exposure to a fixed yield. The strategy works as long as borrowing costs stay below the PT's implied yield.

    Under favorable conditions with four to five times leverage, these loops have produced returns in the high double digits from the spread alone. Many setups also receive additional boosts from points programs and token incentives.

    However, that fixed return comes with a specific and asymmetric risk profile. PT looping is heavily dependent on how different platforms price these assets. Aave prices PTs based on Pendle's implied yields, with protective guardrails such as minimum PT prices and LTV “killswitches.” The USDe side is typically priced in a way that reduces sensitivity to short-term price swings but concentrates risk in tail events where Ethena itself fails.

    Other venues like Euler and some Morpho markets use more market-sensitive pricing that reacts to actual trading prices. This means short-lived price dislocations can make positions look undercollateralized even when the underlying collateral remains sound. Different pricing approaches across venues have already produced divergent outcomes in practice, with identical positions surviving on some platforms while being liquidated on others during the same market stress events.

    PT loops also create unwinding frictions. To exit, a user must reverse several steps: repay the borrowed stablecoin, withdraw PT collateral, and sell PT back into often thin Pendle liquidity. This makes positions far stickier than simple lending arrangements and adds execution risk, slippage, and transaction costs exactly when markets are stressed.

    PT looping is also extremely sensitive to borrowing costs and liquidity. The upside is capped once you lock in a fixed yield, but the downside remains open-ended. If borrowing rates spike above the PT's implied yield, the spread that made the strategy attractive can disappear or even turn negative. At the same time, PT liquidity on Pendle can be shallow relative to position sizes. In some cases, PT supply has exceeded ten times the available trading liquidity, leaving large positions exposed to severe price impact if forced to unwind quickly.

    The split-token model also creates more traditional vulnerabilities. YT tokens can be illiquid, especially for less popular assets, and their value is highly sensitive to changes in expected yields. Unwinding YT positions before maturity can involve substantial slippage, particularly during market stress when investors most want to exit.

    In contrast, PT-focused looping strategies offer a cleaner payoff structure but carry their own risks from pricing mechanisms, market liquidity, and variable borrowing costs. The overall result is a strategy where upside is capped at a fixed yield, while various factors can significantly reduce or even erase the expected return, despite the apparent safety of holding principal tokens.

    ### Points Farming: Speculative Yield Through Future Tokens

    Where Ethena offers stable returns through market-neutral strategies and Pendle enables sophisticated yield trading, points farming represents an entirely different category: betting on future protocol success before a token even exists. This approach involves participating in protocols that haven't yet distributed tokens, earning "points" or accrual metrics that may eventually convert into valuable airdrops.

    The mechanics are straightforward but the outcomes uncertain due to protocols generally being very secretive about the criteria. Participants supply liquidity, execute trades, stake assets, or run infrastructure nodes on pre-token protocols to accumulate points based on their activity levels. Successful farming requires targeting programs with transparent, on-chain accrual rules and sustainable underlying activity rather than purely extractive point systems.

    Optimization becomes a complex balancing act between cost and potential returns. Farmers must manage gas fees, borrowing costs, and opportunity costs across multiple accounts while avoiding Sybil detection filters that could disqualify their participation. The most sophisticated farmers develop systematic approaches to evaluate program quality, estimate token values, and allocate capital across multiple simultaneous campaigns.

    The uncertain nature of these rewards introduces distinct challenges. Points farming yields depend entirely on future protocol decisions, with protocols frequently changing rules mid-campaign. Not all points translate proportionally to tokens, and distributions can face delays, dilution, caps, KYC requirements, or complete cancellation. The primary risks are opportunity cost and program risk, with standard protocol vulnerabilities adding additional exposure.

    Despite these uncertainties, points farming has generated substantial returns for early participants in successful protocols. Major airdrops like Hyperliquid, Ethena, and Usual have created significant wealth for active users, validating the strategy's potential. The approach represents a bet on both protocol success and fair token distribution, two variables entirely outside participants' control.

    ### Options Vaults: Systematic Premium Collection

    In contrast to points farming's uncertain future payoffs, options vaults offer a more structured approach to yield generation by automating classic institutional income strategies. Where points farming bets on eventual token distributions, options vaults generate immediate returns through systematic premium collection. The most common implementations include covered call vaults and cash-secured put vaults, each targeting different market conditions and risk profiles.

    Covered call vaults operate by accepting deposits of volatile assets like ETH or BTC, then systematically selling out-of-the-money call options against these holdings. When users deposit ETH, the vault sells weekly call options at strikes typically 5-15% above current market prices. If prices remain below the strike, the vault keeps the premium and rolls to new options at expiry. If prices exceed the strike, the options get exercised and the vault delivers the underlying assets at the predetermined price.

    Cash-secured put vaults follow the inverse strategy, holding stablecoins and selling put options on volatile assets. These vaults collect premiums by agreeing to buy assets at below-market prices. If the underlying asset's price remains above the strike, the vault keeps the premium. If prices fall below the strike, the vault purchases the asset at the strike price using its stablecoin reserves.

    The yield generation comes primarily from option premiums, which vary widely depending on market volatility, strike selection, fees, and incentive structures. Many vaults also receive additional incentives from protocols seeking to bootstrap liquidity or from option market makers paying for flow. Performance depends critically on volatility levels, strike selection algorithms, and fee structures, with most vaults operating on weekly cycles.

    Premium collection strategies carry inherent trade-offs worth considering. Upside capping represents the primary risk for covered call strategies, during strong rallies, the vault's assets get called away at predetermined strikes, limiting participation in further gains. Assignment risk affects put strategies when market downturns force the vault to purchase assets at above-market prices. Volatility crush can rapidly erode recent gains when implied volatility collapses, making previously profitable premiums insufficient to cover subsequent losses. The complexity of options pricing and settlement creates additional attack surfaces compared to simpler yield strategies, requiring robust security measures and careful risk management protocols.

=== "KO"

    대출 프로토콜과 DEX가 기반 인프라를 제공함에 따라, DeFi는 전통 금융에 존재하지 않거나 소매 투자자에게 제공되지 않는 새로운 정교함의 레이어인 수익 최적화 전략을 가능하게 한다. 이러한 메커니즘은 자본에서 수익을 얻는 방법에 대한 우리의 생각을 변화시키며, 완전히 새로운 금융 기회 카테고리를 만든다.

    각 접근법은 수익 생성에 대한 다른 철학을 나타낸다. 생태계는 스테이킹과 대출과 같은 기초 메커니즘에서 유동성 제공, 실물 자산 수익, 복잡한 파생상품 구조를 포함하는 더 정교한 전략까지 확장된다. 이러한 메커니즘이 실제로 어떻게 작동하는지 설명하기 위해, 이 섹션에서는 DeFi의 독특한 역량을 보여주는 네 가지 혁신적인 접근법을 살펴본다: 안정적인 수익을 만드는 델타 중립 헤징 전략, 트레이더가 미래 수익 자체를 교환할 수 있게 하는 시간 기반 파생상품, 변동성 프리미엄을 수확하는 체계적 옵션 전략, 미래 토큰 배포에 베팅하는 투기적 파밍.

    ### Ethena: 델타 중립 수익 달러

    Ethena는 DeFi가 새로운 수익 생성 메커니즘을 만들기 위해 여러 금융 프리미티브를 어떻게 결합할 수 있는지 보여준다. 프로토콜의 USDe는 **델타 중립(Delta-Neutral)** 헤징을 통한 합성 달러 설계의 새로운 접근법을 나타낸다. 이 전략은 주식을 소유하면서 동시에 선물을 공매도하는 것과 유사하다. 이익과 손실이 상쇄되어 배당금을 받으면서 안정적인 포지션을 남긴다. (USDe와 같은 합성 메커니즘을 포함한 스테이블코인 카테고리에 대한 더 넓은 검토는 Chapter IX를 참조하라.)

    프로토콜은 스테이킹된 ETH, BTC, 기타 리퀴드 스테이킹 토큰, 준비 자산으로 USDe를 뒷받침하면서 무기한 선물 시장에서 상쇄 숏 포지션을 취한다(Chapter VI). 사용자가 USDe를 발행하면, 그들의 담보는 스테이킹 보상을 생성하고 숏 포지션은 방향성 가격 노출을 중화한다.

    세 가지 수익원이 나타난다. 스테이킹 보상은 기초 담보에서 기준 수익을 제공한다. 숏 무기한 포지션에서의 펀딩 비율 지불은 일반적으로 추가 수익을 생성하며, 특히 펀딩 비율이 양수인 경향이 있는 상승장에서 그렇다. 국채 유사 자산에서의 준비금 수입은 세 번째 수익 구성 요소를 제공한다. 이 조합은 안정적인 자산으로 기능하는 것에 대해 매력적인 수익을 생성할 수 있다.

    Ethena의 혁신은 스테이블코인 발행을 수동적인 지원 메커니즘에서 능동적인 수익 생성 전략으로 변환하는 데 있다. 사용자는 USDe 보유를 스테이킹하는 sUSDe를 통해 수익을 더욱 복리화할 수 있다. 이것은 DeFi의 조합 가능성이 전통 시스템에서 불가능한 금융 상품을 어떻게 가능하게 하는지 보여준다.

    그러나 Ethena는 주목할 만한 독특한 위험을 도입한다. 펀딩 비율 위험은 음의 펀딩 비율이 수익을 잠식할 수 있는 하락장에서 중요해진다. 이를 완화하기 위해 Ethena는 준비금 펀드를 유지하고 음의 펀딩 기간 동안 국채 유사 금리를 받는 리퀴드 스테이블로 지원 자산을 동적으로 재할당하여 사용자를 손실로부터 보호한다.

    커스터디 위험은 헤징 포지션을 위한 중앙화 거래소 의존에서 발생한다. 위험은 Copper, Ceffu, Fireblocks를 포함한 장외 정산(Off-Exchange Settlement, OES) 제공자를 사용하여 지원 자산을 보유함으로써 부분적으로 완화된다. 이러한 제공자는 파산 원격 신탁이나 MPC 지갑을 사용하여 자산을 보호하지만, 운영 문제가 발행 및 상환 기능을 일시적으로 방해할 수 있다. Ethena는 여러 OES 제공자와 거래소와의 빈번한 PnL 정산을 통해 이를 다양화한다.

    페그 안정성은 일반적으로 상환 메커니즘을 통해 유지되지만 절대적이지 않다. USDe는 2025년 10월 10일 Binance 특정 이벤트 중에 잠시 $0.62까지 거래되었다가 회복되었다. Binance의 수익 프로그램은 루핑 기회를 통해 거래소에 상당한 레버리지 USDe 노출을 집중시켜 4-10배의 효과적인 레버리지를 가능하게 했다. 시장이 폭락했을 때, Binance의 내부 가격 시스템이 청산 연쇄를 촉발했다. 이 시스템은 더 넓은 다중 거래소 데이터보다 자체 현물 시장에 주로 의존했기 때문에, 얇은 USDe 오더북은 심각한 유동성 부족 상태가 되었다.

    중요하게도, 온체인 풀은 이 이벤트 내내 $1 근처를 유지했고 USDe는 과잉 담보 상태를 유지하여, 문제가 USDe 자체에 대한 시스템적인 것이 아니라 거래소 특정적이었음을 보여주었다. 이 에피소드는 중요한 구별을 강조한다: 오라클 설계와 거래소 특정 레버리지 집중이 기초 담보 구조가 건전하게 유지되는 경우에도 심각한 국지적 가격 편차를 만들 수 있다.

    ### Pendle: 시간 자체의 거래

    Ethena가 가격 위험을 중화하는 헤징 전략을 통한 수익 생성을 보여주는 반면, Pendle은 수익 자체를 해체하는 근본적으로 다른 접근법을 취한다. 파생상품을 통해 안정적인 수익을 만드는 대신, Pendle은 사용자가 화폐의 시간 가치를 직접 분리하고 거래할 수 있게 한다.

    스테이킹된 이더리움이나 sUSDe와 같은 수익 생성 자산을 가져와 두 구성 요소로 분할함으로써, Pendle은 완전히 새로운 거래 가능한 상품을 만든다. **원금 토큰(Principal Token, PT)**은 만기 시 기초 자산에 대한 청구권을 나타내며, 무이표 채권과 유사하다. **수익 토큰(Yield Token, YT)**은 만기까지 생성된 모든 수익에 대한 청구권을 나타낸다. 수학적 관계는 PT 가격과 YT 가격의 합이 기초 자산 가격을 추적하도록 보장하며, 차익 거래가 일반적으로 닫는 작은 편차가 있어 흥미로운 거래 기회를 만든다.

    이 분리는 정교한 전략을 가능하게 한다. 고정 금리를 원하는 사용자는 예치 직후 YT를 즉시 매도하여 보장된 수익을 확보할 수 있다. 더 높은 미래 수익을 추측하는 사람들은 금리 변화에 대한 레버리지 노출을 위해 YT 토큰을 구매할 수 있다. 다른 사람들은 포트폴리오 전반에 걸쳐 금리 위험을 헤지하기 위해 다양한 PT와 YT 조합을 사용한다.

    PT는 Aave, Euler, Morpho와 같은 대출 시장에서 핵심 담보가 되었다. Aave의 PT-sUSDe와 PT-USDe 시장은 공격적인 고정 수익 레버리지 거래와 인센티브에 힘입어 낮은 9자리수에서 만기 전체에 걸쳐 대략 낮은 한 자릿수 십억 달러의 총 PT 공급으로 성장했다. 프로토콜에게 이것은 TVL을 부트스트랩하는 매력적인 방법이 되었다: 모든 루프 사이클은 대출 시장에 더 많은 PT를 잠그고 Pendle 내부에 더 많은 기초 자산을 잠근다.

    지배적인 PT 사용 사례는 루핑이 되었다. 사용자가 대출 시장에 PT를 담보로 예치하고, 그 담보에 대해 스테이블코인을 빌리고, 그 스테이블코인을 사용하여 Pendle에서 더 많은 PT를 구매하고, 사이클을 반복하는 전략이다. PT는 기초 자산에 대해 할인 거래되고 만기에 전체 가치로 상승하므로, 이 루프는 효과적으로 고정 수익에 대한 레버리지 노출을 만든다. 전략은 차입 비용이 PT의 내재 수익률 아래에 머무는 한 작동한다.

    유리한 조건에서 4-5배 레버리지로, 이러한 루프는 스프레드만으로 높은 두 자릿수 수익을 생성했다. 많은 설정은 또한 포인트 프로그램과 토큰 인센티브로부터 추가 부스트를 받는다.

    그러나 그 고정 수익은 특정하고 비대칭적인 위험 프로필과 함께 온다. PT 루핑은 다른 플랫폼이 이러한 자산을 어떻게 가격 책정하는지에 크게 의존한다. Aave는 최소 PT 가격과 LTV "킬스위치"와 같은 보호 가드레일과 함께 Pendle의 내재 수익률을 기반으로 PT를 가격 책정한다. USDe 측은 일반적으로 단기 가격 변동에 대한 민감도를 줄이지만 Ethena 자체가 실패하는 꼬리 이벤트에 위험을 집중시키는 방식으로 가격이 책정된다.

    Euler와 일부 Morpho 시장과 같은 다른 거래소는 실제 거래 가격에 반응하는 더 시장 민감한 가격 책정을 사용한다. 이것은 기초 담보가 건전하게 유지되는 경우에도 단기 가격 변위가 포지션을 담보 부족으로 보이게 할 수 있음을 의미한다. 거래소 간의 다른 가격 책정 접근법은 실제로 이미 분기된 결과를 생성했으며, 동일한 시장 스트레스 이벤트 동안 일부 플랫폼에서 동일한 포지션이 생존하고 다른 플랫폼에서 청산되었다.

    PT 루프는 또한 언와인딩 마찰을 만든다. 종료하려면 사용자는 여러 단계를 되돌려야 한다: 빌린 스테이블코인을 상환하고, PT 담보를 인출하고, 종종 얇은 Pendle 유동성에 PT를 다시 매도해야 한다. 이것은 포지션을 단순한 대출 계약보다 훨씬 더 끈적이게 만들고 시장이 스트레스를 받을 때 정확히 실행 위험, 슬리피지, 거래 비용을 추가한다.

    PT 루핑은 또한 차입 비용과 유동성에 극도로 민감하다. 상승 여지는 고정 수익을 확보하면 제한되지만, 하락 여지는 무한정 열려 있다. 차입 금리가 PT의 내재 수익률 이상으로 급등하면, 전략을 매력적으로 만든 스프레드가 사라지거나 심지어 음수로 전환될 수 있다. 동시에 Pendle의 PT 유동성은 포지션 규모에 비해 얕을 수 있다. 경우에 따라 PT 공급이 사용 가능한 거래 유동성의 10배를 초과하여, 빠르게 언와인딩해야 할 경우 큰 포지션이 심각한 가격 영향에 노출된다.

    분할 토큰 모델은 또한 더 전통적인 취약성을 만든다. YT 토큰은 비유동적일 수 있으며, 특히 덜 인기 있는 자산의 경우, 그 가치는 예상 수익 변화에 매우 민감하다. 만기 전에 YT 포지션을 언와인딩하면 상당한 슬리피지가 발생할 수 있으며, 특히 투자자들이 가장 종료하고 싶어하는 시장 스트레스 시에 그렇다.

    대조적으로, PT 중심 루핑 전략은 더 깨끗한 수익 구조를 제공하지만 가격 메커니즘, 시장 유동성, 가변 차입 비용으로부터 자체적인 위험을 수반한다. 전체 결과는 상승이 고정 수익으로 제한되는 전략이지만, 원금 토큰 보유의 명백한 안전에도 불구하고 다양한 요인이 예상 수익을 상당히 줄이거나 심지어 지울 수 있다.

    ### 포인트 파밍: 미래 토큰을 통한 투기적 수익

    Ethena가 시장 중립 전략을 통해 안정적인 수익을 제공하고 Pendle이 정교한 수익 거래를 가능하게 하는 반면, 포인트 파밍은 완전히 다른 카테고리를 나타낸다: 토큰이 존재하기도 전에 미래 프로토콜 성공에 베팅하는 것. 이 접근법은 아직 토큰을 배포하지 않은 프로토콜에 참여하여 가치 있는 에어드롭으로 최종 전환될 수 있는 "포인트" 또는 누적 지표를 얻는 것을 포함한다.

    메커니즘은 간단하지만 결과는 프로토콜이 일반적으로 기준에 대해 매우 비밀스럽기 때문에 불확실하다. 참여자는 활동 수준에 따라 포인트를 축적하기 위해 프리토큰 프로토콜에 유동성을 공급하고, 거래를 실행하고, 자산을 스테이킹하거나, 인프라 노드를 운영한다. 성공적인 파밍은 순수하게 추출적인 포인트 시스템보다 투명한 온체인 누적 규칙과 지속 가능한 기초 활동을 가진 프로그램을 목표로 해야 한다.

    최적화는 비용과 잠재적 수익 사이의 복잡한 균형 작용이 된다. 파머는 시빌 탐지 필터에 의해 참여가 실격될 수 있는 것을 피하면서 여러 계정에 걸쳐 가스 수수료, 차입 비용, 기회 비용을 관리해야 한다. 가장 정교한 파머는 프로그램 품질을 평가하고, 토큰 가치를 추정하고, 여러 동시 캠페인에 자본을 할당하기 위한 체계적인 접근법을 개발한다.

    이러한 보상의 불확실한 특성은 뚜렷한 도전을 도입한다. 포인트 파밍 수익은 전적으로 미래 프로토콜 결정에 달려 있으며, 프로토콜은 캠페인 중간에 규칙을 자주 변경한다. 모든 포인트가 토큰으로 비례적으로 전환되는 것은 아니며, 배포는 지연, 희석, 상한, KYC 요구사항 또는 완전한 취소에 직면할 수 있다. 주요 위험은 기회 비용과 프로그램 위험이며, 표준 프로토콜 취약성이 추가 노출을 더한다.

    이러한 불확실성에도 불구하고, 포인트 파밍은 성공적인 프로토콜의 초기 참여자에게 상당한 수익을 생성했다. Hyperliquid, Ethena, Usual과 같은 주요 에어드롭은 활발한 사용자에게 상당한 부를 창출하여 전략의 잠재력을 검증했다. 이 접근법은 프로토콜 성공과 공정한 토큰 배포에 대한 베팅을 나타내며, 참여자의 통제 밖에 있는 두 가지 변수이다.

    ### 옵션 볼트: 체계적 프리미엄 수집

    포인트 파밍의 불확실한 미래 수익과 대조적으로, 옵션 볼트는 고전적인 기관 수입 전략을 자동화하여 수익 생성에 더 구조화된 접근법을 제공한다. 포인트 파밍이 최종 토큰 배포에 베팅하는 반면, 옵션 볼트는 체계적인 프리미엄 수집을 통해 즉각적인 수익을 생성한다. 가장 일반적인 구현에는 커버드 콜 볼트와 현금 담보 풋 볼트가 포함되며, 각각 다른 시장 조건과 위험 프로필을 대상으로 한다.

    커버드 콜 볼트는 ETH나 BTC와 같은 변동성 자산의 예치를 수락한 다음, 이러한 보유에 대해 체계적으로 외가격 콜 옵션을 매도하여 운영한다. 사용자가 ETH를 예치하면, 볼트는 일반적으로 현재 시장 가격보다 5-15% 높은 행사가에 주간 콜 옵션을 매도한다. 가격이 행사가 아래로 유지되면, 볼트는 프리미엄을 유지하고 만기에 새로운 옵션으로 롤오버한다. 가격이 행사가를 초과하면, 옵션이 행사되고 볼트는 기초 자산을 미리 결정된 가격에 인도한다.

    현금 담보 풋 볼트는 역전략을 따르며, 스테이블코인을 보유하고 변동성 자산에 대한 풋 옵션을 매도한다. 이 볼트는 시장 이하 가격에 자산을 구매하는 데 동의하여 프리미엄을 수집한다. 기초 자산 가격이 행사가 위로 유지되면, 볼트는 프리미엄을 유지한다. 가격이 행사가 아래로 떨어지면, 볼트는 스테이블코인 준비금을 사용하여 행사가에 자산을 구매한다.

    수익 생성은 주로 옵션 프리미엄에서 나오며, 시장 변동성, 행사가 선택, 수수료, 인센티브 구조에 따라 크게 다르다. 많은 볼트는 또한 유동성을 부트스트랩하려는 프로토콜이나 플로우에 대해 지불하는 옵션 시장 조성자로부터 추가 인센티브를 받는다. 성과는 변동성 수준, 행사가 선택 알고리즘, 수수료 구조에 크게 의존하며, 대부분의 볼트는 주간 사이클로 운영된다.

    프리미엄 수집 전략은 고려해야 할 고유한 트레이드오프를 수반한다. 상승 제한은 커버드 콜 전략의 주요 위험을 나타내며, 강한 랠리 동안 볼트의 자산이 미리 결정된 행사가에 콜되어 추가 상승 참여를 제한한다. 배정 위험은 시장 하락이 볼트가 시장 이상 가격에 자산을 구매하도록 강제할 때 풋 전략에 영향을 미친다. 변동성 붕괴는 내재 변동성이 급락할 때 최근 이익을 빠르게 잠식할 수 있으며, 이전에 수익성이 있었던 프리미엄이 후속 손실을 커버하기에 불충분하게 된다. 옵션 가격 책정과 정산의 복잡성은 더 단순한 수익 전략에 비해 추가적인 공격 표면을 만들어, 강력한 보안 조치와 신중한 위험 관리 프로토콜을 필요로 한다.

## Section V: Infrastructure Dependencies

=== "EN"

    The sophisticated DeFi mechanisms explored above (from AMMs and lending protocols to complex yield strategies) all rest on shared infrastructure layers that operate beneath the application surface. While protocol teams focus on optimizing their specific mechanisms, understanding these dependencies reveals where systemic risks concentrate. Oracle failures, flash loan exploits, and bridge vulnerabilities have historically caused more devastating protocol failures than flaws in core protocol logic. A perfectly designed lending protocol can still be drained by oracle failures, and robust DEXs can lose funds when flash loans amplify subtle reentrancy bugs. This section examines the critical infrastructure that determines whether DeFi protocols succeed or fail under stress.

    ### Oracle Networks

    Smart contracts face a fundamental limitation: they cannot directly access external data like asset prices, weather information, or sports scores. This creates the **oracle problem**, where bringing off-chain data on-chain in a trustworthy way becomes essential for protocol operation.

    Price oracles serve as critical infrastructure for decentralized finance. Lending protocols depend on accurate prices to calculate collateral ratios and trigger liquidations. Stablecoin systems require price feeds to maintain pegs and manage collateral positions. Decentralized exchanges need reference prices to detect arbitrage opportunities and set fair exchange rates.

    Chainlink dominates the oracle space through its Off-Chain Reporting system, where multiple nodes aggregate data off-chain and submit single transactions to reduce gas costs. (Chainlink's LINK token utility model is discussed in Chapter XII.) Updates trigger based on two mechanisms: deviation thresholds when prices move by preset percentages, and heartbeats that ensure regular updates regardless of price movement.

    Pyth Network uses a "pull" model where applications fetch the latest attested price on demand rather than continuous pushing. This approach proves more cost-effective for applications that don't need constant updates, particularly on high-throughput chains where frequent updates would be prohibitively expensive.

    Alternative networks like RedStone and Band provide different architectures and redundancy. Many protocols use multiple oracle sources and implement medianization to improve reliability and resist manipulation attempts, reducing single points of failure.

    #### Oracle Configuration Types in Lending Markets

    Lending protocols implement oracles in fundamentally different ways, each carrying distinct risk profiles. Understanding these configurations is essential for assessing liquidation risk and potential bad debt accumulation.

    ##### Fundamental Oracles

    Fundamental oracles derive prices from internal exchange rates and on-chain accounting rather than secondary market trading. For liquid staking tokens and credit vaults, these oracles calculate prices based on the underlying asset ratio, essentially the net asset value per share. A liquid staking derivative might be priced using the vault's exchange rate (exchangeRate \= totalAssets / totalShares) multiplied by the underlying asset's USD price, reflecting its redeemable value regardless of secondary market prices.

    These oracles resist DEX price manipulation and flash loan attacks since they don't rely on DEX spot prices. However, they create severe bad debt risk during liquidity crises or backing failures. If secondary market prices crash below the oracle price and redemptions become impossible due to insufficient liquidity or smart contract failures, the protocol cannot liquidate positions effectively. Lenders face losses as the collateral's real market value falls below borrowed amounts while the oracle continues reporting an inflated price based on theoretical backing that may no longer be accessible.

    ##### Hardcoded Oracles

    Hardcoded oracles fix the price relationship between assets, typically for stablecoins assumed to maintain pegs. Aave's current configuration for USDe exemplifies this approach: the protocol prices USDe 1:1 versus USDT (using Chainlink's USDT/USD feed), effectively treating USDe \= USDT ≈ $1. This creates dependency on both USDe and USDT maintaining their pegs.

    The oracle logic is trivial and updates are rare, reducing gas costs and implementation complexity compared to dedicated dynamic price feeds. The risks mirror those of fundamental oracles. During a depeg event, liquidations fail to trigger at appropriate thresholds. Bad debt accumulates as the real market value diverges from the hardcoded assumption, especially when LTVs are high and the depeg is severe. The protocol effectively bets its solvency on both assets maintaining their pegs indefinitely.

    ##### Market-Reliant Oracles

    Market-reliant oracles source prices from secondary market trading, whether through direct on-chain pool queries like Uniswap V3 TWAPs or through aggregated feeds like Chainlink and Pyth that combine CEX and DEX prices across multiple sources. These oracles reflect actual tradeable prices and enable real liquidations during market stress. Positions can be unwound at prices that match where assets can actually be sold.

    Direct DEX oracle implementations introduce manipulation vulnerabilities if poorly designed. Flash loan attacks against shallow pools represent the canonical example. During liquidity crises, market-reliant oracles may report accurate but rapidly moving prices that create liquidation cascades, potentially overwhelming the protocol's ability to process liquidations efficiently.

    ##### Fundamental Tradeoffs and Hybrid Solutions

    The choice between these configurations represents fundamental tradeoffs. Fundamental and hardcoded oracles optimize for manipulation resistance at the cost of bad debt risk during market dislocations or backing failures. Market-reliant oracles accept manipulation risk and potential volatility cascades in exchange for liquidatable positions that reflect actual market conditions.

    Sophisticated protocols increasingly deploy hybrid risk oracles that combine multiple approaches. These systems might use fundamental exchange rates as a baseline while monitoring market prices, implementing circuit breakers or LTV adjustments when the two diverge significantly, and incorporating freeze guardians that can pause operations during extreme events. Aave's ongoing USDe governance discussions and risk-oracle development work illustrate this trend, moving from simple fixed ratios toward more dynamic risk management with redemption-based logic and emergency controls.

    ### Oracle Attack Vectors and Defense Mechanisms

    Oracle failures have caused some of DeFi's largest losses, making understanding attack patterns essential.

    #### Common Attack Vectors

    Flash loan price manipulation represents a frequent attack vector where attackers use flash loans to manipulate prices in thin liquidity pools, then use these inflated prices as collateral to borrow from lending protocols. The entire attack and profit extraction happens in a single transaction, highlighting how atomic transactions can amplify risks.

    Stale price exploitation occurs when oracles fail to update during volatile periods, allowing attackers to exploit gaps between oracle prices and market reality. More subtle attacks use callbacks and reentrancy to manipulate prices within the same transaction that consumes them, bypassing simple time-weighted average protections.

    #### Defense Layers

    Robust protocols implement multiple defense mechanisms. Staleness checks reject prices older than specified thresholds. Circuit breakers pause operations when prices move too dramatically. Medianization uses multiple oracle sources and takes median values to resist outliers. Read-only reentrancy guards prevent price manipulation through callbacks. Time-weighted averages smooth out short-term manipulation attempts.

    #### Practical Considerations

    When oracle design is inadequate, even the most robust protocol logic becomes vulnerable. The March 2023 USDC depeg provided a stress test of how protocols handle extreme oracle challenges. Curve's 3pool worked mathematically as designed but couldn't prevent liquidity flight during the crisis. This underscores why understanding oracle architecture and failure modes matters as much as understanding the protocols themselves.

    Before depositing into any lending protocol, research its oracle configuration for each supported asset. Understand whether prices come from internal exchange rates, fixed relationships between stablecoins, direct DEX pools, or aggregated market feeds. Assess the liquidity backing any market-reliant oracles. Consider what happens if an asset depegs, loses liquidity, or faces redemption failures. The oracle design determines whether you face manipulation risk, bad debt risk, or some combination thereof, and whether the protocol has guards in place to handle edge cases.

    ### Flash Loans: Double-Edged Innovation

    Flash loans represent one of DeFi's most innovative and dangerous features, having powered both groundbreaking financial operations and some of the ecosystem's most damaging hacks. Understanding their mechanics reveals the fundamental tension of atomic composability.

    Flash loans allow borrowing up to the available liquidity and/or protocol-set limits in a pool, using it within a transaction, and repaying it plus a fee before the transaction completes. If repayment fails, the entire transaction reverts as if it never happened. This is only possible because of Ethereum's atomic transaction execution (Chapter II), where all operations within a transaction either succeed together or fail together. This mechanism enables capital-efficient operations impossible in traditional finance.

    However, flash loans are limited to a single transaction on one chain or L2. Cross-chain "flash" behaviors rely on bridges and trust assumptions, making them not truly atomic end-to-end.

    Legitimate use cases include arbitrage across exchanges without holding capital, collateral swaps in lending protocols executed atomically, liquidations where liquidators can liquidate positions and immediately sell collateral, and refinancing to move debt between protocols in single transactions.

    The dark side emerges when flash loans amplify other vulnerabilities. As detailed in the previous section on oracles, flash loans are a primary tool for amplifying price manipulation attacks, enabling attackers to manipulate thin liquidity pools with borrowed capital and exploit those distorted prices in lending protocols, all within a single atomic transaction.

    Complex exploit chains leverage flash loans to provide capital for multi-step attacks that would otherwise require significant upfront investment. While attackers remain bounded by pool liquidity, per-asset caps, and per-transaction gas limits, these constraints often still allow for substantial damage.

    Beyond price oracles, flash loans can facilitate governance-related attacks, such as borrowing voting power when governance systems aren't snapshot- or anti-flash-loan-hardened.

    Protocol defenses require multiple layers of safeguards. First, implement the checks-effects-interactions pattern and apply reentrancy guards with appropriate granularity, typically on externally callable, state-changing entry points. Overly broad or global guards can hinder intended callbacks, though they may be acceptable for some contracts. The key is preserving intended composability while blocking unsafe reentrancy.

    Oracle protections form another critical defense layer. Use multi-block TWAPs (time-weighted average prices) or medians sourced from venues that cannot be dominated within a single block, such as Chainlink. Incorporate independent data sources with staleness checks. While using only previous-block prices can help, this approach is brittle around reorgs or thin markets. Where feasible, prefer market-scoped circuit breakers, escalating to protocol-wide pauses for systemic issues.

    Additional protective measures include isolation modes with debt ceilings and supply/borrow caps per asset. Conservative LTV (loan-to-value) ratios and liquidation thresholds provide further safeguards. Implement per-block rate limits on oracle consumers and slippage checks with minimum-out protections on DEX operations within transactions.

    Flash loans exemplify DeFi's core tension: the same composability that enables innovation also amplifies risks. They don't create vulnerabilities but rather amplify existing ones, requiring protocols to be designed securely even when attackers have substantial capital available within the constraints of pool liquidity and transaction limits.

    Fees are typically small but not uniform, some protocols set or dynamically adjust them, which can render thin arbitrage opportunities unprofitable, providing some natural economic protection. Some tokens also support flash minting (mint and burn within a single transaction), which functions similarly to a flash loan for that specific token.

=== "KO"

    위에서 탐구한 정교한 DeFi 메커니즘(AMM과 대출 프로토콜에서 복잡한 수익 전략까지)은 모두 애플리케이션 표면 아래에서 작동하는 공유 인프라 레이어에 달려 있다. 프로토콜 팀이 특정 메커니즘을 최적화하는 데 집중하는 동안, 이러한 의존성을 이해하면 시스템적 위험이 어디에 집중되는지 드러난다. 오라클 실패, 플래시론 익스플로잇, 브릿지 취약성은 역사적으로 핵심 프로토콜 로직의 결함보다 더 치명적인 프로토콜 실패를 야기했다. 완벽하게 설계된 대출 프로토콜도 오라클 실패로 인해 자금이 유출될 수 있고, 강력한 DEX도 플래시론이 미묘한 재진입 버그를 증폭할 때 자금을 잃을 수 있다. 이 섹션에서는 스트레스 하에서 DeFi 프로토콜의 성공 또는 실패를 결정하는 핵심 인프라를 검토한다.

    ### 오라클 네트워크

    스마트 컨트랙트는 근본적인 한계에 직면한다: 자산 가격, 날씨 정보, 스포츠 점수와 같은 외부 데이터에 직접 접근할 수 없다. 이것은 **오라클 문제(Oracle Problem)**를 만드는데, 오프체인 데이터를 신뢰할 수 있는 방식으로 온체인에 가져오는 것이 프로토콜 운영에 필수적이 된다.

    가격 오라클은 탈중앙화 금융을 위한 핵심 인프라 역할을 한다. 대출 프로토콜은 담보 비율을 계산하고 청산을 트리거하기 위해 정확한 가격에 의존한다. 스테이블코인 시스템은 페그를 유지하고 담보 포지션을 관리하기 위해 가격 피드가 필요하다. 탈중앙화 거래소는 차익 거래 기회를 감지하고 공정한 환율을 설정하기 위해 참조 가격이 필요하다.

    Chainlink는 오프체인 보고 시스템을 통해 오라클 공간을 지배하며, 여러 노드가 오프체인에서 데이터를 집계하고 가스 비용을 줄이기 위해 단일 트랜잭션을 제출한다. (Chainlink의 LINK 토큰 유틸리티 모델은 Chapter XII에서 논의된다.) 업데이트는 두 가지 메커니즘에 의해 트리거된다: 가격이 사전 설정된 백분율만큼 이동할 때의 편차 임계값, 그리고 가격 이동과 관계없이 정기 업데이트를 보장하는 하트비트.

    Pyth Network는 애플리케이션이 지속적인 푸시 대신 필요에 따라 최신 증명된 가격을 가져오는 "풀" 모델을 사용한다. 이 접근법은 지속적인 업데이트가 필요하지 않은 애플리케이션에 더 비용 효율적이며, 특히 빈번한 업데이트가 과도하게 비쌀 수 있는 고처리량 체인에서 그렇다.

    RedStone과 Band와 같은 대안 네트워크는 다른 아키텍처와 중복성을 제공한다. 많은 프로토콜이 여러 오라클 소스를 사용하고 중앙값 처리를 구현하여 신뢰성을 개선하고 조작 시도에 저항하여 단일 장애 지점을 줄인다.

    #### 대출 시장에서의 오라클 구성 유형

    대출 프로토콜은 근본적으로 다른 방식으로 오라클을 구현하며, 각각 뚜렷한 위험 프로필을 수반한다. 이러한 구성을 이해하는 것은 청산 위험과 잠재적 부실 채권 축적을 평가하는 데 필수적이다.

    ##### 기본 오라클

    기본 오라클은 2차 시장 거래가 아닌 내부 환율과 온체인 회계에서 가격을 도출한다. 리퀴드 스테이킹 토큰과 크레딧 볼트의 경우, 이 오라클은 기초 자산 비율, 본질적으로 주당 순자산 가치를 기반으로 가격을 계산한다. 리퀴드 스테이킹 파생상품은 볼트의 환율(exchangeRate = totalAssets / totalShares)에 기초 자산의 USD 가격을 곱하여 가격이 책정될 수 있으며, 2차 시장 가격과 관계없이 상환 가능한 가치를 반영한다.

    이러한 오라클은 DEX 현물 가격에 의존하지 않기 때문에 DEX 가격 조작과 플래시론 공격에 저항한다. 그러나 유동성 위기나 지원 실패 시 심각한 부실 채권 위험을 만든다. 2차 시장 가격이 오라클 가격 아래로 폭락하고 유동성 부족이나 스마트 컨트랙트 실패로 인해 상환이 불가능해지면, 프로토콜은 효과적으로 포지션을 청산할 수 없다. 대출자는 담보의 실제 시장 가치가 대출 금액 아래로 떨어지면서 손실에 직면하고, 오라클은 더 이상 접근할 수 없을 수 있는 이론적 지원에 기반한 부풀려진 가격을 계속 보고한다.

    ##### 하드코딩 오라클

    하드코딩 오라클은 자산 간의 가격 관계를 고정하며, 일반적으로 페그를 유지하는 것으로 가정되는 스테이블코인에 대해 그렇다. Aave의 USDe에 대한 현재 구성이 이 접근법을 예시한다: 프로토콜은 USDe를 USDT에 대해 1:1로 가격 책정하며(Chainlink의 USDT/USD 피드를 사용), 효과적으로 USDe = USDT ≈ $1로 취급한다. 이것은 USDe와 USDT 모두가 페그를 유지하는 데 의존성을 만든다.

    오라클 로직은 사소하고 업데이트는 드물어서, 전용 동적 가격 피드에 비해 가스 비용과 구현 복잡성을 줄인다. 위험은 기본 오라클의 것을 반영한다. 디페그 이벤트 동안 청산이 적절한 임계값에서 트리거되지 못한다. 담보의 실제 시장 가치가 하드코딩된 가정에서 벗어나면서 부실 채권이 축적되며, 특히 LTV가 높고 디페그가 심할 때 그렇다. 프로토콜은 효과적으로 두 자산 모두가 페그를 무기한 유지하는 데 지급 능력을 건다.

    ##### 시장 의존 오라클

    시장 의존 오라클은 Uniswap V3 TWAP과 같은 직접 온체인 풀 쿼리를 통해서든, 여러 소스에 걸쳐 CEX와 DEX 가격을 결합하는 Chainlink 및 Pyth와 같은 집계 피드를 통해서든 2차 시장 거래에서 가격을 가져온다. 이러한 오라클은 실제 거래 가능한 가격을 반영하고 시장 스트레스 동안 실제 청산을 가능하게 한다. 자산이 실제로 판매될 수 있는 가격과 일치하는 가격에 포지션을 언와인딩할 수 있다.

    잘못 설계된 경우 직접 DEX 오라클 구현은 조작 취약성을 도입한다. 얕은 풀에 대한 플래시론 공격이 대표적인 예이다. 유동성 위기 동안 시장 의존 오라클은 정확하지만 빠르게 움직이는 가격을 보고하여 청산 연쇄를 만들 수 있으며, 잠재적으로 프로토콜의 청산 효율적 처리 능력을 압도할 수 있다.

    ##### 근본적인 트레이드오프와 하이브리드 솔루션

    이러한 구성 간의 선택은 근본적인 트레이드오프를 나타낸다. 기본 및 하드코딩 오라클은 시장 변위나 지원 실패 동안 부실 채권 위험을 대가로 조작 저항을 최적화한다. 시장 의존 오라클은 실제 시장 조건을 반영하는 청산 가능한 포지션과 교환하여 조작 위험과 잠재적 변동성 연쇄를 수용한다.

    정교한 프로토콜은 여러 접근법을 결합하는 하이브리드 위험 오라클을 점점 더 배포한다. 이러한 시스템은 기본 환율을 기준선으로 사용하면서 시장 가격을 모니터링하고, 둘이 크게 벗어날 때 서킷 브레이커나 LTV 조정을 구현하고, 극단적 이벤트 동안 운영을 일시 중지할 수 있는 동결 가디언을 통합할 수 있다. Aave의 진행 중인 USDe 거버넌스 논의와 위험 오라클 개발 작업은 이 트렌드를 보여주며, 단순한 고정 비율에서 상환 기반 로직과 긴급 제어를 가진 더 동적인 위험 관리로 이동한다.

    ### 오라클 공격 벡터와 방어 메커니즘

    오라클 실패는 DeFi에서 가장 큰 손실을 야기했으며, 공격 패턴을 이해하는 것이 필수적이다.

    #### 일반적인 공격 벡터

    플래시론 가격 조작은 빈번한 공격 벡터로, 공격자가 플래시론을 사용하여 얇은 유동성 풀에서 가격을 조작한 다음, 이러한 부풀려진 가격을 담보로 사용하여 대출 프로토콜에서 빌린다. 전체 공격과 이익 추출이 단일 트랜잭션에서 발생하며, 원자적 트랜잭션이 어떻게 위험을 증폭할 수 있는지 강조한다.

    부실 가격 악용은 오라클이 변동성 기간 동안 업데이트에 실패할 때 발생하여 공격자가 오라클 가격과 시장 현실 간의 간격을 악용할 수 있게 한다. 더 미묘한 공격은 콜백과 재진입을 사용하여 동일 트랜잭션 내에서 가격을 조작하며, 단순한 시간 가중 평균 보호를 우회한다.

    #### 방어 레이어

    강력한 프로토콜은 여러 방어 메커니즘을 구현한다. 부실성 검사는 지정된 임계값보다 오래된 가격을 거부한다. 서킷 브레이커는 가격이 너무 급격하게 움직일 때 운영을 일시 중지한다. 중앙값 처리는 여러 오라클 소스를 사용하고 이상치에 저항하기 위해 중앙값을 취한다. 읽기 전용 재진입 가드는 콜백을 통한 가격 조작을 방지한다. 시간 가중 평균은 단기 조작 시도를 평활화한다.

    #### 실제 고려사항

    오라클 설계가 부적절하면, 가장 강력한 프로토콜 로직도 취약해진다. 2023년 3월 USDC 디페그는 프로토콜이 극단적인 오라클 도전을 어떻게 처리하는지에 대한 스트레스 테스트를 제공했다. Curve의 3pool은 수학적으로 설계대로 작동했지만 위기 동안 유동성 이탈을 막지 못했다. 이것은 오라클 아키텍처와 실패 모드를 이해하는 것이 프로토콜 자체를 이해하는 것만큼 중요한 이유를 강조한다.

    대출 프로토콜에 예치하기 전에, 지원되는 각 자산에 대한 오라클 구성을 조사하라. 가격이 내부 환율에서, 스테이블코인 간의 고정 관계에서, 직접 DEX 풀에서, 또는 집계된 시장 피드에서 나오는지 이해하라. 시장 의존 오라클을 지원하는 유동성을 평가하라. 자산이 디페그되거나, 유동성을 잃거나, 상환 실패에 직면하면 어떻게 되는지 고려하라. 오라클 설계는 조작 위험, 부실 채권 위험, 또는 그 조합에 직면하는지, 그리고 프로토콜이 엣지 케이스를 처리하기 위한 가드가 있는지를 결정한다.

    ### 플래시론: 양날의 검 혁신

    플래시론은 DeFi의 가장 혁신적이고 위험한 기능 중 하나를 나타내며, 획기적인 금융 운영과 생태계에서 가장 파괴적인 해킹 모두를 구동했다. 그 메커니즘을 이해하면 원자적 조합 가능성의 근본적인 긴장이 드러난다.

    플래시론은 풀에서 사용 가능한 유동성 및/또는 프로토콜 설정 한도까지 빌려서, 트랜잭션 내에서 사용하고, 트랜잭션이 완료되기 전에 수수료와 함께 상환할 수 있게 한다. 상환에 실패하면, 전체 트랜잭션이 마치 일어나지 않은 것처럼 되돌려진다. 이것은 모든 작업이 함께 성공하거나 함께 실패하는 이더리움의 원자적 트랜잭션 실행(Chapter II) 때문에만 가능하다. 이 메커니즘은 전통 금융에서 불가능한 자본 효율적 운영을 가능하게 한다.

    그러나 플래시론은 단일 체인이나 L2에서 단일 트랜잭션으로 제한된다. 크로스체인 "플래시" 동작은 브릿지와 신뢰 가정에 의존하여 진정으로 원자적인 엔드투엔드가 아니다.

    합법적인 사용 사례에는 자본을 보유하지 않고 거래소 간 차익 거래, 대출 프로토콜에서 원자적으로 실행되는 담보 스왑, 청산인이 포지션을 청산하고 즉시 담보를 판매할 수 있는 청산, 그리고 단일 트랜잭션에서 프로토콜 간 부채를 이동하는 재융자가 포함된다.

    플래시론이 다른 취약성을 증폭할 때 어두운 면이 나타난다. 이전 오라클 섹션에서 자세히 설명했듯이, 플래시론은 가격 조작 공격을 증폭하는 주요 도구로, 공격자가 빌린 자본으로 얇은 유동성 풀을 조작하고 대출 프로토콜에서 그 왜곡된 가격을 악용할 수 있게 하며, 모든 것이 단일 원자적 트랜잭션 내에서 이루어진다.

    복잡한 익스플로잇 체인은 플래시론을 활용하여 상당한 선행 투자가 필요한 다단계 공격에 자본을 제공한다. 공격자는 풀 유동성, 자산별 상한, 트랜잭션별 가스 한도에 의해 제한되지만, 이러한 제약은 종종 여전히 상당한 피해를 허용한다.

    가격 오라클을 넘어, 플래시론은 거버넌스 시스템이 스냅샷이나 플래시론 방지가 강화되지 않은 경우 투표 권한을 빌리는 것과 같은 거버넌스 관련 공격을 촉진할 수 있다.

    프로토콜 방어에는 여러 레이어의 보호 장치가 필요하다. 먼저, 검사-효과-상호작용 패턴을 구현하고 적절한 세분화, 일반적으로 외부 호출 가능하고 상태 변경하는 진입점에 재진입 가드를 적용한다. 지나치게 넓거나 전역적인 가드는 의도된 콜백을 방해할 수 있지만, 일부 컨트랙트에서는 허용될 수 있다. 핵심은 안전하지 않은 재진입을 차단하면서 의도된 조합 가능성을 보존하는 것이다.

    오라클 보호는 또 다른 중요한 방어 레이어를 형성한다. 단일 블록 내에서 지배될 수 없는 장소에서 가져온 다중 블록 TWAP(시간 가중 평균 가격) 또는 중앙값, 예를 들어 Chainlink를 사용한다. 부실성 검사와 함께 독립적인 데이터 소스를 통합한다. 이전 블록 가격만 사용하면 도움이 될 수 있지만, 이 접근법은 재조직이나 얇은 시장에서 취약하다. 가능한 경우 시장 범위 서킷 브레이커를 선호하고, 시스템적 문제에 대해서는 프로토콜 전체 일시 중지로 확대한다.

    추가 보호 조치에는 자산별 부채 상한과 공급/차입 상한을 가진 격리 모드가 포함된다. 보수적인 LTV(담보 대출 비율) 비율과 청산 임계값은 추가 보호를 제공한다. 오라클 소비자에 대한 블록별 속도 제한과 트랜잭션 내 DEX 운영에 대한 슬리피지 검사 및 최소 출력 보호를 구현한다.

    플래시론은 DeFi의 핵심 긴장을 예시한다: 혁신을 가능하게 하는 동일한 조합 가능성이 위험도 증폭한다. 그들은 취약성을 만들지 않고 오히려 기존의 것을 증폭하여, 공격자가 풀 유동성과 트랜잭션 한도의 제약 내에서 상당한 자본을 사용할 수 있을 때에도 안전하게 설계되어야 하는 프로토콜을 필요로 한다.

    수수료는 일반적으로 작지만 균일하지 않으며, 일부 프로토콜은 이를 설정하거나 동적으로 조정하여 얇은 차익 거래 기회를 수익성 없게 만들어 약간의 자연스러운 경제적 보호를 제공할 수 있다. 일부 토큰은 또한 플래시 발행(단일 트랜잭션 내 발행 및 소각)을 지원하며, 이는 해당 특정 토큰에 대한 플래시론과 유사하게 기능한다.

