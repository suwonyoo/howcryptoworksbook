# Chapter I: A Comprehensive Introduction to Bitcoin

## Section I: Bitcoin Core Concepts

=== "EN"

    Bitcoin emerged from the ashes of the 2008 global financial crisis. On January 3rd, 2009, its anonymous creator, Satoshi Nakamoto, inscribed a telling message into Bitcoin's **genesis block**, the first block in its blockchain. The headline from *The Times* read: "Chancellor on brink of second bailout for banks." It served as a permanent statement of purpose, a critique embedded in code against centralized financial systems that had failed the world.

    Bitcoin's design draws from the cypherpunk movement, which championed using cryptography to protect individual freedom and financial sovereignty. Rather than relying on banks or governments, Bitcoin functions as a peer-to-peer electronic cash system with no trusted intermediaries.

    Its monetary policy is transparent, predictable, and enforced by mathematics rather than central bankers. It's perhaps the only asset in the world with a limited supply that can be independently verified. This programmed scarcity stands in stark contrast to fiat currencies, which can be printed without limit, and to hard assets like gold, which has a theoretically finite supply but no one actually knows the total amount in existence.

    But this vision raised a fundamental question: How could thousands of computers scattered across the globe reach consensus on who owns what, without any central authority to settle disputes?

    ### Mining and Proof of Work

    Bitcoin's Proof of Work system enables miners to prove they've expended enormous computational effort in a way that anyone can quickly verify. At the heart of this process is a **hash function**: a mathematical operation that takes any input data and transforms it into a fixed-length string of characters. What makes hash functions special is that they're one-way: you can't recover the input from the output, and even the tiniest change to the input produces a completely different, unpredictable result.

    Miners bundle transactions into a block and then try to solve a computational puzzle. Think of it like rolling dice with astronomical odds, trying to get a number below a certain threshold. Except miners are "rolling" trillions of times per second. They do this by repeatedly running the block data through the SHA-256 hashing algorithm. SHA-256 is a cryptographic hash function standardized by the U.S. government, and Bitcoin applies it twice for additional security. Each run produces a random-looking output.

    Each attempt uses a different number called a **nonce**, essentially just a counter that increments from zero to about 4 billion. Each nonce generates a different, unpredictable hash result. When a miner finally finds an output below the network's target threshold, they've solved the puzzle and can add their block to the blockchain.

    But modern mining hardware is so fast it can exhaust all 4 billion nonce values in seconds. When that happens, miners need another way to vary their input. This is where the coinbase transaction comes in. Every block contains a special coinbase transaction that pays the miner their block reward plus any transaction fees, effectively "creating" new bitcoin. This transaction is unrelated to the exchange of the same name. Miners can modify a field within this coinbase transaction called the extra nonce, or they can increment the block's timestamp. Either change alters the block header hash and resets their search space.

    The speed at which miners make these attempts is called hash rate, measured in terahashes or exahashes per second. It shows how many hashes a miner or the entire network can try each second. You might think a higher network hash rate would make blocks come faster, but the network automatically adjusts the difficulty to compensate. Every 2,016 blocks, roughly every two weeks, the network performs a difficulty retarget. It measures how long those blocks actually took and adjusts the target accordingly. To prevent wild swings, these adjustments are capped between one-quarter and four times the previous difficulty, keeping the average block time stable at 10 minutes.

    Miners use specialized chips called **ASICs**, designed specifically for SHA-256 proof-of-work. These chips are thousands of times more efficient than regular computers for this task. Even with the best hardware, solo mining is like playing a massive lottery where you might wait years without finding a single block. To smooth out this variance, miners join **mining pools**. These pools use a communication standard called Stratum to coordinate work between miners. The pool combines everyone's computing power and shares rewards proportionally based on each miner's contribution. This provides steady, predictable payouts instead of long dry spells.

    The newly created coins from a block's coinbase transaction can't be spent immediately. They must wait until 100 more blocks have been added on top, which takes about 16 to 17 hours. This delay makes it much harder for miners to profit from attempting to rewrite recent blockchain history.

    ### Consensus and Chain Selection

    Now that we understand how mining works, we can explore how the network reaches agreement on which chain is valid.

    Bitcoin's network is composed of nodes, which are computers running Bitcoin software that independently verify every transaction and block to ensure they follow the rules. These nodes maintain a complete copy of the blockchain and relay valid information to other participants. Miners typically run nodes themselves to verify the blocks they build, but many participants run nodes without mining, simply to validate Bitcoin's state independently and contribute to the network's decentralization. When people refer to "nodes" in Bitcoin discussions, they usually mean these non-mining participants who verify but don't produce blocks.

    Bitcoin solves consensus through a robust mechanism called **Nakamoto Consensus**, which is often simplified as the "longest chain rule" but is more accurately described as the chain with the most cumulative work. Think of two hikers taking different routes: one takes 1,000 easy steps, the other 600 hard steps. The system doesn't score by steps (block count) but by energy required (a stand in for work), so the steeper, harder route can "weigh" more even with fewer steps. Nodes follow the same principle, choosing whichever chain required the most cumulative computational work to produce. An attacker can't rewrite history by simply creating more blocks; they must produce at least as much total work as the honest chain, and then some.

    Occasionally, two miners find valid blocks at nearly the same time, creating temporary forks in the blockchain. Different parts of the network will initially follow different blocks depending on which one they heard about first. The tie is broken when the next block is found. Whichever fork gets extended first becomes longer and automatically wins. At that point, all nodes on the network switch to follow the longer chain, abandoning the shorter one. The block on the losing fork becomes stale, meaning it's discarded and not included in the final blockchain, and its transactions go back to being unconfirmed. This whole process usually resolves within minutes.

    These chain reorganizations (or "reorgs") are a normal and expected part of Bitcoin's operation. One-block reorgs occur occasionally, two-block reorgs are rare, three or more are extremely rare absent an attack or severe network partition. This probabilistic behavior is why confirmations matter: the probability that a transaction is affected by a reorg falls exponentially with each additional block. Merchants typically wait for multiple confirmations (often six) before considering large payments final.

    Beyond natural forks, Bitcoin faces other potential attacks. Eclipse attacks involve isolating a node's network connections to feed it a distorted view of the blockchain. Selfish mining involves withholding found blocks to mine privately and publish strategically for a revenue advantage. Diversity of peers, network-level protections, and monitoring help mitigate these risks.

    ### Monetary Policy

    Bitcoin has a predictable, algorithmic monetary policy with a fixed issuance schedule. The block reward, or subsidy, is cut in half every 210,000 blocks, an event known as the "**halving**" that occurs roughly every four years. The subsidy began at 50 BTC and has since been reduced to 25, 12.5, 6.25, and most recently to 3.125 BTC after the 2024 halving.

    This mechanism makes Bitcoin a disinflationary asset, as its inflation rate trends toward zero. Around the year 2140, the subsidy will cease, and miners will be compensated solely by transaction fees. Due to integer rounding in halvings, the terminal supply converges to \~20,999,999.9769 BTC. As of early 2026, roughly 95% of the eventual 21 million BTC has already been mined and is in circulation.

    Miners earn revenue from two sources: the block subsidy (new issuance of BTC) and transaction fees paid by users. The vast majority of miner revenue comes from the block subsidy. In 2024, the block subsidy accounted for approximately 94% of total earnings. This combined revenue, known as the **security budget**, determines the cost of attacking the network, explored in detail in Section IV.

    Bitcoin's predictable scarcity forms a cornerstone of its store of value proposition. However, scarcity alone doesn't guarantee price appreciation as price ultimately depends on sustained demand from buyers. Decreasing issuance creates favorable supply dynamics, but this only translates to price appreciation if accompanied by buying pressure that exceeds selling pressure in the market.

=== "KO"

    비트코인은 2008년 글로벌 금융 위기의 잿더미 속에서 탄생했다. 2009년 1월 3일, 익명의 창시자 사토시 나카모토(Satoshi Nakamoto)는 비트코인 블록체인의 첫 번째 블록인 **제네시스 블록(Genesis block)**에 의미심장한 메시지를 새겨 넣었다. *The Times*의 헤드라인은 이렇게 적혀 있었다: "Chancellor on brink of second bailout for banks(재무장관, 은행 2차 구제금융 직전)." 이는 세계를 실망시킨 중앙화된 금융 시스템에 대한 비판이자, 코드에 영구히 새겨진 목적 선언문으로서 기능했다.

    비트코인의 설계는 암호학을 사용하여 개인의 자유와 금융 주권을 보호하고자 했던 사이퍼펑크(Cypherpunk) 운동에서 영감을 받았다. 은행이나 정부에 의존하는 대신, 비트코인은 신뢰할 수 있는 중개자 없이 작동하는 P2P(Peer-to-Peer) 전자 현금 시스템으로 기능한다.

    비트코인의 통화 정책은 투명하고 예측 가능하며, 중앙은행이 아닌 수학에 의해 강제된다. 이는 아마도 세계에서 유일하게 독립적으로 검증 가능한 제한된 공급량을 가진 자산일 것이다. 이러한 프로그래밍된 희소성은 무제한으로 발행될 수 있는 법정화폐(fiat currency)나, 이론적으로는 유한한 공급량을 가지지만 실제로 총량을 아무도 모르는 금과 같은 경성 자산과 극명한 대조를 이룬다.

    그러나 이 비전은 근본적인 질문을 제기했다: 분쟁을 해결할 중앙 권위 없이, 전 세계에 흩어진 수천 대의 컴퓨터가 어떻게 누가 무엇을 소유하는지에 대해 합의에 도달할 수 있을까?

    ### 채굴과 작업 증명

    비트코인의 작업 증명(Proof of Work) 시스템은 채굴자(Miner)가 막대한 연산 노력을 투입했음을 누구나 빠르게 검증할 수 있는 방식으로 증명할 수 있게 한다. 이 과정의 핵심에는 **해시 함수(Hash function)**가 있다: 이는 어떤 입력 데이터든 받아서 고정된 길이의 문자열로 변환하는 수학적 연산이다. 해시 함수의 특별한 점은 일방향성이라는 것이다: 출력에서 입력을 복원할 수 없으며, 입력에 아주 작은 변화만 있어도 완전히 다르고 예측 불가능한 결과가 나온다.

    채굴자들은 거래들을 블록에 묶은 다음 연산 퍼즐을 풀려고 시도한다. 이것을 천문학적인 확률의 주사위를 굴려 특정 임계값 아래의 숫자를 얻으려는 것으로 생각해보라. 단, 채굴자들은 초당 수조 번을 "굴리고" 있다. 그들은 블록 데이터를 SHA-256 해싱 알고리즘에 반복적으로 통과시킴으로써 이를 수행한다. SHA-256은 미국 정부가 표준화한 암호학적 해시 함수이며, 비트코인은 추가적인 보안을 위해 이를 두 번 적용한다. 각 실행은 무작위처럼 보이는 출력을 생성한다.

    각 시도는 **논스(Nonce)**라고 불리는 다른 숫자를 사용하는데, 이는 본질적으로 0에서 약 40억까지 증가하는 카운터이다. 각 논스는 다르고 예측 불가능한 해시 결과를 생성한다. 채굴자가 마침내 네트워크의 목표 임계값 아래의 출력을 찾으면, 퍼즐을 풀고 자신의 블록을 블록체인에 추가할 수 있다.

    그러나 현대 채굴 하드웨어는 너무 빨라서 40억 개의 모든 논스 값을 몇 초 만에 소진할 수 있다. 이런 경우, 채굴자들은 입력을 변경할 다른 방법이 필요하다. 여기서 코인베이스 트랜잭션(Coinbase transaction)이 등장한다. 모든 블록에는 채굴자에게 블록 보상(Block reward)과 모든 거래 수수료를 지급하는 특별한 코인베이스 트랜잭션이 포함되어 있으며, 이는 사실상 새로운 비트코인을 "생성"한다. 이 트랜잭션은 같은 이름의 거래소와는 관련이 없다. 채굴자들은 이 코인베이스 트랜잭션 내의 extra nonce라는 필드를 수정하거나 블록의 타임스탬프를 증가시킬 수 있다. 어느 쪽이든 블록 헤더 해시를 변경하고 검색 공간을 재설정한다.

    채굴자들이 이러한 시도를 수행하는 속도를 해시레이트(Hash rate)라고 하며, 테라해시 또는 엑사해시/초 단위로 측정된다. 이는 채굴자나 전체 네트워크가 매초 시도할 수 있는 해시 수를 보여준다. 네트워크 해시레이트가 높아지면 블록이 더 빨리 나온다고 생각할 수 있지만, 네트워크는 이를 보상하기 위해 자동으로 난이도를 조정한다. 매 2,016블록마다, 대략 2주마다, 네트워크는 난이도 재조정(Difficulty retarget)을 수행한다. 해당 블록들이 실제로 얼마나 걸렸는지 측정하고 그에 따라 목표를 조정한다. 급격한 변동을 방지하기 위해 이러한 조정은 이전 난이도의 4분의 1에서 4배 사이로 제한되어 평균 블록 시간을 10분으로 안정적으로 유지한다.

    채굴자들은 **ASIC(Application-Specific Integrated Circuit, 주문형 반도체)**이라는 특수 칩을 사용하며, 이는 SHA-256 Proof of Work을 위해 특별히 설계되었다. 이 칩들은 이 작업에서 일반 컴퓨터보다 수천 배 더 효율적이다. 최고의 하드웨어를 사용하더라도 단독 채굴은 단일 블록을 찾는 데 수년을 기다릴 수 있는 대규모 복권과 같다. 이러한 변동성을 완화하기 위해 채굴자들은 **마이닝 풀(Mining pool)**에 참여한다. 이러한 풀들은 Stratum이라는 통신 표준을 사용하여 채굴자들 간의 작업을 조율한다. 풀은 모든 참여자의 연산력을 결합하고 각 채굴자의 기여도에 비례하여 보상을 분배한다. 이는 긴 무수확 기간 대신 안정적이고 예측 가능한 지급을 제공한다.

    블록의 코인베이스 트랜잭션에서 새로 생성된 코인은 즉시 사용할 수 없다. 그 위에 100개의 블록이 더 추가될 때까지 기다려야 하며, 이는 약 16~17시간이 걸린다. 이 지연은 채굴자들이 최근 블록체인 기록을 다시 쓰려는 시도로 이익을 얻기 훨씬 어렵게 만든다.

    ### 합의와 체인 선택

    채굴이 어떻게 작동하는지 이해했으니, 이제 네트워크가 어떤 체인이 유효한지에 대해 어떻게 합의에 도달하는지 탐구할 수 있다.

    비트코인 네트워크는 노드(Node)로 구성되며, 이는 비트코인 소프트웨어를 실행하고 모든 거래와 블록을 독립적으로 검증하여 규칙을 따르는지 확인하는 컴퓨터이다. 이 노드들은 블록체인의 완전한 사본을 유지하고 유효한 정보를 다른 참여자들에게 전달한다. 채굴자들은 일반적으로 자신이 구축하는 블록을 검증하기 위해 직접 노드를 운영하지만, 많은 참여자들은 채굴 없이 노드를 운영하여 단순히 비트코인의 상태를 독립적으로 검증하고 네트워크의 탈중앙화에 기여한다. 비트코인 논의에서 "노드"를 언급할 때, 일반적으로 검증은 하지만 블록을 생성하지 않는 이러한 비채굴 참여자들을 의미한다.

    비트코인은 **나카모토 합의(Nakamoto Consensus)**라는 강력한 메커니즘을 통해 합의를 해결하며, 이는 종종 "최장 체인 규칙"으로 단순화되지만, 더 정확하게는 가장 많은 누적 작업을 가진 체인으로 설명된다. 두 등산객이 서로 다른 경로를 택하는 것으로 생각해보라: 한 명은 1,000개의 쉬운 계단을 밟고, 다른 한 명은 600개의 어려운 계단을 밟는다. 시스템은 계단 수(블록 수)가 아니라 필요한 에너지(작업의 대리물)로 점수를 매기므로, 더 가파르고 어려운 경로가 계단이 적더라도 더 "무거울" 수 있다. 노드들은 같은 원칙을 따르며, 생성하는 데 가장 많은 누적 연산 작업이 필요한 체인을 선택한다. 공격자는 단순히 더 많은 블록을 생성하여 역사를 다시 쓸 수 없다; 정직한 체인만큼의 총 작업량, 그리고 그 이상을 생성해야 한다.

    때때로 두 채굴자가 거의 동시에 유효한 블록을 찾아 블록체인에 일시적인 포크(Fork)가 생긴다. 네트워크의 서로 다른 부분들은 어떤 블록을 먼저 들었는지에 따라 처음에 다른 블록을 따를 것이다. 다음 블록이 발견되면 무승부가 깨진다. 먼저 확장되는 포크가 더 길어지고 자동으로 승리한다. 그 시점에서 네트워크의 모든 노드는 더 긴 체인을 따르도록 전환하고 더 짧은 것을 포기한다. 패배한 포크의 블록은 스테일(Stale)이 되어, 즉 폐기되고 최종 블록체인에 포함되지 않으며, 그 거래들은 미확인 상태로 돌아간다. 이 전체 과정은 보통 몇 분 내에 해결된다.

    이러한 체인 재구성(Chain reorganization, 또는 "Reorg")은 비트코인 운영의 정상적이고 예상되는 부분이다. 1블록 재구성은 가끔 발생하고, 2블록 재구성은 드물며, 3개 이상은 공격이나 심각한 네트워크 분할이 없으면 극히 드물다. 이 확률적 동작 때문에 컨펌(Confirmation)이 중요하다: 거래가 재구성에 영향을 받을 확률은 추가 블록마다 기하급수적으로 감소한다. 상인들은 일반적으로 큰 결제를 최종으로 간주하기 전에 여러 확인(보통 6개)을 기다린다.

    자연적인 포크 외에도, 비트코인은 다른 잠재적 공격에 직면한다. 이클립스 공격(Eclipse attack)은 노드의 네트워크 연결을 격리하여 블록체인의 왜곡된 뷰를 제공하는 것을 포함한다. 이기적 채굴(Selfish mining)은 발견한 블록을 보류하여 비공개로 채굴하고 수익 이점을 위해 전략적으로 공개하는 것을 포함한다. 피어의 다양성, 네트워크 수준 보호 및 모니터링이 이러한 위험을 완화하는 데 도움이 된다.

    ### 통화 정책

    비트코인은 고정된 발행 일정을 가진 예측 가능한 알고리즘적 통화 정책을 가지고 있다. 블록 보상 또는 보조금(Subsidy)은 210,000블록마다 절반으로 줄어들며, 이 이벤트는 대략 4년마다 발생하는 "**반감기(Halving)**"로 알려져 있다. 보조금은 50 BTC로 시작하여 이후 25, 12.5, 6.25으로 감소했으며, 2024년 반감기 이후 가장 최근에 3.125 BTC로 줄었다.

    이 메커니즘은 비트코인을 디스인플레이션(Disinflationary) 자산으로 만들며, 인플레이션율이 0을 향해 수렴한다. 2140년경에 보조금은 중단되고 채굴자들은 거래 수수료만으로 보상받게 될 것이다. 반감기에서의 정수 반올림으로 인해 최종 공급량은 ~20,999,999.9769 BTC에 수렴한다. 2026년 초 기준으로, 최종 2,100만 BTC의 약 95%가 이미 채굴되어 유통 중이다.

    채굴자들은 두 가지 원천에서 수익을 얻는다: 블록 보조금(BTC의 새로운 발행)과 사용자가 지불하는 거래 수수료. 채굴자 수익의 대부분은 블록 보조금에서 나온다. 2024년에 블록 보조금은 총 수익의 약 94%를 차지했다. **보안 예산(Security budget)**으로 알려진 이 결합 수익은 네트워크 공격 비용을 결정하며, Section IV에서 자세히 다룬다.

    비트코인의 예측 가능한 희소성은 가치 저장 수단으로서의 제안의 초석을 형성한다. 그러나 희소성만으로는 가격 상승을 보장하지 않으며, 가격은 궁극적으로 구매자들의 지속적인 수요에 달려 있다. 감소하는 발행은 유리한 공급 역학을 만들지만, 이는 시장에서 매도 압력을 초과하는 매수 압력이 동반될 때만 가격 상승으로 이어진다.

## Section II: Bitcoin Technical Architecture

=== "EN"

    Understanding Bitcoin's core concepts (mining, consensus, and monetary policy) provides the foundation. But to truly grasp how Bitcoin works, we need to examine the technical architecture that makes these concepts operational: how ownership is represented, how transactions are structured, and how the system maintains privacy and security at the protocol level.

    ### UTXO Model

    Bitcoin tracks ownership differently than traditional banks through its Unspent Transaction Output (UTXO) model. The best way to understand this is through a cash analogy.

    Imagine physical cash in your wallet: not a single account balance, but individual bills of different denominations like a $20, two $5s, and some $1s. When you buy something for $7, you hand over a $5 and two $1s, getting change back if needed. You can't split a single bill, you use the denominations you have and receive new ones in return.

    Bitcoin operates on the same principle. Your wallet holds a collection of UTXOs, individual digital "coins" of varying amounts. When you send bitcoin, your wallet selects which UTXOs to spend (a process called coin selection that involves privacy and fee tradeoffs), consumes them entirely, and creates new UTXOs: one for the recipient and one as "change" back to you. This design elegantly prevents double-spending because once a UTXO appears in a confirmed transaction, it's permanently removed from the spendable set and cannot be used again.

    Every full node independently maintains its own view of this global UTXO set, the complete collection of all spendable outputs, by validating the entire blockchain. Ownership of these UTXOs is controlled by **private keys**, extremely large random numbers (roughly between 1 and 2²⁵⁶, about 10⁷⁷ possibilities) that function as the cryptographic secret proving control over funds. Your wallet generates these from high-quality randomness, similar to flipping a fair coin 256 times and treating the sequence of heads and tails as a 256-bit number. The private key is the core secret in Bitcoin: it lets your wallet produce digital signatures that satisfy the spending rules on your UTXOs.

    Put simply: you “own” bitcoin if you control the private keys needed to spend specific UTXOs. If you lose those keys, those coins are effectively gone. If you keep them safe, only you can move those coins.

    The rules for spending these UTXOs are defined by **Bitcoin Script**, a simple programming language. Each output includes a locking script that sets the spending conditions. Think of it as a lock that specifies what key is needed. When someone wants to spend that output, they provide unlocking data (essentially the key) to satisfy those conditions. The Bitcoin network verifies that the key fits the lock before allowing the transaction.

    Bitcoin Script also supports timelocks, which keep transactions invalid until a specified time or block height is reached. These enable sophisticated contracts like Lightning channels, vaults, and escrow arrangements. For example, you could create a transaction that can only be spent after a certain date, or one that requires multiple signatures but allows a backup key after a timeout period.

    ### Address Types and Formats

    Bitcoin addresses have evolved over time, and you'll encounter several formats. Don't worry about memorizing the technical details. What matters is understanding that each generation improved on the last in terms of efficiency, privacy, or features. Modern wallets handle the complexity for you.

    The key concept is that an address is not the same as a public key. Instead, an address is typically a shorter, encoded version of a public key hash or script hash, like a nickname that's easier to share than the full cryptographic data it represents.

    The relationship between private keys, public keys, and addresses follows a specific cryptographic chain. From your private key, Bitcoin derives a public key using **elliptic curve cryptography**. Think of this as a one-way mathematical function: your private key transforms into a public key that's mathematically linked but computationally impossible to reverse. This public key then gets hashed (compressed through a one-way function) to create your Bitcoin address. The hashing keeps your public key hidden until you spend and makes addresses shorter and easier to share.

    The address formats you'll encounter reflect this evolution. Legacy addresses, which start with 1, are the original format and work everywhere but typically incur slightly higher fees. P2SH addresses start with 3 and serve as a wrapper format often used for multisig setups or older SegWit compatibility. Native SegWit addresses start with bc1q and represent the modern default, offering lower fees and all-lowercase characters for easier error checking. Taproot addresses start with bc1p and represent the newest format. Unlike earlier types that hash the public key, Taproot encodes a version of the public key directly, enabling more flexible and private spending conditions where complex scripts can hide behind what looks like a simple single-key payment. Taproot has broad support across modern wallets, though some older services are still catching up.

    For most users, simply use whatever address type your wallet generates by default. It will typically be Native SegWit or Taproot, both of which offer good fee efficiency and security.

    ### Transaction Structure and Prioritization

    A Bitcoin transaction consists of inputs (the UTXOs being spent) and outputs (the new UTXOs being created). The transaction fee equals the sum of inputs minus the sum of outputs. Once broadcast, transactions enter each node's **mempool**, which is a pool of unconfirmed transactions waiting to be included in a block.

    Here's where economics comes into play. Since blocks have limited space, miners must choose which transactions to include from the mempool. They naturally prioritize transactions that maximize their revenue. However, transactions vary in size. A simple payment might be small while a complex transaction consolidating dozens of small inputs or batching payments to many recipients could be much larger. This is why miners look at fee rate (fee per unit of size) rather than absolute fee. A small transaction paying 10 sats might have a higher rate than a large transaction paying 100 sats. Fee rate is measured in satoshis per virtual byte (sats/vB), where a satoshi is the smallest unit of bitcoin (100 million satoshis equal one bitcoin).

    This creates a fee market where users essentially bid for block space. Users needing quick confirmation during network congestion pay higher fee rates. Those who can wait pay less and wait for a quieter period. If a transaction gets stuck, users can use **Replace by Fee (RBF)** to broadcast a higher fee replacement, or **Child Pays for Parent (CPFP)** to create a high fee child transaction that incentivizes miners to include the parent. CPFP is used when the sender can't (or doesn't want to) replace the parent but controls one of its outputs (sender's change or the recipient's output). RBF is used when the sender controls the original transaction and it can be replaced.

    ### Privacy Model

    Bitcoin is **pseudonymous**, not anonymous. While addresses are not directly linked to real-world identity, transaction graph analysis can be used to cluster addresses and track the flow of funds. This risk is significantly increased by address reuse, which is why using a fresh address for each transaction is considered a best practice. Furthermore, KYC/AML regulations at crypto exchanges create links between on-chain activity and real-world identity, creating privacy gaps. Companies like Chainalysis have built billion dollar businesses on de-anonymizing blockchains.

    At the transaction level, this pseudonymity has specific implications. When you receive bitcoin, only your address (the hash of your public key) appears on the blockchain. But when you spend bitcoin, you must reveal your actual public key along with a digital signature that proves you know the corresponding private key. This is a critical detail: the signature proves ownership without exposing the private key itself. Anyone can verify the signature matches the public key, and that the public key hashes to the address that received the funds, but they can't derive your private key from this information. This revelation of the public key at spending time is why the double-hashing that creates addresses provides an extra security layer, keeping your public key private until the moment you choose to spend.

    The coin selection process mentioned earlier in the UTXO section has direct privacy implications. When your wallet chooses which UTXOs to spend, it's creating on-chain patterns that analysts use to cluster addresses. Spending multiple UTXOs together in one transaction strongly suggests they belong to the same owner. Similarly, the change output returning to your wallet can be identified through various heuristics, further linking your addresses.

    To address these privacy limitations, various techniques have emerged. Common privacy practices include avoiding address reuse and optionally leveraging CoinJoin-style tools to reduce heuristic linking. **CoinJoin** combines inputs from many users into a single transaction that produces many outputs of identical (or near identical) denominations. Because all inputs sign the same transaction, on-chain observers cannot reliably determine which input funded which output. This breaks common heuristics like "multi-inputs belong to the same owner" and "change output detection," creating an anonymity set where each coin could plausibly belong to any participant. Modern implementations add features like input registration over Tor, output blinding, equal output denominations, and multi-round mixing to further resist clustering and improve plausible deniability.

=== "KO"

    비트코인의 핵심 개념(채굴, 합의, 통화 정책)을 이해하면 기반이 마련된다. 그러나 비트코인이 어떻게 작동하는지 진정으로 파악하려면, 이러한 개념을 작동하게 만드는 기술 아키텍처를 검토해야 한다: 소유권이 어떻게 표현되는지, 거래가 어떻게 구조화되는지, 그리고 시스템이 프로토콜 수준에서 어떻게 프라이버시와 보안을 유지하는지.

    ### UTXO 모델

    비트코인은 **미사용 트랜잭션 출력(Unspent Transaction Output, UTXO)** 모델을 통해 전통적인 은행과 다르게 소유권을 추적한다. 이를 이해하는 가장 좋은 방법은 현금 비유를 통해서이다.

    지갑 안의 물리적 현금을 상상해보라: 단일 계좌 잔액이 아니라 $20 한 장, $5 두 장, 그리고 몇 장의 $1처럼 다양한 액면가의 개별 지폐들. $7짜리 물건을 살 때, $5 한 장과 $1 두 장을 건네고 필요하면 거스름돈을 받는다. 단일 지폐를 쪼갤 수는 없으며, 가지고 있는 액면가를 사용하고 그 대가로 새로운 것을 받는다.

    비트코인도 같은 원리로 작동한다. 지갑은 다양한 금액의 개별 디지털 "코인"인 UTXO 모음을 보유한다. 비트코인을 보낼 때, 지갑은 어떤 UTXO를 사용할지 선택하고(프라이버시와 수수료 트레이드오프를 수반하는 코인 선택이라는 과정), 그것들을 완전히 소비하고, 새로운 UTXO를 생성한다: 하나는 수신자를 위한 것이고 하나는 "거스름돈"으로 자신에게 돌아온다. 이 설계는 UTXO가 확인된 거래에 나타나면 영구적으로 사용 가능한 집합에서 제거되어 다시 사용될 수 없기 때문에 이중 지불을 우아하게 방지한다.

    모든 풀 노드는 전체 블록체인을 검증하여 사용 가능한 모든 출력의 완전한 모음인 이 전역 UTXO 집합에 대한 자체 뷰를 독립적으로 유지한다. 이러한 UTXO의 소유권은 **개인키(Private Key)**에 의해 제어되며, 이는 자금에 대한 통제를 증명하는 암호학적 비밀로 기능하는 매우 큰 난수(대략 1에서 2²⁵⁶ 사이, 약 10⁷⁷개의 가능성)이다. 지갑은 고품질 무작위성에서 이것들을 생성하며, 공정한 동전을 256번 던지고 앞면과 뒷면의 순서를 256비트 숫자로 취급하는 것과 유사하다. Private Key는 비트코인의 핵심 비밀이다: 이를 통해 지갑은 UTXO의 지출 규칙을 충족하는 디지털 서명을 생성할 수 있다.

    간단히 말해: 특정 UTXO를 사용하는 데 필요한 개인키를 통제하면 비트코인을 "소유"하는 것이다. 그 키를 잃으면 그 코인은 사실상 사라진다. 키를 안전하게 보관하면 오직 당신만이 그 코인을 옮길 수 있다.

    이러한 UTXO를 사용하는 규칙은 단순한 프로그래밍 언어인 **비트코인 스크립트(Bitcoin Script)**에 의해 정의된다. 각 출력은 지출 조건을 설정하는 잠금 스크립트를 포함한다. 어떤 키가 필요한지 명시하는 자물쇠로 생각하라. 누군가 그 출력을 사용하려면 해당 조건을 충족하는 잠금 해제 데이터(본질적으로 열쇠)를 제공한다. 비트코인 네트워크는 거래를 허용하기 전에 열쇠가 자물쇠에 맞는지 검증한다.

    Bitcoin Script는 또한 타임락(Timelock)을 지원하여 지정된 시간이나 블록 높이에 도달할 때까지 거래를 무효로 유지한다. 이를 통해 Lightning 채널, 볼트(Vault), 에스크로 계약과 같은 정교한 컨트랙트가 가능해진다. 예를 들어, 특정 날짜 이후에만 사용할 수 있는 거래를 만들거나, 여러 서명이 필요하지만 시간 초과 후 백업 키를 허용하는 거래를 만들 수 있다.

    ### 주소 유형과 형식

    비트코인 주소는 시간이 지나면서 발전해왔으며, 여러 형식을 접하게 될 것이다. 기술적 세부 사항을 암기하는 것에 대해 걱정하지 마라. 중요한 것은 각 세대가 효율성, 프라이버시 또는 기능 면에서 이전을 개선했다는 것을 이해하는 것이다. 현대 지갑은 복잡성을 대신 처리해준다.

    핵심 개념은 주소가 공개키(Public key)와 동일하지 않다는 것이다. 대신, 주소는 일반적으로 공개키 해시 또는 스크립트 해시의 더 짧고 인코딩된 버전이며, 그것이 나타내는 전체 암호학적 데이터보다 공유하기 쉬운 별명과 같다.

    개인키, 공개키, 주소 간의 관계는 특정 암호학적 체인을 따른다. 개인키에서 비트코인은 **타원 곡선 암호(Elliptic Curve Cryptography)**를 사용하여 공개키를 도출한다. 이것을 일방향 수학 함수로 생각하라: 개인키가 수학적으로 연결되어 있지만 계산적으로 되돌리는 것이 불가능한 공개키로 변환된다. 이 공개키는 그 다음 해시되어(일방향 함수를 통해 압축되어) 비트코인 주소를 생성한다. 해싱은 사용할 때까지 공개키를 숨기고 주소를 더 짧고 공유하기 쉽게 만든다.

    접하게 될 주소 형식들은 이 진화를 반영한다. 1로 시작하는 레거시(Legacy) 주소는 원래 형식이며 어디서나 작동하지만 일반적으로 약간 더 높은 수수료가 발생한다. 3으로 시작하는 P2SH 주소는 다중 서명 설정이나 이전 SegWit 호환성에 자주 사용되는 래퍼 형식이다. bc1q로 시작하는 네이티브 SegWit(Native SegWit) 주소는 현대의 기본값을 나타내며, 더 낮은 수수료와 더 쉬운 오류 확인을 위한 모두 소문자 문자를 제공한다. bc1p로 시작하는 Taproot 주소는 최신 형식을 나타낸다. 공개키를 해시하는 이전 유형과 달리, Taproot는 공개키의 버전을 직접 인코딩하여 단순한 단일 키 지불처럼 보이는 것 뒤에 복잡한 스크립트가 숨을 수 있는 더 유연하고 프라이빗한 지출 조건을 가능하게 한다. Taproot는 현대 지갑에서 광범위하게 지원되지만, 일부 오래된 서비스는 아직 따라잡는 중이다.

    대부분의 사용자에게, 지갑이 기본으로 생성하는 주소 유형을 그냥 사용하면 된다. 일반적으로 Native SegWit 또는 Taproot이며, 둘 다 좋은 수수료 효율성과 보안을 제공한다.

    ### 거래 구조와 우선순위

    비트코인 거래는 입력(사용되는 UTXO)과 출력(생성되는 새로운 UTXO)으로 구성된다. 거래 수수료는 입력의 합에서 출력의 합을 뺀 것과 같다. 브로드캐스트되면 거래는 각 노드의 **멤풀(Mempool)**에 들어가며, 이는 블록에 포함되기를 기다리는 미확인 거래의 풀이다.

    여기서 경제학이 작용한다. 블록은 공간이 제한되어 있으므로, 채굴자들은 멤풀에서 어떤 거래를 포함할지 선택해야 한다. 그들은 자연스럽게 수익을 최대화하는 거래를 우선시한다. 그러나 거래 크기는 다양하다. 간단한 결제는 작을 수 있지만, 수십 개의 작은 입력을 통합하거나 많은 수신자에게 일괄 결제하는 복잡한 거래는 훨씬 클 수 있다. 이것이 채굴자들이 절대 수수료가 아닌 수수료율(크기 단위당 수수료)을 보는 이유이다. 10 사토시를 지불하는 작은 거래가 100 사토시를 지불하는 큰 거래보다 더 높은 비율을 가질 수 있다. 수수료율은 가상 바이트당 사토시(sats/vB)로 측정되며, 사토시(Satoshi)는 비트코인의 가장 작은 단위이다(1억 사토시가 1 비트코인과 같다).

    이것은 사용자들이 본질적으로 블록 공간에 입찰하는 수수료 시장을 만든다. 네트워크 혼잡 시 빠른 확인이 필요한 사용자는 더 높은 수수료율을 지불한다. 기다릴 수 있는 사람들은 덜 지불하고 더 조용한 기간을 기다린다. 거래가 막히면, 사용자는 **수수료 대체(Replace by Fee, RBF)**를 사용하여 더 높은 수수료의 대체 거래를 브로드캐스트하거나, **자식이 부모를 지불(Child Pays for Parent, CPFP)**을 사용하여 채굴자가 부모를 포함하도록 인센티브를 주는 높은 수수료의 자식 거래를 만들 수 있다. CPFP는 발신자가 부모를 대체할 수 없거나(대체하고 싶지 않거나) 그 출력 중 하나(발신자의 거스름돈이나 수신자의 출력)를 제어할 때 사용된다. RBF는 발신자가 원래 거래를 제어하고 대체할 수 있을 때 사용된다.

    ### 프라이버시 모델

    비트코인은 익명이 아니라 **가명(Pseudonymous)**이다. 주소가 실제 신원과 직접 연결되지 않지만, 거래 그래프 분석을 사용하여 주소를 클러스터링하고 자금 흐름을 추적할 수 있다. 이 위험은 주소 재사용으로 크게 증가하며, 이것이 각 거래마다 새로운 주소를 사용하는 것이 모범 사례로 간주되는 이유이다. 또한, 암호화폐 거래소의 KYC/AML 규정은 온체인 활동과 실제 신원 사이의 연결을 생성하여 프라이버시 격차를 만든다. Chainalysis와 같은 회사들은 블록체인 비익명화에 수십억 달러 규모의 사업을 구축했다.

    거래 수준에서, 이 가명성은 특정한 함의를 가진다. 비트코인을 받을 때, 블록체인에는 주소(공개키의 해시)만 나타난다. 그러나 비트코인을 사용할 때, 해당 개인키를 알고 있음을 증명하는 디지털 서명과 함께 실제 공개키를 공개해야 한다. 이것은 중요한 세부 사항이다: 서명은 개인키 자체를 노출하지 않고 소유권을 증명한다. 누구나 서명이 공개키와 일치하는지, 그리고 공개키가 자금을 받은 주소로 해시되는지 검증할 수 있지만, 이 정보에서 개인키를 도출할 수는 없다. 지출 시 공개키의 이러한 공개가 주소를 생성하는 이중 해싱이 추가적인 보안 계층을 제공하는 이유이며, 사용하기로 선택하는 순간까지 공개키를 비공개로 유지한다.

    UTXO 섹션에서 앞서 언급한 코인 선택 과정은 직접적인 프라이버시 영향을 미친다. 지갑이 어떤 UTXO를 사용할지 선택할 때, 분석가들이 주소를 클러스터링하는 데 사용하는 온체인 패턴을 생성한다. 하나의 거래에서 여러 UTXO를 함께 사용하면 그것들이 같은 소유자에게 속한다는 것을 강하게 시사한다. 마찬가지로, 지갑으로 돌아오는 거스름돈 출력은 다양한 휴리스틱을 통해 식별될 수 있어 주소를 더욱 연결한다.

    이러한 프라이버시 한계를 해결하기 위해 다양한 기술이 등장했다. 일반적인 프라이버시 관행에는 주소 재사용 회피와 선택적으로 휴리스틱 연결을 줄이기 위한 CoinJoin 스타일 도구 활용이 포함된다. **코인조인(CoinJoin)**은 많은 사용자의 입력을 동일한(또는 거의 동일한) 액면가의 많은 출력을 생성하는 단일 거래로 결합한다. 모든 입력이 같은 거래에 서명하기 때문에, 온체인 관찰자는 어떤 입력이 어떤 출력에 자금을 제공했는지 신뢰성 있게 결정할 수 없다. 이는 "다중 입력은 같은 소유자에게 속한다" 및 "거스름돈 출력 탐지"와 같은 일반적인 휴리스틱을 깨뜨리며, 각 코인이 그럴듯하게 어떤 참가자에게도 속할 수 있는 익명 집합을 만든다. 현대 구현은 Tor를 통한 입력 등록, 출력 블라인딩, 동일한 출력 액면가, 다중 라운드 믹싱과 같은 기능을 추가하여 클러스터링에 더욱 저항하고 그럴듯한 부인 가능성을 향상시킨다.

## Section III: Bitcoin Upgrades and Scaling

=== "EN"

    Bitcoin's technical architecture provides a robust foundation, but no system is perfect from inception. The question becomes: how does a decentralized network evolve without central authority? This section explores Bitcoin's governance model, the mechanisms for upgrading the protocol, and the major improvements that have been deployed over its history.

    ### Bitcoin Core

    The Bitcoin protocol is the set of rules that define how Bitcoin works: what makes a block valid, how transactions are structured, how much new bitcoin is created, and so on. It can be thought of as the "specification" for Bitcoin.

    Bitcoin Core is software that implements these rules. It's the most widely used Bitcoin node software, originally written by Satoshi Nakamoto and now maintained by a global community of developers. When running a Bitcoin node, one is most likely running Bitcoin Core.

    Here's where it gets interesting: Bitcoin has no formal written specification separate from the code. Instead, Bitcoin Core's consensus code has become the de facto reference that defines the rules. Other node implementations exist, like btcd or libbitcoin, but they maintain compatibility by matching Core's behavior. This means Core holds significant influence not because it controls Bitcoin, but because the economic majority has chosen to run it.

    ### Consensus Rules vs. Policy Rules

    Understanding Bitcoin requires distinguishing between two types of rules that nodes enforce. Consensus rules are the fundamental laws that define what makes a block or transaction valid on the blockchain itself. These rules are enforced by all full nodes when validating blocks, and any violation results in permanent rejection. Examples include blocks not exceeding 4,000,000 weight units, outputs not exceeding inputs plus the coinbase reward, and signatures being cryptographically valid. Breaking a consensus rule means a transaction or block is invalid and will never be accepted into the blockchain, regardless of miner support.

    Policy rules, also called mempool policy or relay policy, represent a different layer entirely. These are optional standards that individual nodes use to decide which unconfirmed transactions they'll accept into their mempool and relay to peers. Working on top of Bitcoin's mandatory consensus rules, these additional local preferences help nodes filter spam, prioritize valuable transactions, and manage resources. Examples include minimum relay fee rates, transaction size limits for relay that are far below the block limit, and standardness restrictions on which types of scripts nodes will relay, favoring common patterns even though more exotic consensus-valid scripts exist.

    The distinction between these rule types creates an important dynamic. A transaction can violate standard policy yet remain perfectly valid under consensus rules. When a transaction uses a non-standard script, for instance, most nodes won't relay it and it won't appear in most mempools. However, if a miner receives it directly, perhaps because the user contacted them, the miner can include it in a block. Once included, all nodes will accept that block as valid because policy rules don't govern what belongs in blocks, only what gets relayed beforehand. This has happened with various non-standard transactions throughout Bitcoin's history.

    This separation serves several important functions. Nodes can reject uneconomical transactions before they waste network bandwidth or blockchain space without requiring network-wide coordination. Different node operators can choose stricter or looser policies based on their needs, hardware capabilities, or philosophies. Policy can be adjusted through Bitcoin Core releases without the coordination challenges of consensus changes, allowing new transaction types to be made consensus-valid while policy rules gradually adopt them over time.

    ### How Changes Happen

    Changes to Bitcoin are proposed through **BIPs (Bitcoin Improvement Proposals)**. Policy changes happen regularly through Bitcoin Core releases and don't require extensive coordination. Node operators can upgrade at their convenience, and the network continues functioning even with mixed policy versions. Recent releases have focused primarily on mempool policy improvements, adjusting things like fee rate minimums and transaction relay rules.

    Consensus changes are far rarer and more significant because they modify the fundamental protocol rules about what makes blocks and transactions valid. These require careful coordination since the entire network needs to agree on the rules. When consensus rules do change, it happens through specific upgrade mechanisms explored below.

    Bitcoin Core's careful development process, extensive testing, and broad adoption make it the standard reference implementation. Major upgrades like SegWit and Taproot were implemented in Core and activated by the network, demonstrating how protocol evolution works through this widely-adopted software. However, ultimate control rests with users and businesses who decide which software to run and which rules to follow.

    ### Understanding Fork Types

    How can a decentralized network be upgraded when no one's in charge? Bitcoin has two main upgrade mechanisms that allow the protocol to evolve while maintaining consensus.

    #### Hard Forks

    Hard forks are incompatible upgrades that loosen or change consensus rules. Think of it like changing from left-hand to right-hand driving: if a driver doesn't switch, they simply can't operate safely on the new roads. Everyone has to upgrade or they'll keep driving on the old side, which becomes a separate road network. Bitcoin avoids this because coordinating such a complete transition is risky and can permanently split the network. Hard forks are extremely rare in Bitcoin due to coordination challenges and the risk of permanent network splits.

    A notable example is Bitcoin Cash (BCH), created in 2017 by changing rules (notably much larger blocks). In practice, that approach fractured liquidity and community mindshare. Over time, BCH has retained only a small fraction of Bitcoin's adoption, hashpower, and market value. Most users, developers, miners, and exchanges coordinated on the original smaller-block BTC chain as the main “Bitcoin,” largely because it kept it cheaper and easier for ordinary people to run full nodes and verify the chain themselves. Critically, though, deciding what's the "real Bitcoin" isn't something the code can decree since there is no central authority. It's a messy blend of social consensus (what users, exchanges, wallets, and merchants run), economic gravity (where liquidity settles), and security assumptions (what most full nodes enforce). Markets have decidedly treated BTC as the Schelling point, but that outcome is ultimately social, not ordained.

    #### Soft Forks

    Soft forks are backward compatible protocol upgrades that tighten consensus rules without breaking the network. Think of it like adding a new traffic rule that existing drivers automatically comply with: upgraded nodes enforce stricter rules (like "no right turn on red at this intersection"), while non-upgraded nodes still see all traffic as valid and the network continues functioning normally. Non upgraded Bitcoin nodes still see new blocks as valid but don't enforce the stricter rules themselves, allowing the network to upgrade without splitting into incompatible versions. They require majority support to avoid chain splits, with examples including SegWit and Taproot.

    #### Activation Mechanisms

    Deciding to implement a soft fork is one thing, but actually activating it across the network requires careful coordination. The network needs a way to measure readiness and ensure enough participants have upgraded before the new rules take effect. This is where activation mechanisms come in. Different methods have been developed to balance miner coordination, economic node participation, and the risk of chain splits.

    **Miner Activated Soft Forks (MASF)** rely on hash power signaling; miners indicate readiness by including version bits in block headers. BIP9 was the standard MASF framework, requiring a high threshold (typically 95%) of blocks to signal support during defined time windows. Once the threshold is reached, the soft fork locks in and activates after a grace period. This was used for upgrades like SegWit (eventually) and most historical soft forks.

    **User Activated Soft Forks (UASF)** represent an alternative where economic nodes coordinate a "flag day" to start enforcing tighter rules, potentially regardless of miner signaling. If enough economic nodes and service providers participate, miners face a simple incentive: follow the new rules to get paid, or mine a chain most users won't accept.

    **Speedy Trial** is a short miner signaling trial with a 90% threshold over 2,016 block windows. If it locks in, activation occurs later at a preset block height; if it times out, no activation occurs and other mechanisms can be considered. This method was successfully used for Taproot activation in 2021\.

    #### The Challenge of Change

    Despite backward compatibility, getting any soft fork into Bitcoin is intentionally difficult. Many developers prioritize **protocol ossification**, the idea that Bitcoin should become increasingly resistant to change as it matures. This conservative approach recognizes a counter-intuitive strength: Bitcoin's power comes partly from what it *doesn't* do. By changing rarely, Bitcoin becomes predictable. Users can trust that the monetary policy won't be altered. The fewer changes made, the lower the risk of introducing bugs or unintended consequences that could compromise a multi-trillion-dollar asset.

    There's also an economic feedback loop at play: as Bitcoin's market cap grows and more economic activity depends on it, the threshold for "this upgrade is worth the risk" rises accordingly. A $100 billion asset might tolerate experimentation; a $2 trillion asset demands extreme conservatism. This isn't a bug, it's a feature that naturally protects the base layer as its importance increases.

    This philosophy means proposals undergo years of review, testing, and community debate.

    ### Bitcoin's Major Upgrades

    #### Segregated Witness (SegWit, 2017\)

    The SegWit activation saga represents one of the most important case studies in Bitcoin's governance, demonstrating how protocol upgrades work (and sometimes don't work) in a truly decentralized system.

    SegWit was a landmark upgrade that solved multiple critical issues. Before SegWit, Bitcoin had a critical bug: third parties could alter a transaction's signature and change its ID (TXID) before confirmation, without affecting the transaction's validity. This **transaction malleability** made it risky to build dependent transactions or second layer protocols like Lightning.

    SegWit moved signature data to a separate "witness" structure, making transaction IDs immutable once created. It also introduced **block weight** (a new measurement system with a 4,000,000 weight unit maximum instead of a simple 1MB limit). This effectively increased block capacity while incentivizing adoption of more efficient SegWit addresses. The weight system counts witness data as one quarter for weight calculation (commonly described as a "75% discount"), creating a backwards compatible blocksize increase.

    To understand the political dynamics, it's helpful to think of pre SegWit Bitcoin as "Bitcoin 1.0" (a system with a hard 1MB blocksize limit and transaction malleability issues). SegWit represented "Bitcoin 1.1" (mostly backwards compatible with Bitcoin 1.0, but fixing protocol bugs and enabling second layer networks while providing a one time capacity increase).

    The original activation mechanism was a MASF using BIP9 with a 95% threshold: during any 2,016 block difficulty adjustment period within the window from November 15, 2016 to November 15, 2017, if 95% or more of mined blocks signaled support, the upgrade would lock in. After a grace period, SegWit would activate and the network would accept the new transaction types.

    To understand what happened next, some context is needed. Bitcoin had been debating how to scale for years. Some factions wanted to increase the block size limit dramatically through a hard fork (which eventually led to the creation of Bitcoin Cash), while others preferred SegWit's approach of fixing transaction malleability and enabling second-layer solutions like Lightning Network. This disagreement became known as the "blocksize wars."

    Some large miners opposed SegWit because they preferred simply increasing block sizes. Even though SegWit had widespread support from developers, businesses, and node operators, these miners could block activation by refusing to signal. The BIP9 mechanism had assumed that signaling meant "my software is technically ready," but these miners were treating it as a political vote. This created an unprecedented governance crisis where a coordinated group of miners could indefinitely veto a beneficial upgrade, even though the upgrade didn't require their technical participation to function.

    BIP 148 represented a proposed solution to this governance deadlock. BIP 148 changed consensus rules for participating nodes by rejecting any non-signaling blocks after August 1st, 2017\. If enough economic nodes (exchanges, services, businesses) ran BIP 148, miners faced a stark choice: signal SegWit support and get paid in bitcoin that the broader economy would accept, or mine a chain that major economic actors would ignore.

    The threat of BIP 148 created powerful economic incentives that ultimately resolved the impasse. BIP 91 locked in on July 21, 2017 and activated two days later, enforcing that miners signal bit 1 and enabling BIP 141 to reach its threshold. With BIP 148's flag day planned for August 1st, the pressure was on. SegWit (BIP 141\) locked in on August 9, 2017 and activated on August 24, 2017 at block 481,824. BIP 91 served as an intermediate solution that allowed miners to signal SegWit support before the UASF deadline, and SegWit successfully activated via the original BIP9 mechanism.

    The SegWit activation demonstrates several crucial principles about Bitcoin governance. Economic nodes ultimately enforce protocol rules when sufficiently coordinated, reinforcing the power dynamics between miners and users. Soft forks can be enforced by users when there's sufficient economic coordination, even against miner resistance. Credible threats matter more than actual deployment, as BIP 148 succeeded largely because the threat was believable rather than because a majority of nodes actually ran it. Finally, Bitcoin's governance proved antifragile: the system found a way to route around the blockade and activate beneficial upgrades despite coordinated resistance.

    #### Taproot (2021)

    The Taproot upgrade significantly improved programmability and confidentiality. Unlike SegWit's contentious activation, Taproot enjoyed broad consensus across miners, developers, and economic nodes. However, even with this agreement, the upgrade still required several years of active community discussion, careful review, and coordination to ensure the changes were thoroughly vetted and safely deployed.

    Taproot used the Speedy Trial activation mechanism with a 90% miner signaling threshold. The signaling period began in May 2021, and the threshold was quickly met, with the upgrade locking in during June 2021\. After a predetermined grace period to allow remaining nodes to upgrade, Taproot activated in November 2021 at block 709,632. The smooth activation demonstrated that when there's genuine consensus, Bitcoin can upgrade efficiently while still maintaining its cautious, deliberate approach to protocol changes.

    The technical improvements were substantial. **Schnorr Signatures** enable key and signature aggregation, allowing complex multi-party transactions to appear as single signatures on-chain. **Merkleized Abstract Syntax Trees (MAST)** structure complex spending conditions efficiently, where only the condition that's met needs to be revealed.

    Together, these features provide major benefits: complex transactions become indistinguishable from simple payments for key path spends, delivering significant privacy and scalability improvements. When script path spends are used, only the revealed branch is disclosed, maintaining privacy for unused conditions.

=== "KO"

    비트코인의 기술 아키텍처는 견고한 기반을 제공하지만, 처음부터 완벽한 시스템은 없다. 질문은 이것이 된다: 탈중앙화된 네트워크가 중앙 권위 없이 어떻게 진화할 수 있을까? 이 섹션에서는 비트코인의 거버넌스 모델, 프로토콜 업그레이드 메커니즘, 그리고 역사를 통해 배포된 주요 개선 사항을 탐구한다.

    ### Bitcoin Core

    비트코인 프로토콜은 비트코인이 작동하는 방식을 정의하는 규칙 집합이다: 무엇이 블록을 유효하게 만드는지, 거래가 어떻게 구조화되는지, 얼마나 많은 새로운 비트코인이 생성되는지 등. 이는 비트코인의 "명세서"로 생각할 수 있다.

    Bitcoin Core는 이러한 규칙을 구현하는 소프트웨어이다. 이는 가장 널리 사용되는 비트코인 노드 소프트웨어로, 원래 사토시 나카모토가 작성했으며 현재는 글로벌 개발자 커뮤니티가 유지 관리한다. 비트코인 노드를 실행할 때, 대부분 Bitcoin Core를 실행하고 있을 가능성이 높다.

    여기서 흥미로워진다: 비트코인은 코드와 별개인 공식적으로 작성된 명세가 없다. 대신, Bitcoin Core의 합의 코드가 규칙을 정의하는 사실상의 참조가 되었다. btcd나 libbitcoin과 같은 다른 노드 구현이 존재하지만, Core의 동작과 일치시켜 호환성을 유지한다. 이는 Core가 비트코인을 통제하기 때문이 아니라, 경제적 다수가 이를 실행하기로 선택했기 때문에 상당한 영향력을 가진다는 것을 의미한다.

    ### 합의 규칙 vs. 정책 규칙

    비트코인을 이해하려면 노드가 시행하는 두 가지 유형의 규칙을 구별해야 한다. 합의 규칙(Consensus rules)은 블록체인 자체에서 블록이나 거래를 유효하게 만드는 것을 정의하는 기본 법칙이다. 이러한 규칙은 블록을 검증할 때 모든 풀 노드에 의해 시행되며, 어떤 위반도 영구적인 거부로 이어진다. 예를 들어 블록이 4,000,000 가중치 단위를 초과하지 않아야 하고, 출력이 입력과 코인베이스 보상을 초과하지 않아야 하며, 서명이 암호학적으로 유효해야 한다. 합의 규칙을 위반하면 거래나 블록이 무효이며 채굴자 지원과 관계없이 블록체인에 절대 수락되지 않는다.

    정책 규칙(Policy rules), 멤풀 정책 또는 릴레이 정책이라고도 불리는 것은 완전히 다른 계층을 나타낸다. 이는 개별 노드가 자신의 멤풀에 수락하고 피어에게 전달할 미확인 거래를 결정하는 데 사용하는 선택적 표준이다. 비트코인의 필수 합의 규칙 위에서 작동하는 이러한 추가적인 로컬 선호도는 노드가 스팸을 필터링하고, 가치 있는 거래에 우선순위를 매기고, 리소스를 관리하는 데 도움이 된다. 예를 들어 최소 릴레이 수수료율, 블록 제한보다 훨씬 낮은 릴레이용 거래 크기 제한, 더 이국적인 합의 유효 스크립트가 존재하더라도 일반적인 패턴을 선호하는 스크립트 유형에 대한 표준성 제한이 있다.

    이러한 규칙 유형 간의 구별은 중요한 역학을 만든다. 거래가 표준 정책을 위반하면서도 합의 규칙 하에서는 완벽하게 유효할 수 있다. 예를 들어 거래가 비표준 스크립트를 사용하면, 대부분의 노드는 이를 릴레이하지 않고 대부분의 멤풀에 나타나지 않는다. 그러나 채굴자가 직접 받으면, 아마도 사용자가 그들에게 연락했기 때문에, 채굴자는 이를 블록에 포함할 수 있다. 포함되면, 정책 규칙이 블록에 속하는 것을 지배하지 않고 사전에 릴레이되는 것만 지배하기 때문에 모든 노드는 해당 블록을 유효한 것으로 수락한다. 이는 비트코인 역사를 통해 다양한 비표준 거래와 함께 발생했다.

    이 분리는 여러 중요한 기능을 제공한다. 노드는 네트워크 전체 조정 없이 네트워크 대역폭이나 블록체인 공간을 낭비하기 전에 비경제적인 거래를 거부할 수 있다. 다른 노드 운영자는 자신의 필요, 하드웨어 기능 또는 철학에 따라 더 엄격하거나 느슨한 정책을 선택할 수 있다. 정책은 합의 변경의 조정 문제 없이 Bitcoin Core 릴리스를 통해 조정될 수 있으며, 새로운 거래 유형이 합의상 유효하게 되면서 정책 규칙이 시간이 지남에 따라 점진적으로 채택할 수 있다.

    ### 변경이 일어나는 방식

    비트코인에 대한 변경은 **BIP(Bitcoin Improvement Proposal, 비트코인 개선 제안)**를 통해 제안된다. 정책 변경은 Bitcoin Core 릴리스를 통해 정기적으로 발생하며 광범위한 조정이 필요하지 않다. 노드 운영자는 편리할 때 업그레이드할 수 있으며, 네트워크는 혼합된 정책 버전에서도 계속 기능한다. 최근 릴리스는 주로 멤풀 정책 개선에 초점을 맞추어 수수료율 최소값과 거래 릴레이 규칙과 같은 것들을 조정했다.

    합의 변경은 블록과 거래를 유효하게 만드는 기본 프로토콜 규칙을 수정하기 때문에 훨씬 드물고 더 중요하다. 이는 전체 네트워크가 규칙에 동의해야 하므로 신중한 조정이 필요하다. 합의 규칙이 변경될 때, 아래에서 탐구하는 특정 업그레이드 메커니즘을 통해 발생한다.

    Bitcoin Core의 신중한 개발 프로세스, 광범위한 테스트, 광범위한 채택은 이를 표준 참조 구현으로 만든다. SegWit과 Taproot와 같은 주요 업그레이드는 Core에서 구현되고 네트워크에 의해 활성화되어, 이 널리 채택된 소프트웨어를 통해 프로토콜 진화가 어떻게 작동하는지 보여준다. 그러나 궁극적인 통제는 어떤 소프트웨어를 실행하고 어떤 규칙을 따를지 결정하는 사용자와 비즈니스에 있다.

    ### 포크 유형 이해

    아무도 책임자가 없을 때 탈중앙화된 네트워크를 어떻게 업그레이드할 수 있을까? 비트코인은 합의를 유지하면서 프로토콜이 진화할 수 있게 하는 두 가지 주요 업그레이드 메커니즘을 가지고 있다.

    #### 하드 포크

    하드 포크(Hard fork)는 합의 규칙을 느슨하게 하거나 변경하는 비호환적인 업그레이드이다. 좌측 통행에서 우측 통행으로 변경하는 것으로 생각하라: 운전자가 전환하지 않으면, 새로운 도로에서 안전하게 운전할 수 없다. 모든 사람이 업그레이드해야 하며, 그렇지 않으면 별도의 도로 네트워크가 되는 이전 방향으로 계속 운전하게 된다. 비트코인은 이러한 완전한 전환을 조정하는 것이 위험하고 네트워크를 영구적으로 분할할 수 있기 때문에 이를 피한다. 하드 포크는 조정 문제와 영구적인 네트워크 분할 위험으로 인해 비트코인에서 극히 드물다.

    주목할 만한 예는 2017년에 규칙(특히 훨씬 큰 블록)을 변경하여 생성된 비트코인 캐시(Bitcoin Cash, BCH)이다. 실제로 그 접근 방식은 유동성과 커뮤니티 관심을 분열시켰다. 시간이 지남에 따라 BCH는 비트코인 채택, 해시파워, 시장 가치의 작은 일부만 유지했다. 대부분의 사용자, 개발자, 채굴자, 거래소는 일반인들이 풀 노드를 실행하고 체인을 직접 검증하는 것을 더 저렴하고 쉽게 유지했기 때문에 원래의 작은 블록 BTC 체인을 주요 "비트코인"으로 조정했다. 그러나 중요한 것은 "진짜 비트코인"이 무엇인지 결정하는 것은 코드가 명령할 수 있는 것이 아니며 중앙 권위가 없다는 것이다. 이는 사회적 합의(사용자, 거래소, 지갑, 상인이 실행하는 것), 경제적 중력(유동성이 정착하는 곳), 보안 가정(대부분의 풀 노드가 시행하는 것)의 복잡한 혼합이다. 시장은 확실히 BTC를 쉘링 포인트(Schelling point)로 취급했지만, 그 결과는 궁극적으로 사회적이지 명령된 것이 아니다.

    #### 소프트 포크

    소프트 포크(Soft fork)는 네트워크를 깨뜨리지 않고 합의 규칙을 강화하는 역호환적 프로토콜 업그레이드이다. 기존 운전자가 자동으로 준수하는 새로운 교통 규칙을 추가하는 것으로 생각하라: 업그레이드된 노드는 더 엄격한 규칙(예: "이 교차로에서 적색 신호시 우회전 금지")을 시행하고, 업그레이드되지 않은 노드는 여전히 모든 트래픽을 유효한 것으로 보며 네트워크는 정상적으로 계속 기능한다. 업그레이드되지 않은 비트코인 노드는 여전히 새 블록을 유효한 것으로 보지만 더 엄격한 규칙 자체를 시행하지 않아, 네트워크가 비호환 버전으로 분할되지 않고 업그레이드할 수 있다. 체인 분할을 피하기 위해 다수의 지지가 필요하며, 예로는 SegWit과 Taproot가 있다.

    #### 활성화 메커니즘

    소프트 포크를 구현하기로 결정하는 것은 한 가지이지만, 실제로 네트워크 전체에서 활성화하려면 신중한 조정이 필요하다. 네트워크는 준비 상태를 측정하고 새 규칙이 발효되기 전에 충분한 참여자가 업그레이드했는지 확인하는 방법이 필요하다. 여기서 활성화 메커니즘이 등장한다. 채굴자 조정, 경제 노드 참여, 체인 분할 위험 사이의 균형을 맞추기 위해 다양한 방법이 개발되었다.

    **채굴자 활성화 소프트 포크(Miner Activated Soft Fork, MASF)**는 해시파워 시그널링에 의존한다; 채굴자들은 블록 헤더에 버전 비트를 포함시켜 준비 상태를 표시한다. BIP9는 표준 MASF 프레임워크였으며, 정의된 시간 창 동안 높은 임계값(일반적으로 95%)의 블록이 지지를 신호하도록 요구했다. 임계값에 도달하면 소프트 포크가 잠기고 유예 기간 후에 활성화된다. 이는 SegWit(결국) 및 대부분의 역사적 소프트 포크와 같은 업그레이드에 사용되었다.

    **사용자 활성화 소프트 포크(User Activated Soft Fork, UASF)**는 경제 노드가 채굴자 시그널링과 관계없이 더 엄격한 규칙을 시행하기 시작하는 "플래그 데이"를 조정하는 대안을 나타낸다. 충분한 경제 노드와 서비스 제공자가 참여하면, 채굴자는 간단한 인센티브에 직면한다: 새 규칙을 따르고 지불받거나, 대부분의 사용자가 수락하지 않을 체인을 채굴하거나.

    **스피디 트라이얼(Speedy Trial)**은 2,016 블록 창에 걸쳐 90% 임계값을 가진 짧은 채굴자 시그널링 시험이다. 잠기면, 활성화는 나중에 사전 설정된 블록 높이에서 발생한다; 시간 초과되면, 활성화가 발생하지 않고 다른 메커니즘이 고려될 수 있다. 이 방법은 2021년 Taproot 활성화에 성공적으로 사용되었다.

    #### 변화의 어려움

    역호환성에도 불구하고, 비트코인에 어떤 소프트 포크든 넣는 것은 의도적으로 어렵다. 많은 개발자들은 **프로토콜 경직화(Protocol ossification)**, 즉 비트코인이 성숙함에 따라 변화에 점점 더 저항해야 한다는 아이디어를 우선시한다. 이 보수적인 접근 방식은 반직관적인 강점을 인식한다: 비트코인의 힘은 부분적으로 그것이 *하지 않는* 것에서 나온다. 드물게 변경함으로써 비트코인은 예측 가능해진다. 사용자는 통화 정책이 변경되지 않을 것이라고 신뢰할 수 있다. 변경이 적을수록, 수조 달러 자산을 손상시킬 수 있는 버그나 의도하지 않은 결과를 도입할 위험이 낮아진다.

    경제적 피드백 루프도 작용한다: 비트코인의 시가총액이 성장하고 더 많은 경제 활동이 그것에 의존할수록, "이 업그레이드가 위험을 감수할 가치가 있다"에 대한 임계값이 그에 따라 올라간다. 1,000억 달러 자산은 실험을 용인할 수 있다; 2조 달러 자산은 극단적인 보수주의를 요구한다. 이것은 버그가 아니며 기본 계층의 중요성이 증가함에 따라 자연스럽게 보호하는 기능이다.

    이 철학은 제안이 수년간의 검토, 테스트, 커뮤니티 토론을 거친다는 것을 의미한다.

    ### 비트코인의 주요 업그레이드

    #### 세그윗(Segregated Witness, SegWit, 2017)

    SegWit 활성화 사가는 비트코인 거버넌스에서 가장 중요한 사례 연구 중 하나를 나타내며, 진정으로 탈중앙화된 시스템에서 프로토콜 업그레이드가 어떻게 작동하는지(그리고 때로는 작동하지 않는지)를 보여준다.

    SegWit은 여러 중요한 문제를 해결한 획기적인 업그레이드였다. SegWit 이전에, 비트코인은 치명적인 버그가 있었다: 제3자가 확인 전에 거래의 서명을 변경하여 거래의 유효성에 영향을 주지 않고 ID(TXID)를 변경할 수 있었다. 이 **거래 가변성(Transaction malleability)**은 의존 거래나 Lightning과 같은 2계층 프로토콜을 구축하는 것을 위험하게 만들었다.

    SegWit은 서명 데이터를 별도의 "증인(Witness)" 구조로 옮겨 거래 ID가 생성되면 불변하게 만들었다. 또한 **블록 가중치(Block weight)**(단순한 1MB 제한 대신 4,000,000 가중치 단위 최대의 새로운 측정 시스템)를 도입했다. 이는 더 효율적인 SegWit 주소 채택을 장려하면서 효과적으로 블록 용량을 증가시켰다. 가중치 시스템은 증인 데이터를 가중치 계산에서 4분의 1로 계산하여(일반적으로 "75% 할인"으로 설명됨), 역호환적 블록 크기 증가를 만든다.

    정치적 역학을 이해하려면, SegWit 이전 비트코인을 "비트코인 1.0"(하드 1MB 블록 크기 제한과 거래 가변성 문제가 있는 시스템)으로 생각하는 것이 도움이 된다. SegWit은 "비트코인 1.1"을 나타냈다(비트코인 1.0과 대부분 역호환되지만, 프로토콜 버그를 수정하고 2계층 네트워크를 가능하게 하면서 일회성 용량 증가를 제공).

    원래 활성화 메커니즘은 95% 임계값의 BIP9를 사용한 MASF였다: 2016년 11월 15일부터 2017년 11월 15일까지의 창 내 어떤 2,016 블록 난이도 조정 기간 동안, 95% 이상의 채굴된 블록이 지지를 신호하면, 업그레이드가 잠기게 된다. 유예 기간 후 SegWit이 활성화되고 네트워크는 새로운 거래 유형을 수락한다.

    다음에 일어난 일을 이해하려면 일부 맥락이 필요하다. 비트코인은 수년간 확장 방법에 대해 논쟁해왔다. 일부 파벌은 하드 포크를 통해 블록 크기 제한을 극적으로 늘리기를 원했고(결국 비트코인 캐시 생성으로 이어짐), 다른 일부는 거래 가변성을 수정하고 Lightning Network와 같은 2계층 솔루션을 가능하게 하는 SegWit의 접근 방식을 선호했다. 이 불일치는 "블록 크기 전쟁"으로 알려지게 되었다.

    일부 대형 채굴자들은 단순히 블록 크기를 늘리는 것을 선호했기 때문에 SegWit에 반대했다. SegWit이 개발자, 비즈니스, 노드 운영자로부터 광범위한 지지를 받았음에도 불구하고, 이 채굴자들은 신호를 거부하여 활성화를 차단할 수 있었다. BIP9 메커니즘은 신호가 "내 소프트웨어가 기술적으로 준비되었다"를 의미한다고 가정했지만, 이 채굴자들은 이를 정치적 투표로 취급했다. 이는 조정된 채굴자 그룹이 업그레이드의 기술적 참여를 요구하지 않았음에도 불구하고 유익한 업그레이드에 무기한 거부권을 행사할 수 있는 전례 없는 거버넌스 위기를 만들었다.

    BIP 148은 이 거버넌스 교착 상태에 대한 제안된 해결책을 나타냈다. BIP 148은 2017년 8월 1일 이후 비신호 블록을 거부하여 참여 노드의 합의 규칙을 변경했다. 충분한 경제 노드(거래소, 서비스, 비즈니스)가 BIP 148을 실행하면, 채굴자들은 냉혹한 선택에 직면했다: SegWit 지지를 신호하고 더 넓은 경제가 수락할 비트코인으로 지불받거나, 주요 경제 행위자들이 무시할 체인을 채굴하거나.

    BIP 148의 위협은 궁극적으로 교착 상태를 해결한 강력한 경제적 인센티브를 만들었다. BIP 91은 2017년 7월 21일에 잠기고 이틀 후에 활성화되어, 채굴자들이 비트 1을 신호하도록 시행하고 BIP 141이 임계값에 도달할 수 있게 했다. BIP 148의 플래그 데이가 8월 1일로 계획되어 있어 압박이 있었다. SegWit(BIP 141)은 2017년 8월 9일에 잠기고 블록 481,824에서 2017년 8월 24일에 활성화되었다. BIP 91은 UASF 마감일 전에 채굴자들이 SegWit 지지를 신호할 수 있게 한 중간 솔루션으로 작용했으며, SegWit은 원래의 BIP9 메커니즘을 통해 성공적으로 활성화되었다.

    SegWit 활성화는 비트코인 거버넌스에 대한 몇 가지 중요한 원칙을 보여준다. 경제 노드는 충분히 조정되면 궁극적으로 프로토콜 규칙을 시행하며, 채굴자와 사용자 간의 권력 역학을 강화한다. 소프트 포크는 채굴자 저항에도 불구하고 충분한 경제적 조정이 있을 때 사용자에 의해 시행될 수 있다. 신뢰할 수 있는 위협이 실제 배포보다 중요하며, BIP 148은 대다수의 노드가 실제로 실행한 것이 아니라 위협이 믿을 만했기 때문에 대부분 성공했다. 마지막으로, 비트코인의 거버넌스는 안티프래질(Antifragile)함이 입증되었다: 시스템은 조정된 저항에도 불구하고 봉쇄를 우회하고 유익한 업그레이드를 활성화하는 방법을 찾았다.

    #### 탭루트(Taproot, 2021)

    Taproot 업그레이드는 프로그래밍 가능성과 기밀성을 크게 개선했다. SegWit의 논쟁적인 활성화와 달리, Taproot는 채굴자, 개발자, 경제 노드 전반에 걸쳐 광범위한 합의를 누렸다. 그러나 이 합의에도 불구하고, 업그레이드는 변경 사항이 철저히 검토되고 안전하게 배포되도록 수년간의 활발한 커뮤니티 토론, 신중한 검토, 조정이 여전히 필요했다.

    Taproot는 90% 채굴자 시그널링 임계값의 스피디 트라이얼 활성화 메커니즘을 사용했다. 시그널링 기간은 2021년 5월에 시작되었고, 임계값은 빠르게 충족되어 2021년 6월에 업그레이드가 잠겼다. 나머지 노드가 업그레이드할 수 있도록 미리 결정된 유예 기간 후, Taproot는 블록 709,632에서 2021년 11월에 활성화되었다. 원활한 활성화는 진정한 합의가 있을 때 비트코인이 신중하고 심사숙고한 프로토콜 변경 접근 방식을 유지하면서 효율적으로 업그레이드할 수 있음을 보여주었다.

    기술적 개선은 상당했다. **슈노르 서명(Schnorr Signatures)**은 키와 서명 집계를 가능하게 하여 복잡한 다자간 거래가 온체인에서 단일 서명으로 나타날 수 있게 한다. **머클화된 추상 구문 트리(Merkleized Abstract Syntax Trees, MAST)**는 복잡한 지출 조건을 효율적으로 구조화하여, 충족된 조건만 공개하면 된다.

    함께, 이러한 기능은 주요 이점을 제공한다: 복잡한 거래가 키 경로 지출에서 단순한 결제와 구별할 수 없게 되어 상당한 프라이버시와 확장성 개선을 제공한다. 스크립트 경로 지출이 사용될 때, 공개된 분기만 드러나 사용되지 않은 조건에 대한 프라이버시를 유지한다.

## Section IV: Bitcoin Network Operations and Security Model

=== "EN"

    Having examined Bitcoin's technical architecture and upgrade mechanisms, we now turn to how the network itself operates. Understanding the security economics that keep Bitcoin running provides essential context for evaluating Layer 2 solutions and Bitcoin's long-term viability.

    We've established that full nodes validate transactions and blocks while miners compete to produce new blocks. Miners almost universally run their own full nodes because they need to independently validate transactions, build upon the latest valid block, and ensure the blocks they produce follow all consensus rules. A miner who builds an invalid block forfeits their reward since the network will reject it.

    Not all participants need to run full nodes, however. Pruned nodes provide the same validation security as full nodes but conserve disk space by discarding old block data after verification. **SPV (Simplified Payment Verification)** clients, commonly found in mobile wallets, take a lighter approach by downloading only block headers and relying on full nodes for transaction validation.

    Miners wield significant but limited influence. They control transaction inclusion and ordering, determine which valid fork to mine on, and can attempt short-term censorship within existing rules. However, as the SegWit activation saga demonstrated, economic nodes ultimately hold the power. Miners must produce blocks that the broader economy will accept, or they don't get paid.

    To find each other, the network maintains its decentralized topology through peer-to-peer discovery mechanisms, primarily using DNS seeds and direct peer-to-peer exchange.

    ### Block Propagation and Network Synchronization

    When a new node joins, it performs an Initial Block Download (IBD) to sync the entire blockchain from its peers. To ensure new blocks propagate quickly and efficiently, the network uses optimized protocols like Compact Block Relay, which minimizes bandwidth by only sending information that nodes don't already have. Nodes also engage in mempool synchronization to share unconfirmed transactions. The network is resilient to partitions (temporary splits), which self heal once connectivity is restored.

    ### Attack Vectors and Economic Security

    Bitcoin's security depends on making attacks too expensive to be profitable for most actors. The most cited threat is a **51% attack**, where an entity controlling a majority of the network's hashpower could attempt to rewrite recent history or double-spend its own coins. For profit-seeking attackers, the immense cost of acquiring and running this hardware, combined with the fact that a successful attack would devalue the asset they're attacking, makes this strategy economically irrational.

    In theory, a nation-state or ideological attacker could ignore direct financial losses and attack for political or strategic reasons. But even then, they face substantial practical hurdles: sourcing and operating enough specialized hardware and energy, coordinating the attack without being detected, and sustaining it in the face of defensive responses (exchanges pausing withdrawals, users waiting for more confirmations, miners re-organizing, or even a community-driven change in the mining algorithm). In practice, nation-states have cheaper and more effective tools like regulation, taxation, surveillance, and pressure on exchanges and custodians than trying to permanently dominate Bitcoin's hashpower.

    #### The Security Budget

    The security budget is the economic foundation that makes attacks prohibitively expensive. As explained in Section I, it consists of the block subsidy plus transaction fees, determining how much hash rate miners deploy to secure the network. While this budget is straightforward to calculate in BTC terms, the relevant metric for gauging attack resistance is USD per unit time, since both miners and potential attackers procure hardware, facilities, and energy in fiat terms.

    Understanding Bitcoin's security model requires understanding how it's actually used. Bitcoin functions more like gold than a payment network. Most bitcoin sits passively in wallets for long periods, with large holders rarely touching their funds. This "set and forget" mentality means transaction volume remains relatively low compared to payment networks, creating implications for the long-term security budget.

    Bitcoin's halving schedule creates a central security challenge: as the block subsidy declines toward zero by 2140, transaction fees must eventually carry the entire security budget. However, if Bitcoin is primarily held rather than frequently transacted, fee generation may remain modest. This creates a critical tension: if transaction fees and BTC price do not rise sufficiently to offset successive halvings, the USD-denominated security budget will trend lower. A materially smaller budget could lead to miner exits, weaker competition for blocks, and reduced costs for would-be attackers to acquire majority hash rate.

    Whether durable fee demand emerges from settlement payments, L2 operations, data inscriptions, rollup commitments, or other block space uses remains an open question critical to Bitcoin's long-term security model.

    #### How Security Works

    As discussed in Section I, security is achieved through confirmation depth. Each subsequent block exponentially increases the work required to alter a transaction. The system is designed so that economic incentives strongly reward miners for honest behavior, backed by the economic resources represented by the security budget.

    Bitcoin is designed to be antifragile, meaning it grows stronger from stress and attacks. Its resilience stems from several factors: geographic distribution of nodes and miners resists localized disruptions, protocol ossification or resistance to change enhances stability and predictability, and its design assumes an adversarial environment, built to function despite malicious actors. The network has survived numerous technical, political, and economic challenges, demonstrating its robust and self-healing nature.

=== "KO"

    비트코인의 기술 아키텍처와 업그레이드 메커니즘을 검토했으니, 이제 네트워크 자체가 어떻게 운영되는지로 넘어간다. 비트코인을 운영하게 하는 보안 경제학을 이해하는 것은 Layer 2 솔루션과 비트코인의 장기적 생존 가능성을 평가하는 데 필수적인 맥락을 제공한다.

    풀 노드가 거래와 블록을 검증하고 채굴자가 새 블록을 생성하기 위해 경쟁한다는 것을 확립했다. 채굴자들은 거래를 독립적으로 검증하고, 최신 유효한 블록 위에 구축하고, 그들이 생성하는 블록이 모든 합의 규칙을 따르도록 해야 하기 때문에 거의 보편적으로 자체 풀 노드를 운영한다. 유효하지 않은 블록을 구축하는 채굴자는 네트워크가 이를 거부하므로 보상을 상실한다.

    그러나 모든 참여자가 풀 노드를 실행할 필요는 없다. 가지치기 노드(Pruned node)는 풀 노드와 동일한 검증 보안을 제공하지만 검증 후 오래된 블록 데이터를 삭제하여 디스크 공간을 절약한다. 모바일 지갑에서 흔히 발견되는 **SPV(간이 결제 검증, Simplified Payment Verification)** 클라이언트는 블록 헤더만 다운로드하고 거래 검증을 풀 노드에 의존하는 더 가벼운 접근 방식을 취한다.

    채굴자는 상당하지만 제한된 영향력을 행사한다. 그들은 거래 포함 및 순서를 제어하고, 어떤 유효한 포크에서 채굴할지 결정하며, 기존 규칙 내에서 단기 검열을 시도할 수 있다. 그러나 SegWit 활성화 사가가 보여주었듯이, 경제 노드가 궁극적으로 권력을 가진다. 채굴자는 더 넓은 경제가 수락할 블록을 생성해야 하며, 그렇지 않으면 지불받지 못한다.

    서로를 찾기 위해, 네트워크는 주로 DNS 시드와 직접적인 P2P 교환을 사용하는 피어 투 피어 발견 메커니즘을 통해 탈중앙화된 토폴로지를 유지한다.

    ### 블록 전파와 네트워크 동기화

    새 노드가 참여하면, 피어로부터 전체 블록체인을 동기화하기 위해 초기 블록 다운로드(Initial Block Download, IBD)를 수행한다. 새 블록이 빠르고 효율적으로 전파되도록 하기 위해, 네트워크는 Compact Block Relay와 같은 최적화된 프로토콜을 사용하여 노드가 이미 가지고 있지 않은 정보만 전송하여 대역폭을 최소화한다. 노드는 또한 미확인 거래를 공유하기 위해 멤풀 동기화에 참여한다. 네트워크는 파티션(일시적 분할)에 복원력이 있으며, 연결이 복원되면 자가 치유된다.

    ### 공격 벡터와 경제적 보안

    비트코인의 보안은 대부분의 행위자에게 공격이 수익성이 없을 정도로 비용을 높게 만드는 데 의존한다. 가장 많이 인용되는 위협은 **51% 공격**으로, 네트워크 해시파워의 과반수를 통제하는 개체가 최근 역사를 다시 쓰거나 자신의 코인을 이중 지불하려고 시도할 수 있다. 이익 추구 공격자에게는 이 하드웨어를 획득하고 운영하는 막대한 비용과 성공적인 공격이 공격하는 자산의 가치를 떨어뜨린다는 사실이 결합되어 이 전략을 경제적으로 비합리적으로 만든다.

    이론적으로, 국가나 이념적 공격자는 직접적인 금전적 손실을 무시하고 정치적이거나 전략적인 이유로 공격할 수 있다. 그러나 그들도 상당한 실질적인 장애물에 직면한다: 충분한 특수 하드웨어와 에너지를 조달하고 운영하는 것, 탐지되지 않고 공격을 조율하는 것, 방어적 대응(거래소 출금 중지, 사용자가 더 많은 확인 대기, 채굴자 재조직, 또는 커뮤니티 주도의 채굴 알고리즘 변경)에 맞서 지속하는 것. 실제로, 국가들은 비트코인의 해시파워를 영구적으로 지배하려는 것보다 규제, 과세, 감시, 거래소와 수탁자에 대한 압박과 같은 더 저렴하고 효과적인 도구를 가지고 있다.

    #### 보안 예산

    보안 예산은 공격을 엄청나게 비싸게 만드는 경제적 기반이다. Section I에서 설명했듯이, 이는 블록 보조금과 거래 수수료로 구성되며, 채굴자가 네트워크를 보호하기 위해 배치하는 해시레이트의 양을 결정한다. 이 예산은 BTC 기준으로 계산하기는 간단하지만, 공격 저항성을 측정하는 관련 지표는 단위 시간당 USD이다. 채굴자와 잠재적 공격자 모두 하드웨어, 시설, 에너지를 법정 화폐로 조달하기 때문이다.

    비트코인의 보안 모델을 이해하려면 그것이 실제로 어떻게 사용되는지 이해해야 한다. 비트코인은 결제 네트워크보다 금과 더 유사하게 기능한다. 대부분의 비트코인은 오랜 기간 지갑에 수동적으로 보관되며, 대량 보유자는 자금을 거의 건드리지 않는다. 이 "설정하고 잊어버리는" 사고방식은 결제 네트워크에 비해 거래량이 상대적으로 낮게 유지됨을 의미하며, 장기 보안 예산에 대한 함의를 만든다.

    비트코인의 반감기 일정은 핵심적인 보안 과제를 만든다: 블록 보조금이 2140년까지 0을 향해 감소함에 따라, 거래 수수료가 결국 전체 보안 예산을 담당해야 한다. 그러나 비트코인이 주로 보유되고 자주 거래되지 않는다면, 수수료 생성은 완만하게 유지될 수 있다. 이는 중요한 긴장을 만든다: 거래 수수료와 BTC 가격이 연속적인 반감기를 상쇄할 만큼 충분히 오르지 않으면, USD 표시 보안 예산은 낮아지는 추세를 보일 것이다. 상당히 작은 예산은 채굴자 이탈, 블록 경쟁 약화, 잠재적 공격자가 과반수 해시레이트를 획득하는 비용 감소로 이어질 수 있다.

    정산 결제, L2 운영, 데이터 인스크립션, 롤업 커밋 또는 기타 블록 공간 사용에서 지속 가능한 수수료 수요가 나타날지 여부는 비트코인의 장기 보안 모델에 중요한 열린 질문으로 남아 있다.

    #### 보안이 작동하는 방식

    Section I에서 논의했듯이, 보안은 확인 깊이를 통해 달성된다. 각 후속 블록은 거래를 변경하는 데 필요한 작업을 기하급수적으로 증가시킨다. 시스템은 경제적 인센티브가 채굴자의 정직한 행동을 강력하게 보상하도록 설계되었으며, 보안 예산이 나타내는 경제적 자원으로 뒷받침된다.

    비트코인은 안티프래질하도록 설계되었으며, 이는 스트레스와 공격으로부터 더 강해진다는 것을 의미한다. 그 복원력은 여러 요인에서 비롯된다: 노드와 채굴자의 지리적 분산이 지역화된 혼란에 저항하고, 프로토콜 경직화 또는 변화에 대한 저항이 안정성과 예측 가능성을 향상시키며, 설계가 적대적 환경을 가정하여 악의적인 행위자에도 불구하고 기능하도록 구축되었다. 네트워크는 수많은 기술적, 정치적, 경제적 도전을 극복하며 견고하고 자가 치유적인 특성을 보여주었다.

## Section V: Bitcoin Layer 2 and Extensions

=== "EN"

    Having established how Bitcoin's network operates and maintains security, we can now explore how these foundational mechanisms enable higher-layer innovation. This section examines two distinct categories of extension: scaling solutions that move transactions off-chain for speed and cost efficiency, and data layer applications that leverage Bitcoin's immutability for on-chain use cases. While these serve fundamentally different purposes (one addresses throughput constraints, the other exploits Bitcoin's censorship-resistant storage), both demonstrate how a simple, constrained base layer can enable sophisticated higher-layer functionality.

    ### Scaling: L2 Classification and Trust Models

    Before examining specific scaling solutions, it's essential to understand what actually qualifies as a Layer 2 (L2) and what security guarantees are possible given Bitcoin's current capabilities. Numerous projects claim to offer Bitcoin L2 solutions with different tradeoff profiles, but evaluating these claims requires a clear definitional framework.

    The fundamental dilemma centers on a basic limitation: while Bitcoin Script can verify signatures and basic spending conditions, it cannot enforce complex constraints on future transactions or verify claims about external state.

    The definitional challenge stems from what constitutes a genuine L2: a scaling solution that inherits the security properties of its base layer without introducing additional trust assumptions. True L2s allow users to unilaterally exit back to the main chain using only cryptographic proofs, no permission needed from any third party. The base layer's consensus mechanism can directly adjudicate disputes and enforce the L2's rules. Most current Bitcoin scaling solutions, however, are more accurately described as sidechains or federated networks with Bitcoin bridges, since they require users to rely on external validators beyond Bitcoin's own consensus.

    This creates a security constraint for L2 bridges and rollups. When someone wants to withdraw funds from an L2 back to Bitcoin's main chain, the system needs a way to verify that the withdrawal is legitimate according to the L2's state. However, Bitcoin Script cannot practically check things like "this withdrawal matches an entry in the L2's state tree" or "these outputs correspond to a valid Merkle proof." Script lacks the needed covenant and introspection primitives to make this practical without reliance on intermediaries.

    As a result, today's Bitcoin L2 solutions fall back on third-party validators, federations of signers, multisig arrangements, or programmatic attesters, to validate and co-sign withdrawals. This is exactly what systems like Stacks' sBTC do with their "decentralized network of signers." While these signers may be distributed across multiple parties, they still represent a fundamental custody risk: if they collude, get compromised, or their software has bugs, user funds can be censored or stolen. The "trustless" promise of cryptocurrency gets reduced to relying on this federation model.

    #### Potential Solutions: Covenants and Alternatives

    Developers have proposed several ways to fix Bitcoin's L2 limitations. Each approach offers different tradeoffs between how soon it could work and how secure it would be.

    The most straightforward solution involves upgrading Bitcoin itself. Developers have proposed adding new opcodes to Bitcoin's programming language through a soft fork. The leading candidates include re-enabling something called OP\_CAT and adding new tools like CTV and CSFS. Together, these would let Bitcoin scripts create custom messages, verify signatures, and set rules about how coins can be spent later.

    For L2 bridges, this would be transformative. Right now, you have to trust a group of signers to approve withdrawals. With **covenants**, Bitcoin's blockchain could check the math itself and enforce the exit rules automatically. You could withdraw your funds using only cryptographic proofs, and no federation could stop you. The debate now focuses on figuring out the smallest set of new opcodes that would enable this safely. None of these proposals are active yet, and they would need broad agreement from the Bitcoin community to implement.

    While covenant opcodes might take years to activate, BitVM takes a different approach. It works with Bitcoin exactly as it exists today, without any upgrades needed. BitVM and its newer versions (BitVM2 and BitVM3) use what's called an optimistic model.

    Here's how it works: an operator makes a claim about what's happening on the L2. If they're lying, anyone can challenge them on the Bitcoin blockchain within a certain window (usually a few days to two weeks). If the challenge succeeds, the operator loses the money they put up as collateral. Recent research claims BitVM3 can reduce the data needed to about 66 kilobytes using something called garbled circuits, but the designs are still changing quickly. In fact, one version from July 2025 had to be pulled back after researchers found a security flaw. These approaches are still experimental rather than ready for real use.

    BitVM systems have important limitations. They're complicated to run and require active participation. Someone has to actually watch for fraud and challenge it within the time window. The security depends on at least one honest person being willing and able to raise the alarm. This is fundamentally different from covenant-based systems, where Bitcoin itself checks the proofs directly without needing anyone to file a dispute.

    The key distinction comes down to who enforces the rules. Today's federation-based systems ask you to trust that most signers will be honest. Covenant-enabled systems would move that enforcement into Bitcoin's consensus rules themselves, making invalid withdrawals literally impossible to include in the blockchain regardless of what any federation tries to do. This would be a major security upgrade.

    Whether Bitcoin will actually adopt these changes, and when, is still an open question in the development community.

    ### Lightning Network

    Bitcoin's base layer is optimized for high-assurance settlement, which makes small everyday payments economically inefficient. High fees and limited block space mean buying coffee with an on-chain transaction doesn't make sense. The Lightning Network attempts to solve this by moving small, frequent payments off the main blockchain.

    The basic concept is straightforward. Instead of broadcasting every payment to the entire network, two parties can open a private **payment channel** by locking funds in a special on-chain transaction that requires both signatures to spend. Once the channel is open, they can update their balances off-chain by creating new versions of how the funds could be split, along with cryptographic penalties that punish anyone who tries to cheat by broadcasting an old state. When they're done transacting, they can close the channel and settle the final balance back to the main blockchain.

    The network becomes more powerful through routing. Users don't need direct channels with everyone they want to pay. If Alice has a channel with Bob, and Bob has a channel with Carol, Alice can pay Carol through Bob. The network uses routing techniques that hide the full payment path from intermediate nodes, providing better privacy than repeatedly using the same on-chain addresses. However, the privacy isn't perfect. Careful analysis of payment amounts, timing, and network probing can still reveal information.

    #### Lightning's Strengths

    When Lightning works well, it delivers compelling advantages. Payments settle in seconds rather than waiting for block confirmations, making it viable for point-of-sale transactions and interactive applications. Transaction costs drop to negligible amounts, often just a few satoshis, enabling microtransactions that would be completely impractical on the base layer. The off-chain nature of payments provides better privacy than repeatedly using the same on-chain addresses, as intermediate routing nodes only see encrypted payment data. For users who establish well-connected channels with sufficient liquidity in both directions, Lightning can provide a smooth payment experience that approaches the convenience of traditional payment systems while maintaining non-custodial control of funds.

    #### The Liquidity Challenge

    Lightning users can only send payments if there's enough balance on their side (outbound capacity), and they can only receive payments if the other side has enough room (inbound capacity). This liquidity constraint is Lightning's biggest practical limitation.

    When channels lack sufficient liquidity in the right direction, payments fail or must be split across multiple routes. Some technical improvements help: payments can be automatically split across several paths to improve success rates, and specialized service providers can help users acquire the inbound capacity needed to receive payments. Channel rebalancing can redistribute liquidity, but it costs fees and takes time. Even with these tools, the fundamental challenge of having liquidity in the right place at the right time remains.

    #### Operational Realities

    Lightning faces several hurdles to adoption. Unlike Bitcoin's base layer where payments arrive automatically even when the recipient is offline, Lightning typically requires users to be online to receive payments. Some services can monitor channels for cheating attempts while you're offline, keeping your funds safe, but they don't enable offline receiving itself.

    Some wallet providers offer workarounds that allow payments to arrive when you're offline, but these often involve trusting the service provider with some custody or control. For users, managing channels is complex. They must acquire inbound capacity to receive payments, stay online or use trusted services, and navigate the separation between L1 and L2. This operational overhead is difficult for non-technical users.

    Higher base layer fees create additional challenges. Opening and closing channels becomes more expensive, and during fee spikes, time-sensitive transactions may need to be confirmed quickly or risk forcing channels to close. Modern improvements allow channels to be resized without fully closing them and enable better fee management, but the operational complexity remains.

    For merchants, integration complexity is compounded by Bitcoin's price volatility, which creates accounting and pricing challenges regardless of whether payments arrive on-chain or through Lightning.

    #### The Custodial Trade-off

    These limitations have led many users toward custodial or semi-custodial Lightning wallet services that manage channels and liquidity on their behalf. While this dramatically improves user experience and payment reliability, it reintroduces the trust requirements and vulnerabilities that Bitcoin was designed to eliminate. Users face custodial risk: funds can be frozen, accounts can be closed, services can fail, and providers must be trusted not to mismanage or steal funds. This represents a fundamental tension between usability and the self-sovereignty that attracted many to Bitcoin in the first place.

    ### Beyond Payments: Bitcoin as a Data Layer

    Having explored scaling solutions aimed at transaction throughput and smart contracts, we now turn to an entirely different category of Bitcoin extension. While Lightning and L2s attempt to reduce on-chain activity, Ordinals and inscription-based systems embrace it, using Bitcoin's immutability and censorship resistance to anchor arbitrary data permanently on the blockchain. This represents a philosophical shift from "Bitcoin as payment rail" to "Bitcoin as permanent storage layer."

    #### Ordinal Theory

    Ordinal theory is a way of treating individual satoshis as unique, collectible units rather than interchangeable currency. The core idea is simple: assign every satoshi a serial number based on when it was mined. This numbering system allows specific satoshis to be tracked as they move through transactions, similar to how you might track a dollar bill by its serial number.

    This tracking system enables a practice called **inscriptions**, where users attach arbitrary data (images, text, or other content) to specific satoshis. The inscribed satoshi becomes a carrier of that digital content, creating something analogous to digital collectibles or NFTs directly on the Bitcoin blockchain.

    Inscriptions use a two-step process. First, a transaction commits to what will be inscribed. Then, a second transaction reveals the actual content by including it in the transaction's witness data. This stores the content directly on the blockchain rather than just storing a reference to external data.

    This approach differs from earlier methods of embedding data in Bitcoin. The inscription data lives in witness space, which can be pruned by nodes that don't want to store it after validation. Archive nodes and specialized indexers maintain the full inscription history, allowing users to retrieve the content even if many nodes have pruned it.

    #### Bitcoin-Native NFTs

    An inscribed satoshi functions like a Bitcoin-native NFT: a unique token with on-chain content and provenance that transfers by moving that specific satoshi. The architectural difference from Ethereum's NFTs is notable. Ethereum relies on smart contract standards like ERC-721, often with media stored off-chain on services like IPFS. Bitcoin achieves uniqueness through ordinal numbering, with the media bytes embedded directly in the blockchain's witness data. The result is a digital artifact whose uniqueness is enforced by Bitcoin's transaction model combined with off-chain indexers that follow ordinal conventions.

    Transferring an inscription requires careful control of which satoshis are being spent. Users must ensure their transaction's input and output ordering moves the target inscribed sat and not the surrounding ones. Purpose-built wallets and specialized tooling provide this precise sat selection capability. Experts recommend keeping inscribed sats in separate addresses to avoid accidental merges or spends, while marketplaces often use partially signed transactions so users can verify exactly which inscription is being transferred before signing.

    #### BRC-20: Experimental Fungible Tokens

    While Ordinals create unique digital artifacts, BRC-20 extends the concept to fungible tokens on Bitcoin. Rather than using smart contracts, BRC-20 uses small JSON inscriptions that describe three fundamental actions: deploy (create a new token), mint (create new units), and transfer (send tokens to someone else). Community-run indexers reconstruct token balances by reading the ordered history of these inscriptions, creating a system of "rules by convention" rather than enforcement by Bitcoin's scripting language.

    The system works like this: a deploy inscription initializes a token ticker (typically four letters) and sets parameters like maximum supply. Mint inscriptions create new units and credit them to whoever owns the mint inscription. Transfer inscriptions earmark amounts to send. Unlike Ethereum tokens where a smart contract enforces all the rules, BRC-20 validity depends on indexers agreeing on the interpretation of these JSON messages.

    #### The Transfer Process

    A BRC-20 transfer follows a two-step process. Think of it like writing a check: First, you create the "check" by making a transfer inscription. This earmarks the funds you want to send. Then, you must physically hand the check to the recipient by sending them the transaction output containing that inscription.

    The technical mechanics work as follows: users first inscribe a JSON object declaring their intent to transfer a specific number of tokens, receiving this transfer inscription in the same wallet that holds their BRC-20 balance. This step moves tokens from an "available" balance to a "transferable" pool in the eyes of indexers. Then, the transfer inscription itself must be sent to the recipient's address. When that transaction confirms, indexers debit the sender's balance and credit the recipient.

    This creates an important distinction from Ordinals: sending an Ordinal inscription resembles moving a unique physical object, while BRC-20 transfers operate more like managing ledger entries with a paper trail.

    #### The Debate

    The emergence of Ordinals and inscriptions has sparked significant debate within the Bitcoin community. Critics argue that storing arbitrary data consumes valuable block space that should be reserved for financial transactions, creates sustained fee pressure that prices out smaller users, and represents a misuse of Bitcoin's design as peer-to-peer electronic cash. Proponents counter that all consensus-valid transactions are legitimate uses of the network, that inscription activity generates fee revenue crucial for long-term miner sustainability as the block subsidy declines, and that preventing users from embedding data would require contentious changes that conflict with Bitcoin's permissionless ethos.

    This tension reflects deeper questions about Bitcoin's purpose and evolution: is it purely a payment and settlement layer, or can it accommodate diverse use cases that leverage its unique properties of immutability and censorship resistance?

    #### Strengths and Limitations

    Ordinals and BRC-20 demonstrate how Bitcoin's base layer can support digital asset systems through creative use of existing features without requiring new opcodes or consensus changes. They use Taproot's witness space and Bitcoin's transaction model to create application-layer conventions. The blockchain itself remains unchanged.

    However, this approach has inherent limitations. Collection-wide rules, royalties, and token supply enforcement exist outside Bitcoin's scripting language and depend on indexers and community conventions rather than cryptographic guarantees. BRC-20 in particular remains explicitly experimental, with even its original creator pointing to alternative systems as more purpose-built solutions. Both systems work across multiple wallets and marketplaces today, but they're best understood as social conventions anchored to real Bitcoin transactions rather than protocol-enforced mechanisms.

=== "KO"

    비트코인의 네트워크가 어떻게 운영되고 보안을 유지하는지 확립했으니, 이제 이러한 기본 메커니즘이 어떻게 상위 계층 혁신을 가능하게 하는지 탐구할 수 있다. 이 섹션에서는 두 가지 뚜렷한 확장 범주를 검토한다: 속도와 비용 효율성을 위해 거래를 오프체인으로 이동하는 스케일링 솔루션과 온체인 사용 사례를 위해 비트코인의 불변성을 활용하는 데이터 레이어 애플리케이션. 이들이 근본적으로 다른 목적을 수행하지만(하나는 처리량 제약을 해결하고 다른 하나는 비트코인의 검열 저항 스토리지를 활용함), 둘 다 단순하고 제한된 기본 계층이 어떻게 정교한 상위 계층 기능을 가능하게 할 수 있는지를 보여준다.

    ### 스케일링: L2 분류와 신뢰 모델

    특정 스케일링 솔루션을 검토하기 전에, 실제로 Layer 2(L2)로 자격이 되는 것이 무엇인지, 비트코인의 현재 기능을 고려할 때 어떤 보안 보장이 가능한지 이해하는 것이 필수적이다. 다양한 트레이드오프 프로필을 가진 비트코인 L2 솔루션을 제공한다고 주장하는 수많은 프로젝트가 있지만, 이러한 주장을 평가하려면 명확한 정의 프레임워크가 필요하다.

    근본적인 딜레마는 기본 한계에 중심을 둔다: Bitcoin Script는 서명과 기본 지출 조건을 검증할 수 있지만, 미래 거래에 대한 복잡한 제약을 시행하거나 외부 상태에 대한 주장을 검증할 수 없다.

    정의적 도전은 진정한 L2가 무엇을 구성하는지에서 비롯된다: 추가적인 신뢰 가정을 도입하지 않고 기본 계층의 보안 속성을 상속하는 스케일링 솔루션. 진정한 L2는 사용자가 암호학적 증명만을 사용하여 메인 체인으로 단독으로 나갈 수 있게 한다. 어떤 제3자의 허가도 필요 없다. 기본 계층의 합의 메커니즘이 분쟁을 직접 중재하고 L2의 규칙을 시행할 수 있다. 그러나 대부분의 현재 비트코인 스케일링 솔루션은 사용자가 비트코인 자체의 합의를 넘어 외부 검증자에 의존해야 하므로, 비트코인 브리지가 있는 사이드체인이나 연합 네트워크로 더 정확하게 설명된다.

    이는 L2 브리지와 롤업에 대한 보안 제약을 만든다. 누군가 L2에서 비트코인 메인 체인으로 자금을 출금하려면, 시스템은 출금이 L2의 상태에 따라 합법적인지 검증하는 방법이 필요하다. 그러나 Bitcoin Script는 "이 출금이 L2의 상태 트리의 항목과 일치한다" 또는 "이 출력이 유효한 머클 증명에 해당한다"와 같은 것을 실질적으로 확인할 수 없다. Script는 중개자에 의존하지 않고 이를 실용적으로 만드는 데 필요한 코버넌트와 내성 프리미티브가 부족하다.

    결과적으로, 오늘날 비트코인 L2 솔루션은 출금을 검증하고 공동 서명하기 위해 제3자 검증자, 서명자 연합, 다중 서명 배열 또는 프로그래밍된 증명자에 의존한다. 이것이 바로 Stacks의 sBTC와 같은 시스템이 "탈중앙화된 서명자 네트워크"로 수행하는 것이다. 이 서명자들이 여러 당사자에 분산되어 있을 수 있지만, 여전히 근본적인 수탁 위험을 나타낸다: 그들이 공모하거나 손상되거나 소프트웨어에 버그가 있으면, 사용자 자금이 검열되거나 도난당할 수 있다. 암호화폐의 "무신뢰" 약속은 이 연합 모델에 의존하는 것으로 축소된다.

    #### 잠재적 해결책: 코버넌트와 대안

    개발자들은 비트코인의 L2 한계를 해결하는 여러 방법을 제안했다. 각 접근 방식은 얼마나 빨리 작동할 수 있는지와 얼마나 안전할지 사이에서 다른 트레이드오프를 제공한다.

    가장 직접적인 해결책은 비트코인 자체를 업그레이드하는 것이다. 개발자들은 소프트 포크를 통해 비트코인의 프로그래밍 언어에 새로운 연산코드를 추가하는 것을 제안했다. 주요 후보로는 OP_CAT이라는 것을 다시 활성화하고 CTV와 CSFS와 같은 새로운 도구를 추가하는 것이 있다. 함께, 이들은 비트코인 스크립트가 커스텀 메시지를 생성하고, 서명을 검증하고, 나중에 코인이 어떻게 사용될 수 있는지에 대한 규칙을 설정할 수 있게 해준다.

    L2 브리지의 경우, 이는 혁신적일 것이다. 현재는 출금을 승인하기 위해 서명자 그룹을 신뢰해야 한다. **코버넌트(Covenant)**를 사용하면, 비트코인의 블록체인이 직접 수학을 확인하고 탈출 규칙을 자동으로 시행할 수 있다. 암호학적 증명만 사용하여 자금을 출금할 수 있으며, 어떤 연합도 당신을 막을 수 없다. 논쟁은 이제 이를 안전하게 가능하게 하는 가장 작은 새 연산코드 집합을 찾는 데 초점을 맞추고 있다. 이러한 제안 중 어느 것도 아직 활성화되지 않았으며, 구현하려면 비트코인 커뮤니티의 광범위한 합의가 필요하다.

    코버넌트 연산코드가 활성화되는 데 수년이 걸릴 수 있는 반면, BitVM은 다른 접근 방식을 취한다. 어떤 업그레이드도 필요 없이 현재 비트코인 그대로 작동한다. BitVM과 그 최신 버전(BitVM2와 BitVM3)은 낙관적 모델이라는 것을 사용한다.

    작동 방식은 다음과 같다: 운영자가 L2에서 무슨 일이 일어나고 있는지에 대해 주장한다. 거짓말을 하면, 특정 창(보통 며칠에서 2주) 내에 누구나 비트코인 블록체인에서 이의를 제기할 수 있다. 이의 제기가 성공하면, 운영자는 담보로 맡긴 돈을 잃는다. 최근 연구에 따르면 BitVM3는 가블드 서킷(garbled circuit)이라는 것을 사용하여 필요한 데이터를 약 66 킬로바이트로 줄일 수 있다고 주장하지만, 설계는 아직 빠르게 변화하고 있다. 사실, 2025년 7월의 한 버전은 연구자들이 보안 결함을 발견한 후 철회해야 했다. 이러한 접근 방식은 실제 사용보다는 아직 실험적이다.

    BitVM 시스템에는 중요한 한계가 있다. 실행하기 복잡하고 적극적인 참여가 필요하다. 누군가가 실제로 사기를 감시하고 시간 창 내에 이의를 제기해야 한다. 보안은 적어도 한 명의 정직한 사람이 기꺼이 경보를 울릴 수 있어야 한다는 데 의존한다. 이는 비트코인 자체가 분쟁 제기 없이 직접 증명을 확인하는 코버넌트 기반 시스템과 근본적으로 다르다.

    핵심 차이는 누가 규칙을 시행하는지에 달려 있다. 오늘날의 연합 기반 시스템은 대부분의 서명자가 정직할 것이라고 신뢰하도록 요청한다. 코버넌트가 활성화된 시스템은 그 시행을 비트코인의 합의 규칙 자체로 이동시켜, 무효한 출금이 어떤 연합이 무엇을 시도하든 블록체인에 포함되는 것을 문자 그대로 불가능하게 만든다. 이는 주요한 보안 업그레이드가 될 것이다.

    비트코인이 실제로 이러한 변경을 채택할지, 그리고 언제 채택할지는 개발 커뮤니티에서 여전히 열린 질문이다.

    ### 라이트닝 네트워크

    비트코인의 기본 계층은 높은 보증 정산에 최적화되어 있어 작은 일상 결제를 경제적으로 비효율적으로 만든다. 높은 수수료와 제한된 블록 공간은 온체인 거래로 커피를 사는 것이 합리적이지 않다는 것을 의미한다. 라이트닝 네트워크(Lightning Network)는 작고 빈번한 결제를 메인 블록체인 밖으로 이동하여 이를 해결하려고 시도한다.

    기본 개념은 간단하다. 모든 결제를 전체 네트워크에 브로드캐스트하는 대신, 두 당사자가 사용하기 위해 양쪽 서명이 필요한 특별한 온체인 거래에 자금을 잠궈 개인적인 **결제 채널(Payment channel)**을 열 수 있다. 채널이 열리면, 그들은 자금이 어떻게 분할될 수 있는지에 대한 새 버전을 생성하여 오프체인에서 잔액을 업데이트할 수 있으며, 오래된 상태를 브로드캐스트하려는 시도를 처벌하는 암호학적 페널티와 함께 제공된다. 거래가 끝나면, 채널을 닫고 최종 잔액을 메인 블록체인에 정산할 수 있다.

    네트워크는 라우팅을 통해 더 강력해진다. 사용자는 결제하려는 모든 사람과 직접 채널이 필요하지 않다. 앨리스가 밥과 채널이 있고, 밥이 캐롤과 채널이 있으면, 앨리스는 밥을 통해 캐롤에게 결제할 수 있다. 네트워크는 중간 노드로부터 전체 결제 경로를 숨기는 라우팅 기술을 사용하여 같은 온체인 주소를 반복적으로 사용하는 것보다 더 나은 프라이버시를 제공한다. 그러나 프라이버시는 완벽하지 않다. 결제 금액, 타이밍, 네트워크 프로빙에 대한 신중한 분석은 여전히 정보를 드러낼 수 있다.

    #### 라이트닝의 강점

    라이트닝이 잘 작동할 때, 설득력 있는 이점을 제공한다. 결제가 블록 확인을 기다리는 대신 몇 초 만에 정산되어 POS 거래와 대화형 애플리케이션에 적합해진다. 거래 비용이 종종 몇 사토시 수준의 무시할 만한 금액으로 떨어져 기본 계층에서는 완전히 비실용적인 마이크로 트랜잭션을 가능하게 한다. 결제의 오프체인 특성은 중간 라우팅 노드가 암호화된 결제 데이터만 보기 때문에 같은 온체인 주소를 반복적으로 사용하는 것보다 더 나은 프라이버시를 제공한다. 양방향으로 충분한 유동성을 가진 잘 연결된 채널을 설정한 사용자에게, 라이트닝은 자금의 비수탁 통제를 유지하면서 전통적인 결제 시스템의 편리함에 접근하는 부드러운 결제 경험을 제공할 수 있다.

    #### 유동성 과제

    라이트닝 사용자는 자신의 쪽에 충분한 잔액(아웃바운드 용량)이 있어야만 결제를 보낼 수 있고, 상대방에 충분한 여유(인바운드 용량)가 있어야만 결제를 받을 수 있다. 이 유동성 제약은 라이트닝의 가장 큰 실질적인 한계이다.

    채널에 올바른 방향으로 충분한 유동성이 부족하면, 결제가 실패하거나 여러 경로로 분할해야 한다. 일부 기술적 개선이 도움이 된다: 결제가 성공률을 높이기 위해 여러 경로로 자동 분할될 수 있고, 전문 서비스 제공자가 사용자가 결제를 받는 데 필요한 인바운드 용량을 획득하는 것을 도울 수 있다. 채널 재균형은 유동성을 재분배할 수 있지만, 수수료가 들고 시간이 걸린다. 이러한 도구를 사용하더라도, 적시에 적절한 장소에 유동성을 확보하는 근본적인 과제는 남아 있다.

    #### 운영 현실

    라이트닝은 채택에 여러 장애물에 직면한다. 수신자가 오프라인이더라도 결제가 자동으로 도착하는 비트코인 기본 계층과 달리, 라이트닝은 일반적으로 사용자가 결제를 받으려면 온라인 상태여야 한다. 일부 서비스는 오프라인일 때 치팅 시도에 대해 채널을 모니터링하여 자금을 안전하게 유지할 수 있지만, 오프라인 수신 자체를 가능하게 하지는 않는다.

    일부 지갑 제공자는 오프라인일 때 결제가 도착할 수 있는 우회책을 제공하지만, 이는 종종 서비스 제공자에게 일부 수탁 또는 통제를 신뢰하는 것을 포함한다. 사용자의 경우, 채널 관리가 복잡하다. 결제를 받기 위해 인바운드 용량을 획득하고, 온라인 상태를 유지하거나 신뢰할 수 있는 서비스를 사용하고, L1과 L2 사이의 분리를 탐색해야 한다. 이 운영 오버헤드는 비기술적 사용자에게 어렵다.

    더 높은 기본 계층 수수료는 추가적인 도전을 만든다. 채널을 열고 닫는 것이 더 비싸지고, 수수료 급등 시 시간에 민감한 거래는 빠르게 확인되어야 하거나 채널이 강제 종료될 위험이 있다. 현대적인 개선으로 채널을 완전히 닫지 않고 크기를 조정하고 더 나은 수수료 관리가 가능하지만, 운영 복잡성은 남아 있다.

    상인의 경우, 통합 복잡성은 비트코인의 가격 변동성으로 인해 복합되며, 이는 결제가 온체인이든 라이트닝을 통해서든 회계와 가격 책정 문제를 만든다.

    #### 수탁 트레이드오프

    이러한 한계로 인해 많은 사용자들이 채널과 유동성을 대신 관리하는 수탁 또는 준수탁 라이트닝 지갑 서비스로 향하게 되었다. 이는 사용자 경험과 결제 신뢰성을 극적으로 개선하지만, 비트코인이 제거하도록 설계된 신뢰 요구 사항과 취약점을 다시 도입한다. 사용자는 수탁 위험에 직면한다: 자금이 동결될 수 있고, 계정이 폐쇄될 수 있고, 서비스가 실패할 수 있으며, 제공자가 자금을 잘못 관리하거나 훔치지 않을 것이라고 신뢰해야 한다. 이는 사용성과 많은 사람들을 비트코인으로 끌어들인 자기 주권 사이의 근본적인 긴장을 나타낸다.

    ### 결제를 넘어서: 데이터 레이어로서의 비트코인

    거래 처리량과 스마트 컨트랙트를 목표로 한 스케일링 솔루션을 탐구했으니, 이제 완전히 다른 범주의 비트코인 확장으로 넘어간다. 라이트닝과 L2가 온체인 활동을 줄이려고 시도하는 반면, 오디널스(Ordinals)와 인스크립션 기반 시스템은 이를 수용하여, 비트코인의 불변성과 검열 저항성을 사용하여 임의의 데이터를 블록체인에 영구적으로 앵커한다. 이는 "결제 레일로서의 비트코인"에서 "영구 저장 레이어로서의 비트코인"으로의 철학적 전환을 나타낸다.

    #### 오디널 이론

    오디널 이론(Ordinal theory)은 개별 사토시를 교환 가능한 화폐가 아닌 고유하고 수집 가능한 단위로 취급하는 방법이다. 핵심 아이디어는 간단하다: 채굴된 시점에 따라 모든 사토시에 일련번호를 부여한다. 이 번호 시스템은 특정 사토시가 거래를 통해 이동할 때 추적할 수 있게 하며, 일련번호로 달러 지폐를 추적하는 것과 유사하다.

    이 추적 시스템은 사용자가 특정 사토시에 임의의 데이터(이미지, 텍스트 또는 기타 콘텐츠)를 첨부하는 **인스크립션(Inscription)**이라는 관행을 가능하게 한다. 인스크립션된 사토시는 그 디지털 콘텐츠의 운반자가 되어, 비트코인 블록체인에서 직접 디지털 수집품이나 NFT와 유사한 것을 만든다.

    인스크립션은 2단계 과정을 사용한다. 먼저, 거래가 인스크립션될 것에 대해 커밋한다. 그런 다음, 두 번째 거래가 거래의 증인 데이터에 실제 콘텐츠를 포함하여 공개한다. 이는 외부 데이터에 대한 참조만 저장하는 대신 콘텐츠를 블록체인에 직접 저장한다.

    이 접근 방식은 비트코인에 데이터를 임베딩하는 이전 방법과 다르다. 인스크립션 데이터는 검증 후 저장하고 싶지 않은 노드가 가지치기할 수 있는 증인 공간에 있다. 아카이브 노드와 전문 인덱서는 전체 인스크립션 기록을 유지하여, 많은 노드가 가지치기한 후에도 사용자가 콘텐츠를 검색할 수 있게 한다.

    #### 비트코인 네이티브 NFT

    인스크립션된 사토시는 비트코인 네이티브 NFT처럼 기능한다: 그 특정 사토시를 이동하여 전송되는 온체인 콘텐츠와 출처를 가진 고유한 토큰. 이더리움의 NFT와의 아키텍처 차이는 주목할 만하다. 이더리움은 ERC-721과 같은 Smart Contract 표준에 의존하며, 미디어는 종종 IPFS와 같은 서비스에 오프체인으로 저장된다. 비트코인은 오디널 번호 매김을 통해 고유성을 달성하며, 미디어 바이트가 블록체인의 증인 데이터에 직접 임베딩된다. 결과는 오디널 규약을 따르는 오프체인 인덱서와 결합된 비트코인의 거래 모델에 의해 고유성이 강제되는 디지털 아티팩트이다.

    인스크립션을 전송하려면 어떤 사토시가 사용되는지 신중하게 제어해야 한다. 사용자는 거래의 입력과 출력 순서가 주변 것이 아닌 대상 인스크립션된 sat을 이동하도록 해야 한다. 전용 지갑과 특수 도구가 이 정밀한 sat 선택 기능을 제공한다. 전문가들은 실수로 병합되거나 사용되는 것을 피하기 위해 인스크립션된 sat을 별도의 주소에 보관할 것을 권장하며, 마켓플레이스는 종종 부분 서명 거래를 사용하여 사용자가 서명하기 전에 정확히 어떤 인스크립션이 전송되는지 확인할 수 있게 한다.

    #### BRC-20: 실험적 대체 가능 토큰

    오디널스가 고유한 디지털 아티팩트를 만드는 반면, BRC-20은 개념을 비트코인의 대체 가능 토큰으로 확장한다. Smart Contract를 사용하는 대신, BRC-20은 세 가지 기본 작업을 설명하는 작은 JSON 인스크립션을 사용한다: deploy(새 토큰 생성), mint(새 단위 생성), transfer(누군가에게 토큰 보내기). 커뮤니티가 운영하는 인덱서는 이러한 인스크립션의 정렬된 기록을 읽어 토큰 잔액을 재구성하여, 비트코인의 스크립팅 언어에 의한 시행이 아닌 "규약에 의한 규칙" 시스템을 만든다.

    시스템은 다음과 같이 작동한다: deploy 인스크립션은 토큰 티커(일반적으로 4글자)를 초기화하고 최대 공급량과 같은 매개변수를 설정한다. mint 인스크립션은 새 단위를 생성하고 mint 인스크립션을 소유한 사람에게 크레딧을 준다. transfer 인스크립션은 보낼 금액을 배정한다. 이더리움 토큰에서 Smart Contract가 모든 규칙을 시행하는 것과 달리, BRC-20 유효성은 인덱서가 이러한 JSON 메시지의 해석에 동의하는 것에 의존한다.

    #### 전송 과정

    BRC-20 전송은 2단계 과정을 따른다. 수표를 쓰는 것으로 생각하라: 먼저, 전송 인스크립션을 만들어 "수표"를 생성한다. 이는 보내려는 자금을 배정한다. 그런 다음, 그 인스크립션을 포함하는 거래 출력을 보내어 수신자에게 물리적으로 수표를 전달해야 한다.

    기술적 메커니즘은 다음과 같이 작동한다: 사용자는 먼저 특정 수의 토큰을 전송하려는 의도를 선언하는 JSON 객체를 인스크립션하고, BRC-20 잔액을 보유한 동일한 지갑에서 이 전송 인스크립션을 받는다. 이 단계는 인덱서의 관점에서 토큰을 "사용 가능한" 잔액에서 "전송 가능한" 풀로 이동한다. 그런 다음, 전송 인스크립션 자체를 수신자의 주소로 보내야 한다. 그 거래가 확인되면, 인덱서는 발신자의 잔액을 차감하고 수신자에게 크레딧을 준다.

    이는 오디널스와 중요한 차이를 만든다: 오디널 인스크립션을 보내는 것은 고유한 물리적 객체를 이동하는 것과 유사하지만, BRC-20 전송은 종이 흔적이 있는 장부 항목을 관리하는 것과 더 유사하게 작동한다.

    #### 논쟁

    오디널스와 인스크립션의 등장은 비트코인 커뮤니티 내에서 상당한 논쟁을 불러일으켰다. 비평가들은 임의의 데이터를 저장하는 것이 금융 거래를 위해 예약되어야 할 귀중한 블록 공간을 소비하고, 작은 사용자들을 배제하는 지속적인 수수료 압력을 만들며, P2P 전자 현금으로서의 비트코인 설계의 오용을 나타낸다고 주장한다. 지지자들은 모든 합의 유효 거래가 네트워크의 합법적인 사용이고, 인스크립션 활동이 블록 보조금이 감소함에 따라 장기 채굴자 지속 가능성에 중요한 수수료 수익을 생성하며, 사용자가 데이터를 임베딩하는 것을 방지하는 것은 비트코인의 무허가 정신과 충돌하는 논쟁적인 변경을 필요로 한다고 반박한다.

    이 긴장은 비트코인의 목적과 진화에 대한 더 깊은 질문을 반영한다: 이것이 순수한 결제 및 정산 레이어인가, 아니면 불변성과 검열 저항성의 고유한 속성을 활용하는 다양한 사용 사례를 수용할 수 있는가?

    #### 강점과 한계

    오디널스와 BRC-20은 비트코인의 기본 계층이 새로운 연산코드나 합의 변경 없이 기존 기능의 창의적 사용을 통해 디지털 자산 시스템을 지원할 수 있음을 보여준다. Taproot의 증인 공간과 비트코인의 거래 모델을 사용하여 애플리케이션 레이어 규약을 만든다. 블록체인 자체는 변경되지 않은 채로 유지된다.

    그러나 이 접근 방식에는 본질적인 한계가 있다. 컬렉션 전체 규칙, 로열티, 토큰 공급 시행은 비트코인의 스크립팅 언어 외부에 존재하며 암호학적 보장이 아닌 인덱서와 커뮤니티 규약에 의존한다. 특히 BRC-20은 명시적으로 실험적이며, 심지어 원래 창시자도 더 목적에 맞게 구축된 솔루션으로 대안 시스템을 지목한다. 두 시스템 모두 오늘날 여러 지갑과 마켓플레이스에서 작동하지만, 프로토콜 시행 메커니즘이 아닌 실제 비트코인 거래에 앵커된 사회적 규약으로 이해하는 것이 가장 좋다.
