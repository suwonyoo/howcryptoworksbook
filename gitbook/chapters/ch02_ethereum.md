# Chapter II: The Ethereum Ecosystem

## Section I: Core Concepts



=== "EN"

    Chapter I introduced Bitcoin's breakthrough: digital scarcity without centralized control. Ethereum extends this concept by making computation itself programmable and decentralized.

    This shift unlocked possibilities that didn't exist before. Decentralized exchanges let people trade tokens without intermediaries. Lending protocols let users earn interest or borrow money using only programs called **smart contracts**. NFT marketplaces create new forms of digital ownership. Notably, these applications work together seamlessly. A lending protocol can automatically interact with an exchange, creating financial products that emerge organically from the platform itself.

    But power requires complexity. Bitcoin prioritized simplicity and security above all else. Ethereum chose a different path. It replaced Bitcoin's straightforward transaction model with an account system that tracks complex application state. It developed a dynamic fee system to manage computational resources. It underwent a technical transition from proof-of-work to **proof-of-stake**. And it spawned an entire ecosystem of scaling solutions to handle real-world usage.

    Understanding Ethereum means grasping how these pieces fit together: how the fee system incentivizes efficient resource use, how proof-of-stake secures the network, and how Layer 2 solutions make the platform practical for everyday applications. This chapter will guide readers through these core mechanics, showing the engineering decisions that power today's significant experiment in decentralized computation.

=== "KO"

    Chapter I에서는 비트코인의 혁신적 돌파구인 중앙화된 통제 없이 디지털 희소성을 구현한 방식을 소개했다. 이더리움은 이 개념을 확장하여 연산(computation) 자체를 프로그래밍 가능하고 탈중앙화된 형태로 만들었다.

    이러한 전환은 이전에는 존재하지 않았던 가능성을 열었다. 탈중앙화 거래소(Decentralized Exchange, DEX)는 중개자 없이 사람들이 토큰을 거래할 수 있게 했다. 대출 프로토콜은 **스마트 컨트랙트(Smart Contract)**라 불리는 프로그램만을 사용하여 사용자가 이자를 얻거나 돈을 빌릴 수 있게 했다. NFT 마켓플레이스는 새로운 형태의 디지털 소유권을 창출했다. 주목할 점은 이러한 애플리케이션들이 서로 원활하게 협력한다는 것이다. 대출 프로토콜이 거래소와 자동으로 상호작용하여 플랫폼 자체에서 자연스럽게 금융 상품이 출현할 수 있다.

    그러나 이러한 힘에는 복잡성이 따른다. 비트코인은 단순성과 보안을 무엇보다 우선시했다. 이더리움은 다른 길을 택했다. 비트코인의 단순한 거래 모델을 복잡한 애플리케이션 상태를 추적하는 계정 시스템으로 대체했다. 연산 자원을 관리하기 위한 동적 수수료 시스템을 개발했다. 작업 증명(Proof of Work)에서 **지분 증명(Proof of Stake)**으로의 기술적 전환을 거쳤다. 그리고 실제 사용량을 처리하기 위한 스케일링 솔루션의 전체 생태계를 탄생시켰다.

    이더리움을 이해한다는 것은 이러한 조각들이 어떻게 맞물리는지 파악하는 것이다: 수수료 시스템이 어떻게 효율적인 자원 사용을 인센티브화하는지, 지분 증명이 어떻게 네트워크를 보호하는지, 그리고 레이어 2(Layer 2) 솔루션이 어떻게 플랫폼을 일상적인 애플리케이션에 실용적으로 만드는지. 이 챕터는 독자들에게 이러한 핵심 메커니즘을 안내하며, 오늘날 탈중앙화 연산의 중요한 실험을 이끄는 엔지니어링 결정들을 보여줄 것이다.

### The Ethereum Virtual Machine

=== "EN"

    At Ethereum's core lies the Ethereum Virtual Machine (EVM), a computational engine that executes code across thousands of computers (called nodes) simultaneously. Unlike Bitcoin, which primarily transfers value, Ethereum runs smart contracts, transforming the network from a simple payment system into a programmable "world computer."

    The EVM operates as a stack-based virtual machine, processing instructions like a stack of plates where you can only add or remove from the top. It uses low-level instructions called opcodes. These include operations like ADD, MULTIPLY, STORE, and CALL. When developers write smart contracts in high-level languages like Solidity or Vyper, compilers translate that code into EVM bytecode (a series of opcodes) that every Ethereum node can execute. This standardization ensures contracts behave identically whether running in New York, Singapore, or Dubai.

    What distinguishes the EVM is its combination of deterministic execution with persistent state management. Every smart contract maintains its own storage space where it saves data between transactions. When someone interacts with a contract, like swapping tokens on Uniswap or borrowing from Aave, the EVM executes the relevant bytecode, reads and writes to storage, and updates account balances. Every node independently performs these same computations and verifies they reach identical final states. This process creates **decentralized consensus**: Ethereum becomes trustworthy without requiring trust in any single party, since thousands of independently run nodes all verify the same results.

    Each operation consumes **gas**, a fee measured in computational work. Gas serves two critical purposes: it compensates node operators for executing computations and prevents spam by making every operation cost something. More complex operations require more gas, which explains why simple transfers cost less than deploying intricate smart contracts. This metering ensures no transaction runs indefinitely, mitigating resource-exhaustion attacks.

    The gas mechanism aims to price operations roughly in line with their actual resource usage. Early attacks exploited underpriced operations, prompting Ethereum to adjust opcode costs over time. These adjustments increased prices for operations that proved too cheap relative to their computational demands, reducing opportunities for denial-of-service attacks and better reflecting underlying resource costs.

    The EVM has evolved into a de facto standard extending far beyond Ethereum itself. Most **rollups** (Arbitrum, Optimism, Base) and many alternative L1s have adopted EVM compatibility, meaning they execute the same bytecode. This compatibility creates enormous value: applications like Uniswap and Aave deploy to these networks with minimal changes, while the entire infrastructure ecosystem (wallets like MetaMask, block explorers, developer tools, indexers) functions almost identically across EVM chains. New blockchains can bootstrap activity by inheriting Ethereum's mature tooling and attracting existing users and developers without requiring them to learn new paradigms. These network effects reinforce Ethereum's dominance.

    This computational model explains Ethereum's scaling challenges. Since every full node replays every transaction in order, Ethereum functions as a globally replicated computer. Protocol parameters like gas limits and block times must remain conservative enough for ordinary machines to keep up. Pushing more computation on-chain risks raising hardware requirements and eroding the decentralization that makes the network secure.

    Rollups and other scaling solutions address this constraint by moving most execution off Ethereum while using the base layer primarily for data availability and final settlement. They batch many off-chain transactions together, posting only compressed data and (in some designs) validity proofs back to Ethereum. This allows many users to share the gas cost of a single L1 transaction, dramatically lowering fees and increasing effective throughput while still inheriting Ethereum's security.

    Understanding the EVM reveals both Ethereum's power (arbitrary programmable logic secured by neutral consensus) and its limitations. The base layer remains a fully replicated machine where every computation is verified everywhere, making raw throughput fundamentally scarce. Higher scale must therefore come from layering and smarter use of that scarce resource.

=== "KO"

    이더리움의 핵심에는 **이더리움 가상 머신(Ethereum Virtual Machine, EVM)**이 있다. 이는 수천 대의 컴퓨터(노드라 불림)에서 동시에 코드를 실행하는 연산 엔진이다. 주로 가치를 전송하는 비트코인과 달리, 이더리움은 스마트 컨트랙트를 실행하여 네트워크를 단순한 결제 시스템에서 프로그래밍 가능한 "세계 컴퓨터"로 변환한다.

    EVM은 스택 기반 가상 머신(stack-based virtual machine)으로 작동하며, 맨 위에서만 추가하거나 제거할 수 있는 접시 더미처럼 명령어를 처리한다. 옵코드(opcode)라 불리는 저수준 명령어를 사용한다. 여기에는 ADD, MULTIPLY, STORE, CALL과 같은 연산이 포함된다. 개발자들이 Solidity나 Vyper와 같은 고수준 언어로 스마트 컨트랙트를 작성하면, 컴파일러가 그 코드를 모든 이더리움 노드가 실행할 수 있는 EVM 바이트코드(일련의 옵코드)로 변환한다. 이러한 표준화는 뉴욕, 싱가포르, 두바이 어디에서 실행되든 컨트랙트가 동일하게 동작하도록 보장한다.

    EVM을 구별 짓는 것은 결정론적 실행(deterministic execution)과 영속적 상태 관리(persistent state management)의 결합이다. 모든 스마트 컨트랙트는 거래 간에 데이터를 저장하는 자체 저장 공간을 유지한다. 누군가 컨트랙트와 상호작용할 때, 예를 들어 Uniswap에서 토큰을 스왑하거나 Aave에서 대출을 받을 때, EVM은 관련 바이트코드를 실행하고, 저장소에서 읽고 쓰며, 계정 잔액을 업데이트한다. 모든 노드는 독립적으로 이러한 동일한 연산을 수행하고 동일한 최종 상태에 도달하는지 검증한다. 이 과정은 **탈중앙화된 합의(decentralized consensus)**를 생성한다: 수천 개의 독립적으로 운영되는 노드가 모두 동일한 결과를 검증하기 때문에, 어떤 단일 주체도 신뢰할 필요 없이 이더리움은 신뢰성을 갖게 된다.

    각 연산은 연산 작업으로 측정되는 수수료인 **가스(Gas)**를 소비한다. 가스는 두 가지 중요한 목적을 수행한다: 연산을 실행하는 노드 운영자에게 보상하고, 모든 연산에 비용을 부과하여 스팸을 방지한다. 더 복잡한 연산은 더 많은 가스를 필요로 하며, 이것이 단순한 전송이 복잡한 스마트 컨트랙트 배포보다 비용이 적게 드는 이유이다. 이러한 계량화는 어떤 거래도 무한정 실행되지 않도록 보장하여 자원 고갈 공격을 완화한다.

    가스 메커니즘은 연산의 가격이 실제 자원 사용량과 대략적으로 일치하도록 목표한다. 초기 공격들은 저가의 연산을 악용했으며, 이로 인해 이더리움은 시간이 지남에 따라 옵코드 비용을 조정했다. 이러한 조정은 연산 요구량에 비해 너무 저렴한 것으로 판명된 연산의 가격을 인상하여 서비스 거부 공격의 기회를 줄이고 기본적인 자원 비용을 더 잘 반영하게 했다.

    EVM은 이더리움 자체를 훨씬 넘어서는 사실상의 표준으로 진화했다. 대부분의 **롤업(Rollup)**(Arbitrum, Optimism, Base)과 많은 대체 L1이 EVM 호환성을 채택하여 동일한 바이트코드를 실행한다. 이러한 호환성은 엄청난 가치를 창출한다: Uniswap이나 Aave 같은 애플리케이션이 최소한의 변경으로 이러한 네트워크에 배포될 수 있고, 전체 인프라 생태계(MetaMask와 같은 지갑, 블록 탐색기, 개발자 도구, 인덱서)가 EVM 체인 전반에서 거의 동일하게 작동한다. 새로운 블록체인들은 이더리움의 성숙한 도구를 상속받아 활동을 부트스트랩할 수 있으며, 기존 사용자와 개발자가 새로운 패러다임을 배우지 않고도 유치할 수 있다. 이러한 네트워크 효과는 이더리움의 지배력을 강화한다.

    이 연산 모델은 이더리움의 스케일링 과제를 설명한다. 모든 풀 노드가 모든 거래를 순서대로 재생해야 하므로, 이더리움은 전역적으로 복제되는 컴퓨터로 기능한다. 가스 한도와 블록 시간 같은 프로토콜 매개변수는 일반 기기가 따라잡을 수 있을 정도로 보수적으로 유지되어야 한다. 더 많은 연산을 온체인에 밀어넣으면 하드웨어 요구 사항이 높아져 네트워크를 안전하게 만드는 탈중앙화가 침식될 위험이 있다.

    롤업과 기타 스케일링 솔루션은 대부분의 실행을 이더리움 밖으로 이동시키면서 기본 레이어를 주로 데이터 가용성(data availability)과 최종 정산에 사용함으로써 이러한 제약을 해결한다. 많은 오프체인 거래를 함께 묶어 압축된 데이터와 (일부 설계에서는) 유효성 증명만 이더리움에 게시한다. 이를 통해 많은 사용자가 단일 L1 거래의 가스 비용을 공유할 수 있어 수수료가 극적으로 낮아지고 유효 처리량이 증가하면서도 이더리움의 보안을 상속받는다.

    EVM을 이해하면 이더리움의 힘(중립적 합의로 보호되는 임의의 프로그래밍 가능한 로직)과 한계가 모두 드러난다. 기본 레이어는 모든 연산이 모든 곳에서 검증되는 완전히 복제된 머신으로 남아 있어 원시 처리량이 근본적으로 희소하다. 따라서 더 높은 규모는 계층화와 그 희소한 자원의 더 스마트한 사용에서 나와야 한다.

### Ethereum's Fee System

=== "EN"

    We've seen how the EVM measures computational work in gas. Now let's examine how Ethereum's fee system actually prices that gas and how it evolved to become more user-friendly.

    Gas powers Ethereum's computational engine like fuel powers a car. Every operation, from sending ETH to a friend to executing a complex smart contract, consumes a specific amount of this computational fuel. A simple ETH transfer between regular wallets burns through 21,000 units of gas, while interacting with smart contracts requires proportionally more. Swapping tokens on Uniswap might use 150,000 gas, while deploying a new smart contract could consume millions.

    When discussing fees, Ethereum users work with specific denominations (unit sizes). While wei represents the smallest possible unit of ether (1 ETH equals 1,000,000,000,000,000,000 wei), fee discussions typically happen in **gwei** (1 gwei equals 1,000,000,000 wei, or one billionth of an ether). This makes gas prices easier to discuss. Instead of saying "the gas price is 50,000,000,000 wei," people say "50 gwei."

    A key development came with EIP-1559, which radically transformed Ethereum's protocol-level fee market. Before this August 2021 upgrade, users participated in a chaotic auction system, constantly trying to outbid each other for block space: you guessed a single gas price and hoped it was neither too low nor unnecessarily high. EIP-1559 introduced a new, more predictable default fee mechanism with two components: a dynamically adjusting **base fee** and a user-set tip. Most modern wallets use this mechanism by default. Legacy type-0 "gasPrice" transactions are still supported and behave more like the old auction, so the extra predictability is available but not strictly mandatory for all transactions.

    Users set maxFeePerGas (the absolute maximum they'll pay per unit of gas) and maxPriorityFeePerGas (an optional tip to validators for faster inclusion) when submitting transactions. The actual gas price paid is calculated as the minimum of either your maximum fee or the sum of the base fee plus your priority fee. The total transaction cost equals the gas used multiplied by this effective gas price.

    Each Ethereum block has a gas limit that defines its capacity: a maximum amount of gas that all transactions in that block can collectively consume. Since EIP-1559, the protocol targets using about half of that limit in each block and treats this target as “100% full” for pricing purposes. When demand spikes, blocks can temporarily expand up to roughly twice the target (up to the gas limit itself), creating so-called elastic blocks.

    Historically, Ethereum used a 30 million gas limit (with a 15 million gas target). Since 2024-2025, validators have gradually raised this to around 45 million, and Fusaka’s EIP-7935 standardizes a 60 million default gas limit per block in client configs. The important rule remains the same: the target gas usage is always half the current gas limit, and blocks can stretch up to roughly twice that target during congestion.

    The base fee is set algorithmically based on network congestion. When blocks use more than the target amount of gas (more than half the gas limit), the base fee rises by up to 12.5% in the next block. When they use less than the target, it falls by up to the same amount. High demand automatically increases prices; low demand decreases them through this self-balancing mechanism.

    The most significant innovation is what happens to fees. Of the total fee paid, the portion covering the base fee (gas used multiplied by the base fee) gets burned, meaning it is destroyed forever and removed from circulation, introducing deflationary pressure on ETH's supply. Only the priority fee (the tip above the base fee) goes to validators. Any unused portion of your maxFeePerGas is refunded, not paid out. This gives users a way to incentivize faster inclusion during busy periods by offering higher tips without permanently overpaying for gas.

    During periods of sustained demand, the base fee burn can exceed new ETH issuance from staking rewards, making the overall supply net deflationary (shrinking rather than growing). Higher network usage increases the burn rate, tightening supply and potentially supporting ETH's value. Since The Merge in September 2022, there have been extended periods where ETH supply has been deflationary. However, upgrades like Dencun and EIP-4844 also made L1 gas cheaper, which in turn reduced fee burn. Since 2024 there have been periods where ETH supply has turned net inflationary again despite the burn mechanism.

    EIP-1559 reduced fee volatility and dramatically improved user experience by making fees more predictable. Users can set reasonable max fees without worrying about overpaying, and wallets can estimate costs more accurately. Importantly, this change modified how fees work without altering Ethereum's consensus mechanism (the system went through this upgrade during proof-of-work and kept it after transitioning to proof-of-stake). The upgrade introduced new validation rules that all nodes must enforce, including the base fee calculation algorithm and the burning mechanism. However, it didn't address all fee market concerns. Issues like transaction censorship (validators choosing to exclude certain transactions) remain active areas of research, with proposals like inclusion lists (rules forcing validators to include certain transactions) still being developed.

=== "KO"

    EVM이 연산 작업을 가스로 측정하는 방법을 살펴보았다. 이제 이더리움의 수수료 시스템이 실제로 그 가스의 가격을 어떻게 책정하는지, 그리고 사용자 친화적으로 어떻게 진화했는지 살펴보자.

    가스는 연료가 자동차에 동력을 공급하듯이 이더리움의 연산 엔진에 동력을 공급한다. 친구에게 ETH를 보내는 것부터 복잡한 스마트 컨트랙트를 실행하는 것까지 모든 연산은 특정 양의 이 연산 연료를 소비한다. 일반 지갑 간의 단순한 ETH 전송은 21,000 단위의 가스를 사용하고, 스마트 컨트랙트와 상호작용하는 것은 비례적으로 더 많이 필요하다. Uniswap에서 토큰을 스왑하면 150,000 가스를 사용할 수 있고, 새로운 스마트 컨트랙트를 배포하면 수백만을 소비할 수 있다.

    수수료를 논의할 때, 이더리움 사용자들은 특정 단위(unit size)로 작업한다. wei가 이더(ether)의 가장 작은 단위를 나타내지만(1 ETH = 1,000,000,000,000,000,000 wei), 수수료 논의는 일반적으로 **gwei**(1 gwei = 1,000,000,000 wei, 즉 이더의 10억분의 1)로 이루어진다. 이렇게 하면 가스 가격을 더 쉽게 논의할 수 있다. "가스 가격이 50,000,000,000 wei다"라고 말하는 대신 "50 gwei"라고 말한다.

    주요 발전은 이더리움의 프로토콜 수준 수수료 시장을 근본적으로 변화시킨 EIP-1559와 함께 왔다. 2021년 8월 이 업그레이드 이전에는 사용자들이 혼란스러운 경매 시스템에 참여하여 블록 공간을 위해 끊임없이 서로를 앞지르려 했다: 단일 가스 가격을 추측하고 너무 낮지도, 불필요하게 높지도 않기를 바랐다. EIP-1559는 두 가지 구성 요소를 가진 새롭고 더 예측 가능한 기본 수수료 메커니즘을 도입했다: 동적으로 조정되는 **기본 수수료(base fee)**와 사용자가 설정하는 팁. 대부분의 현대 지갑은 기본적으로 이 메커니즘을 사용한다. 레거시 type-0 "gasPrice" 거래는 여전히 지원되며 옛 경매처럼 동작하므로, 추가적인 예측 가능성은 사용 가능하지만 모든 거래에 엄격히 의무적인 것은 아니다.

    사용자는 거래를 제출할 때 maxFeePerGas(가스 단위당 지불할 절대 최대값)와 maxPriorityFeePerGas(더 빠른 포함을 위해 검증자에게 주는 선택적 팁)를 설정한다. 실제로 지불되는 가스 가격은 최대 수수료 또는 기본 수수료와 우선 수수료의 합 중 작은 값으로 계산된다. 총 거래 비용은 사용된 가스에 이 유효 가스 가격을 곱한 것과 같다.

    각 이더리움 블록에는 용량을 정의하는 가스 한도(gas limit)가 있다: 해당 블록의 모든 거래가 집합적으로 소비할 수 있는 최대 가스량이다. EIP-1559 이후, 프로토콜은 각 블록에서 해당 한도의 약 절반을 사용하는 것을 목표로 하며 가격 책정 목적상 이 목표를 "100% 가득 참"으로 취급한다. 수요가 급증하면 블록은 목표의 약 두 배(가스 한도 자체까지)로 일시적으로 확장될 수 있어 이른바 탄력적 블록(elastic blocks)을 만든다.

    역사적으로 이더리움은 3,000만 가스 한도(1,500만 가스 목표)를 사용했다. 2024-2025년 이후로 검증자들은 이를 약 4,500만으로 점진적으로 올렸고, Fusaka의 EIP-7935는 클라이언트 구성에서 블록당 6,000만 기본 가스 한도를 표준화한다. 중요한 규칙은 동일하게 유지된다: 목표 가스 사용량은 항상 현재 가스 한도의 절반이며, 혼잡 시 블록은 해당 목표의 약 두 배까지 늘어날 수 있다.

    기본 수수료는 네트워크 혼잡도에 따라 알고리즘적으로 설정된다. 블록이 목표 가스량(가스 한도의 절반)보다 더 많이 사용하면, 기본 수수료는 다음 블록에서 최대 12.5% 상승한다. 더 적게 사용하면, 동일한 비율만큼 하락한다. 높은 수요는 자동으로 가격을 올리고, 낮은 수요는 이 자체 균형 메커니즘을 통해 가격을 낮춘다.

    가장 중요한 혁신은 수수료에 무슨 일이 일어나는가이다. 지불된 총 수수료 중 기본 수수료를 커버하는 부분(사용된 가스에 기본 수수료를 곱한 것)은 **소각(burn)**된다. 이는 영원히 파괴되어 유통에서 제거되며, ETH 공급에 디플레이션 압력을 도입한다. 우선 수수료(기본 수수료 위의 팁)만 검증자에게 간다. maxFeePerGas의 미사용 부분은 환불되지, 지불되지 않는다. 이를 통해 사용자는 바쁜 기간에 더 높은 팁을 제공하여 더 빠른 포함을 인센티브화하면서도 가스에 영구적으로 과다 지불하지 않을 수 있다.

    지속적인 수요 기간 동안 기본 수수료 소각이 스테이킹 보상에서 새로운 ETH 발행을 초과할 수 있어, 전체 공급이 순 디플레이션(성장하는 대신 축소)이 된다. 더 높은 네트워크 사용량은 소각률을 증가시켜 공급을 조이고 잠재적으로 ETH의 가치를 지지한다. 2022년 9월 더 머지(The Merge) 이후, ETH 공급이 디플레이션이었던 확장된 기간들이 있었다. 그러나 Dencun과 EIP-4844 같은 업그레이드도 L1 가스를 더 저렴하게 만들어 수수료 소각을 줄였다. 2024년 이후로 소각 메커니즘에도 불구하고 ETH 공급이 다시 순 인플레이션으로 전환된 기간들이 있었다.

    EIP-1559는 수수료 변동성을 줄이고 수수료를 더 예측 가능하게 만들어 사용자 경험을 극적으로 개선했다. 사용자는 과다 지불 걱정 없이 합리적인 최대 수수료를 설정할 수 있고, 지갑은 비용을 더 정확하게 추정할 수 있다. 중요한 것은 이 변경이 이더리움의 합의 메커니즘(시스템이 작업 증명 동안 이 업그레이드를 거쳤고 지분 증명으로 전환한 후에도 유지)을 변경하지 않고 수수료 작동 방식을 수정했다는 것이다. 업그레이드는 기본 수수료 계산 알고리즘과 소각 메커니즘을 포함하여 모든 노드가 시행해야 하는 새로운 검증 규칙을 도입했다. 그러나 모든 수수료 시장 문제를 해결하지는 못했다. 거래 검열(검증자가 특정 거래를 제외하기로 선택하는 것) 같은 문제는 여전히 활발한 연구 영역이며, 포함 목록(inclusion lists, 검증자가 특정 거래를 포함하도록 강제하는 규칙)과 같은 제안이 여전히 개발 중이다.

### How Ethereum Identifies Accounts and Assets

=== "EN"

    While understanding gas helps users manage transaction costs, knowing how Ethereum identifies accounts and assets is equally important for navigating the ecosystem effectively.

    Ethereum's account model differs fundamentally from Bitcoin's UTXO model (explained in Chapter I). Bitcoin tracks ownership through chains of unspent transaction outputs that must be consumed and recreated with each transfer. Ethereum maintains persistent accounts with balances that get updated directly. Think of it like the difference between using cash (UTXOs that get exchanged) versus a bank account (a balance that increases and decreases). This architectural choice enables the complex state management that smart contracts require, allowing contracts to store data and maintain balances across multiple transactions without the complexity of tracking individual UTXOs.

    Ethereum has two types of accounts. **Externally Owned Accounts (EOAs)** are regular user wallets controlled by private keys (like hot wallets or hardware wallets). Smart contract accounts are programmable accounts that execute code when triggered. Every participant in Ethereum (whether a person or a smart contract) has a unique address that serves as their public identifier.

    These addresses look like cryptographic gibberish: a 40 character string of numbers and letters such as 0x742d35Cc6634C0532925a3b844Bc454e4438f44e. Behind this seemingly random sequence lies mathematics. For EOAs, the address represents the last 20 bytes of a cryptographic hash (a one-way mathematical function) of the account's public key. The public key is derived from your private key, so your address is mathematically linked to your key without revealing it.

    The Ethereum Name Service (ENS) addresses this usability challenge by allowing users to register human-readable names like `alice.eth` that resolve to these hexadecimal addresses. This naming system works similarly to DNS for websites, making it easier to send funds and interact with accounts without copying and pasting long strings of characters.

    Smart contracts also receive addresses when they're deployed, generated deterministically from the deployer's address and other parameters.

    This distinction between EOAs and smart contracts is beginning to blur. Account abstraction proposals like EIP-7702 (introduced in Pectra) allow EOAs to temporarily delegate control to smart contract code, enabling features like sponsored transactions, batch operations, and improved key recovery without requiring users to migrate to entirely new account types.

    With accounts and addresses established, Ethereum's next key development was creating standards that allowed different applications to work together effectively. The most important example is the ERC-20 token standard, which created a universal language for digital assets.

    Before ERC-20, every new token was essentially a unique snowflake, requiring custom code for wallets and exchanges to support it. ERC-20 changed this by establishing a common blueprint: every compliant token must implement the same basic functions like transfer(), approve(), and balanceOf(). This seemingly simple standardization unleashed what many call the "Cambrian explosion" of DeFi.

    Suddenly, developers could build applications that worked with thousands of different tokens without writing custom code for each one. A decentralized exchange could list any ERC-20 token, a lending protocol could accept any ERC-20 as collateral, and users could seamlessly move assets between different applications. This **composability** (the ability for different protocols to work together like Lego blocks) became one of Ethereum's defining characteristics, enabling complex multi-step operations that either complete entirely or revert with no partial execution. Chapter VII explores these DeFi applications in detail.

    The ecosystem continued to evolve with additional standards: ERC-721 and ERC-1155 for NFTs (which Chapter XI explores), and various other token standards that extended Ethereum's capabilities. But all of this (the EVM, the fee market, the account system, the token standards) depends on thousands of validators agreeing on the state of the network. Ethereum's approach to achieving that agreement transformed fundamentally in 2022\.

=== "KO"

    가스를 이해하면 사용자가 거래 비용을 관리하는 데 도움이 되지만, 이더리움이 계정과 자산을 어떻게 식별하는지 아는 것도 생태계를 효과적으로 탐색하는 데 똑같이 중요하다.

    이더리움의 계정 모델은 비트코인의 UTXO 모델(Chapter I에서 설명)과 근본적으로 다르다. 비트코인은 각 전송마다 소비되고 재생성되어야 하는 미사용 트랜잭션 출력의 체인을 통해 소유권을 추적한다. 이더리움은 직접 업데이트되는 잔액을 가진 영속적 계정을 유지한다. 현금(교환되는 UTXO) 사용과 은행 계좌(증가하고 감소하는 잔액) 사용의 차이로 생각하라. 이 아키텍처 선택은 스마트 컨트랙트가 요구하는 복잡한 상태 관리를 가능하게 하여, 개별 UTXO를 추적하는 복잡성 없이 컨트랙트가 여러 거래에 걸쳐 데이터를 저장하고 잔액을 유지할 수 있게 한다.

    이더리움에는 두 가지 유형의 계정이 있다. **외부 소유 계정(Externally Owned Account, EOA)**은 개인키로 제어되는 일반 사용자 지갑이다(핫 월렛이나 하드웨어 지갑처럼). 스마트 컨트랙트 계정은 트리거될 때 코드를 실행하는 프로그래밍 가능한 계정이다. 이더리움의 모든 참여자(사람이든 스마트 컨트랙트든)는 공개 식별자 역할을 하는 고유한 주소를 가진다.

    이러한 주소는 암호학적 알아볼 수 없는 문자열처럼 보인다: 0x742d35Cc6634C0532925a3b844Bc454e4438f44e와 같은 40자리의 숫자와 문자열이다. 이 겉보기에 무작위인 순서 뒤에는 수학이 있다. EOA의 경우, 주소는 계정의 공개키에 대한 암호학적 해시(일방향 수학 함수)의 마지막 20바이트를 나타낸다. 공개키는 개인키에서 파생되므로, 주소는 키를 공개하지 않고도 수학적으로 키와 연결된다.

    **이더리움 네임 서비스(Ethereum Name Service, ENS)**는 사용자가 `alice.eth`와 같이 사람이 읽을 수 있는 이름을 등록하여 이러한 16진수 주소로 해석할 수 있게 함으로써 이 사용성 문제를 해결한다. 이 명명 시스템은 웹사이트의 DNS와 유사하게 작동하여 긴 문자열을 복사하고 붙여넣지 않고도 자금을 보내고 계정과 상호작용하기 쉽게 만든다.

    스마트 컨트랙트도 배포될 때 주소를 받으며, 배포자의 주소와 기타 매개변수에서 결정론적으로 생성된다.

    EOA와 스마트 컨트랙트 간의 이 구분은 흐려지기 시작하고 있다. EIP-7702(Pectra에서 도입됨)와 같은 계정 추상화(account abstraction) 제안은 EOA가 스마트 컨트랙트 코드에 일시적으로 제어를 위임할 수 있게 하여, 사용자가 완전히 새로운 계정 유형으로 마이그레이션하지 않고도 후원 거래, 일괄 작업, 개선된 키 복구와 같은 기능을 가능하게 한다.

    계정과 주소가 확립되면서, 이더리움의 다음 주요 발전은 서로 다른 애플리케이션이 효과적으로 협력할 수 있게 하는 표준을 만드는 것이었다. 가장 중요한 예는 디지털 자산을 위한 보편적 언어를 만든 ERC-20 토큰 표준이다.

    ERC-20 이전에는 모든 새로운 토큰이 본질적으로 독특한 눈송이여서 지갑과 거래소가 지원하기 위해 맞춤 코드가 필요했다. ERC-20은 공통 청사진을 확립하여 이를 변화시켰다: 모든 호환 토큰은 transfer(), approve(), balanceOf()와 같은 동일한 기본 함수를 구현해야 한다. 이 겉보기에 단순한 표준화는 많은 이들이 DeFi의 "캄브리아기 대폭발"이라 부르는 것을 촉발했다.

    갑자기 개발자들은 각각에 대해 맞춤 코드를 작성하지 않고도 수천 개의 다른 토큰과 작동하는 애플리케이션을 구축할 수 있게 되었다. 탈중앙화 거래소는 모든 ERC-20 토큰을 상장할 수 있고, 대출 프로토콜은 모든 ERC-20을 담보로 수락할 수 있으며, 사용자는 서로 다른 애플리케이션 간에 원활하게 자산을 이동할 수 있었다. 이 **조합 가능성(composability)**(다른 프로토콜이 레고 블록처럼 함께 작동하는 능력)은 이더리움의 정의적 특성 중 하나가 되어, 전체가 완료되거나 부분 실행 없이 되돌려지는 복잡한 다단계 작업을 가능하게 했다. Chapter VII에서 이러한 DeFi 애플리케이션을 자세히 탐구한다.

    생태계는 추가 표준으로 계속 진화했다: NFT를 위한 ERC-721과 ERC-1155(Chapter XI에서 탐구), 그리고 이더리움의 기능을 확장한 다양한 기타 토큰 표준. 그러나 이 모든 것(EVM, 수수료 시장, 계정 시스템, 토큰 표준)은 네트워크 상태에 동의하는 수천 명의 검증자에 달려 있다. 이 합의를 달성하는 이더리움의 접근 방식은 2022년에 근본적으로 변화했다.

## Section II: Ethereum Consensus and Staking



=== "EN"

    This section explores how Ethereum reaches agreement on the state of its blockchain. While Bitcoin uses Proof of Work to achieve consensus (as explained in Chapter I), Ethereum transitioned to a fundamentally different approach called Proof of Stake. Understanding this shift requires first examining how Ethereum's upgrade process works.

=== "KO"

    이 섹션에서는 이더리움이 블록체인 상태에 대해 어떻게 합의에 도달하는지 탐구한다. 비트코인이 합의를 달성하기 위해 Proof of Work을 사용하는 반면(Chapter I에서 설명), 이더리움은 지분 증명(Proof of Stake)이라 불리는 근본적으로 다른 접근 방식으로 전환했다. 이 전환을 이해하려면 먼저 이더리움의 업그레이드 프로세스가 어떻게 작동하는지 살펴봐야 한다.

### How Ethereum Evolves: The EIP Process

=== "EN"

    That 2022 transformation happened through Ethereum's unique governance model. Unlike traditional software where a company decides what features to build, Ethereum evolves through a public, community-driven process centered on **Ethereum Improvement Proposals (EIPs)**. These formal proposals move through stages (Draft, Review, Last Call, and Final) with extensive technical review, security analysis, and testing on networks like Sepolia and Holesky before deployment to mainnet.

    Core EIPs modify the protocol itself, requiring coordinated hard forks (backwards-incompatible protocol changes). ERC (Ethereum Request for Comment) proposals define application-level standards like ERC-20 tokens that make different applications compatible. Major upgrades bundle multiple EIPs together with names like Shapella (staking withdrawals), Dencun (blob transactions via EIP-4844), and Pectra (account delegation via EIP-7702).

    This process intentionally prioritizes caution over speed. Changes to a system securing hundreds of billions of dollars require widespread coordination among thousands of node operators and thorough vetting to prevent catastrophic bugs. You will see EIP numbers referenced throughout this chapter. They represent the careful evolution that makes Ethereum both stable and capable of major transformations.

=== "KO"

    그 2022년 변혁은 이더리움의 독특한 거버넌스 모델을 통해 일어났다. 회사가 어떤 기능을 구축할지 결정하는 전통적인 소프트웨어와 달리, 이더리움은 **이더리움 개선 제안(Ethereum Improvement Proposal, EIP)**을 중심으로 한 공개적이고 커뮤니티 주도적인 프로세스를 통해 진화한다. 이러한 공식 제안은 초안(Draft), 검토(Review), 최종 호출(Last Call), 최종(Final) 단계를 거치며 메인넷에 배포되기 전에 Sepolia와 Holesky와 같은 네트워크에서 광범위한 기술 검토, 보안 분석, 테스트를 거친다.

    코어 EIP는 프로토콜 자체를 수정하여 조율된 하드 포크(이전 버전과 호환되지 않는 프로토콜 변경)를 필요로 한다. ERC(Ethereum Request for Comment) 제안은 서로 다른 애플리케이션을 호환 가능하게 만드는 ERC-20 토큰과 같은 애플리케이션 수준 표준을 정의한다. 주요 업그레이드는 Shapella(스테이킹 출금), Dencun(EIP-4844를 통한 블롭 거래), Pectra(EIP-7702를 통한 계정 위임)와 같은 이름으로 여러 EIP를 함께 번들링한다.

    이 프로세스는 의도적으로 속도보다 신중함을 우선시한다. 수천억 달러를 보호하는 시스템에 대한 변경은 수천 명의 노드 운영자 간의 광범위한 조율과 치명적인 버그를 방지하기 위한 철저한 검증이 필요하다. 이 챕터 전반에 걸쳐 EIP 번호가 참조되는 것을 볼 것이다. 이들은 이더리움을 안정적이면서도 주요 변혁이 가능하게 만드는 신중한 진화를 나타낸다.

### The Great Transition: From Mining to Staking

=== "EN"

    The most significant transformation to emerge from this process was The Merge. September 15, 2022, marked a watershed moment in Ethereum history. On that day, The Merge was completed, a years-long engineering effort that transitioned the network from energy-intensive mining to a proof-of-stake system. The upgrade represented a reimagining of how Ethereum secures itself.

    The transformation was unprecedented in scope. Bitcoin miners race to solve computational puzzles using large amounts of electricity. Ethereum's new system relies instead on **validators** who lock up their own ETH as collateral. These validators earn rewards for honest behavior and face severe penalties for malicious actions. The result? Ethereum reduced its energy consumption by over 99.9% while maintaining comparable security guarantees.

    Beyond energy efficiency, The Merge restructured Ethereum's architecture itself: it separated Ethereum's execution layer (which processes transactions) from its consensus layer (which decides on block order and finality). This separation, embodied in the Beacon Chain, created a foundation for future scalability improvements that would have been impossible under the old mining system.

=== "KO"

    이 프로세스에서 나온 가장 중요한 변혁은 더 머지(The Merge)였다. 2022년 9월 15일은 이더리움 역사에서 분수령이 되는 순간이었다. 그날 더 머지가 완료되었으며, 이는 에너지 집약적인 채굴에서 지분 증명 시스템으로 네트워크를 전환한 수년간의 엔지니어링 노력이었다. 이 업그레이드는 이더리움이 스스로를 보호하는 방식의 재구상을 나타냈다.

    그 변혁은 범위에서 전례가 없었다. 비트코인 채굴자들은 대량의 전기를 사용하여 연산 퍼즐을 풀기 위해 경쟁한다. 이더리움의 새로운 시스템은 대신 자신의 ETH를 담보로 잠그는 **검증자(validator)**에 의존한다. 이 검증자들은 정직한 행동에 대해 보상을 받고 악의적인 행동에 대해 심각한 처벌을 받는다. 결과적으로? 이더리움은 비슷한 수준의 보안 보장을 유지하면서 에너지 소비를 99.9% 이상 줄였다.

    에너지 효율성을 넘어, 더 머지는 이더리움의 아키텍처 자체를 재구성했다: 이더리움의 실행 레이어(거래를 처리하는 부분)를 합의 레이어(블록 순서와 최종성을 결정하는 부분)에서 분리했다. 비콘 체인(Beacon Chain)에 구현된 이 분리는 이전 채굴 시스템에서는 불가능했을 미래의 확장성 개선을 위한 기반을 만들었다.

### How Ethereum Achieves Consensus

=== "EN"

    Ethereum's proof-of-stake system operates like a carefully choreographed dance, with thousands of validators working together in precise intervals to maintain network security.

    Time in Ethereum moves in precise intervals: every 12 seconds marks a slot, and every 32 slots (about 6.4 minutes) forms an epoch. In each slot, the protocol randomly selects one validator to propose a new block using a cryptographic seed derived from the previous epoch, while hundreds of others provide attestations, which are cryptographic votes confirming that the proposed block follows all the rules.

    The path to **finality** (the point where a transaction becomes irreversible) follows a two step process. First, a block becomes justified when it receives attestations from at least two thirds of validators. Then, in the following epoch, if another supermajority confirms that justification, the block becomes finalized. This process typically takes about 12.8 minutes. After finalization, reversing a transaction would require coordinated attacks triggering severe financial penalties called **slashing**, which scale with the number of validators involved.

    Becoming a validator requires staking a minimum of 32 ETH to activate, but since the Pectra hard fork (EIP-7251), validators can now scale their effective balance (the amount of staked ETH that counts toward their voting power and rewards) up to 2048 ETH, reshaping the staking landscape. While 32 ETH remains the activation threshold per validator key, operators can now attach additional ETH to a single validator to increase its attestation weight, rewards, and penalties proportionally. This reduces operational overhead through fewer keys and attestations but concentrates stake and potential slashing risk per validator. The change reduces the incentive to run many 32 ETH validators. Large operators can consolidate into fewer, higher-stake validators, while solo stakers can continue running standard 32 ETH setups.

    The system achieves efficiency through advanced cryptographic techniques. Ethereum uses BLS signatures, which allow thousands of individual validator signatures to be compressed into a single, compact proof. Instead of processing thousands of separate attestations, the network can verify the collective opinion of all validators with minimal computational overhead.

    Security comes through slashing, the system's mechanism for punishing malicious behavior. Validators who break the rules (like proposing conflicting blocks or making contradictory attestations) face financial penalties. The base penalty is intentionally small: on the order of hundredths of an ETH for a 32 ETH validator and around half an ETH for a fully "scaled-up" 2048 ETH validator under the new Pectra rules. This means isolated mistakes aren't catastrophic. But correlated attacks are punished much more severely. When many validators misbehave together, a correlation penalty scales up with the share of the validator set that's slashed, and large coordinated attacks can destroy a substantial fraction of each participant's stake. The protocol also includes inactivity leaks that gradually drain the balances of offline validators during long network partitions, allowing the remaining active validators to regain a supermajority and finalize the chain.

=== "KO"

    이더리움의 지분 증명 시스템은 신중하게 안무된 춤처럼 운영되며, 수천 명의 검증자가 네트워크 보안을 유지하기 위해 정확한 간격으로 함께 작동한다.

    이더리움에서 시간은 정확한 간격으로 움직인다: 12초마다 슬롯(slot)을 표시하고, 32개의 슬롯(약 6.4분)마다 에포크(epoch)를 형성한다. 각 슬롯에서 프로토콜은 이전 에포크에서 파생된 암호학적 시드를 사용하여 새 블록을 제안할 검증자 한 명을 무작위로 선택하고, 수백 명의 다른 검증자들은 제안된 블록이 모든 규칙을 따르는지 확인하는 암호학적 투표인 증명(attestation)을 제공한다.

    **최종성(finality)**(거래가 되돌릴 수 없게 되는 지점)으로 가는 경로는 2단계 과정을 따른다. 먼저 블록이 검증자의 최소 3분의 2로부터 증명을 받으면 정당화(justified)된다. 그런 다음 다음 에포크에서 또 다른 슈퍼 다수가 그 정당화를 확인하면 블록은 확정(finalized)된다. 이 과정은 일반적으로 약 12.8분이 걸린다. 확정 후 거래를 되돌리려면 **슬래싱(slashing)**이라 불리는 심각한 재정적 처벌을 촉발하는 조율된 공격이 필요하며, 이 처벌은 관련된 검증자 수에 따라 확대된다.

    검증자가 되려면 활성화를 위해 최소 32 ETH를 스테이킹해야 하지만, Pectra 하드 포크(EIP-7251) 이후로 검증자는 이제 유효 잔액(투표 권한과 보상에 반영되는 스테이킹된 ETH의 양)을 최대 2048 ETH까지 확장할 수 있어 스테이킹 환경을 재편하고 있다. 32 ETH는 검증자 키당 활성화 임계값으로 유지되지만, 운영자는 이제 증명 가중치, 보상, 처벌을 비례적으로 증가시키기 위해 단일 검증자에 추가 ETH를 부착할 수 있다. 이는 더 적은 키와 증명을 통해 운영 오버헤드를 줄이지만 검증자당 스테이크와 잠재적 슬래싱 위험을 집중시킨다. 이 변경은 많은 32 ETH 검증자를 운영할 인센티브를 줄인다. 대형 운영자는 더 적고 더 높은 스테이크의 검증자로 통합할 수 있고, 솔로 스테이커는 표준 32 ETH 설정을 계속 운영할 수 있다.

    시스템은 고급 암호학적 기술을 통해 효율성을 달성한다. 이더리움은 BLS 서명을 사용하여 수천 개의 개별 검증자 서명을 단일의 컴팩트한 증명으로 압축할 수 있다. 수천 개의 별도 증명을 처리하는 대신, 네트워크는 최소한의 연산 오버헤드로 모든 검증자의 집합적 의견을 검증할 수 있다.

    보안은 악의적인 행동을 처벌하는 시스템 메커니즘인 슬래싱을 통해 달성된다. 규칙을 위반하는 검증자(충돌하는 블록을 제안하거나 모순되는 증명을 하는 것과 같은)는 재정적 처벌을 받는다. 기본 처벌은 의도적으로 작다: 32 ETH 검증자의 경우 수백분의 1 ETH 정도이고, 새로운 Pectra 규칙에 따라 완전히 "스케일업된" 2048 ETH 검증자의 경우 약 0.5 ETH이다. 이는 고립된 실수가 치명적이지 않다는 것을 의미한다. 그러나 상관 공격은 훨씬 더 심각하게 처벌된다. 많은 검증자가 함께 잘못 행동하면, 상관 처벌(correlation penalty)이 슬래싱된 검증자 집합의 비율에 따라 확대되며, 대규모 조율된 공격은 각 참가자 스테이크의 상당 부분을 파괴할 수 있다. 프로토콜은 또한 긴 네트워크 분할 동안 오프라인 검증자의 잔액을 점진적으로 고갈시키는 비활동 유출(inactivity leak)을 포함하여, 남은 활성 검증자가 슈퍼 다수를 회복하고 체인을 확정할 수 있게 한다.

### Liquid Staking

=== "EN"

    The capital requirements described above shaped the evolution of Ethereum's staking ecosystem. Stakers face a difficult choice: lock up tokens to help secure the network and earn rewards, or keep them liquid for other uses. Even though withdrawals became possible after the Shapella upgrade, exiting your stake isn't instant. You have to wait in a queue that can take days or even longer when the network is busy. The problem is clear: staked capital becomes locked up and can't be used in the broader decentralized finance (DeFi) ecosystem. You're forced to choose between earning staking yields and having the flexibility to lend, trade, or provide liquidity with your assets.

    Liquid staking protocols solve this problem by collecting deposits from many users, staking them with network validators, and issuing tradeable **Liquid Staking Tokens (LSTs)** that represent your share of the staked pool plus earned rewards. This means you earn staking yields while holding a liquid, transferable token usable across DeFi protocols.

    Two approaches dominate the space:

    Lido is by far the largest LST provider, controlling over 85% of the market as of early 2026 and managing roughly 25% of all staked ETH. It issues stETH, a rebasing token whose balance automatically grows daily as staking rewards accumulate. In other words, the number of tokens in your wallet changes over time rather than each token’s price increasing. Lido uses a curated set of professional node operators (recently expanded to include permissionless participation) and relies on a committee that reports daily balance updates from the beacon chain to power the rebasing mechanism. This approach enabled Lido to scale rapidly and dominate the LST market.

    Rocket Pool takes a more decentralized path. It's the second largest protocol with approximately 5% market share as of early 2026, enabling thousands of independent operators to run validators. It issues rETH, which works differently. Your token balance stays constant, but its exchange rate against ETH appreciates as rewards accumulate. The protocol allows operators to create validators with as little as 8 ETH of their own capital, with the rest coming from user deposits, making validator participation more accessible while maintaining permissionless entry.

    Liquid staking offers clear advantages, but it also comes with risks you need to understand. Lido's dominance raises serious questions about protocol governance and network resilience. If too much staking power concentrates in one provider, it could threaten the security and decentralization of the underlying network. Smart contract vulnerabilities are another pressing concern. Today, most validator withdrawal credentials are managed off-chain, which limits a protocol bug's ability to directly drain validator balances. However, bugs can still break accounting, misroute rewards, or block withdrawals. If future upgrades shift more withdrawal control on-chain, the blast radius of such bugs could grow further.

    Validator penalties from misbehavior or technical failures affect everyone in the pool. Finally, liquidity risk can surface during periods of market stress. LST tokens might trade below their true value (we saw this with stETH discounts in 2022), which creates potential losses if you need to exit your position quickly.

    With consensus secured and staking economics established, Ethereum's remaining bottleneck is scale; hence the rise of Layer 2 rollups.

=== "KO"

    위에서 설명한 자본 요구 사항은 이더리움 스테이킹 생태계의 진화를 형성했다. 스테이커들은 어려운 선택에 직면한다: 네트워크 보안에 도움을 주고 보상을 얻기 위해 토큰을 잠그거나, 다른 용도를 위해 유동성을 유지하거나. Shapella 업그레이드 후 출금이 가능해졌지만, 스테이크를 종료하는 것은 즉각적이지 않다. 대기열에서 기다려야 하며, 네트워크가 바쁠 때는 며칠 이상 걸릴 수 있다. 문제는 명확하다: 스테이킹된 자본은 잠기게 되어 더 넓은 탈중앙화 금융(DeFi) 생태계에서 사용될 수 없다. 스테이킹 수익을 얻는 것과 자산으로 대출, 거래, 유동성 제공의 유연성을 갖는 것 사이에서 선택을 강요받는다.

    **유동 스테이킹(Liquid Staking)** 프로토콜은 많은 사용자로부터 예치금을 수집하고, 네트워크 검증자에 스테이킹한 다음, 스테이킹된 풀의 지분과 획득한 보상을 나타내는 거래 가능한 **유동 스테이킹 토큰(Liquid Staking Token, LST)**을 발행하여 이 문제를 해결한다. 이는 DeFi 프로토콜 전반에서 사용 가능한 유동적이고 양도 가능한 토큰을 보유하면서 스테이킹 수익을 얻을 수 있다는 것을 의미한다.

    두 가지 접근 방식이 이 공간을 지배한다:

    Lido는 가장 큰 LST 제공자로, 2026년 초 기준 시장의 85% 이상을 통제하며 모든 스테이킹된 ETH의 약 25%를 관리한다. stETH를 발행하는데, 이는 스테이킹 보상이 축적됨에 따라 잔액이 매일 자동으로 증가하는 리베이싱(rebasing) 토큰이다. 다시 말해, 각 토큰의 가격이 증가하는 것이 아니라 지갑에 있는 토큰 수가 시간이 지남에 따라 변한다. Lido는 선별된 전문 노드 운영자 세트(최근 무허가 참여를 포함하도록 확장됨)를 사용하고, 리베이싱 메커니즘에 동력을 공급하기 위해 비콘 체인의 일일 잔액 업데이트를 보고하는 위원회에 의존한다. 이 접근 방식은 Lido가 빠르게 확장하고 LST 시장을 지배할 수 있게 했다.

    Rocket Pool은 더 탈중앙화된 길을 택한다. 2026년 초 기준 약 5%의 시장 점유율로 두 번째로 큰 프로토콜이며, 수천 명의 독립 운영자가 검증자를 운영할 수 있게 한다. rETH를 발행하는데, 이는 다르게 작동한다. 토큰 잔액은 일정하게 유지되지만, 보상이 축적됨에 따라 ETH에 대한 환율이 상승한다. 프로토콜은 운영자가 자신의 자본 8 ETH만으로 검증자를 생성할 수 있게 하며, 나머지는 사용자 예치금에서 나와 무허가 진입을 유지하면서 검증자 참여를 더 접근 가능하게 만든다.

    유동 스테이킹은 명확한 장점을 제공하지만, 이해해야 할 위험도 함께 온다. Lido의 지배력은 프로토콜 거버넌스와 네트워크 복원력에 대한 심각한 질문을 제기한다. 너무 많은 스테이킹 파워가 한 제공자에게 집중되면, 기본 네트워크의 보안과 탈중앙화를 위협할 수 있다. 스마트 컨트랙트 취약성은 또 다른 절박한 우려 사항이다. 현재 대부분의 검증자 출금 자격 증명은 오프체인에서 관리되어 프로토콜 버그가 검증자 잔액을 직접 빼내는 능력을 제한한다. 그러나 버그는 여전히 회계를 깨뜨리고, 보상을 잘못 경로 지정하거나, 출금을 차단할 수 있다. 향후 업그레이드가 더 많은 출금 제어를 온체인으로 이동시키면, 그러한 버그의 영향 범위는 더 커질 수 있다.

    잘못된 행동이나 기술적 실패로 인한 검증자 처벌은 풀의 모든 사람에게 영향을 미친다. 마지막으로, 유동성 위험은 시장 스트레스 기간 동안 나타날 수 있다. LST 토큰이 실제 가치 이하로 거래될 수 있으며(2022년 stETH 할인에서 이를 봤다), 이는 빠르게 포지션을 종료해야 할 때 잠재적 손실을 만든다.

    합의가 보장되고 스테이킹 경제학이 확립되면서, 이더리움의 남은 병목 현상은 규모이다; 따라서 레이어 2 롤업의 부상이다.

## Section III: Ethereum Scaling and Layer 2 Solutions



=== "EN"



=== "KO"



### The Rollup Revolution

=== "EN"

    Recall from the EVM section that every full node must process every transaction. This design choice, essential for decentralization and security, constrains throughput to what a typical node on consumer hardware can verify and propagate within a 12-second slot. The result is on the order of a few dozen simple transactions per second, far too slow for mainstream adoption. A single popular application can congest the entire network, sending gas fees soaring to hundreds of dollars per transaction during periods of extreme demand.

    The solution cannot be to simply "make blocks bigger" or "process transactions faster." Raising gas limits or shortening block times would increase bandwidth, CPU, and storage requirements, quietly pushing slower nodes off the network. This would concentrate validation in the hands of fewer, more powerful operators and undermine decentralization. Ethereum's core developers therefore prioritize keeping node requirements low enough that anyone with reasonably affordable consumer hardware and a decent internet connection can participate in securing the network.

    Rollups address this constraint by moving most computation off Layer 1 while anchoring security to Ethereum. Transactions execute on a separate Layer 2 chain that runs much faster and cheaper because it doesn't require every Ethereum node to re-run every step. The rollup then posts compressed transaction data (and, depending on the design, proofs or fraud-detection mechanisms) back to Layer 1, which provides data availability, dispute resolution, and final settlement.

    This security inheritance only works fully when data availability lives on Ethereum itself. For a rollup to be truly secure, anyone must be able to reconstruct its state from data posted to Layer 1\. If transaction data disappears or becomes unavailable, users can't prove they own their funds or challenge invalid state transitions. Rollups that use external data availability (called validiums, since they validate transactions but store data elsewhere) sacrifice this guarantee and require additional trust assumptions.

    A common criticism of the rollup scaling approach claims that L2s extract value from Ethereum by launching their own tokens, pulling investor attention and capital away from ETH. The concern breaks down into two main issues. First, users end up speculating on L2 tokens rather than ETH itself. Second, valuable revenues from **sequencers** (the entities that order and batch transactions on L2s) and transaction fees get captured at the rollup level instead of flowing back to Ethereum's base layer.

    However, rollups that post their data to Ethereum still generate L1 fees and contribute to ETH's deflationary burn mechanism, especially as L2 usage grows. The choice of gas token matters here: some rollups denominate user gas in a native L2 token, others in ETH, but in all cases sequencers ultimately need to acquire ETH to pay for L1 data availability. This forces part of the system's revenue back into ETH demand. Additionally, factors like sequencer decentralization and how tightly a rollup's economics couple to Ethereum's settlement layer all determine whether value flows back to ETH holders or gets mostly captured at the L2 level.

    The rollup ecosystem has evolved into two primary approaches, each making different compromises:

    #### Optimistic Rollups: Trust but Verify

    Optimistic rollups, exemplified by Arbitrum and Optimism, embrace an "innocent until proven guilty" philosophy. They optimistically assume all transactions are valid and immediately post new state updates to Layer 1\. This assumption allows for fast execution and low costs, but it comes with an important caveat: a challenge period of roughly seven days during which anyone can submit a **fraud proof** if they detect invalid transactions.

    This security model balances speed against finality. While users enjoy fast, cheap transactions on the rollup itself, withdrawing funds back to mainnet requires patience. The seven day waiting period ensures that any fraudulent activity can be detected and reversed, but it means that optimistic rollups aren't ideal for users who need immediate access to their funds on Layer 1\.

    However, the market has responded to this friction with third-party fast withdrawal services. Liquidity providers like Hop Protocol and Across Protocol will front users their funds on Layer 1 immediately, charging a fee for the convenience. These providers assume the risk during the challenge period. If a fraud proof invalidates the transaction, they bear the loss. Users who need speed pay a premium; those willing to wait can withdraw for free.

    #### ZK Rollups: Mathematical Certainty

    ZK rollups, including Starknet, zkSync, and Scroll, take an entirely different approach. Instead of assuming validity and waiting for challenges, they use **validity proofs** (advanced cryptographic techniques that mathematically prove the correctness of every batch of transactions). These rollups first commit transaction data to Layer 1, then submit a proof that validates the entire batch.

    These zero-knowledge proofs are advanced mathematical techniques. They allow a rollup to prove that thousands of transactions were processed correctly without requiring Layer 1 to re-execute them. The proof provides strong cryptographic certainty about the validity of an entire batch (though like all cryptography, this relies on certain mathematical assumptions being sound).

    Different ZK rollups use different proof systems, each with distinct properties. Scroll uses pure SNARKs, generating tiny proofs of just a few hundred bytes that minimize L1 costs, but requiring a trusted setup where initial parameters must be securely generated and destroyed, like destroying the mold after casting a master key so nobody can secretly mint more keys later. Starknet uses STARKs, producing much larger proofs of hundreds of kilobytes, but offering stronger security properties: no trusted setup, transparency, and better resistance to potential future quantum computers. zkSync takes a hybrid approach, generating STARK proofs internally for security, then wrapping them in a SNARK for cost-efficient on-chain verification. This still requires a trusted setup for the SNARK wrapper.

    The advantage over optimistic rollups is compelling. ZK rollups avoid the week long withdrawal delays that plague optimistic systems. Once a validity proof is verified on Layer 1, users can access their funds without any challenge period (though they still wait for proof generation and verification, which typically takes minutes to hours depending on system load). However, this security comes at a cost. The cryptographic machinery required to generate these proofs is more complex and computationally intensive than optimistic approaches.

    #### Additional Rollup Considerations

    Beyond the core differences between optimistic and ZK approaches, several other dimensions matter when evaluating rollups.

    In practice, most rollups currently rely on centralized sequencers to achieve the fast confirmations users expect. Unlike Ethereum mainnet, which distributes block proposal across thousands of validators, these rollups use a single entity to order transactions and produce blocks. While this represents a temporary engineering choice rather than a permanent design, it introduces potential censorship risks and single points of failure. Leading rollups are actively developing solutions to eliminate sequencer centralization while preserving performance. Shared sequencing networks distribute ordering responsibility across multiple parties, creating redundancy without sacrificing speed. Sequencer rotation systems periodically change which entity handles transaction ordering, preventing long-term control by any single party. Inclusion lists require sequencers to include certain transactions within specified timeframes, making censorship more difficult. Preconfirmations allow sequencers to make soft commitments about transaction inclusion before formal consensus, improving user experience while maintaining reversion options through slashing mechanisms and dispute windows.

    Proof systems continue to evolve in maturity and coverage. Many ZK-rollups still operate with "training wheels" (additional security mechanisms that can pause or override the system during early phases while the technology matures). Optimistic rollups depend on robust fault proof systems that are still being refined and battle-tested. Fee structures combine L2 execution costs with L1 data availability and inclusion fees. Additionally, rollups operate in different data availability modes. True rollups post all data to Ethereum, while validiums use external data availability or hybrid approaches that trade cost savings against stronger trust requirements.

    Not all rollups prioritize decentralization equally. Some projects deliberately embrace centralized architectures to achieve consumer-app-like responsiveness. MegaETH, for example, uses a single active sequencer and 10-millisecond “miniblocks” to target millisecond-level latency and on the order of 100,000 transactions per second. This design accepts risks like single points of failure and potential censorship in exchange for high speed. Such approaches reveal the inherent tensions in blockchain design: decentralization, security, and performance exist in constant competition, with different applications requiring different balances.

=== "KO"

    EVM 섹션에서 모든 풀 노드가 모든 거래를 처리해야 한다는 것을 상기하라. 탈중앙화와 보안에 필수적인 이 설계 선택은 일반적인 노드가 12초 슬롯 내에서 검증하고 전파할 수 있는 것으로 처리량을 제한한다. 결과는 초당 수십 개의 단순한 거래 정도로, 대중적 채택에는 너무 느리다. 단일 인기 애플리케이션이 전체 네트워크를 혼잡하게 만들 수 있으며, 극단적인 수요 기간에는 가스 수수료가 거래당 수백 달러까지 치솟는다.

    해결책은 단순히 "블록을 더 크게" 또는 "거래를 더 빠르게" 처리하는 것이 아니다. 가스 한도를 높이거나 블록 시간을 단축하면 대역폭, CPU, 스토리지 요구 사항이 증가하여 조용히 느린 노드를 네트워크에서 밀어낸다. 이는 검증을 더 적고 더 강력한 운영자의 손에 집중시켜 네트워크를 안전하게 만드는 탈중앙화를 약화시킨다. 따라서 이더리움 핵심 개발자들은 합리적으로 저렴한 소비자 하드웨어와 적절한 인터넷 연결을 가진 누구나 네트워크 보안에 참여할 수 있을 정도로 노드 요구 사항을 낮게 유지하는 것을 우선시한다.

    롤업은 대부분의 연산을 레이어 1 밖으로 이동시키면서 이더리움에 보안을 고정함으로써 이 제약을 해결한다. 거래는 모든 이더리움 노드가 모든 단계를 재실행할 필요가 없기 때문에 훨씬 빠르고 저렴하게 실행되는 별도의 레이어 2 체인에서 실행된다. 그런 다음 롤업은 압축된 거래 데이터(그리고 설계에 따라 증명이나 사기 탐지 메커니즘)를 레이어 1로 다시 게시하여 데이터 가용성, 분쟁 해결, 최종 정산을 제공한다.

    이 보안 상속은 데이터 가용성이 이더리움 자체에 있을 때만 완전히 작동한다. 롤업이 진정으로 안전하려면, 누구나 레이어 1에 게시된 데이터에서 그 상태를 재구성할 수 있어야 한다. 거래 데이터가 사라지거나 사용할 수 없게 되면, 사용자는 자금을 소유하고 있음을 증명하거나 유효하지 않은 상태 전환에 이의를 제기할 수 없다. 외부 데이터 가용성을 사용하는 롤업(거래를 검증하지만 데이터를 다른 곳에 저장하기 때문에 validium이라 불림)은 이 보장을 희생하고 추가적인 신뢰 가정을 필요로 한다.

    롤업 스케일링 접근 방식에 대한 일반적인 비판은 L2가 자체 토큰을 출시하여 이더리움에서 가치를 추출하고 투자자의 관심과 자본을 ETH에서 멀어지게 한다고 주장한다. 우려는 두 가지 주요 문제로 나뉜다. 첫째, 사용자들이 ETH 자체가 아닌 L2 토큰에 투기하게 된다. 둘째, **시퀀서(sequencer)**(L2에서 거래를 정렬하고 묶는 주체)와 거래 수수료에서 나오는 가치 있는 수익이 이더리움의 기본 레이어로 흘러가는 대신 롤업 수준에서 포착된다.

    그러나 데이터를 이더리움에 게시하는 롤업은 여전히 L1 수수료를 생성하고 ETH의 디플레이션 소각 메커니즘에 기여하며, 특히 L2 사용량이 증가함에 따라 그렇다. 가스 토큰의 선택이 여기서 중요하다: 일부 롤업은 사용자 가스를 네이티브 L2 토큰으로 표시하고, 다른 것들은 ETH로 하지만, 모든 경우에 시퀀서는 궁극적으로 L1 데이터 가용성을 지불하기 위해 ETH를 획득해야 한다. 이는 시스템 수익의 일부를 ETH 수요로 다시 강제한다. 추가로, 시퀀서 탈중앙화와 롤업의 경제가 이더리움의 정산 레이어에 얼마나 긴밀하게 결합되는지와 같은 요소들이 가치가 ETH 보유자에게 흘러가는지 아니면 대부분 L2 수준에서 포착되는지를 결정한다.

    롤업 생태계는 두 가지 주요 접근 방식으로 진화했으며, 각각 다른 타협점을 가진다:

    #### 낙관적 롤업: 신뢰하되 검증하라

    Arbitrum과 Optimism으로 대표되는 **낙관적 롤업(Optimistic Rollup)**은 "유죄가 입증될 때까지 무죄"라는 철학을 채택한다. 모든 거래가 유효하다고 낙관적으로 가정하고 즉시 새로운 상태 업데이트를 레이어 1에 게시한다. 이 가정은 빠른 실행과 낮은 비용을 허용하지만, 중요한 단서가 있다: 누구나 유효하지 않은 거래를 감지하면 **사기 증명(fraud proof)**을 제출할 수 있는 대략 7일의 이의 제기 기간이 있다.

    이 보안 모델은 속도와 최종성 사이의 균형을 맞춘다. 사용자는 롤업 자체에서 빠르고 저렴한 거래를 즐기지만, 메인넷으로 자금을 인출하려면 인내심이 필요하다. 7일 대기 기간은 모든 사기 행위가 감지되고 되돌려질 수 있도록 보장하지만, 이는 낙관적 롤업이 레이어 1에서 자금에 즉각적으로 접근해야 하는 사용자에게는 이상적이지 않다는 것을 의미한다.

    그러나 시장은 이 마찰에 대해 제3자 빠른 인출 서비스로 대응했다. Hop Protocol과 Across Protocol과 같은 유동성 제공자가 레이어 1에서 사용자에게 즉시 자금을 선불해주고 그 편의를 위해 수수료를 부과한다. 이 제공자들은 이의 제기 기간 동안 위험을 부담한다. 사기 증명이 거래를 무효화하면, 그들이 손실을 감당한다. 속도가 필요한 사용자는 프리미엄을 지불하고, 기다릴 의향이 있는 사용자는 무료로 인출할 수 있다.

    #### ZK 롤업: 수학적 확실성

    Starknet, zkSync, Scroll을 포함한 **ZK 롤업**은 완전히 다른 접근 방식을 취한다. 유효성을 가정하고 이의 제기를 기다리는 대신, 모든 거래 배치의 정확성을 수학적으로 증명하는 고급 암호학적 기술인 **유효성 증명(validity proof)**을 사용한다. 이 롤업들은 먼저 거래 데이터를 레이어 1에 커밋한 다음, 전체 배치를 검증하는 증명을 제출한다.

    이 영지식 증명(zero-knowledge proof)은 고급 수학적 기술이다. 롤업이 레이어 1에서 재실행하지 않고도 수천 건의 거래가 정확하게 처리되었음을 증명할 수 있게 한다. 증명은 전체 배치의 유효성에 대해 강력한 암호학적 확실성을 제공한다(모든 암호학처럼 이것도 특정 수학적 가정이 건전하다는 것에 의존하지만).

    다른 ZK 롤업은 각각 고유한 속성을 가진 다른 증명 시스템을 사용한다. Scroll은 순수 SNARK를 사용하여 불과 수백 바이트의 작은 증명을 생성해 L1 비용을 최소화하지만, 초기 매개변수가 안전하게 생성되고 파괴되어야 하는 신뢰 설정(trusted setup)이 필요하다. 이는 마스터 키를 주조한 후 아무도 몰래 더 많은 키를 만들 수 없도록 금형을 파괴하는 것과 같다. Starknet은 STARK를 사용하여 수백 킬로바이트의 훨씬 큰 증명을 생성하지만, 더 강력한 보안 속성을 제공한다: 신뢰 설정 없음, 투명성, 잠재적인 미래 양자 컴퓨터에 대한 더 나은 저항력. zkSync는 하이브리드 접근 방식을 취하여 보안을 위해 내부적으로 STARK 증명을 생성한 다음 비용 효율적인 온체인 검증을 위해 SNARK로 래핑한다. 이것은 여전히 SNARK 래퍼에 대한 신뢰 설정이 필요하다.

    낙관적 롤업에 비해 장점이 매력적이다. ZK 롤업은 낙관적 시스템을 괴롭히는 일주일간의 인출 지연을 피한다. 유효성 증명이 레이어 1에서 검증되면, 사용자는 이의 제기 기간 없이 자금에 접근할 수 있다(시스템 부하에 따라 몇 분에서 몇 시간이 걸리는 증명 생성 및 검증을 기다려야 하지만). 그러나 이 보안에는 비용이 따른다. 이러한 증명을 생성하는 데 필요한 암호학적 기계장치는 낙관적 접근 방식보다 더 복잡하고 연산 집약적이다.

    #### 추가적인 롤업 고려사항

    낙관적 접근 방식과 ZK 접근 방식 간의 핵심 차이점 외에도, 롤업을 평가할 때 여러 다른 차원이 중요하다.

    실제로 대부분의 롤업은 현재 사용자가 기대하는 빠른 확인을 달성하기 위해 중앙화된 시퀀서에 의존한다. 수천 명의 검증자에게 블록 제안을 분산시키는 이더리움 메인넷과 달리, 이 롤업들은 단일 주체를 사용하여 거래를 정렬하고 블록을 생성한다. 이것은 영구적인 설계가 아닌 임시 엔지니어링 선택이지만, 잠재적인 검열 위험과 단일 장애점을 도입한다. 주요 롤업들은 성능을 유지하면서 시퀀서 중앙화를 제거하기 위한 솔루션을 적극적으로 개발하고 있다. 공유 시퀀싱 네트워크(shared sequencing network)는 정렬 책임을 여러 당사자에게 분산시켜 속도를 희생하지 않고 중복성을 만든다. 시퀀서 로테이션 시스템은 거래 정렬을 처리하는 주체를 주기적으로 변경하여 어떤 단일 당사자의 장기적 통제를 방지한다. 포함 목록(inclusion list)은 시퀀서가 지정된 시간 내에 특정 거래를 포함하도록 요구하여 검열을 더 어렵게 만든다. 사전 확인(preconfirmation)은 시퀀서가 공식 합의 전에 거래 포함에 대한 소프트 커밋먼트를 할 수 있게 하여, 슬래싱 메커니즘과 분쟁 창을 통한 되돌림 옵션을 유지하면서 사용자 경험을 개선한다.

    증명 시스템은 성숙도와 커버리지에서 계속 진화하고 있다. 많은 ZK 롤업은 기술이 성숙해지는 초기 단계에서 시스템을 일시 중지하거나 재정의할 수 있는 추가 보안 메커니즘인 "훈련 바퀴"로 여전히 운영된다. 낙관적 롤업은 여전히 정제되고 실전 테스트되고 있는 강력한 장애 증명 시스템에 의존한다. 수수료 구조는 L2 실행 비용과 L1 데이터 가용성 및 포함 수수료를 결합한다. 추가로, 롤업은 다른 데이터 가용성 모드에서 운영된다. 진정한 롤업은 모든 데이터를 이더리움에 게시하고, validium은 외부 데이터 가용성이나 비용 절감을 위해 더 강한 신뢰 요구 사항과 거래하는 하이브리드 접근 방식을 사용한다.

    모든 롤업이 탈중앙화를 동등하게 우선시하는 것은 아니다. 일부 프로젝트는 소비자 앱과 같은 응답성을 달성하기 위해 의도적으로 중앙화된 아키텍처를 채택한다. 예를 들어, MegaETH는 단일 활성 시퀀서와 10밀리초 "미니블록"을 사용하여 밀리초 수준의 지연 시간과 초당 약 100,000건의 거래를 목표로 한다. 이 설계는 높은 속도를 위해 단일 장애점과 잠재적 검열과 같은 위험을 수용한다. 이러한 접근 방식은 블록체인 설계의 본질적인 긴장을 드러낸다: 탈중앙화, 보안, 성능은 끊임없는 경쟁 관계에 있으며, 다른 애플리케이션은 다른 균형을 필요로 한다.

### Solving the Data Availability Challenge

=== "EN"

    With rollups defined, the dominant cost driver becomes data availability. Before March 2024, rollups had to store their data permanently in Ethereum's expensive execution layer, making data availability costs account for 80-95% of total rollup fees.

    EIP-4844, implemented in the Dencun upgrade, fundamentally changed this economics by introducing blob-carrying transactions. EIP-4844 introduced **blobs** with a separate fee market and temporary retention (\~18 days), cutting rollup DA costs. These blobs are large packets of data (about 128 KB each) that live temporarily on Ethereum's consensus layer before being automatically pruned, establishing a separate, much cheaper data market specifically designed for rollups.

    The system maintains security through KZG commitments, which are cryptographic fingerprints that uniquely identify each blob's contents. Imagine rollups renting billboard space on mainnet: they paste a huge poster (the blob) that stays up for roughly 18 days, then the city takes it down. The city keeps only a sealed, signed thumbnail that uniquely commits to the poster (the KZG commitment). Later, anyone can verify a specific square of that poster with a tiny receipt (a proof) without the city storing the full poster forever.

    Through this design, Ethereum created two separate fee markets: blob space operates with its own base fee mechanism (similar to regular gas pricing), while normal transaction fees continue unchanged. With Pectra, EIP-7691 raised blob limits (target 3→6, max 6→9 per block) and made blob fees fall more aggressively when blobs are underused, further reducing costs for rollups while keeping prices responsive without overshooting.

    This design is the first step toward full danksharding, Ethereum's long-term vision for massive data availability scaling. KZG commitments enable nodes to verify blob integrity while remaining forward-compatible with future upgrades that will let even resource-constrained devices verify data availability by checking only small samples rather than downloading everything.

    #### Alternative Data Availability Solutions

    For applications requiring even lower costs than Ethereum's blobs provide, several alternative Data Availability (DA) layers have emerged. Each makes different security compromises to achieve cost reduction. Understanding these design choices is essential for evaluating which rollups to use.

    Celestia represents the most ambitious alternative. It's a specialized blockchain that provides consensus and data availability only, without execution. Its key innovation is Data Availability Sampling, which allows even devices with limited resources to gain high confidence that full block data was published by checking only small, random pieces rather than downloading everything. The system also lets different rollups efficiently prove their data was included without downloading irrelevant information from other rollups. Security relies on validators and an honest majority of independent samplers, with full nodes able to produce fraud proofs if data is incorrectly encoded.

    EigenDA leverages Ethereum's restaking ecosystem (described in Section IV) to provide high-throughput data availability. A disperser coordinates the encoding and distribution of data across operators who attest to its availability. Throughput can be high, but security depends on the value restaked by operators and the specific quorum assumptions of each deployment.

    Validium and committee-based systems take a different approach entirely, keeping data off-chain under the control of a committee or bonded set of operators. This can be cheaper than on-chain alternatives but weakens security guarantees since data availability isn't enforced by Layer 1 protocol rules.

    Many rollups operate in hybrid modes, posting state commitments to Ethereum while using external data availability for the bulk of their data, or switching between different DA providers based on market conditions.

    The data availability landscape continues to evolve rapidly, with new solutions emerging and existing ones improving their efficiency and security models. As rollups mature and user adoption grows, the choice of data availability solution will likely become as important as the choice of consensus mechanism itself.

=== "KO"

    롤업이 정의되면서, 지배적인 비용 요인은 데이터 가용성이 된다. 2024년 3월 이전에는 롤업이 이더리움의 비싼 실행 레이어에 데이터를 영구적으로 저장해야 했으며, 데이터 가용성 비용이 총 롤업 수수료의 80-95%를 차지했다.

    Dencun 업그레이드에서 구현된 EIP-4844는 블롭 운반 거래(blob-carrying transaction)를 도입하여 이 경제학을 근본적으로 변화시켰다. EIP-4844는 별도의 수수료 시장과 임시 보존(약 18일)을 가진 **블롭(blob)**을 도입하여 롤업 DA 비용을 절감했다. 이 블롭들은 이더리움의 합의 레이어에 자동으로 정리되기 전에 임시로 존재하는 큰 데이터 패킷(각각 약 128KB)으로, 롤업을 위해 특별히 설계된 훨씬 저렴한 별도의 데이터 시장을 구축한다.

    시스템은 각 블롭의 내용을 고유하게 식별하는 암호학적 지문인 KZG 커밋먼트(KZG commitment)를 통해 보안을 유지한다. 롤업이 메인넷에서 빌보드 공간을 임대하는 것을 상상하라: 약 18일 동안 유지되는 거대한 포스터(블롭)를 붙이면, 그 후 도시가 그것을 철거한다. 도시는 포스터에 고유하게 커밋하는 봉인되고 서명된 썸네일(KZG 커밋먼트)만 보관한다. 나중에 누구나 도시가 전체 포스터를 영원히 저장하지 않고도 작은 영수증(증명)으로 그 포스터의 특정 사각형을 검증할 수 있다.

    이 설계를 통해 이더리움은 두 개의 별도 수수료 시장을 만들었다: 블롭 공간은 자체 기본 수수료 메커니즘(일반 가스 가격 책정과 유사)으로 운영되고, 일반 거래 수수료는 변경되지 않는다. Pectra와 함께 EIP-7691은 블롭 한도(목표 3→6, 최대 6→9 블록당)를 높이고 블롭이 덜 사용될 때 블롭 수수료가 더 공격적으로 하락하게 하여, 가격이 과도하게 상승하지 않고 반응적으로 유지되면서 롤업 비용을 더욱 줄였다.

    이 설계는 이더리움의 장기적 대규모 데이터 가용성 스케일링 비전인 완전한 댕크샤딩(danksharding)을 향한 첫 번째 단계이다. KZG 커밋먼트는 노드가 블롭 무결성을 검증하면서 리소스가 제한된 기기조차도 모든 것을 다운로드하지 않고 작은 샘플만 확인하여 데이터 가용성을 검증할 수 있는 미래 업그레이드와 전방 호환되도록 한다.

    #### 대안적 데이터 가용성 솔루션

    이더리움의 블롭이 제공하는 것보다 더 낮은 비용이 필요한 애플리케이션을 위해, 여러 대안적 데이터 가용성(DA) 레이어가 등장했다. 각각은 비용 절감을 달성하기 위해 다른 보안 타협을 한다. 이러한 설계 선택을 이해하는 것은 어떤 롤업을 사용할지 평가하는 데 필수적이다.

    Celestia는 가장 야심찬 대안을 나타낸다. 실행 없이 합의와 데이터 가용성만 제공하는 전문화된 블록체인이다. 핵심 혁신은 데이터 가용성 샘플링(Data Availability Sampling)으로, 제한된 리소스를 가진 기기조차도 모든 것을 다운로드하지 않고 작은 무작위 조각만 확인하여 전체 블록 데이터가 게시되었다는 높은 확신을 얻을 수 있게 한다. 시스템은 또한 다른 롤업이 다른 롤업의 관련 없는 정보를 다운로드하지 않고도 자신의 데이터가 포함되었음을 효율적으로 증명할 수 있게 한다. 보안은 검증자와 독립적인 샘플러의 정직한 다수에 의존하며, 풀 노드는 데이터가 잘못 인코딩된 경우 사기 증명을 생성할 수 있다.

    EigenDA는 이더리움의 리스테이킹 생태계(Section IV에서 설명)를 활용하여 고처리량 데이터 가용성을 제공한다. 분산자(disperser)가 가용성을 증명하는 운영자들에게 데이터의 인코딩과 분산을 조정한다. 처리량은 높을 수 있지만, 보안은 운영자가 리스테이킹한 가치와 각 배포의 특정 쿼럼 가정에 달려 있다.

    Validium과 위원회 기반 시스템은 완전히 다른 접근 방식을 취하여, 위원회나 담보가 있는 운영자 세트의 통제 하에 데이터를 오프체인에 보관한다. 이는 온체인 대안보다 저렴할 수 있지만, 데이터 가용성이 레이어 1 프로토콜 규칙에 의해 강제되지 않기 때문에 보안 보장을 약화시킨다.

    많은 롤업이 하이브리드 모드로 운영되며, 상태 커밋먼트를 이더리움에 게시하면서 대부분의 데이터에는 외부 데이터 가용성을 사용하거나, 시장 조건에 따라 다른 DA 제공자 간에 전환한다.

    데이터 가용성 환경은 새로운 솔루션이 등장하고 기존 솔루션이 효율성과 보안 모델을 개선하면서 빠르게 진화하고 있다. 롤업이 성숙하고 사용자 채택이 증가함에 따라, 데이터 가용성 솔루션 선택은 합의 메커니즘 선택만큼 중요해질 것이다.

## Section IV: Restaking



=== "EN"

    Rollups multiply Ethereum's transaction capacity by moving computation off-chain. Proof-of-stake enabled a different kind of multiplication: the ability to reuse staked capital across multiple protocols simultaneously. This innovation, called **restaking**, represents a new frontier in capital efficiency with its own set of risks and rewards.

=== "KO"

    롤업은 연산을 오프체인으로 이동시켜 이더리움의 거래 용량을 배가시킨다. 지분 증명은 다른 종류의 배가를 가능하게 했다: 스테이킹된 자본을 동시에 여러 프로토콜에 재사용하는 능력이다. **리스테이킹(restaking)**이라 불리는 이 혁신은 자체적인 위험과 보상을 가진 자본 효율성의 새로운 개척지를 나타낸다.

### The Core Mechanism

=== "EN"

    EigenLayer pioneered this approach by creating a system where validators can opt in to secure **Actively Validated Services (AVSs)**. These are external protocols that need the kind of security that comes from having real money at stake. For native restaking, validators point their withdrawal credentials to an EigenPod and delegate to an operator. Alternatively, liquid staking token holders can deposit their tokens into EigenLayer strategies. Either way, participants commit to follow the rules of their chosen AVSs, and breaking those rules means facing additional slashing penalties on top of any Ethereum-level punishments.

    Multiple protocols can now tap into Ethereum's massive validator set and the billions of dollars they have at stake. This provides shared security rather than building separate systems from scratch. AVSs cover a wide range of applications: data availability layers like EigenDA, oracle networks that provide price feeds, cross-chain bridges, rollup sequencers, and automated keeper networks that maintain DeFi protocols. Each AVS defines its own slashing conditions, the specific rules validators must follow to avoid penalties. A data availability service might require validators to prove they're storing certain data, while an oracle network might slash validators who submit price feeds that deviate too far from consensus.

=== "KO"

    EigenLayer는 검증자가 **능동적 검증 서비스(Actively Validated Service, AVS)**를 보호하기 위해 옵트인할 수 있는 시스템을 만들어 이 접근 방식을 개척했다. 이것들은 실제 돈이 걸려 있는 보안을 필요로 하는 외부 프로토콜이다. 네이티브 리스테이킹의 경우, 검증자는 출금 자격 증명을 EigenPod로 지정하고 운영자에게 위임한다. 또는 유동 스테이킹 토큰 보유자가 자신의 토큰을 EigenLayer 전략에 예치할 수 있다. 어느 쪽이든, 참가자들은 선택한 AVS의 규칙을 따르기로 약속하며, 그 규칙을 위반하면 이더리움 수준의 처벌 위에 추가적인 슬래싱 처벌을 받게 된다.

    이제 여러 프로토콜이 이더리움의 방대한 검증자 세트와 그들이 스테이킹한 수십억 달러를 활용할 수 있다. 이는 처음부터 별도의 시스템을 구축하는 대신 공유 보안을 제공한다. AVS는 광범위한 애플리케이션을 포괄한다: EigenDA와 같은 데이터 가용성 레이어, 가격 피드를 제공하는 오라클 네트워크, 크로스체인 브릿지, 롤업 시퀀서, DeFi 프로토콜을 유지하는 자동화된 키퍼 네트워크. 각 AVS는 처벌을 피하기 위해 검증자가 따라야 하는 구체적인 규칙인 자체 슬래싱 조건을 정의한다. 데이터 가용성 서비스는 검증자가 특정 데이터를 저장하고 있음을 증명하도록 요구할 수 있고, 오라클 네트워크는 합의에서 너무 벗어난 가격 피드를 제출하는 검증자를 슬래싱할 수 있다.

### Technical Architecture

=== "EN"

    EigenLayer's design reflects careful consideration of how multiple protocols and validators interact. The architecture separates concerns into distinct layers that enable flexible composition while maintaining clear security boundaries.

    Strategy contracts handle deposits and withdrawals for ERC-20-based restaking. When users deposit LSTs or other supported tokens, these strategies track ownership and manage the underlying assets. Each strategy represents a different restaked token: one for stETH, another for cbETH, EIGEN, and so on. Native restaking is tracked separately through EigenPods, contract instances that hold validator withdrawal credentials and account for restaked beacon-chain ETH. This modular split lets EigenLayer support both liquid staking derivatives and native staking without one monolithic contract trying to handle every asset type.

    Slashing contracts enforce each AVS's specific rules independently. This separation is crucial: it prevents bugs in one AVS's slashing logic from affecting other services or compromising the core deposit/withdrawal mechanisms. When an AVS needs to slash a misbehaving operator, it interacts only with its own slashing contract, which then coordinates with the core system to execute penalties.

    The system enables delegation, allowing users who don't want to run validator infrastructure to stake through professional operators. Delegators retain control over their withdrawal rights and can exit and delegate to a different operator after serving the required withdrawal delay, but they also inherit the operator's performance and slashing risks. Operators can signal their commission rates and which AVSs they support, creating a marketplace where delegators can choose based on expertise, fees, and risk profiles.

    Different AVSs employ varying proof systems depending on their security needs. Some rely on fraud proofs that assume honest behavior unless challenged. If someone detects invalid behavior during a challenge window, they can submit evidence that triggers slashing. Others use validity proofs based on zero-knowledge cryptography that mathematically guarantee correctness before any state change occurs. Still others depend on committee signatures from trusted parties, which are faster and simpler but introduce trust assumptions about committee honesty and availability.

    EigenLayer's security model includes veto committees as an extra layer for critical slashing decisions. Rather than allowing immediate, automated slashing for all violations, some conditions require committee approval. This prevents hasty or incorrect penalty enforcement. Imagine a bug in an AVS that incorrectly flags honest behavior as malicious. The veto committee can pause the slashing, investigate the issue, and prevent unjust penalties. However, this introduces governance risk and potential delays in enforcing legitimate slashing. The exact veto-committee design and implementation have been evolving alongside the rollout of slashing, so details may change over time.

    Perhaps most intriguingly, EigenLayer introduces intersubjective slashing, where some violations can’t be proven purely on-chain and instead rely on shared human judgment (social consensus) to decide when to slash. Consider an oracle AVS where validators should report accurate price data. If a validator reports an obviously wrong price (claiming ETH trades at $1 when all exchanges show $3,000), the violation is clear to humans but hard to prove on-chain without introducing centralized price feeds. Intersubjective slashing allows such cases to be resolved through social consensus and governance processes. Token holders or designated committees vote on whether slashing should occur based on off-chain evidence. This flexibility enables the system to handle complex, real-world scenarios that pure algorithmic approaches might miss, but it introduces governance risks and the potential for contentious decisions that divide the community.

=== "KO"

    EigenLayer의 설계는 여러 프로토콜과 검증자가 어떻게 상호작용하는지에 대한 신중한 고려를 반영한다. 아키텍처는 명확한 보안 경계를 유지하면서 유연한 구성을 가능하게 하는 구별된 레이어로 관심사를 분리한다.

    전략 컨트랙트(Strategy contract)는 ERC-20 기반 리스테이킹의 예치금과 출금을 처리한다. 사용자가 LST나 기타 지원되는 토큰을 예치하면, 이 전략들은 소유권을 추적하고 기본 자산을 관리한다. 각 전략은 다른 리스테이킹된 토큰을 나타낸다: stETH용, cbETH용, EIGEN용 등. 네이티브 리스테이킹은 EigenPod를 통해 별도로 추적되며, 이는 검증자 출금 자격 증명을 보유하고 리스테이킹된 비콘 체인 ETH를 계산하는 컨트랙트 인스턴스이다. 이 모듈식 분할은 EigenLayer가 모든 자산 유형을 처리하려는 하나의 거대한 컨트랙트 없이 유동 스테이킹 파생상품과 네이티브 스테이킹을 모두 지원할 수 있게 한다.

    슬래싱 컨트랙트(Slashing contract)는 각 AVS의 특정 규칙을 독립적으로 시행한다. 이 분리는 매우 중요하다: 한 AVS의 슬래싱 로직에 있는 버그가 다른 서비스에 영향을 주거나 핵심 예치/출금 메커니즘을 손상시키는 것을 방지한다. AVS가 잘못 행동하는 운영자를 슬래싱해야 할 때, 자체 슬래싱 컨트랙트와만 상호작용하고, 이 컨트랙트가 처벌을 실행하기 위해 핵심 시스템과 조율한다.

    시스템은 위임(delegation)을 가능하게 하여, 검증자 인프라를 운영하고 싶지 않은 사용자가 전문 운영자를 통해 스테이킹할 수 있게 한다. 위임자는 출금 권리에 대한 통제를 유지하고 필요한 출금 지연을 거친 후 다른 운영자에게 종료하고 위임할 수 있지만, 운영자의 성능과 슬래싱 위험도 상속받는다. 운영자는 수수료율과 지원하는 AVS를 신호로 보낼 수 있어, 위임자가 전문성, 수수료, 위험 프로필에 따라 선택할 수 있는 마켓플레이스를 만든다.

    다른 AVS는 보안 필요에 따라 다양한 증명 시스템을 사용한다. 일부는 이의 제기 창 동안 누군가 유효하지 않은 행동을 감지하면 슬래싱을 촉발하는 증거를 제출할 수 있는, 정직한 행동을 가정하는 사기 증명에 의존한다. 다른 것들은 어떤 상태 변경이 발생하기 전에 정확성을 수학적으로 보장하는 영지식 암호학 기반의 유효성 증명을 사용한다. 또 다른 것들은 신뢰할 수 있는 당사자의 위원회 서명에 의존하는데, 이는 더 빠르고 단순하지만 위원회의 정직성과 가용성에 대한 신뢰 가정을 도입한다.

    EigenLayer의 보안 모델은 중요한 슬래싱 결정에 대한 추가 레이어로 거부권 위원회(veto committee)를 포함한다. 모든 위반에 대해 즉각적이고 자동화된 슬래싱을 허용하는 대신, 일부 조건은 위원회 승인이 필요하다. 이는 성급하거나 잘못된 처벌 시행을 방지한다. 정직한 행동을 악의적으로 잘못 플래그하는 AVS의 버그를 상상해보라. 거부권 위원회가 슬래싱을 일시 중지하고 문제를 조사하여 부당한 처벌을 방지할 수 있다. 그러나 이는 거버넌스 위험과 정당한 슬래싱 시행의 잠재적 지연을 도입한다. 정확한 거부권 위원회 설계와 구현은 슬래싱 롤아웃과 함께 진화해왔으므로, 세부 사항은 시간이 지남에 따라 변경될 수 있다.

    아마도 가장 흥미롭게도, EigenLayer는 상호주관적 슬래싱(intersubjective slashing)을 도입하는데, 일부 위반은 순수하게 온체인에서 증명될 수 없고 대신 슬래싱할 시기를 결정하기 위해 공유된 인간 판단(사회적 합의)에 의존한다. 검증자가 정확한 가격 데이터를 보고해야 하는 오라클 AVS를 생각해보라. 검증자가 모든 거래소가 $3,000을 보여줄 때 ETH가 $1에 거래된다고 명백히 잘못된 가격을 보고하면, 위반은 인간에게는 명확하지만 중앙화된 가격 피드를 도입하지 않고는 온체인에서 증명하기 어렵다. 상호주관적 슬래싱은 이러한 경우를 사회적 합의와 거버넌스 프로세스를 통해 해결할 수 있게 한다. 토큰 보유자나 지정된 위원회가 오프체인 증거를 기반으로 슬래싱이 발생해야 하는지 투표한다. 이 유연성은 시스템이 순수 알고리즘적 접근 방식이 놓칠 수 있는 복잡한 현실 세계 시나리오를 처리할 수 있게 하지만, 거버넌스 위험과 커뮤니티를 분열시키는 논쟁적인 결정의 가능성을 도입한다.

### Current Economic Reality

=== "EN"

    On paper, restaking looks like a clean win: more protocols can "rent" Ethereum's security instead of bootstrapping their own validator sets. In practice, the system is still early and somewhat lopsided. A large amount of ETH and liquid staking tokens has been restaked into EigenLayer and liquid restaking wrappers, but only a subset of AVSs see meaningful real-world demand today. Most of the incremental rewards restakers currently earn come from incentive programs, airdrops, and protocol token emissions rather than durable fee revenue generated by AVSs themselves. For now, restaking behaves less like a mature cash-flow asset class and more like a leveraged bet on the future success of the EigenLayer ecosystem.

    This timing mismatch matters significantly. The extra liabilities are live today (additional smart contract risk, governance risk, and correlated slashing exposure across multiple AVSs), while the long-run fee markets that are supposed to compensate restakers are still being designed and battle-tested. When you hear claims about "reusing security" or "unlocking capital efficiency," it's worth remembering that many restakers are currently taking on large tail risks for economics that depend on ongoing incentives and a still-uncertain AVS adoption curve.

=== "KO"

    서류상으로 리스테이킹은 깔끔한 승리처럼 보인다: 더 많은 프로토콜이 자체 검증자 세트를 부트스트랩하는 대신 이더리움의 보안을 "임대"할 수 있다. 실제로 시스템은 여전히 초기 단계이며 다소 불균형하다. 상당량의 ETH와 유동 스테이킹 토큰이 EigenLayer와 유동 리스테이킹 래퍼에 리스테이킹되었지만, 오늘날 의미 있는 실제 수요를 보는 것은 AVS의 일부에 불과하다. 현재 리스테이커가 얻는 증분 보상의 대부분은 AVS 자체가 생성하는 지속 가능한 수수료 수익이 아닌 인센티브 프로그램, 에어드롭, 프로토콜 토큰 배출에서 나온다. 현재로서는 리스테이킹이 성숙한 현금 흐름 자산 클래스보다는 EigenLayer 생태계의 미래 성공에 대한 레버리지 베팅처럼 동작한다.

    이 타이밍 불일치는 상당히 중요하다. 추가적인 부채는 오늘날 살아있다(추가적인 스마트 컨트랙트 위험, 거버넌스 위험, 여러 AVS에 걸친 상관 슬래싱 노출), 반면 리스테이커를 보상해야 하는 장기 수수료 시장은 여전히 설계되고 실전 테스트되고 있다. "보안 재사용" 또는 "자본 효율성 해제"에 대한 주장을 들을 때, 많은 리스테이커가 현재 진행 중인 인센티브와 여전히 불확실한 AVS 채택 곡선에 의존하는 경제학을 위해 큰 꼬리 위험을 감수하고 있다는 것을 기억할 가치가 있다.

### The Risk Landscape

=== "EN"

    Understanding the technical architecture reveals why restaking carries significant risks. The most pressing concern is correlated slashing risk. When validators secure multiple AVSs simultaneously, a single mistake or malicious action can trigger penalties across all services at once, amplifying potential losses far beyond standard Ethereum staking. This makes AVS risk assessment essential, since each service brings its own slashing conditions, upgrade mechanisms, and governance structures that validators must understand and trust.

    Choosing the right operator becomes pivotal in this environment. Most restakers delegate their validation duties to professional operators who must maintain infrastructure for multiple protocols at once. Poor operator performance or malicious behavior doesn't just affect one service; it impacts all delegated stake across every AVS that operator supports.

    Withdrawal delays can extend well beyond Ethereum's standard unbonding periods. EigenLayer adds its own roughly two-week escrow period (currently about 14–17 days depending on the contract version) on top of Beacon Chain exit timing. Individual AVSs or LRT (liquid restaking token) protocols may impose additional withdrawal restrictions on top of this.

    The liquid restaking ecosystem introduces systemic risks that compound on top of the liquid staking risks discussed earlier. Liquidity cascades could emerge if LRT tokens lose their peg to underlying ETH, potentially forcing mass withdrawals that create destructive feedback loops across the entire restaking ecosystem. There's also basis risk between the underlying ETH staking yields and LRT token prices, adding complexity for users who expect predictable returns. When you layer restaking on top of liquid staking protocols like Lido or Rocket Pool, you're compounding multiple layers of smart contract risk, economic assumptions, and potential failure points.

=== "KO"

    기술 아키텍처를 이해하면 왜 리스테이킹이 상당한 위험을 수반하는지 드러난다. 가장 절박한 우려는 상관 슬래싱 위험(correlated slashing risk)이다. 검증자가 동시에 여러 AVS를 보호할 때, 단일 실수나 악의적인 행동이 모든 서비스에서 한 번에 처벌을 촉발하여 잠재적 손실을 표준 이더리움 스테이킹을 훨씬 넘어서 증폭시킬 수 있다. 이는 AVS 위험 평가를 필수적으로 만드는데, 각 서비스가 검증자가 이해하고 신뢰해야 하는 자체 슬래싱 조건, 업그레이드 메커니즘, 거버넌스 구조를 가져오기 때문이다.

    이 환경에서 올바른 운영자를 선택하는 것이 중요해진다. 대부분의 리스테이커는 여러 프로토콜에 대한 인프라를 동시에 유지해야 하는 전문 운영자에게 검증 의무를 위임한다. 운영자의 성능 저하나 악의적인 행동은 단 하나의 서비스에만 영향을 미치지 않는다; 해당 운영자가 지원하는 모든 AVS에 걸쳐 모든 위임된 스테이크에 영향을 미친다.

    출금 지연은 이더리움의 표준 언본딩 기간을 훨씬 넘어서 연장될 수 있다. EigenLayer는 비콘 체인 종료 타이밍 위에 자체적으로 대략 2주의 에스크로 기간(현재 컨트랙트 버전에 따라 약 14-17일)을 추가한다. 개별 AVS나 LRT(유동 리스테이킹 토큰) 프로토콜은 이 위에 추가적인 출금 제한을 부과할 수 있다.

    **유동 리스테이킹(Liquid Restaking)** 생태계는 앞서 논의한 유동 스테이킹 위험 위에 복합되는 시스템적 위험을 도입한다. LRT 토큰이 기본 ETH에 대한 페그를 잃으면 유동성 연쇄반응(liquidity cascade)이 발생할 수 있으며, 잠재적으로 전체 리스테이킹 생태계에 걸쳐 파괴적인 피드백 루프를 만드는 대량 출금을 강제할 수 있다. 또한 기본 ETH 스테이킹 수익률과 LRT 토큰 가격 사이에 베이시스 위험(basis risk)이 있어 예측 가능한 수익을 기대하는 사용자에게 복잡성을 더한다. Lido나 Rocket Pool과 같은 유동 스테이킹 프로토콜 위에 리스테이킹을 레이어링하면, 여러 층의 스마트 컨트랙트 위험, 경제적 가정, 잠재적 실패 지점을 복합하게 된다.

