# Chapter VIII: MEV

=== "English"

    Control over transaction ordering creates and redistributes value on-chain. This chapter explores who extracts that value, how it impacts regular users, and what protections exist to return value or reduce harm.

    ## Section I: MEV Fundamentals

        Picture a busy marketplace with a peculiar setup. A big whiteboard where everyone must post their intended purchases before they can buy anything. A trader writes "buying 10 tomatoes from Stall A," and suddenly chaos erupts.

        A fast-moving reseller spots the order, sprints to Stall A, buys the tomatoes first, then offers them back to the trader at a markup. Another reseller notices the trader is about to make a large purchase that will drive up tomato prices, so they buy just before the trader and sell immediately after, pocketing the price difference the trade created. Meanwhile, the market manager starts auctioning off the right to decide who gets served first: whoever pays the highest tip jumps to the front of the line.

        This market chaos mirrors exactly what happens in the mempool, the public waiting area where transactions sit before being added to the blockchain (introduced in Chapter I for Bitcoin and Chapter II for Ethereum). While both networks use mempools, MEV primarily manifests on Ethereum and other smart contract platforms where complex DeFi transactions create extraction opportunities. The environment resembles what researchers call a "dark forest," borrowing from Liu Cixin's science fiction novel to describe a place where any visible movement attracts predators. In the mempool, revealing a profitable trade is that visible movement.

        **Maximal Extractable Value** (MEV) is the profit that emerges from this system. Originally called "Miner Extractable Value" during Ethereum's proof-of-work era, MEV represents revenue extracted beyond standard block rewards and transaction fees by strategically ordering, including, or excluding transactions within blocks.

        In our market analogy, the key players have clear roles: **searchers** are the fast-moving resellers scanning for opportunities, **builders** are market managers who construct blocks and bid their value to proposers (validators), and **proposers** are the market owners who choose which manager's arrangement to accept. This relationship has been formalized through auction systems that create a liquid market for block space by essentially letting market managers bid for the right to organize transactions.

        The fundamental insight is that MEV arises from controlling transaction visibility and ordering. Some activities, like ensuring prices stay aligned or liquidating bad debt, can stabilize the market. However, the overall effect imposes an implicit tax on regular users through worse execution, while only well-funded professionals with the fastest infrastructure consistently win.

        This creates the core tension: how transaction ordering, designed to be neutral infrastructure, becomes a sophisticated value extraction mechanism that threatens the very decentralization it's meant to serve.

    ## Section II: How Value Gets Extracted

        ### Benevolent vs. Malignant MEV

        Before examining specific extraction strategies, we need a framework for evaluating their market impact. Not all MEV harms markets equally, and distinguishing productive from predatory extraction matters for both protocol design and user protection.

        Benevolent MEV serves necessary economic functions. CEX-DEX arbitrage keeps execution prices for the same asset roughly aligned across venues, so traders see broadly similar prices wherever they trade once you account for liquidity and fees, rather than some venues being systematically "worse" to trade on. Liquidations preserve the solvency of lending protocols by ensuring under-collateralized positions get closed before they become bad debt that would burden all protocol users. These activities extract value, but they also deliver clear benefits: tighter price spreads and healthier lending markets.

        Malignant MEV extracts value without providing commensurate benefits. **Sandwich attacks** exemplify this: the victim pays more, the searcher profits, and the market gains nothing. This is pure wealth transfer enabled by privileged information and ordering control.

        **Just-in-time liquidity** demonstrates this ambiguity. When searchers see a large trade pending, they quickly add liquidity to the relevant pool just for that block, capture the swap fees from executing the trade, and then remove their liquidity in the next block. On one hand, this provides liquidity exactly when needed and can reduce slippage for the trader. On the other hand, it crowds out passive liquidity providers who can't compete with such precision, potentially degrading liquidity depth over time.

        Similarly, oracle updates create another ambiguous MEV channel. When a price feed like Chainlink posts a new price on-chain, searchers try to **back-run** that update by placing their arbitrage trade in the very next transaction. They use the fresh quote to trade against AMMs or perpetual futures that are still priced off the old level, snapping prices back into line. The system benefits from faster price correction, but in practice the profits accrue almost entirely to specialized operators with the fastest infrastructure.

        The key distinction isn't whether value gets extracted (it always does), but whether that extraction serves a necessary function or merely exploits information and ordering advantages. This framework helps us evaluate the strategies that follow.

        ### MEV Extraction Strategies

        From this chaos emerged a hierarchy of exploitation strategies, each more sophisticated than the last. Arbitrage, as described above, sits at the benevolent end. But when competition heats up, searchers get more aggressive.

        They start **front-running**, which means copying a trader's transaction but paying extra to go first. For example, when a trader spots an arbitrage opportunity where they can buy ETH for $3,000 on one DEX and immediately sell it for $3,050 on another, a bot sees the pending transaction and submits the exact same trade with a higher fee to jump ahead in line, capturing that $50 profit before the original trader can.

        Understanding why these strategies work requires recalling how AMMs function (covered in Chapter VII). The deterministic pricing curves mean the price impact of any proposed swap can be calculated in advance. Combined with the public mempool where transactions sit before inclusion, searchers can see a pending trade, estimate exactly how far it will move the price, and position their own transactions around it. Predictable pricing, visible intent, and reorderable transactions create a perfect environment for extraction.

        Consider a representative sandwich attack. A trader submits a transaction to swap ETH for USDC on Uniswap. A searcher's bot detects this pending transaction in the mempool and immediately constructs a three-transaction bundle. First, the bot front-runs by buying USDC using ETH, which pushes the pool price higher. Then the victim's trade executes at this inflated price, receiving significantly less USDC than expected based on the original pool state. Finally, the bot back-runs by immediately selling its USDC position back to the pool. As the price settles back down, the bot exits with a profit after accounting for fees and slippage.

        The trader pays an invisible tax for revealing their intent publicly. The bot risks minimal capital (the trade bundle either executes atomically or reverts entirely) while extracting pure profit. This single transaction illustrates the MEV extraction dynamic in miniature: sophisticated actors use privileged information about pending transactions to extract value from regular users through strategic positioning and timing.

        Beyond price manipulation, liquidations represent another MEV category. Lending protocols (such as Aave, discussed in Chapter VII) set collateral ratios that are safe at the time of borrowing, and positions only become liquidatable when market moves push collateral value down (or debt value up) enough that they fall below the liquidation threshold. When an oracle update reflects that new price, searchers race to be first to repay part of the debt, seize a slice of the collateral, and collect the liquidation bonus. In practice they often back-run oracle updates by placing their liquidation transactions immediately after the price feed update in the same block. Unlike sandwiching, this competition serves a necessary function by clearing under-collateralized positions and keeping the protocol solvent, but it still turns user stress events into MEV auctions and concentrates rewards in the fastest operators.

        Priority-gas-auction bidding historically spiked gas costs as bots competed for transaction priority; today much of that competition is off-chain via specialized auction systems where searchers bid for transaction ordering rights, reducing broad mempool fee spikes but often shifting costs into worse execution for users or rebates captured by intermediaries. This harm is far from theoretical. Every sandwich attack represents value directly transferred from a user to a well-capitalized operator, even if the fee externalities now appear less in the public mempool and more in private routing markets.

        ### How Users Can Protect Themselves

        Given the MEV extraction landscape described above, what practical steps can users take? When submitting transactions to public mempools, assume exploitation is likely.

        The first line of defense is setting tight slippage tolerances to control how much worse a price you will accept. Starting with 0.5 to 1 percent works for most trades, though tokens with low liquidity may still be vulnerable. Setting tolerances too tight, below 0.3 percent, risks failed transactions during normal market swings.

        Private transaction routing offers stronger protection. Services like Flashbots Protect route transactions through private channels instead of broadcasting them to the public mempool. This shields your intent until inclusion, protecting against front-running and sandwich attacks. Failed transactions through these services typically do not cost fees, and some services rebate part of the MEV they help you avoid. The tradeoff is weaker propagation: your order depends on a smaller set of relays and builders rather than the full public network, so inclusion can be less predictable.

        Batch auction systems provide protection through mechanism design rather than just hiding intent. CoW Swap groups orders into batches and uses competitive solvers to find the best execution paths (as introduced in Chapter VII's intent-based systems section), which prevents sandwich attacks that rely on sequential processing. UniswapX uses a declining-price auction where parties compete to fill orders at progressively better prices for the user. Both approaches make extraction structurally harder.

        For large trades, splitting orders across multiple blocks reduces per-trade price impact and makes sandwich attacks less profitable. Time-weighted average price strategies, covered in Chapter VI, break trades into smaller pieces executed over time. Combining this approach with private routing or batch auctions provides layered protection.

        Some platforms build protection directly into their design. Encrypted-mempool systems like Shutter Network keep transaction contents hidden until ordering is fixed, making frontrunning much harder. Over time, Uniswap v4 may add MEV-aware features like dynamic fees or anti-sandwich protections at the pool level.

        The goal is not complete MEV elimination, which is impossible, but making extraction harder and less profitable. These protections help against sandwich attacks but cannot stop all MEV types. The battle constantly evolves as new attack methods emerge.

        ### A Warning About "Easy Money"

        Observing the profitability of MEV extraction, some newcomers wonder whether they should become searchers themselves. A reality check: being a searcher is not free money. Winning priority requires paying fees and accepting price impact, and poorly calibrated attempts often lose money. Because AMM pricing makes each additional unit more expensive to buy, naive bots frequently donate value to professional searchers, builders, and validators when they misjudge fees or slippage. Without precise simulation and risk controls, frontrunning or sandwich attempts often overpay for execution and end up losing rather than extracting value.

    ## Section III: Flashbots: Taming the Dark Forest

        These user-facing protections emerged partly because the industry recognized that individual defenses alone weren't enough. By 2020, Ethereum faced exactly this market chaos at scale. The priority gas auctions described earlier were creating network congestion, while miners were capturing MEV through opaque, off-chain deals that favored well-capitalized participants.

        Enter Flashbots, a research organization founded in 2020 with a radical proposition: instead of trying to eliminate MEV, create transparent infrastructure to make it more fair and efficient. Their insight was that the current system was wasteful, and that channeling extraction through better infrastructure could reduce harm.

        ### MEV-Geth and the First Solution

        In January 2021, Flashbots released MEV-Geth, a modified Ethereum client that let miners accept transaction bundles over a private Flashbots channel instead of only from the public mempool. Rather than spamming ever-higher gas bids in priority gas auctions, searchers could submit bundles directly to miners running MEV-Geth. Miners simulated and ranked these bundles and included the most profitable ones in their blocks. This moved most of the competition off-chain, cutting down on bidding wars in the public mempool while still letting professional searchers compete for MEV opportunities.

        ### The Transition to Proof-of-Stake

        When Ethereum moved to proof-of-stake in September 2022 (a transition detailed in Chapter II), the entire MEV landscape needed rebuilding. Flashbots developed **MEV-Boost**, an open-source middleware that provides **Proposer-Builder Separation** (PBS), a design where specialized builders construct blocks and validators simply choose which block to propose, rather than validators doing both jobs themselves. This expanded the builder-validator relationship introduced earlier into a full competitive marketplace via relays. As of early 2026, approximately 90% of Ethereum blocks are built via MEV-Boost.

        This separation currently exists outside Ethereum's core protocol, implemented through MEV-Boost rather than built into the blockchain itself. Researchers continue working on enshrined PBS, which would make proposer-builder separation a native part of Ethereum, but that work remains in development.

        ### How MEV-Boost Works

        This process is facilitated by trusted entities called **relays**. Relays act as a neutral escrow and auctioneer: builders send them full blocks, and the relay verifies their validity and bid. The relay then forwards only the block header and the bid to the proposer (validators are also called proposers in this context). The proposer chooses a header without seeing the block's contents, preventing them from stealing the MEV opportunity. The system evolved from individual miners making direct deals to a sophisticated auction where multiple builders compete for validator selection, with relays facilitating the bidding process.

        These trust assumptions are not just theoretical. In April 2023, a validator exploited a vulnerability in MEV-Boost and relay handling to "unbundle" private bundles, copy profitable MEV transactions, and siphon more than $20 million from other searchers in a single block. The episode triggered urgent client patches and became the basis for the first high-profile U.S. criminal case about MEV infrastructure: in 2024, federal prosecutors charged two MIT-educated brothers with wire fraud and money laundering for allegedly orchestrating the exploit, with the case still being litigated as of early 2026. Whatever one thinks of the legal theory, it underscored that MEV relays and builders are no longer just technical plumbing but also legal and regulatory attack surfaces.

        ### Expanding User Protection

        Recognizing that infrastructure alone was not enough, Flashbots also launched the user-facing protection service mentioned earlier: Flashbots Protect. By routing transactions through private channels that bypass the public mempool, ordinary users gain protection from sandwich and frontrunning attacks while potentially receiving rebates from captured MEV. These transactions still compete in the builder auction but are never exposed to public mempool predation.

        The Flashbots approach represents a pragmatic philosophy: given that extraction is baked into how ordering markets function, the goal should be making it transparent, efficient, and less harmful. Rather than fighting the economic forces, they built infrastructure to channel them constructively. However, this infrastructure-based solution revealed an uncomfortable truth: organizing MEV markets efficiently also created powerful chokepoints that concentrated control in unexpected ways.

    ## Section IV: The Centralization Crisis

        Despite Flashbots' innovations, the MEV ecosystem faces a fundamental challenge: concentration of power among a small number of operators.

        The extent of this concentration becomes clear when examining recent data. In October 2024, just two builders produced 90% of blocks over a two-week period. From October 2023 through March 2024, three builders controlled approximately 80% of MEV-Boost blocks. During this same timeframe, a significant share of blocks, often around 60%, were relayed via OFAC-compliant infrastructure (adhering to U.S. Office of Foreign Assets Control sanctions). The pattern is unmistakable: these high barriers to entry have consolidated power among a handful of operators, directly undermining blockchain's decentralized principles.

        The relay layer introduces additional centralization concerns. Because only a handful of trusted relays dominate the market, their compliance decisions (such as filtering transactions to adhere to OFAC sanctions) can have network-wide effects. These supposedly neutral intermediaries become powerful chokepoints that shape which transactions actually make it into blocks regardless of individual validator preferences. The choice of which relays to trust can determine transaction inclusion, making censorship resistance vulnerable to a small set of gatekeepers.

        ### Responses to Centralization

        The concentration revealed by these metrics made clear that MEV-Boost alone couldn't solve the centralization problem. The relay layer remained a chokepoint, and builder concentration continued unabated. The industry needed more fundamental restructuring.

        In November 2024, major players launched BuilderNet, a decentralized block-building network jointly operated by Flashbots, Beaverbuild, and Nethermind. BuilderNet uses specialized hardware that creates secure enclaves where code runs in isolation, even from the machine's owner. This technology enables multiple operators to share transaction order flow and coordinate block building while keeping contents private until finalization, since no single party can see or manipulate the data being processed.

        The goal is to create a more transparent and permissionless system for MEV distribution, replacing the opaque, custom deals that currently define the market. Beaverbuild has already begun transitioning its centralized builder to this network, with additional permissionless features planned for future releases.

        Beyond BuilderNet, the ecosystem has developed several complementary approaches to combat centralization and return value to users.

        One approach focuses on returning value directly to users. **Order flow auctions** let users auction off their transaction flow to the highest bidder, potentially earning rebates from the MEV their trades create. The private routing solutions discussed earlier represent one implementation, while encrypted mempools hide transaction details until execution.

        At the protocol level, researchers are exploring ways to distribute MEV rewards more evenly across validators rather than letting them concentrate among the fastest operators. Enshrined PBS would build the proposer-builder separation directly into Ethereum's protocol rather than relying on external infrastructure like MEV-Boost.

        More advanced attacks also require attention. **Time-bandit attacks**, where validators attempt to reorganize recent blocks to capture MEV, are constrained by stronger finality guarantees under proof-of-stake, though related attack vectors remain an active research concern.

        While these solutions show promise, results in practice remain mixed, and the arms race between MEV extraction and protection continues to evolve.

    ## Section V: The Cross-Domain Challenge

        But even as these solutions emerge for single-chain MEV, a far larger threat looms. Just as the industry began addressing extraction within individual blockchains, a new challenge emerged that threatens to dwarf the current problems.

        **Cross-Domain MEV** represents extraction strategies that span multiple blockchains simultaneously, exploiting price differences and timing advantages across separate domains.

        This is not theoretical. Advanced searchers are already executing arbitrage and other strategies across different blockchains, exploiting price differences between DEXs on separate networks. The timing and latency of blockchain bridges become critical factors, enabling complex, multi-block MEV strategies that are even harder to mitigate than their single-chain counterparts.

        Researchers warn it could pose severe risks (sometimes described as 'existential') to decentralization. If specialized participants gain control over transaction ordering across multiple domains, the centralization pressures described earlier could compound exponentially. The cross-domain nature makes coordination harder and value extraction more opaque, potentially creating a new class of MEV that's both more profitable and more harmful to users.

        The fundamental challenge: as the ecosystem grows and interconnects, each new bridge, each new chain, each new connection creates fresh opportunities for value extraction. The solutions that work for single-chain MEV (batch auctions, private orderflow, fair ordering) become exponentially more complex when they must coordinate across multiple domains with different consensus mechanisms, block times, and economic models.

=== "한국어"

    트랜잭션 순서에 대한 통제는 온체인에서 가치를 창출하고 재분배한다. 이 챕터는 누가 그 가치를 추출하는지, 그것이 일반 사용자에게 어떤 영향을 미치는지, 그리고 가치를 돌려주거나 피해를 줄이기 위해 어떤 보호 장치가 존재하는지 탐구한다.

    ## Section I: MEV 기초

        특이한 설정을 가진 분주한 시장을 상상해 보라. 모든 사람이 무엇을 사기 전에 자신의 구매 의도를 게시해야 하는 큰 화이트보드가 있다. 한 거래자가 "A 노점에서 토마토 10개 구매"라고 적자마자 혼란이 일어난다.

        빠르게 움직이는 중개인이 그 주문을 발견하고, A 노점으로 뛰어가 토마토를 먼저 사고, 그 거래자에게 마진을 붙여 다시 판다. 또 다른 중개인은 거래자가 토마토 가격을 올릴 대량 구매를 하려는 것을 알아채고, 거래자보다 먼저 사서 거래 직후에 팔아 그 거래가 만들어낸 가격 차이를 챙긴다. 한편, 시장 관리자는 누가 먼저 서비스를 받을지 결정할 권리를 경매하기 시작한다: 가장 높은 팁을 주는 사람이 줄 앞으로 뛰어들 수 있다.

        이 시장 혼란은 **멤풀(Mempool)**(Chapter I의 비트코인과 Chapter II의 이더리움에서 소개된, 트랜잭션이 블록체인에 추가되기 전에 대기하는 공개 대기 영역)에서 일어나는 일과 정확히 일치한다. 두 네트워크 모두 멤풀을 사용하지만, MEV는 주로 복잡한 DeFi 트랜잭션이 추출 기회를 만드는 이더리움과 다른 스마트 컨트랙트 플랫폼에서 나타난다. 이 환경은 연구자들이 **"다크 포레스트(Dark Forest)"**라 부르는 것과 유사한데, 류츠신의 SF 소설에서 빌려온 이 용어는 보이는 움직임이 포식자를 끌어들이는 장소를 묘사한다. 멤풀에서 수익성 있는 거래를 드러내는 것이 바로 그 보이는 움직임이다.

        **최대 추출 가능 가치(Maximal Extractable Value, MEV)**는 이 시스템에서 발생하는 이익이다. 원래 이더리움의 작업 증명(Proof of Work) 시대에는 "채굴자 추출 가능 가치(Miner Extractable Value)"라고 불렸는데, MEV는 블록 내에서 트랜잭션을 전략적으로 순서화하거나, 포함하거나, 제외함으로써 표준 블록 보상과 트랜잭션 수수료를 넘어 추출되는 수익을 나타낸다.

        우리의 시장 비유에서, 핵심 참여자들은 명확한 역할을 가진다: **서처(Searcher)**는 기회를 찾아 스캔하는 빠르게 움직이는 중개인이고, **빌더(Builder)**는 블록을 구성하고 그 가치를 프로포저(검증자)에게 입찰하는 시장 관리자이며, **프로포저(Proposer)**는 어떤 관리자의 배열을 수락할지 선택하는 시장 소유자이다. 이 관계는 본질적으로 시장 관리자들이 트랜잭션을 조직할 권리를 입찰하게 함으로써 블록 공간에 대한 유동적 시장을 만드는 경매 시스템을 통해 공식화되었다.

        근본적인 통찰은 MEV가 트랜잭션 가시성과 순서화에 대한 통제에서 발생한다는 것이다. 가격을 정렬하거나 부실 채권을 청산하는 것과 같은 일부 활동은 시장을 안정시킬 수 있다. 그러나 전체적인 효과는 더 나쁜 체결을 통해 일반 사용자에게 암묵적인 세금을 부과하는 반면, 가장 빠른 인프라를 갖춘 자금력 있는 전문가들만이 지속적으로 승리한다.

        이것이 핵심적인 긴장을 만든다: 중립적인 인프라가 되도록 설계된 트랜잭션 순서화가 어떻게 그것이 봉사해야 할 탈중앙화 자체를 위협하는 정교한 가치 추출 메커니즘이 되는가.

    ## Section II: 가치가 추출되는 방식

        ### 선의적 MEV vs 악의적 MEV

        특정 추출 전략을 검토하기 전에, 그들의 시장 영향을 평가하기 위한 프레임워크가 필요하다. 모든 MEV가 시장에 동등하게 해를 끼치는 것은 아니며, 생산적인 추출과 약탈적인 추출을 구별하는 것이 프로토콜 설계와 사용자 보호 모두에 중요하다.

        **선의적 MEV(Benevolent MEV)**는 필요한 경제적 기능을 수행한다. CEX-DEX 차익 거래는 유동성과 수수료를 고려한 후 동일한 자산의 체결 가격을 거래소 전반에 걸쳐 대략 정렬시켜, 일부 거래소가 체계적으로 거래하기에 "더 나쁜" 곳이 되지 않도록 거래자들이 어디서든 대체로 유사한 가격을 볼 수 있게 한다. 청산은 담보 부족 포지션이 모든 프로토콜 사용자에게 부담이 될 부실 채권이 되기 전에 닫히도록 보장함으로써 대출 프로토콜의 지급 능력을 유지한다. 이러한 활동은 가치를 추출하지만, 더 좁은 가격 스프레드와 더 건강한 대출 시장이라는 명확한 이점도 제공한다.

        **악의적 MEV(Malignant MEV)**는 상응하는 이점을 제공하지 않고 가치를 추출한다. **샌드위치 공격(Sandwich Attack)**이 이를 잘 보여준다: 피해자는 더 많이 지불하고, 서처는 이익을 얻고, 시장은 아무것도 얻지 못한다. 이것은 특권적 정보와 순서화 통제에 의해 가능해진 순수한 부의 이전이다.

        **적시 유동성(Just-In-Time Liquidity, JIT Liquidity)**은 이 모호함을 보여준다. 서처가 대규모 거래가 대기 중인 것을 보면, 해당 블록에서만 관련 풀에 빠르게 유동성을 추가하고, 거래를 실행하면서 스왑 수수료를 캡처한 다음, 다음 블록에서 유동성을 제거한다. 한편으로 이것은 정확히 필요할 때 유동성을 제공하고 거래자의 슬리피지를 줄일 수 있다. 다른 한편으로 이것은 그러한 정밀함과 경쟁할 수 없는 수동적 유동성 공급자를 밀어내어, 시간이 지남에 따라 잠재적으로 유동성 깊이를 저하시킬 수 있다.

        마찬가지로, 오라클 업데이트는 또 다른 모호한 MEV 채널을 만든다. Chainlink와 같은 가격 피드가 새로운 가격을 온체인에 게시할 때, 서처들은 동일한 블록 내에서 가격 피드 업데이트 바로 다음에 차익 거래를 배치하여 해당 업데이트를 **백러닝(Back-running)**하려고 한다. 그들은 새로운 호가를 사용하여 여전히 이전 수준으로 가격이 매겨진 AMM이나 무기한 선물에 대해 거래하여, 가격을 다시 일치시킨다. 시스템은 더 빠른 가격 조정으로부터 이점을 얻지만, 실제로 이익은 거의 전적으로 가장 빠른 인프라를 가진 전문 운영자에게 돌아간다.

        핵심적인 구별은 가치가 추출되는지 여부(항상 추출된다)가 아니라, 그 추출이 필요한 기능을 수행하는지 아니면 단순히 정보와 순서화 이점을 착취하는지이다. 이 프레임워크는 다음에 나올 전략들을 평가하는 데 도움이 된다.

        ### MEV 추출 전략

        이 혼란에서 착취 전략의 위계가 등장했으며, 각각은 이전보다 더 정교하다. 위에서 설명한 차익 거래는 선의적인 끝에 위치한다. 그러나 경쟁이 치열해지면 서처들은 더 공격적이 된다.

        그들은 **프런트러닝(Front-running)**을 시작하는데, 이것은 거래자의 트랜잭션을 복사하되 먼저 가기 위해 추가 비용을 지불하는 것을 의미한다. 예를 들어, 거래자가 한 DEX에서 ETH를 $3,000에 사서 다른 DEX에서 즉시 $3,050에 팔 수 있는 차익 거래 기회를 발견하면, 봇이 대기 중인 트랜잭션을 보고 줄을 앞서기 위해 더 높은 수수료로 정확히 같은 거래를 제출하여, 원래 거래자가 하기 전에 그 $50 이익을 캡처한다.

        이러한 전략이 왜 작동하는지 이해하려면 AMM이 어떻게 기능하는지 상기해야 한다(Chapter VII에서 다룸). 결정론적 가격 곡선은 제안된 스왑의 가격 영향을 미리 계산할 수 있다는 것을 의미한다. 트랜잭션이 포함되기 전에 대기하는 공개 멤풀과 결합하면, 서처들은 대기 중인 거래를 보고, 그것이 가격을 얼마나 움직일지 정확히 추정하고, 그 주변에 자신의 트랜잭션을 배치할 수 있다. 예측 가능한 가격 책정, 보이는 의도, 재순서화 가능한 트랜잭션이 추출을 위한 완벽한 환경을 만든다.

        대표적인 샌드위치 공격을 고려해 보자. 거래자가 Uniswap에서 ETH를 USDC로 스왑하는 트랜잭션을 제출한다. 서처의 봇이 멤풀에서 이 대기 중인 트랜잭션을 감지하고 즉시 세 개의 트랜잭션 번들을 구성한다. 먼저, 봇은 ETH를 사용하여 USDC를 구매함으로써 프런트러닝하여 풀 가격을 높인다. 그 다음 피해자의 거래가 이 부풀려진 가격에 실행되어, 원래 풀 상태를 기준으로 예상했던 것보다 상당히 적은 USDC를 받는다. 마지막으로, 봇은 USDC 포지션을 풀에 다시 매도함으로써 백러닝한다. 가격이 다시 정착하면서, 봇은 수수료와 슬리피지를 감안한 후 이익으로 빠져나간다.

        거래자는 자신의 의도를 공개적으로 드러낸 것에 대해 보이지 않는 세금을 낸다. 봇은 최소한의 자본을 위험에 노출시키면서(거래 번들은 원자적으로 실행되거나 완전히 되돌려진다) 순수한 이익을 추출한다. 이 단일 트랜잭션은 MEV 추출 역학을 축소판으로 보여준다: 정교한 행위자들이 대기 중인 트랜잭션에 대한 특권적 정보를 사용하여 전략적 포지셔닝과 타이밍을 통해 일반 사용자로부터 가치를 추출한다.

        가격 조작 외에도, 청산은 또 다른 MEV 범주를 나타낸다. 대출 프로토콜(Chapter VII에서 논의된 Aave와 같은)은 대출 시점에 안전한 담보 비율을 설정하며, 포지션은 시장 움직임이 담보 가치를 낮추거나(또는 부채 가치를 높여) 청산 임계값 아래로 떨어질 때만 청산 가능해진다. 오라클 업데이트가 새로운 가격을 반영하면, 서처들은 부채의 일부를 상환하고 담보의 일부를 압류하며 청산 보너스를 받기 위해 먼저가 되려고 경쟁한다. 실제로 그들은 종종 동일한 블록 내에서 가격 피드 업데이트 바로 다음에 청산 트랜잭션을 배치하여 오라클 업데이트를 백러닝한다. 샌드위칭과 달리, 이 경쟁은 담보 부족 포지션을 청산하고 프로토콜의 지급 능력을 유지하는 필요한 기능을 수행하지만, 여전히 사용자 스트레스 이벤트를 MEV 경매로 바꾸고 보상을 가장 빠른 운영자에게 집중시킨다.

        우선순위 가스 경매 입찰은 역사적으로 봇들이 트랜잭션 우선순위를 위해 경쟁하면서 가스 비용을 급등시켰다; 오늘날 그 경쟁의 대부분은 서처들이 트랜잭션 순서화 권리를 입찰하는 전문 경매 시스템을 통해 오프체인에서 이루어져, 광범위한 멤풀 수수료 급등을 줄이지만 종종 사용자에게 더 나쁜 체결로 비용을 이전시키거나 중개자가 캡처하는 리베이트로 전환한다. 이 피해는 이론적이지 않다. 모든 샌드위치 공격은 사용자에서 자본력 있는 운영자에게 직접 이전되는 가치를 나타내며, 수수료 외부효과가 이제 공개 멤풀에서 덜 나타나고 개인 라우팅 시장에서 더 많이 나타나더라도 마찬가지이다.

        ### 사용자가 스스로를 보호하는 방법

        위에서 설명한 MEV 추출 환경을 감안할 때, 사용자가 취할 수 있는 실질적인 조치는 무엇인가? 공개 멤풀에 트랜잭션을 제출할 때, 착취가 일어날 가능성이 높다고 가정하라.

        첫 번째 방어선은 수용할 수 있는 가격 악화 정도를 제어하기 위해 **타이트한 슬리피지 허용치(Slippage Tolerance)**를 설정하는 것이다. 0.5%에서 1%로 시작하는 것이 대부분의 거래에 적합하지만, 낮은 유동성을 가진 토큰은 여전히 취약할 수 있다. 0.3% 미만으로 허용치를 너무 타이트하게 설정하면 정상적인 시장 변동에서 트랜잭션 실패 위험이 있다.

        **프라이빗 트랜잭션 라우팅(Private Transaction Routing)**은 더 강력한 보호를 제공한다. Flashbots Protect와 같은 서비스는 공개 멤풀에 브로드캐스트하는 대신 프라이빗 채널을 통해 트랜잭션을 라우팅한다. 이것은 포함될 때까지 당신의 의도를 보호하여, 프런트러닝과 샌드위치 공격으로부터 보호한다. 이러한 서비스를 통한 실패한 트랜잭션은 일반적으로 수수료가 들지 않으며, 일부 서비스는 당신이 피한 MEV의 일부를 리베이트로 제공한다. 트레이드오프는 더 약한 전파이다: 당신의 주문은 전체 공개 네트워크가 아닌 더 작은 릴레이와 빌더 세트에 의존하므로 포함이 덜 예측 가능할 수 있다.

        **배치 옥션 시스템(Batch Auction System)**은 단순히 의도를 숨기는 것이 아니라 메커니즘 설계를 통해 보호를 제공한다. CoW Swap은 주문을 배치로 그룹화하고 경쟁적 솔버를 사용하여 최상의 체결 경로를 찾으며(Chapter VII의 인텐트 기반 시스템 섹션에서 소개됨), 이는 순차적 처리에 의존하는 샌드위치 공격을 방지한다. UniswapX는 당사자들이 사용자에게 점진적으로 더 좋은 가격으로 주문을 채우기 위해 경쟁하는 하락 가격 경매를 사용한다. 두 접근법 모두 추출을 구조적으로 더 어렵게 만든다.

        대규모 거래의 경우, 여러 블록에 걸쳐 주문을 분할하면 거래당 가격 영향이 줄어들고 샌드위치 공격의 수익성이 낮아진다. Chapter VI에서 다룬 **시간 가중 평균 가격(Time-Weighted Average Price, TWAP) 전략**은 거래를 시간에 걸쳐 실행되는 더 작은 조각으로 분할한다. 이 접근법을 프라이빗 라우팅이나 배치 옥션과 결합하면 계층화된 보호를 제공한다.

        일부 플랫폼은 설계에 직접 보호를 내장한다. Shutter Network와 같은 **암호화된 멤풀(Encrypted Mempool)** 시스템은 순서화가 고정될 때까지 트랜잭션 내용을 숨겨, 프런트러닝을 훨씬 더 어렵게 만든다. 시간이 지남에 따라, Uniswap v4는 풀 수준에서 동적 수수료나 샌드위치 방지 보호와 같은 MEV 인식 기능을 추가할 수 있다.

        목표는 불가능한 완전한 MEV 제거가 아니라, 추출을 더 어렵고 덜 수익성 있게 만드는 것이다. 이러한 보호 장치는 샌드위치 공격에 대해 도움이 되지만 모든 MEV 유형을 막을 수는 없다. 새로운 공격 방법이 등장함에 따라 전투는 끊임없이 진화한다.

        ### "쉬운 돈"에 대한 경고

        MEV 추출의 수익성을 관찰하면서, 일부 신규 참여자들은 스스로 서처가 되어야 할지 궁금해한다. 현실 점검: 서처가 되는 것은 공짜 돈이 아니다. 우선순위를 이기려면 수수료를 지불하고 가격 영향을 감수해야 하며, 잘못 조정된 시도는 종종 돈을 잃는다. AMM 가격 책정이 각 추가 단위를 더 비싸게 만들기 때문에, 순진한 봇들은 수수료나 슬리피지를 잘못 판단하면 종종 전문 서처, 빌더, 검증자에게 가치를 기부하게 된다. 정밀한 시뮬레이션과 위험 통제 없이, 프런트러닝이나 샌드위치 시도는 종종 체결에 과다 지불하고 가치를 추출하기보다 잃게 된다.

    ## Section III: Flashbots: 다크 포레스트 길들이기

        이러한 사용자 대상 보호 장치는 부분적으로 업계가 개인적인 방어만으로는 충분하지 않다는 것을 인식했기 때문에 등장했다. 2020년까지 이더리움은 정확히 이 시장 혼란을 대규모로 직면했다. 앞서 설명한 우선순위 가스 경매가 네트워크 혼잡을 만들고 있었고, 채굴자들은 자금력 있는 참가자에게 유리한 불투명한 오프체인 거래를 통해 MEV를 캡처하고 있었다.

        **Flashbots**가 등장했다. 2020년에 설립된 이 연구 조직은 급진적인 제안을 했다: MEV를 제거하려 하지 말고, 더 공정하고 효율적으로 만들기 위한 투명한 인프라를 만들자. 그들의 통찰은 현재 시스템이 낭비적이며, 더 나은 인프라를 통해 추출을 채널링하면 피해를 줄일 수 있다는 것이었다.

        ### MEV-Geth와 첫 번째 솔루션

        2021년 1월, Flashbots는 **MEV-Geth**를 출시했다. 이것은 채굴자가 공개 멤풀뿐만 아니라 프라이빗 Flashbots 채널을 통해 트랜잭션 번들을 수락할 수 있게 해주는 수정된 이더리움 클라이언트였다. 우선순위 가스 경매에서 점점 더 높은 가스 입찰을 스팸하는 대신, 서처들은 MEV-Geth를 실행하는 채굴자에게 직접 번들을 제출할 수 있었다. 채굴자들은 이러한 번들을 시뮬레이션하고 순위를 매긴 후 가장 수익성 있는 것을 블록에 포함시켰다. 이것은 대부분의 경쟁을 오프체인으로 이동시켜, 전문 서처들이 여전히 MEV 기회를 위해 경쟁하면서도 공개 멤풀에서의 입찰 전쟁을 줄였다.

        ### 지분 증명으로의 전환

        이더리움이 2022년 9월에 지분 증명(Proof of Stake)으로 이동했을 때(Chapter II에서 자세히 설명된 전환), 전체 MEV 환경은 재구축이 필요했다. Flashbots는 **MEV-Boost**를 개발했다. 이것은 **제안자-빌더 분리(Proposer-Builder Separation, PBS)**를 제공하는 오픈 소스 미들웨어로, 전문 빌더가 블록을 구성하고 검증자는 단순히 어떤 블록을 제안할지 선택하는 설계이다(검증자가 두 작업을 모두 하는 것이 아니라). 이것은 앞서 소개한 빌더-검증자 관계를 릴레이를 통한 완전한 경쟁적 마켓플레이스로 확장했다. 2026년 초 현재, 약 90%의 이더리움 블록이 MEV-Boost를 통해 빌드된다.

        이 분리는 현재 이더리움의 핵심 프로토콜 외부에 존재하며, 블록체인 자체에 내장되지 않고 MEV-Boost를 통해 구현된다. 연구자들은 제안자-빌더 분리를 이더리움의 네이티브 부분으로 만드는 **내장 PBS(Enshrined PBS)**에 대해 계속 작업하고 있지만, 그 작업은 여전히 개발 중이다.

        ### MEV-Boost 작동 방식

        이 프로세스는 **릴레이(Relay)**라 불리는 신뢰받는 엔티티에 의해 촉진된다. 릴레이는 중립적인 에스크로와 경매인 역할을 한다: 빌더가 그들에게 전체 블록을 보내면, 릴레이는 그 유효성과 입찰을 검증한다. 그 다음 릴레이는 프로포저(검증자도 이 맥락에서 프로포저라 불림)에게 블록 헤더와 입찰만 전달한다. 프로포저는 블록의 내용을 보지 않고 헤더를 선택하여, MEV 기회를 훔치는 것을 방지한다. 시스템은 개별 채굴자가 직접 거래를 하던 것에서 여러 빌더가 검증자 선택을 위해 경쟁하는 정교한 경매로 진화했으며, 릴레이가 입찰 프로세스를 촉진한다.

        이러한 신뢰 가정은 이론적인 것만이 아니다. 2023년 4월, 한 검증자가 MEV-Boost와 릴레이 처리의 취약점을 악용하여 프라이빗 번들을 "언번들"하고, 수익성 있는 MEV 트랜잭션을 복사하여, 단일 블록에서 다른 서처들로부터 2천만 달러 이상을 빼돌렸다. 이 에피소드는 긴급한 클라이언트 패치를 촉발했고 MEV 인프라에 대한 첫 번째 주목할 만한 미국 형사 사건의 근거가 되었다: 2024년, 연방 검찰은 이 익스플로잇을 조직한 혐의로 MIT 출신의 두 형제를 와이어 사기와 자금 세탁 혐의로 기소했으며, 2026년 초 현재 사건은 여전히 소송 중이다. 법적 이론에 대해 어떻게 생각하든, 이것은 MEV 릴레이와 빌더가 더 이상 단순한 기술적 배관이 아니라 법적, 규제적 공격 표면이기도 하다는 것을 강조했다.

        ### 사용자 보호 확대

        인프라만으로는 충분하지 않다는 것을 인식하고, Flashbots는 앞서 언급한 사용자 대상 보호 서비스인 **Flashbots Protect**도 출시했다. 공개 멤풀을 우회하는 프라이빗 채널을 통해 트랜잭션을 라우팅함으로써, 일반 사용자는 샌드위치와 프런트러닝 공격으로부터 보호를 받으면서 잠재적으로 캡처된 MEV로부터 리베이트를 받을 수 있다. 이러한 트랜잭션은 여전히 빌더 옥션에서 경쟁하지만 공개 멤풀 약탈에는 노출되지 않는다.

        Flashbots 접근법은 실용주의적 철학을 대표한다: 추출이 순서화 시장이 기능하는 방식에 내장되어 있다면, 목표는 그것을 투명하고, 효율적이며, 덜 해롭게 만드는 것이어야 한다. 경제적 힘과 싸우기보다, 그들은 그것을 건설적으로 채널링하는 인프라를 구축했다. 그러나 이 인프라 기반 솔루션은 불편한 진실을 드러냈다: MEV 시장을 효율적으로 조직하는 것은 또한 예상치 못한 방식으로 통제를 집중시키는 강력한 병목점을 만들었다.

    ## Section IV: 중앙화 위기

        Flashbots의 혁신에도 불구하고, MEV 생태계는 근본적인 도전에 직면한다: 소수의 운영자에게 권력이 집중되는 것.

        이 집중의 정도는 최근 데이터를 검토하면 명확해진다. 2024년 10월, 단 두 명의 빌더가 2주간 블록의 90%를 생산했다. 2023년 10월부터 2024년 3월까지, 세 명의 빌더가 MEV-Boost 블록의 약 80%를 통제했다. 같은 기간 동안, 블록의 상당 부분(종종 약 60%)이 OFAC 준수 인프라(미국 해외자산통제국 제재 준수)를 통해 릴레이되었다. 패턴은 명백하다: 이러한 높은 진입 장벽은 소수의 운영자에게 권력을 집중시켜, 블록체인의 탈중앙화 원칙을 직접적으로 훼손한다.

        릴레이 레이어는 추가적인 중앙화 우려를 도입한다. 소수의 신뢰받는 릴레이만이 시장을 지배하기 때문에, 그들의 컴플라이언스 결정(OFAC 제재를 준수하기 위해 트랜잭션을 필터링하는 것과 같은)은 네트워크 전체에 영향을 미칠 수 있다. 이러한 가정상 중립적인 중개자들은 개별 검증자 선호도와 관계없이 어떤 트랜잭션이 실제로 블록에 들어가는지를 형성하는 강력한 병목점이 된다. 어떤 릴레이를 신뢰할지 선택하는 것이 트랜잭션 포함을 결정할 수 있어, 검열 저항성이 소수의 게이트키퍼에 취약해진다.

        ### 중앙화에 대한 대응

        이러한 지표로 드러난 집중은 MEV-Boost만으로는 중앙화 문제를 해결할 수 없다는 것을 명확히 했다. 릴레이 레이어는 병목점으로 남아 있었고, 빌더 집중은 계속되었다. 업계는 더 근본적인 구조 조정이 필요했다.

        2024년 11월, 주요 참여자들이 **BuilderNet**을 출시했다. 이것은 Flashbots, Beaverbuild, Nethermind가 공동으로 운영하는 탈중앙화 블록 빌딩 네트워크이다. BuilderNet은 기계 소유자로부터도 격리된 상태에서 코드가 실행되는 보안 엔클레이브를 만드는 특수 하드웨어를 사용한다. 이 기술은 여러 운영자가 트랜잭션 주문 흐름을 공유하고 블록 빌딩을 조율하면서 최종화될 때까지 내용을 비공개로 유지할 수 있게 해준다. 어떤 단일 당사자도 처리되는 데이터를 보거나 조작할 수 없기 때문이다.

        목표는 현재 시장을 정의하는 불투명한 맞춤형 거래를 대체하여 MEV 분배를 위한 더 투명하고 무허가적인 시스템을 만드는 것이다. Beaverbuild는 이미 중앙화된 빌더를 이 네트워크로 전환하기 시작했으며, 추가적인 무허가 기능이 향후 출시에 계획되어 있다.

        BuilderNet 외에도, 생태계는 중앙화에 대응하고 사용자에게 가치를 돌려주기 위한 여러 보완적 접근법을 개발했다.

        한 가지 접근법은 사용자에게 직접 가치를 돌려주는 데 초점을 맞춘다. **주문 흐름 경매(Order Flow Auction)**는 사용자가 트랜잭션 흐름을 최고 입찰자에게 경매하여, 잠재적으로 그들의 거래가 만드는 MEV로부터 리베이트를 받을 수 있게 한다. 앞서 논의된 프라이빗 라우팅 솔루션이 한 가지 구현을 나타내며, 암호화된 멤풀은 실행될 때까지 트랜잭션 세부 정보를 숨긴다.

        프로토콜 수준에서, 연구자들은 MEV 보상을 가장 빠른 운영자에게 집중시키는 대신 검증자 전체에 더 균등하게 분배하는 방법을 탐구하고 있다. 내장 PBS는 제안자-빌더 분리를 MEV-Boost와 같은 외부 인프라에 의존하지 않고 이더리움 프로토콜에 직접 구축할 것이다.

        더 고급 공격도 주의가 필요하다. **타임밴딧 공격(Time-Bandit Attack)**은 검증자가 최근 블록을 재구성하여 MEV를 캡처하려는 시도로, 지분 증명 하에서 더 강력한 최종성 보장에 의해 제한되지만, 관련 공격 벡터는 여전히 활발한 연구 관심사로 남아 있다.

        이러한 솔루션은 가능성을 보여주지만, 실제 결과는 여전히 혼합되어 있으며, MEV 추출과 보호 사이의 군비 경쟁은 계속 진화하고 있다.

    ## Section V: 크로스 도메인 도전

        이러한 솔루션들이 단일 체인 MEV에 대해 등장하고 있는 동안에도, 훨씬 더 큰 위협이 다가오고 있다. 업계가 개별 블록체인 내의 추출을 다루기 시작할 무렵, 현재 문제를 왜소하게 만들 위협이 될 수 있는 새로운 도전이 등장했다.

        **크로스 도메인 MEV(Cross-Domain MEV)**는 여러 블록체인에 동시에 걸쳐 작동하는 추출 전략을 나타내며, 별도의 도메인 간의 가격 차이와 타이밍 이점을 착취한다.

        이것은 이론적이지 않다. 고급 서처들은 이미 서로 다른 블록체인에 걸쳐 차익 거래 및 기타 전략을 실행하며, 별도의 네트워크에 있는 DEX 간의 가격 차이를 착취하고 있다. 블록체인 브릿지의 타이밍과 지연이 중요한 요소가 되어, 단일 체인 대응물보다 완화하기 훨씬 더 어려운 복잡한 다중 블록 MEV 전략을 가능하게 한다.

        연구자들은 이것이 탈중앙화에 심각한 위험(때때로 '실존적'으로 묘사됨)을 제기할 수 있다고 경고한다. 전문화된 참가자가 여러 도메인에 걸쳐 트랜잭션 순서화에 대한 통제권을 얻으면, 앞서 설명한 중앙화 압력이 기하급수적으로 복합될 수 있다. 크로스 도메인 특성은 조율을 더 어렵게 만들고 가치 추출을 더 불투명하게 만들어, 잠재적으로 더 수익성 있고 사용자에게 더 해로운 새로운 클래스의 MEV를 만들 수 있다.

        근본적인 도전: 생태계가 성장하고 상호 연결됨에 따라, 새로운 브릿지, 새로운 체인, 새로운 연결 각각이 가치 추출을 위한 새로운 기회를 만든다. 단일 체인 MEV에 효과적인 솔루션(배치 옥션, 프라이빗 주문 흐름, 공정한 순서화)은 서로 다른 합의 메커니즘, 블록 시간, 경제 모델을 가진 여러 도메인에 걸쳐 조율해야 할 때 기하급수적으로 더 복잡해진다.