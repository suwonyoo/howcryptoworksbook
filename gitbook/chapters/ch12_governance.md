# Chapter XII: Governance and Token Economics

=== "EN"

    In 2020, Uniswap team dropped the ultimate surprise: 400 UNI tokens to every wallet that had ever used their protocol. On day one, those 400 UNI were worth roughly $2,000 and a few months later, the same 400 UNI airdrop was worth about $6,000. Was this democracy or chaos?

    This single moment crystallized the central tension of decentralized governance. How can thousands of strangers coordinate to make billion-dollar decisions? How can they do this without traditional management, boards of directors, or even legal entities? How can systems prevent the wealthy from simply buying control while still rewarding meaningful participation?

    Welcome to the world of **DAOs (Decentralized Autonomous Organizations)**, where code becomes constitution, tokens become voting power, and communities attempt to govern themselves at internet scale.

=== "KO"

    2020년, Uniswap 팀은 궁극의 서프라이즈를 선보였다. 프로토콜을 한 번이라도 사용한 모든 지갑에 400 UNI 토큰을 에어드롭한 것이다. 첫날 400 UNI의 가치는 약 2,000달러였고, 몇 달 후 같은 400 UNI 에어드롭의 가치는 약 6,000달러가 되었다. 이것은 민주주의였을까, 아니면 혼돈이었을까?

    이 단 하나의 순간이 탈중앙화 거버넌스(Decentralized Governance)의 핵심 긴장을 결정화했다. 수천 명의 낯선 사람들이 어떻게 수십억 달러 규모의 결정에 협력할 수 있을까? 전통적인 경영진, 이사회, 심지어 법인 없이 어떻게 이것이 가능할까? 부유한 이들이 단순히 지배권을 사는 것을 어떻게 막으면서도 의미 있는 참여에는 보상할 수 있을까?

    **DAO(탈중앙화 자율 조직, Decentralized Autonomous Organization)**의 세계에 오신 것을 환영한다. 여기서 코드는 헌법이 되고, 토큰은 투표권이 되며, 커뮤니티는 인터넷 규모에서 스스로를 통치하려 시도한다.

## Section I: The Foundations of Digital Democracy

=== "EN"

    ### The Great Experiment Begins

    The Uniswap airdrop was a milestone, but it wasn't crypto's first experiment with digital democracy. That story begins with a far more cautionary tale.

    It's 2016, and Ethereum has been live for barely a year. A group of developers launches "The DAO", a venture capital fund with no managers, no office, and no legal structure. Just smart contracts and the collective wisdom of token holders. Within weeks, it raises $150 million, becoming the largest crowdfunding campaign in history.

    Then a week later it gets hacked for $60 million due to a smart contract bug.

    The DAO's spectacular rise and fall taught the crypto world a crucial lesson: decentralized governance requires more than writing smart contracts; it requires reimagining how humans coordinate at scale. If every stakeholder held direct voting power, the thinking went, then no CEO could make self-serving decisions and no board could prioritize shareholders over users. The elimination of traditional principal-agent problems seemed within reach.

    The theory was elegant, but reality proved messier. Democracy works differently when voters are pseudonymous, the treasury is programmable money, and decisions execute automatically through immutable code.

    ### From Code to Constitution

    Think of a DAO as a digital nation with programmable laws. The "constitution" is written in smart contract code, and amendments happen through governance proposals that can directly modify protocol parameters, allocate treasury funds, or upgrade entire systems.

    This represents a fundamental shift from traditional corporate governance. In Apple, shareholders vote for a board, which hires executives who make decisions. In a DAO, token holders vote on many of the decisions themselves. When a proposal passes, the contracts unlock a predefined set of on-chain actions: an executor (often the proposer, a designated execution contract, or even any user) can trigger those actions after a **timelock** period, subject to whatever safeguards the system enforces. Execution is mediated and constrained by code, but it is not fully automatic. Someone still has to submit the transaction, and in many systems security or treasury multisigs can intervene on sensitive changes.

    But here's the catch: unlike owning Apple stock, holding **governance tokens** doesn't necessarily give legal ownership of anything. It only provides the ability to vote. A holder's power is defined entirely by smart contracts and operational controls like timelocks and multisigs. A token holder can steer the protocol but does not "own" it in any traditional sense.

    ### The Voting Dilemma: Four Approaches to Digital Democracy

    How should voting be structured to be both fair and effective? The crypto world has experimented with multiple governance mechanisms, each with dramatic successes and failures.

    #### Token-Weighted Voting

    Most DAOs start with the corporate model: one token, one vote. Own 1% of the supply, get 1% of voting power. But in practice, **delegation** is the norm. Platforms like Uniswap and Aave allow token holders to delegate their voting power to active participants, addressing voter apathy while creating new concentration risks.

    The concentration problem is severe. In major DAOs, single-digit entities often control enough voting power to reach **quorum** (the minimum participation threshold required for a vote to be valid) or pass proposals. Foundations, early investors, and team members typically control large portions from day one, but the picture is worse than just initial allocation: most "ordinary users" either sell their governance tokens, park them in farms, or hold amounts too small to justify following proposals and paying gas to vote. The combination of skewed distribution and rational apathy means that, in practice, a small set of funds, foundations, and professional delegates end up shaping most outcomes. These large delegates become new bottlenecks and potential points of failure.

    #### Time-Weighted Voting (veTokenomics)

    Vote-escrow tokenomics (often called "veTokenomics") rewards long-term alignment: voting power scales with lock duration. The "ve" prefix stands for "vote-escrow," indicating tokens locked in exchange for voting rights. Curve's veCRV model pioneered this approach. (Curve's AMM mechanics were covered in Chapter VII.) Holders lock their tokens for longer periods (therefore giving up the ability to sell them) and in exchange receive more voting weight. Because voting power is time-locked and non-transferable, ve-style systems mitigate flash-loan governance capture while naturally filtering out short-term speculation.

    On Curve, each liquidity pool has a gauge, which is a configuration that determines what share of weekly CRV emissions that pool will receive. More votes to a pool's gauge means more CRV inflation directed to that pool, which translates into higher yields for its liquidity providers. That yield makes the pool more attractive, deepening liquidity for whatever asset pair it hosts.

    veTokenomics spawned unexpected consequences: vote-bribe markets emerged, where protocols that want deeper liquidity for their own tokens pay veCRV holders to direct gauge votes toward their pools. In effect, protocols buy a slice of future CRV emissions by bribing voters today. This created delegate cartels and new forms of rent extraction, but it also revealed genuine economic demand for governance influence over where emissions (and therefore liquidity) flow.

    #### Quadratic Voting

    Under quadratic voting, the cost of k votes is k², usually paid with vote credits under a fixed budget; the system needs a way to verify that each participant is a unique person, preventing one person from pretending to be many. In this system, casting one vote requires one credit, but casting two votes requires four credits (2²), three votes requires nine credits (3²), and so on.

    It helps prevent wealthy participants or entities from accumulating disproportionate control over decision-making processes. By requiring exponentially more credits to cast additional votes, quadratic voting mitigates risks of oligopolies dominating governance through sheer token accumulation and reduces the direct translation of large stakeholder wealth into outsized political influence over network governance.

    #### Experimental Frontiers: Futarchy

    Beyond these established models, the governance design space continues to evolve with more exotic experiments that challenge fundamental assumptions about how collective decisions should be made.

    Futarchy takes a radically different approach: "vote on values, bet on beliefs." Token holders vote on high-level objectives (e.g., "maximize protocol TVL"), but decisions about how to achieve those objectives get made through prediction markets. TVL refers to the total value of assets deposited in the protocol, a common measure of a protocol's size. A proposal to change fee parameters would create two markets: "Protocol TVL if the proposal passes" and "Protocol TVL if it fails." The proposal automatically executes based on which market predicts higher TVL. The theory is elegant: decision markets aggregate dispersed information more efficiently than voting, while preventing the tyranny of the majority on technical questions.

    Early experiments, like Gnosis' conditional markets, never reached broad protocol-level adoption. More recently, MetaDAO on Solana has gone further by actually wiring futarchy into governance so that prediction markets *decide* proposals rather than merely informing them. Still, futarchy remains a niche experiment: no systemically important DeFi protocol has handed core control to this model yet, largely because it requires deep, liquid markets, clear on-chain metrics, and communities willing to let markets overrule traditional token voting.

    #### Governance Attacks: When Democracy Gets Hijacked

    The worst-case scenario isn't voter apathy but active exploitation. Flash loan governance attacks (using the uncollateralized borrowing mechanism described in Chapter VII) work by borrowing massive amounts of governance tokens, voting to pass a malicious proposal, and returning the tokens all in a single transaction. In April 2022, Beanstalk DAO suffered exactly this fate: an attacker used flash loans from Aave to borrow $1 billion worth of various assets, used them to amass STALK (Beanstalk's governance power accrued through its Silo mechanisms) to gain 67% voting power, passed a malicious proposal to transfer $182 million from the treasury to their own wallet, and executed it. The entire attack completed within a single Ethereum transaction, happening within seconds. By the time the community noticed, the funds were gone.

    The defense against this isn't any single mechanism but rather a layered timing system. Snapshot-based voting is the foundational protection: voting power is determined by token balances at a specific past block, set when the proposal is created. An attacker who borrows tokens during the voting period has zero voting power because they didn't hold those tokens at the snapshot point. This is combined with a voting delay (the time between proposal creation and when voting begins, allowing the snapshot to be effectively locked in) and a voting period (the window during which votes can be cast). Finally, a timelock adds delay between a vote passing and its execution, giving the community time to react to suspicious outcomes or discovered bugs.

    Beanstalk's critical mistake was allowing proposals to pass and execute within the same block without any snapshot mechanism or timelock delay. Modern governance systems record token balances at fixed points in time, either on-chain or through off-chain tools like Snapshot, to ensure voting power cannot be manipulated through temporary token acquisition. But sophisticated attacks evolve: governance bribery involves paying token holders to vote a certain way, proposal spam clogs governance with noise to hide malicious changes, and 51% attacks involve slowly accumulating tokens to gain permanent control.

    #### The Meta-Lesson

    No single mechanism solves digital democracy. The "best" system depends on what is being governed, who the stakeholders are, and how much complexity the community can handle.

    Some projects are taking a radical approach: reduce what governance can control rather than perfecting how it controls things. This governance minimization trend includes immutable protocols like Uniswap's AMM cores (v3/v4), algorithmic parameter setting, constrained fee switches, and projects publicly aiming to freeze their code or limit governance scope (e.g., Lido's "minimal governance" direction). It also includes constitutional constraints that remove certain decisions from human discretion entirely.

    The logic: if governance is inevitably flawed, whether through plutocracy, apathy, or capture, then minimize the attack surface by making fewer things governable. The trade-off is obvious: reduced adaptability. When market conditions change or new opportunities arise, these systems can't pivot quickly. But they gain credible neutrality and resistance to both internal politics and external pressure.

=== "KO"

    ### 위대한 실험의 시작

    Uniswap 에어드롭은 이정표였지만, 암호화폐의 디지털 민주주의 첫 실험은 아니었다. 그 이야기는 훨씬 더 경고적인 사례에서 시작된다.

    2016년, 이더리움이 겨우 1년째 운영되던 때였다. 한 개발자 그룹이 "The DAO"를 출시했다. 관리자도, 사무실도, 법적 구조도 없는 벤처 캐피탈 펀드였다. 오직 스마트 컨트랙트와 토큰 보유자들의 집단 지혜만이 존재했다. 몇 주 만에 1억 5천만 달러를 모금하며 역사상 최대의 크라우드펀딩 캠페인이 되었다.

    그리고 일주일 후 스마트 컨트랙트 버그로 인해 6천만 달러가 해킹당했다.

    The DAO의 극적인 성공과 몰락은 암호화폐 세계에 중요한 교훈을 남겼다: 탈중앙화 거버넌스는 단순히 스마트 컨트랙트를 작성하는 것 이상을 요구한다. 인간이 대규모로 협력하는 방식을 재상상하는 것이 필요하다. 모든 이해관계자가 직접 투표권을 가진다면, CEO가 이기적인 결정을 내릴 수 없고 이사회가 사용자보다 주주를 우선시할 수 없다는 생각이었다. 전통적인 주인-대리인 문제의 제거가 손에 닿는 듯 보였다.

    이론은 우아했지만, 현실은 더 복잡했다. 투표자가 익명이고, 재무부가 프로그래머블 머니이며, 결정이 불변의 코드를 통해 자동으로 실행될 때 민주주의는 다르게 작동한다.

    ### 코드에서 헌법으로

    DAO를 프로그래머블 법률을 가진 디지털 국가로 생각해보라. "헌법"은 스마트 컨트랙트 코드로 작성되고, 수정은 프로토콜 파라미터를 직접 수정하거나, 재무 자금을 배분하거나, 전체 시스템을 업그레이드할 수 있는 거버넌스 제안을 통해 이루어진다.

    이것은 전통적인 기업 거버넌스로부터의 근본적인 전환을 나타낸다. 애플에서는 주주들이 이사회를 선출하고, 이사회가 경영진을 고용하며, 경영진이 결정을 내린다. DAO에서는 토큰 보유자들이 많은 결정에 직접 투표한다. 제안이 통과되면, 컨트랙트가 미리 정의된 온체인 액션 세트를 언락한다: 실행자(종종 제안자, 지정된 실행 컨트랙트, 또는 심지어 모든 사용자)가 **타임락(Timelock)** 기간 이후에 해당 액션을 트리거할 수 있으며, 시스템이 적용하는 모든 세이프가드의 적용을 받는다. 실행은 코드에 의해 중재되고 제약되지만, 완전히 자동은 아니다. 누군가가 여전히 트랜잭션을 제출해야 하고, 많은 시스템에서 보안 또는 재무 멀티시그가 민감한 변경에 개입할 수 있다.

    하지만 여기에 함정이 있다: 애플 주식을 소유하는 것과 달리, **거버넌스 토큰(Governance Token)**을 보유하는 것이 반드시 어떤 것의 법적 소유권을 부여하지는 않는다. 오직 투표 능력만 제공한다. 보유자의 권한은 전적으로 스마트 컨트랙트와 타임락 및 멀티시그와 같은 운영 통제에 의해 정의된다. 토큰 보유자는 프로토콜을 조종할 수 있지만 전통적인 의미에서 "소유"하지는 않는다.

    ### 투표 딜레마: 디지털 민주주의의 네 가지 접근법

    투표는 공정하고 효과적이 되려면 어떻게 구조화되어야 할까? 암호화폐 세계는 여러 거버넌스 메커니즘을 실험해왔으며, 각각 극적인 성공과 실패를 겪었다.

    #### 토큰 가중 투표

    대부분의 DAO는 기업 모델로 시작한다: 한 토큰, 한 표. 공급량의 1%를 소유하면 투표권의 1%를 얻는다. 그러나 실제로는 **위임(Delegation)**이 표준이다. Uniswap과 Aave 같은 플랫폼은 토큰 보유자가 자신의 투표권을 적극적인 참여자에게 위임할 수 있게 하여, 투표자 무관심 문제를 해결하면서 새로운 집중 위험을 만든다.

    집중 문제는 심각하다. 주요 DAO에서 한 자릿수의 주체들이 종종 **정족수(Quorum)**(투표가 유효하기 위해 필요한 최소 참여 임계값)에 도달하거나 제안을 통과시키기에 충분한 투표권을 통제한다. 재단, 초기 투자자, 팀 멤버들이 일반적으로 처음부터 큰 비중을 통제하지만, 상황은 단순히 초기 배분보다 더 나쁘다: 대부분의 "일반 사용자"는 거버넌스 토큰을 팔거나, 파밍에 넣어두거나, 제안을 따르고 가스비를 내고 투표하기에는 너무 작은 양을 보유한다. 왜곡된 분배와 합리적 무관심의 결합은 실제로 소수의 펀드, 재단, 전문 대리인들이 대부분의 결과를 형성하게 된다는 것을 의미한다. 이러한 대형 대리인들은 새로운 병목점이자 잠재적 실패 지점이 된다.

    #### 시간 가중 투표 (veTokenomics)

    투표-예치 토크노믹스(Vote-escrow Tokenomics), 흔히 "veTokenomics"라고 불리는 방식은 장기적 정렬에 보상을 준다: 투표권이 락업 기간에 비례하여 증가한다. "ve" 접두사는 "vote-escrow"를 의미하며, 투표권과 교환으로 토큰이 락업됨을 나타낸다. Curve의 veCRV 모델이 이 접근법을 개척했다. (Curve의 AMM 메커니즘은 제7장에서 다루었다.) 보유자들은 더 긴 기간 동안 토큰을 락업하고(따라서 판매 능력을 포기하고) 그 대가로 더 많은 투표 가중치를 받는다. 투표권이 시간으로 락업되고 양도 불가능하기 때문에, ve 스타일 시스템은 플래시론 거버넌스 탈취를 완화하면서 자연스럽게 단기 투기를 걸러낸다.

    Curve에서 각 유동성 풀에는 게이지(Gauge)가 있는데, 이는 해당 풀이 주간 CRV 배출의 어떤 비율을 받을지 결정하는 구성이다. 풀의 게이지에 더 많은 투표가 갈수록 해당 풀에 더 많은 CRV 인플레이션이 향하고, 이는 유동성 공급자에게 더 높은 수익률로 번역된다. 그 수익률은 풀을 더 매력적으로 만들어 호스팅하는 자산 쌍의 유동성을 깊게 한다.

    veTokenomics는 예상치 못한 결과를 낳았다: 투표-뇌물 시장이 등장했다. 자신의 토큰에 대한 더 깊은 유동성을 원하는 프로토콜이 veCRV 보유자에게 자신의 풀로 게이지 투표를 유도하도록 지불한다. 실제로 프로토콜은 오늘 투표자에게 뇌물을 주어 미래 CRV 배출의 한 몫을 산다. 이것은 대리인 카르텔과 새로운 형태의 지대 추출을 만들었지만, 배출(따라서 유동성)이 어디로 흐르는지에 대한 거버넌스 영향력에 대한 진정한 경제적 수요를 드러내기도 했다.

    #### 이차 투표

    이차 투표(Quadratic Voting)에서 k표의 비용은 k²이다. 일반적으로 고정 예산 하에서 투표 크레딧으로 지불하며, 시스템은 각 참가자가 고유한 사람임을 확인하여 한 사람이 여러 사람인 척하는 것을 방지해야 한다. 이 시스템에서 한 표를 던지려면 한 크레딧이 필요하지만, 두 표를 던지려면 네 크레딧(2²)이, 세 표를 던지려면 아홉 크레딧(3²)이 필요하며, 이런 식으로 계속된다.

    이것은 부유한 참가자나 주체가 의사결정 과정에서 불균형적인 통제력을 축적하는 것을 방지하는 데 도움이 된다. 추가 투표를 던지는 데 기하급수적으로 더 많은 크레딧을 요구함으로써, 이차 투표는 순전한 토큰 축적을 통해 과두제가 거버넌스를 지배하는 위험을 완화하고 대형 이해관계자의 부가 네트워크 거버넌스에 대한 과도한 정치적 영향력으로 직접 번역되는 것을 줄인다.

    #### 실험적 프론티어: 퓨타키

    이러한 확립된 모델들을 넘어, 거버넌스 설계 공간은 집단 의사결정이 어떻게 이루어져야 하는지에 대한 근본적인 가정에 도전하는 더 이국적인 실험들로 계속 진화하고 있다.

    퓨타키(Futarchy)는 근본적으로 다른 접근법을 취한다: "가치에 투표하고, 신념에 베팅하라." 토큰 보유자들은 고수준의 목표(예: "프로토콜 TVL 최대화")에 투표하지만, 그 목표를 어떻게 달성할지에 대한 결정은 예측 시장을 통해 이루어진다. TVL은 프로토콜에 예치된 자산의 총 가치를 의미하며, 프로토콜 규모의 일반적인 척도이다. 수수료 파라미터를 변경하는 제안은 두 개의 시장을 생성한다: "제안이 통과되면 프로토콜 TVL"과 "제안이 실패하면 프로토콜 TVL". 제안은 어느 시장이 더 높은 TVL을 예측하는지에 따라 자동으로 실행된다. 이론은 우아하다: 의사결정 시장은 투표보다 분산된 정보를 더 효율적으로 집계하면서, 기술적 질문에 대한 다수의 횡포를 방지한다.

    Gnosis의 조건부 시장과 같은 초기 실험들은 광범위한 프로토콜 수준 채택에 이르지 못했다. 더 최근에는 솔라나의 MetaDAO가 예측 시장이 제안을 단순히 알리기보다 *결정*하도록 실제로 퓨타키를 거버넌스에 연결하는 데까지 갔다. 그러나 퓨타키는 여전히 틈새 실험으로 남아 있다: 시스템적으로 중요한 DeFi 프로토콜 중 핵심 통제를 이 모델에 넘긴 곳은 아직 없다. 주로 깊고 유동적인 시장, 명확한 온체인 메트릭, 그리고 시장이 전통적인 토큰 투표를 무효화하도록 허용할 의향이 있는 커뮤니티가 필요하기 때문이다.

    #### 거버넌스 공격: 민주주의가 하이재킹될 때

    최악의 시나리오는 투표자 무관심이 아니라 적극적인 악용이다. 플래시론 거버넌스 공격(제7장에서 설명한 무담보 차입 메커니즘 사용)은 대량의 거버넌스 토큰을 빌리고, 악의적인 제안을 통과시키기 위해 투표하고, 토큰을 반환하는 것을 모두 단일 트랜잭션 내에서 수행한다. 2022년 4월, Beanstalk DAO가 정확히 이 운명을 겪었다: 공격자가 Aave에서 플래시론으로 10억 달러 상당의 다양한 자산을 빌리고, 이를 사용하여 STALK(Beanstalk의 Silo 메커니즘을 통해 축적되는 거버넌스 파워)를 축적하여 67% 투표권을 얻고, 재무부에서 1억 8,200만 달러를 자신의 지갑으로 이전하는 악의적인 제안을 통과시키고, 실행했다. 전체 공격은 단일 이더리움 트랜잭션 내에서, 몇 초 내에 완료되었다. 커뮤니티가 알아차렸을 때, 자금은 이미 사라졌다.

    이에 대한 방어는 어떤 단일 메커니즘이 아니라 계층화된 타이밍 시스템이다. 스냅샷 기반 투표가 기초적인 보호다: 투표권은 제안이 생성될 때 설정된 과거 특정 블록의 토큰 잔액으로 결정된다. 투표 기간 동안 토큰을 빌린 공격자는 스냅샷 시점에 해당 토큰을 보유하지 않았기 때문에 투표권이 0이다. 이것은 투표 지연(제안 생성과 투표 시작 사이의 시간으로, 스냅샷이 효과적으로 잠기게 함)과 투표 기간(투표가 던져질 수 있는 창)과 결합된다. 마지막으로, 타임락은 투표 통과와 실행 사이에 지연을 추가하여 커뮤니티가 의심스러운 결과나 발견된 버그에 반응할 시간을 준다.

    Beanstalk의 치명적인 실수는 스냅샷 메커니즘이나 타임락 지연 없이 제안이 같은 블록 내에서 통과되고 실행되도록 허용한 것이었다. 현대 거버넌스 시스템은 온체인 또는 Snapshot 같은 오프체인 도구를 통해 고정된 시점의 토큰 잔액을 기록하여 일시적인 토큰 획득을 통한 투표권 조작을 방지한다. 그러나 정교한 공격은 진화한다: 거버넌스 뇌물은 토큰 보유자에게 특정 방식으로 투표하도록 지불하고, 제안 스팸은 악의적인 변경을 숨기기 위해 노이즈로 거버넌스를 막고, 51% 공격은 영구적인 통제를 얻기 위해 천천히 토큰을 축적하는 것을 포함한다.

    #### 메타 레슨

    어떤 단일 메커니즘도 디지털 민주주의를 해결하지 못한다. "최선의" 시스템은 무엇이 통치되는지, 이해관계자가 누구인지, 커뮤니티가 얼마나 많은 복잡성을 다룰 수 있는지에 따라 달라진다.

    일부 프로젝트는 급진적인 접근법을 취하고 있다: 거버넌스가 어떻게 통제하는지를 완벽하게 하기보다, 거버넌스가 통제할 수 있는 것을 줄이는 것이다. 이 거버넌스 최소화 추세는 Uniswap의 AMM 코어(v3/v4)와 같은 불변 프로토콜, 알고리즘적 파라미터 설정, 제한된 수수료 스위치, 그리고 코드를 동결하거나 거버넌스 범위를 제한하는 것을 공개적으로 목표로 하는 프로젝트(예: Lido의 "최소 거버넌스" 방향)를 포함한다. 또한 특정 결정을 인간의 재량에서 완전히 제거하는 헌법적 제약도 포함한다.

    논리는 다음과 같다: 거버넌스가 금권정치, 무관심, 또는 탈취를 통해 필연적으로 결함이 있다면, 통치할 수 있는 것을 줄여 공격 표면을 최소화하라. 트레이드오프는 명백하다: 적응성 감소. 시장 조건이 변하거나 새로운 기회가 생기면, 이러한 시스템은 빠르게 전환할 수 없다. 그러나 신뢰할 수 있는 중립성과 내부 정치 및 외부 압력에 대한 저항을 얻는다.

## Section II: From Discord Drama to On-Chain Democracy

=== "EN"

    But for the protocols that do embrace active governance, how do these theoretical mechanisms actually work in practice? Let's follow a real proposal through the complete lifecycle of DAO decision-making.

    Suppose a proposer aims to add a new 0.15% fee tier for certain trading pairs on Uniswap. A vote cannot simply be submitted and left to chance. Successful DAO governance follows a carefully orchestrated process designed to prevent chaos, build consensus, and avoid costly mistakes.

    ### The Proposal Lifecycle

    #### Stage 1: The RFC Phase

    Every proposal starts with conversation. The proposer posts a new fee-tier proposal on Uniswap's governance forum, explaining the reasoning: a 0.15% tier could capture trading volume that currently splits between the 0.05% and 0.3% tiers. This would optimize liquidity provision for mid-volatility pairs. Then the proposer shares the link on Uniswap's Discord to increase visibility. Responses start appearing. Some participants support it ("This could address the liquidity gaps we've been seeing"), others oppose it ("We have enough tiers already"), and technical reviewers start scrutinizing the math.

    This informal discussion phase, often called a Request for Comment (RFC), serves as a crucial filter. Bad ideas get shot down before wasting anyone's time or money. Good ideas get refined through community feedback. A simple fee-tier addition evolves into a nuanced plan with specific technical parameters, implementation timelines, and analysis of how it might affect existing liquidity across other tiers.

    #### Stage 2: The Temperature Check and Consensus Check (Snapshot Polling)

    Once the proposal has survived the Discord and forum gauntlet, preliminary votes begin. Uniswap uses a two-phase Snapshot process (a temperature check and then a consensus check), although many protocols use just one. Snapshot is a gasless, off-chain voting platform that lets the community signal support without spending any money on transaction fees.

    By this point, most of the real refinement should already have happened in the RFC phase: parameters debated, edge cases surfaced, alternatives considered. The temperature check is less about redesigning the proposal and more about answering a simpler question: *"Is there enough rough consensus to justify taking this on-chain in its current form?"* If support is weak or sharply split, the idea usually goes back to the forum for another round (or quietly dies). If support is strong, the proposer can move forward with confidence.

    If the temperature check passes the minimum threshold, the proposer moves to a consensus check with a near-final version. This second round of Snapshot voting (with short polls and minimum yes-vote thresholds) must also hit specific requirements before proceeding on-chain. As discussed earlier, the platform prevents manipulation by recording voting power at a fixed block before voting begins, so attackers cannot borrow tokens, vote, and return them within a single transaction. (The platform's name comes from this "snapshot" of token balances at a specific block number.)

    #### Stage 3: The Formal Proposal (On-Chain Submission)

    If the consensus check passes the minimum threshold, the proposal moves to official status. Submitting an on-chain governance proposal requires skin in the game: the proposer must have substantial UNI delegated (currently representing significant value) just to create the proposal. This ensures only serious proposals with significant backing make it this far.

    The proposal contains more than text: it encodes a specific set of on-chain actions that will be triggered if the vote passes. These actions specify what contracts to call, which functions to execute, and with what parameters. In our Uniswap example, that means specifying exactly which new fee tier to add, how the factory contracts should be updated, and what happens during the transition period. There's no room for ambiguity: the exact instructions describing those function calls are the proposal itself.

    #### Stage 4: The Voting Period (Democracy in Action)

    For the next 7 days, token holders cast their votes. Unlike traditional elections, individual vote choices are visible in real time. Whale wallets, small holders, and delegates all participate in a transparent process where every vote is recorded on-chain forever.

    But here's where delegation culture becomes crucial: large delegates and the Uniswap Foundation's governance portal heavily influence outcomes. Social consensus built through forum discussions and delegate calls often determines the proposal's fate before the on-chain vote even begins. The proposal needs significant token support to reach quorum and pass.

    Despite billions at stake, typical voter participation rates hover around 3-5% of total token supply in most DAOs, and quorum failures are common even among the top 100 protocols.

    #### Stage 5: The Execution (Code Becomes Law)

    If the proposal passes with sufficient support, the timelock safeguard kicks in. The changes are queued for a minimum delay (and potentially longer for more sensitive changes), giving the community time to react if someone spotted a critical bug in the implementation code or if the proposal passed through manipulation.

    Most DAOs don't trust pure on-chain governance for critical operations. A **multi-sig wallet** requires multiple trusted parties (typically 5 out of 9 signers, or 6 out of 10) to approve sensitive actions like emergency pauses, cancelling or vetoing queued proposals, or executing upgrades within a narrowly defined scope. These multisigs act as both operational security (no single private key can unilaterally act) and governance backstops during timelock periods.

    The trade-off is re-centralization, but in practice the powers are usually constrained by contract design: many multisigs cannot arbitrarily drain the treasury or rewrite core logic, they can only trigger specific admin functions the DAO has pre-authorized. Even so, this still creates a privileged "emergency brake" layer controlled by a small group of signers, whose identities are typically public and documented for accountability.

    #### Treasury Operations and Multi-Sig Reality

    DAOs collectively control tens of billions of dollars in digital assets, yet most lack sophisticated treasury management strategies. The typical DAO treasury holds primarily its own governance token plus stablecoins for operational expenses. This creates circular dependencies where treasury value crashes with token price. More mature DAOs are diversifying into ETH, BTC, and yield-bearing assets, though every diversification requires contentious governance votes.

    Should treasuries deploy capital into DeFi protocols to generate yield (adding smart contract risk)? Should they invest in other protocols' tokens (creating conflicts of interest)? Should they hold physical assets or traditional securities (requiring legal entities)? Most DAOs solve this by creating specialized treasury committees with delegated authority for routine operations, reserving major decisions for token holder votes. But accountability remains murky: unlike corporate boards, DAO treasury managers face no fiduciary duties and limited legal recourse if funds are mismanaged.

    Once the timelock expires and no emergency action has been taken, anyone can trigger the execution. In our Uniswap example, this updates the factory contracts to support the new 0.15% fee tier, and liquidity providers can begin creating pools with this option.

    #### Tooling

    This entire process is supported by a growing stack of specialized tools. Safe (formerly Gnosis Safe) provides multi-sig wallet infrastructure for treasury security. Governance platforms like Tally offer dashboards where participants can track proposals, view voting history, analyze delegate performance, and cast votes. Discussion platforms like Discourse and Commonwealth host the initial debates and RFC threads, while Snapshot enables gasless off-chain voting for temperature checks. Together, these tools transform raw smart contracts into functional governance systems that humans can actually navigate.

    ### The Social Layer

    But these tools are merely infrastructure for the real action. The actual work of DAO governance happens in Discord channels, forum debates, and delegate calls long before anyone casts a vote. A small group of core contributors and engaged community members vet proposals, refine ideas, and build consensus through informal discussions. These dozens of highly active participants shape governance while thousands of token holders remain passive observers, and this concentration of engagement is both essential for quality decision-making and a vulnerability when contributors burn out.

    And burn out they do. Contributing to DAO governance is often thankless work: endless Discord debates, technical proposal reviews, community conflict resolution, and the constant pressure of making million-dollar decisions with incomplete information. Many DAOs struggle to retain top contributors because compensation is inconsistent, decision-making is chaotic, and the same few people shoulder disproportionate responsibility without the authority or support structures of traditional organizations. When key contributors leave, institutional knowledge evaporates and governance quality degrades, sometimes irreversibly.

    A handful of professional delegates dominate governance across multiple DAOs, accumulating voting power and influence that can determine any proposal's outcome. These delegates bring expertise and consistency but also represent a recentralization of power, sometimes coordinating across protocols to advance shared interests. By the time proposals reach on-chain voting, social consensus among these key stakeholders has usually already sealed their fate, making formal votes largely a ratification of decisions reached through back-channel coordination.

    The most successful DAOs accept that purely decentralized governance is a fiction. They invest in community building, compensate sustained contribution, and maintain transparency about which decisions require broad consensus versus expert judgment. Effective governance emerges not from perfect voting mechanisms but from cultivating communities of people who care enough to show up consistently, coordinate despite pseudonymity, and navigate the tension between democratic ideals and the practical need for efficient decision-making by informed participants.

=== "KO"

    그러나 적극적인 거버넌스를 수용하는 프로토콜들에게, 이러한 이론적 메커니즘이 실제로 어떻게 작동할까? 실제 제안이 DAO 의사결정의 완전한 수명 주기를 거치는 과정을 따라가 보자.

    제안자가 Uniswap의 특정 거래 쌍에 새로운 0.15% 수수료 티어를 추가하는 것을 목표로 한다고 가정하자. 투표를 단순히 제출하고 운에 맡길 수는 없다. 성공적인 DAO 거버넌스는 혼란을 방지하고, 합의를 구축하고, 비용이 많이 드는 실수를 피하기 위해 신중하게 조율된 프로세스를 따른다.

    ### 제안 수명 주기

    #### 1단계: RFC 단계

    모든 제안은 대화로 시작한다. 제안자가 Uniswap의 거버넌스 포럼에 새로운 수수료 티어 제안을 게시하고 논리를 설명한다: 0.15% 티어가 현재 0.05%와 0.3% 티어 사이에서 분할되는 거래량을 포착할 수 있다. 이것은 중간 변동성 쌍에 대한 유동성 공급을 최적화할 것이다. 그런 다음 제안자가 가시성을 높이기 위해 Uniswap의 디스코드에서 링크를 공유한다. 응답이 나타나기 시작한다. 일부 참여자는 지지하고("이것은 우리가 보아온 유동성 갭을 해결할 수 있습니다"), 다른 이들은 반대하며("우리는 이미 충분한 티어가 있습니다"), 기술 리뷰어들이 수학을 면밀히 조사하기 시작한다.

    코멘트 요청(Request for Comment, RFC)이라고 종종 불리는 이 비공식 토론 단계는 중요한 필터 역할을 한다. 나쁜 아이디어는 누구의 시간이나 돈을 낭비하기 전에 걸러진다. 좋은 아이디어는 커뮤니티 피드백을 통해 다듬어진다. 단순한 수수료 티어 추가가 특정 기술 파라미터, 구현 타임라인, 그리고 다른 티어에 걸쳐 기존 유동성에 어떤 영향을 미칠 수 있는지에 대한 분석을 포함한 세련된 계획으로 진화한다.

    #### 2단계: 온도 체크와 합의 체크 (스냅샷 투표)

    제안이 디스코드와 포럼의 관문을 통과하면, 예비 투표가 시작된다. Uniswap은 두 단계 스냅샷 프로세스(온도 체크와 합의 체크)를 사용하지만, 많은 프로토콜은 하나만 사용한다. 스냅샷(Snapshot)은 가스 없는 오프체인 투표 플랫폼으로 커뮤니티가 트랜잭션 수수료에 돈을 쓰지 않고 지지를 표시할 수 있게 한다.

    이 시점에서 대부분의 실제 개선은 이미 RFC 단계에서 이루어졌어야 한다: 파라미터 토론, 엣지 케이스 표면화, 대안 고려. 온도 체크는 제안을 재설계하는 것보다 더 간단한 질문에 답하는 것에 가깝다: *"현재 형태로 이것을 온체인으로 가져갈 것을 정당화할 만큼 충분한 대략적인 합의가 있는가?"* 지지가 약하거나 심하게 분열되면, 아이디어는 보통 또 다른 라운드를 위해 포럼으로 돌아가거나(또는 조용히 사라진다). 지지가 강하면, 제안자는 확신을 가지고 전진할 수 있다.

    온도 체크가 최소 임계값을 통과하면, 제안자는 거의 최종 버전으로 합의 체크로 이동한다. 이 두 번째 라운드의 스냅샷 투표(짧은 투표와 최소 찬성 투표 임계값)도 온체인으로 진행하기 전에 특정 요구 사항을 충족해야 한다. 앞서 논의한 대로, 플랫폼은 투표가 시작되기 전에 고정된 블록에서 투표권을 기록하여 조작을 방지하므로, 공격자가 토큰을 빌리고, 투표하고, 단일 트랜잭션 내에서 반환할 수 없다. (플랫폼의 이름은 특정 블록 번호의 토큰 잔액 "스냅샷"에서 유래한다.)

    #### 3단계: 공식 제안 (온체인 제출)

    합의 체크가 최소 임계값을 통과하면, 제안은 공식 상태로 이동한다. 온체인 거버넌스 제안을 제출하려면 피부가 게임에 있어야 한다: 제안자는 상당한 가치를 나타내는 UNI를 위임받아야만 제안을 생성할 수 있다. 이것은 상당한 지원을 가진 진지한 제안만이 여기까지 오도록 보장한다.

    제안에는 텍스트 이상의 것이 포함된다: 투표가 통과되면 트리거될 특정 온체인 액션 세트를 인코딩한다. 이러한 액션들은 어떤 컨트랙트를 호출할지, 어떤 함수를 실행할지, 어떤 파라미터로 할지를 명시한다. 우리의 Uniswap 예에서, 이것은 정확히 어떤 새로운 수수료 티어를 추가할지, 팩토리 컨트랙트가 어떻게 업데이트되어야 하는지, 전환 기간 동안 무엇이 일어나는지를 명시하는 것을 의미한다. 모호함의 여지가 없다: 그러한 함수 호출을 설명하는 정확한 지침이 제안 그 자체이다.

    #### 4단계: 투표 기간 (민주주의 실행)

    다음 7일 동안 토큰 보유자들이 투표를 한다. 전통적인 선거와 달리, 개별 투표 선택은 실시간으로 볼 수 있다. 고래 지갑, 소규모 보유자, 대리인 모두가 모든 투표가 영원히 온체인에 기록되는 투명한 프로세스에 참여한다.

    그러나 여기서 위임 문화가 중요해진다: 대형 대리인과 Uniswap 재단의 거버넌스 포털이 결과에 크게 영향을 미친다. 포럼 토론과 대리인 회의를 통해 구축된 사회적 합의가 종종 온체인 투표가 시작되기 전에 제안의 운명을 결정한다. 제안이 정족수에 도달하고 통과하려면 상당한 토큰 지지가 필요하다.

    수십억 달러가 걸려 있음에도 불구하고, 대부분의 DAO에서 일반적인 투표 참여율은 총 토큰 공급량의 약 3-5% 수준이며, 상위 100개 프로토콜에서도 정족수 실패가 흔하다.

    #### 5단계: 실행 (코드가 법이 된다)

    제안이 충분한 지지로 통과되면, 타임락 세이프가드가 작동한다. 변경 사항은 최소 지연(그리고 더 민감한 변경의 경우 잠재적으로 더 긴 지연)을 위해 대기열에 넣어지며, 커뮤니티가 구현 코드에서 치명적인 버그를 발견하거나 제안이 조작을 통해 통과된 경우 반응할 시간을 준다.

    대부분의 DAO는 중요한 운영에 순수한 온체인 거버넌스를 신뢰하지 않는다. **다중 서명 지갑(Multi-sig Wallet)**은 긴급 일시정지, 대기 중인 제안의 취소 또는 거부권 행사, 또는 좁게 정의된 범위 내에서 업그레이드를 실행하는 것과 같은 민감한 행동을 승인하기 위해 여러 신뢰할 수 있는 당사자들(일반적으로 9명 중 5명 또는 10명 중 6명의 서명자)을 요구한다. 이러한 멀티시그는 운영 보안(단일 개인키가 일방적으로 행동할 수 없음)과 타임락 기간 동안의 거버넌스 백스톱 역할을 한다.

    트레이드오프는 재중앙화이지만, 실제로 권한은 일반적으로 컨트랙트 설계에 의해 제약된다: 많은 멀티시그는 임의로 재무부를 빼거나 핵심 로직을 다시 작성할 수 없으며, DAO가 사전 승인한 특정 관리 함수만 트리거할 수 있다. 그럼에도 불구하고, 이것은 여전히 소수의 서명자 그룹이 통제하는 특권적인 "비상 브레이크" 레이어를 만들며, 그들의 신원은 일반적으로 책임을 위해 공개되고 문서화된다.

    #### 재무 운영과 멀티시그 현실

    DAO들은 집합적으로 수백억 달러의 디지털 자산을 통제하지만, 대부분은 정교한 재무 관리 전략이 부족하다. 일반적인 DAO 재무부는 주로 자체 거버넌스 토큰과 운영 비용을 위한 스테이블코인을 보유한다. 이것은 재무부 가치가 토큰 가격과 함께 하락하는 순환적 의존성을 만든다. 더 성숙한 DAO들은 ETH, BTC, 수익 창출 자산으로 다각화하고 있지만, 모든 다각화에는 논쟁적인 거버넌스 투표가 필요하다.

    재무부가 수익을 창출하기 위해 DeFi 프로토콜에 자본을 배치해야 할까(스마트 컨트랙트 리스크 추가)? 다른 프로토콜의 토큰에 투자해야 할까(이해 충돌 생성)? 물리적 자산이나 전통 증권을 보유해야 할까(법인 필요)? 대부분의 DAO는 일상 운영에 대한 위임 권한을 가진 전문 재무 위원회를 만들어 이를 해결하고, 주요 결정은 토큰 보유자 투표에 맡긴다. 그러나 책임은 모호하게 남아 있다: 기업 이사회와 달리, DAO 재무 관리자들은 수탁 의무가 없고 자금이 잘못 관리되면 법적 구제가 제한된다.

    타임락이 만료되고 긴급 조치가 취해지지 않으면, 누구나 실행을 트리거할 수 있다. 우리의 Uniswap 예에서, 이것은 새로운 0.15% 수수료 티어를 지원하도록 팩토리 컨트랙트를 업데이트하고, 유동성 공급자들은 이 옵션으로 풀을 생성할 수 있다.

    #### 도구

    이 전체 프로세스는 특수화된 도구들의 성장하는 스택에 의해 지원된다. Safe(이전 Gnosis Safe)는 재무 보안을 위한 멀티시그 지갑 인프라를 제공한다. Tally와 같은 거버넌스 플랫폼은 참여자들이 제안을 추적하고, 투표 기록을 보고, 대리인 성과를 분석하고, 투표를 던질 수 있는 대시보드를 제공한다. Discourse와 Commonwealth와 같은 토론 플랫폼은 초기 토론과 RFC 스레드를 호스팅하고, 스냅샷은 온도 체크를 위한 가스 없는 오프체인 투표를 가능하게 한다. 이러한 도구들이 함께 원시 스마트 컨트랙트를 인간이 실제로 탐색할 수 있는 기능적 거버넌스 시스템으로 변환한다.

    ### 소셜 레이어

    그러나 이러한 도구들은 단지 실제 행동을 위한 인프라일 뿐이다. DAO 거버넌스의 실제 작업은 누구든 투표를 던지기 훨씬 전에 디스코드 채널, 포럼 토론, 대리인 회의에서 일어난다. 소수의 핵심 기여자와 참여하는 커뮤니티 멤버들이 제안을 검토하고, 아이디어를 다듬고, 비공식 토론을 통해 합의를 구축한다. 이러한 수십 명의 고도로 활동적인 참여자들이 수천 명의 토큰 보유자들이 수동적인 관찰자로 남아 있는 동안 거버넌스를 형성하며, 이러한 참여의 집중은 질 높은 의사결정에 필수적이면서도 기여자들이 지칠 때 취약점이 된다.

    그리고 그들은 지친다. DAO 거버넌스에 기여하는 것은 종종 보상 없는 일이다: 끝없는 디스코드 토론, 기술 제안 검토, 커뮤니티 갈등 해결, 그리고 불완전한 정보로 백만 달러 규모의 결정을 내리는 끊임없는 압박. 많은 DAO가 최고의 기여자를 유지하는 데 어려움을 겪는다. 보상이 일관되지 않고, 의사결정이 혼란스럽고, 같은 소수의 사람들이 전통적인 조직의 권한이나 지원 구조 없이 불균형적인 책임을 진다. 핵심 기여자들이 떠나면, 제도적 지식이 증발하고 거버넌스 품질이 하락한다. 때로는 회복 불가능하게.

    소수의 전문 대리인들이 여러 DAO에 걸쳐 거버넌스를 지배하며, 어떤 제안의 결과도 결정할 수 있는 투표권과 영향력을 축적한다. 이러한 대리인들은 전문성과 일관성을 가져오지만 권력의 재중앙화를 나타내며, 때로는 공유된 이익을 추진하기 위해 프로토콜 간에 조율한다. 제안이 온체인 투표에 도달할 때쯤, 이러한 핵심 이해관계자들 간의 사회적 합의가 보통 이미 그들의 운명을 결정했기 때문에, 공식 투표는 대체로 백채널 조율을 통해 도달한 결정의 비준이 된다.

    가장 성공적인 DAO는 순수하게 탈중앙화된 거버넌스가 허구임을 받아들인다. 커뮤니티 빌딩에 투자하고, 지속적인 기여에 보상하며, 어떤 결정이 광범위한 합의를 필요로 하는지 대 전문가 판단을 필요로 하는지에 대해 투명성을 유지한다. 효과적인 거버넌스는 완벽한 투표 메커니즘에서가 아니라, 일관되게 나타나고, 익명성에도 불구하고 조율하고, 민주적 이상과 정보를 가진 참여자들의 효율적인 의사결정에 대한 실질적 필요 사이의 긴장을 탐색할 만큼 충분히 신경 쓰는 사람들의 커뮤니티를 육성하는 것에서 나온다.

## Section III: Token Economics and Distribution

=== "EN"

    But what drives people to participate in this messy, time-consuming process in the first place? Why should anyone spend weeks crafting proposals, debating in Discord, and mobilizing millions of dollars worth of voting power? The answer lies in how governance tokens are designed and distributed. A poorly designed token economy creates apathy and manipulation. A well-designed one aligns individual incentives with collective success.

    ### The Token Designer's Dilemma

    Creating a governance token is like designing a new form of money, voting system, and incentive structure all at once. Get it right, and you create a self-sustaining ecosystem where participants are motivated to contribute to long-term success. Get it wrong, and you end up with mercenary capital, voter apathy, and governance attacks.

    The challenge starts with a fundamental question: What should a token actually do?

    #### The Four Flavors of Token Value

    ##### Pure Governance Tokens: The Democratic Bet

    These tokens operate on a simple premise: ownership grants voting rights, and voting rights determine the protocol's future. Holders can propose changes, vote on protocol parameters, and shape strategic decisions. There's no guaranteed income stream or built-in utility beyond governance participation. Value comes entirely from the market's belief that governance control will be valuable as the protocol grows and evolves. Governance tokens give token holders a clean slate but they can evolve into other types by voting.

    Take Uniswap's UNI token: hold it, vote with it, hope the protocol succeeds. No immediate utility, no guaranteed returns. Just the right to shape a protocol's future. It's like owning shares in a company that might never pay dividends, where your only value comes from other people wanting to buy your voting rights. Risky? Absolutely. But when governance decisions can unlock billions in value (like enabling fee switches), those voting rights become incredibly valuable.

    ##### Revenue-Sharing Tokens: The Dividend Play

    Revenue-sharing tokens distribute protocol earnings directly to holders based on their stake. When the protocol generates fees, trading revenue, or other income, it flows proportionally to token holders who stake or lock their tokens. It's the most straightforward value proposition: the more successful the protocol, the more money flows to token holders.

    Some tokens cut straight to the chase: hold them, earn money. When dYdX generates trading fees, it distributes a portion of them directly to DYDX stakers. No complex governance required, just stake your tokens and collect your share of protocol revenue. It's the closest thing to traditional dividend-paying stocks in DeFi, but with the added complexity of smart contract risk and token price volatility.

    ##### Buyback-and-Burn Tokens: The Scarcity Game

    Instead of distributing profits, this approach uses protocol revenue to purchase tokens from the open market and permanently destroy them. The buying creates upward price pressure, while burning reduces total supply over time. The theory is that decreasing supply plus steady or growing demand equals higher token prices. Success depends entirely on the protocol generating substantial and consistent revenue.

    Hyperliquid (examined in depth in Chapter X) takes this approach with HYPE. Instead of distributing profits, the protocol uses revenue to buy HYPE tokens from the market and burn them forever. Buying tokens creates constant buy pressure, burning tokens makes the remaining supply scarcer. It's like a stock buyback program but relies on the protocol generating meaningful revenue.

    ##### Utility Tokens: Pay-to-Play

    These tokens function as the native currency for accessing protocol services. Users must hold or spend the token to interact with the protocol, creating natural demand independent of speculation or governance participation. The stronger the demand for the protocol's services, the stronger the demand for the token. However, this model faces the risk of being displaced if competitors offer superior services.

    Chainlink's LINK token serves a clear function: paying for oracle services. Today, Data Streams supports payment in assets other than LINK (with a surcharge), while Functions bills in LINK. Holding LINK varies by service. This creates natural demand regardless of governance participation while maintaining payment flexibility. The downside? If someone builds a better oracle, your token's utility (and value) could evaporate overnight.

    #### The Supply Dilemma: Scarcity vs. Sustainability

    Every token designer faces the same impossible choice: create scarcity to drive value, or ensure enough tokens exist to fund long-term development. It's like trying to be both Bitcoin and the Federal Reserve simultaneously.

    ##### Fixed Supply: The Bitcoin Approach

    Some protocols launch with a hard cap: say, 100 million tokens, never to be increased. This creates scarcity and can drive price appreciation, but it also creates a funding problem. How are developers paid in year five when the initial token allocation is exhausted? Uniswap's initial tokenomics, for example, defined a total supply of 1 billion UNI with the option for governance to introduce up to 2% annual perpetual inflation after the initial four-year distribution schedule. The mechanism exists on paper to fund ongoing development and ecosystem growth, but actually activating it is a political choice that token holders must vote on.

    ##### Inflation: The Central Bank Model

    Other protocols embrace inflation from the start. New tokens are minted continuously to fund development, liquidity incentives, and governance participation. It's sustainable but dilutive. Every new token reduces the percentage ownership of existing holders. The key is keeping inflation low enough that protocol growth outpaces token dilution.

    ##### Deflation: The Scarcity Spiral

    The most aggressive approach burns tokens faster than they're created, shrinking supply over time. Ethereum's EIP-1559 burns ETH with every transaction, and many DeFi protocols burn tokens using revenue. It sounds great for holders until tokens become so valuable that people stop using them for governance, defeating the entire purpose.

    #### Vesting: Preventing the Founder Dump

    Nothing kills a DAO faster than founders showing no conviction in the tokens they created. Vesting schedules solve this by locking up insider allocations for years, but they create their own dynamics and predictable market pressures.

    ##### The Industry Standard: 1+3 Vesting

    Most legitimate projects use a "1+3" schedule: a 1-year **cliff** with zero token releases, followed by 3 years of linear vesting where approximately 1/36th of the allocation unlocks monthly. This structure is simple, legible to investors, and ensures team and investor alignment while creating predictable moments of potential selling pressure.

    ##### The Cliff Effect and Supply Overhang

    That initial cliff release often triggers significant selling as insiders finally gain liquidity after a year of lockup. But not all unlocked tokens hit markets immediately. Supply overhang models combine vesting calendars with holder behavior assumptions to anticipate actual selling pressure rather than just theoretical supply. Different recipients have very different incentives: venture capital funds might liquidate aggressively to realize gains or rebalance, while teams might hold longer to signal commitment or avoid tanking their own token.

    ##### Hedging Against Unlocks

    Sophisticated recipients often hedge their vesting allocations rather than selling immediately. By taking short positions in perpetual futures (the instrument covered in Chapter VI), insiders can lock in current prices without dumping their tokens on the spot market. If the token price falls, their short position profits and offsets the loss in value of their locked tokens. This strategy shifts selling pressure from spot markets to derivatives markets. As a result, major unlock events can create visible effects in derivatives pricing: funding rates (the periodic payments between long and short traders) may turn negative as more traders go short, and the gap between futures and spot prices may widen. Traders watch these signals to anticipate unlock-related pressure even when spot selling remains muted.

    ##### Linear vs. Milestone Vesting

    Linear vesting releases tokens gradually and predictably over time, making supply schedules easy to model and communicate. Milestone-based vesting instead ties token releases to specific achievements such as user growth, revenue targets, feature launches, or protocol KPIs. Milestone vesting better aligns incentives with performance, but it introduces uncertainty about when tokens will actually hit circulation, complicating supply forecasts and making it harder for markets to price in future unlocks.

    ### The Distribution Wars: Who Gets the Tokens?

    How tokens are distributed determines who controls a DAO. Give too many to insiders, and a plutocracy is created. Give too many to random users, and apathetic governance results. The crypto world has experimented with four main distribution strategies, each with dramatic successes and spectacular failures.

    #### Retroactive Airdrops

    Uniswap's legendary 2020 airdrop set the gold standard for token distributions, instantly creating community ownership by rewarding nearly every wallet that had interacted with the protocol. The message was crystal clear: early adopters had helped build the protocol and now owned part of it.

    But success bred imitation and unintended consequences. Once future airdrops became anticipated events, user behavior fundamentally shifted. Instead of genuinely engaging with protocols, people began using them solely to qualify for potential token rewards. This spawned industrial-scale **"airdrop farming"** operations running tens of thousands of wallets, each trying to game anticipated criteria. This dynamic corrupted the very metrics protocols use to demonstrate traction: usage numbers, unique wallets, and TVL became increasingly unreliable indicators, often artificially inflated by farmers rather than reflecting genuine adoption.

    The result is a destructive cycle: Protocols hint at generous airdrops (sometimes leaked to insiders), which drives apparent usage and impressive metrics. These inflated numbers help secure high-valuation funding rounds from VCs. But once the airdrop occurs and farming incentives disappear, activity typically collapses. Only a handful of protocols have retained meaningful engagement post-airdrop without continuous incentives.

    Up and coming protocols now face a dilemma: they need artificial traction to bootstrap activity and raise funds while knowing that same traction will likely disappear post-token launch. Meanwhile, genuine users increasingly find themselves competing with sophisticated farming operations for limited token allocations. The irony is stark: a tool designed to democratize ownership has inadvertently professionalized it, creating a new inequality between industrial farmers and genuine users.

    #### Point Programs

    Point programs (a form of points farming introduced in Chapter VII's yield generation section) have evolved far beyond simple pre-launch incentives into sophisticated, ongoing engagement mechanisms that continue operating even after tokens launch. Unlike traditional one-and-done airdrops, modern point programs operate in "seasons", recurring periods typically lasting 3-6 months where users compete for rewards through sustained activity.

    This seasonal approach has become the dominant retention strategy because it directly addresses the post-airdrop abandonment problem. Rather than watching engagement collapse after token distribution, protocols can maintain user activity indefinitely through the promise of future seasons. Users who might otherwise move on after claiming initial rewards instead remain active, hoping to qualify for subsequent distributions.

    #### Two Strategic Approaches to Season Design

    The seasonal model has given rise to two distinct approaches to criteria transparency, each with strategic advantages:

    ##### Transparent Criteria Seasons

    These seasons publish exact point formulas and qualifying requirements upfront. Users know precisely how many transactions they need, what volume thresholds to hit, or which specific actions earn points. This transparency creates predictable behavior and allows protocols to direct user activity toward desired outcomes, whether increasing TVL, driving trading volume, or encouraging specific feature adoption.

    ##### Opaque "Guessing Game" Seasons

    These seasons deliberately obscure their criteria, creating speculation about which actions will be rewarded. This uncertainty serves multiple strategic purposes. It prevents gaming by making optimization impossible, encourages broader protocol exploration as users try different strategies, and maintains engagement through mystery and anticipation. These systems often retrospectively reward unexpected behaviors, perhaps favoring users who interacted during specific time windows, demonstrated loyalty during market downturns, or engaged with less popular features.

    ##### Strategic Implications and Market Impact

    This seasonal economy fundamentally transforms user relationships with protocols. Instead of extractive farming followed by abandonment, seasons create ongoing "membership" where users maintain positions and activity to remain eligible for future rewards. Protocols can leverage seasons to test new features, gather behavioral data, and build competitive moats through user lock-in.

    The success of seasonal point programs has made them virtually mandatory for new DeFi protocols, transforming crypto from a series of one-time incentive events into an ongoing "game" where users maintain positions across multiple protocols simultaneously, always positioning for the next season's rewards.

=== "KO"

    그러나 무엇이 사람들로 하여금 이 지저분하고 시간 소모적인 프로세스에 처음부터 참여하게 만드는가? 누군가가 왜 제안을 만드는 데 몇 주를 보내고, 디스코드에서 토론하고, 수백만 달러 가치의 투표권을 동원해야 하는가? 답은 거버넌스 토큰이 어떻게 설계되고 분배되는지에 있다. 잘못 설계된 토큰 경제는 무관심과 조작을 만든다. 잘 설계된 것은 개인의 인센티브를 집단적 성공과 정렬한다.

    ### 토큰 설계자의 딜레마

    거버넌스 토큰을 만드는 것은 새로운 형태의 화폐, 투표 시스템, 인센티브 구조를 한꺼번에 설계하는 것과 같다. 제대로 하면, 참여자들이 장기적 성공에 기여하도록 동기 부여되는 자체 유지 생태계를 만든다. 잘못하면, 용병 자본, 투표자 무관심, 거버넌스 공격으로 끝난다.

    도전은 근본적인 질문에서 시작된다: 토큰이 실제로 무엇을 해야 하는가?

    #### 토큰 가치의 네 가지 유형

    ##### 순수 거버넌스 토큰: 민주적 베팅

    이 토큰들은 간단한 전제에서 작동한다: 소유권이 투표권을 부여하고, 투표권이 프로토콜의 미래를 결정한다. 보유자들은 변경을 제안하고, 프로토콜 파라미터에 투표하고, 전략적 결정을 형성할 수 있다. 거버넌스 참여 외에 보장된 수익 흐름이나 내장된 유틸리티가 없다. 가치는 전적으로 프로토콜이 성장하고 진화함에 따라 거버넌스 통제가 가치 있을 것이라는 시장의 믿음에서 나온다. 거버넌스 토큰은 토큰 보유자에게 백지 상태를 주지만 투표를 통해 다른 유형으로 진화할 수 있다.

    Uniswap의 UNI 토큰을 예로 들어보자: 보유하고, 투표하고, 프로토콜이 성공하기를 바란다. 즉각적인 유틸리티도, 보장된 수익도 없다. 프로토콜의 미래를 형성할 권리만 있다. 배당금을 절대 지급하지 않을 수도 있는 회사의 주식을 소유하는 것과 같으며, 가치는 오직 다른 사람들이 당신의 투표권을 사려는 것에서 나온다. 위험한가? 절대적으로. 그러나 거버넌스 결정이 수수료 스위치 활성화와 같이 수십억 달러의 가치를 언락할 수 있을 때, 그 투표권은 엄청나게 가치 있어진다.

    ##### 수익 공유 토큰: 배당금 플레이

    수익 공유 토큰은 프로토콜 수익을 스테이크에 따라 보유자에게 직접 분배한다. 프로토콜이 수수료, 거래 수익, 또는 기타 수입을 창출하면, 토큰을 스테이킹하거나 락업한 토큰 보유자에게 비례하여 흐른다. 가장 직접적인 가치 제안이다: 프로토콜이 더 성공할수록, 토큰 보유자에게 더 많은 돈이 흐른다.

    일부 토큰은 바로 본론으로 들어간다: 보유하고, 돈을 번다. dYdX가 거래 수수료를 생성하면, 그 일부를 DYDX 스테이커에게 직접 분배한다. 복잡한 거버넌스가 필요 없다. 토큰을 스테이킹하고 프로토콜 수익의 몫을 수집하면 된다. DeFi에서 전통적인 배당금 지급 주식에 가장 가까운 것이지만, 스마트 컨트랙트 리스크와 토큰 가격 변동성의 추가 복잡성이 있다.

    ##### 바이백-앤-번 토큰: 희소성 게임

    이익을 분배하는 대신, 이 접근법은 프로토콜 수익을 사용하여 공개 시장에서 토큰을 구매하고 영구적으로 소멸시킨다. 구매는 가격 상승 압력을 만들고, 소각은 시간이 지남에 따라 총 공급을 줄인다. 이론은 공급 감소 + 안정적이거나 증가하는 수요 = 더 높은 토큰 가격이다. 성공은 전적으로 프로토콜이 상당하고 일관된 수익을 창출하는 데 달려 있다.

    Hyperliquid(제10장에서 심층 분석)가 HYPE로 이 접근법을 취한다. 이익을 분배하는 대신, 프로토콜은 수익을 사용하여 시장에서 HYPE 토큰을 구매하고 영원히 소각한다. 토큰 구매는 지속적인 매수 압력을 만들고, 토큰 소각은 남은 공급을 더 희소하게 만든다. 주식 환매 프로그램과 비슷하지만 프로토콜이 의미 있는 수익을 창출하는 데 의존한다.

    ##### 유틸리티 토큰: 플레이 투 플레이

    이 토큰들은 프로토콜 서비스에 접근하기 위한 네이티브 통화로 기능한다. 사용자들은 프로토콜과 상호작용하기 위해 토큰을 보유하거나 사용해야 하며, 투기나 거버넌스 참여와 무관하게 자연스러운 수요를 창출한다. 프로토콜 서비스에 대한 수요가 강할수록, 토큰에 대한 수요도 강해진다. 그러나 이 모델은 경쟁자가 우수한 서비스를 제공하면 대체될 위험에 직면한다.

    Chainlink의 LINK 토큰은 명확한 기능을 제공한다: 오라클 서비스 비용 지불. 현재 Data Streams는 LINK 외의 자산으로 결제를 지원하고(할증료 포함), Functions는 LINK로 청구한다. LINK 보유는 서비스에 따라 다르다. 이것은 거버넌스 참여와 무관하게 자연스러운 수요를 창출하면서 결제 유연성을 유지한다. 단점은? 누군가가 더 나은 오라클을 만들면, 토큰의 유틸리티(와 가치)가 하루아침에 증발할 수 있다.

    #### 공급 딜레마: 희소성 대 지속 가능성

    모든 토큰 설계자가 같은 불가능한 선택에 직면한다: 가치를 끌어올리기 위해 희소성을 만들 것인가, 아니면 장기 개발 자금을 위해 충분한 토큰이 존재하도록 할 것인가. 비트코인과 연방준비제도를 동시에 되려는 것과 같다.

    ##### 고정 공급: 비트코인 접근법

    일부 프로토콜은 하드 캡으로 출시한다: 예를 들어, 1억 토큰이고 절대 증가하지 않는다. 이것은 희소성을 만들고 가격 상승을 이끌 수 있지만, 펀딩 문제도 만든다. 초기 토큰 배분이 고갈되면 5년 차에 개발자들은 어떻게 급여를 받는가? 예를 들어 Uniswap의 초기 토크노믹스는 10억 UNI의 총 공급량을 정의했으며, 초기 4년 분배 일정 후 거버넌스가 연간 최대 2%의 영구 인플레이션을 도입할 수 있는 옵션이 있다. 메커니즘은 지속적인 개발과 생태계 성장에 자금을 대기 위해 문서상에 존재하지만, 실제로 활성화하는 것은 토큰 보유자들이 투표해야 하는 정치적 선택이다.

    ##### 인플레이션: 중앙은행 모델

    다른 프로토콜들은 처음부터 인플레이션을 수용한다. 새로운 토큰이 지속적으로 발행되어 개발, 유동성 인센티브, 거버넌스 참여에 자금을 댄다. 지속 가능하지만 희석적이다. 모든 새로운 토큰은 기존 보유자의 백분율 소유권을 줄인다. 핵심은 프로토콜 성장이 토큰 희석을 앞지르도록 인플레이션을 충분히 낮게 유지하는 것이다.

    ##### 디플레이션: 희소성 나선

    가장 공격적인 접근법은 토큰을 만드는 것보다 빠르게 소각하여 시간이 지남에 따라 공급을 줄인다. 이더리움의 EIP-1559는 모든 트랜잭션마다 ETH를 소각하고, 많은 DeFi 프로토콜이 수익을 사용하여 토큰을 소각한다. 보유자에게는 좋게 들리지만, 토큰이 너무 가치 있어져서 사람들이 거버넌스에 사용하지 않게 되면 전체 목적을 무너뜨린다.

    #### 베스팅: 창업자 덤프 방지

    DAO를 죽이는 것 중 창업자들이 자신이 만든 토큰에 신념이 없음을 보여주는 것보다 빠른 것은 없다. 베스팅(Vesting) 일정은 내부자 배분을 수년간 락업하여 이를 해결하지만, 그들만의 역학과 예측 가능한 시장 압력을 만든다.

    ##### 업계 표준: 1+3 베스팅

    대부분의 합법적인 프로젝트는 "1+3" 일정을 사용한다: 토큰 릴리스가 전혀 없는 1년 **클리프(Cliff)**와 매월 배분의 약 1/36이 언락되는 3년의 선형 베스팅. 이 구조는 단순하고, 투자자에게 읽기 쉽고, 예측 가능한 잠재적 매도 압력의 순간을 만들면서 팀과 투자자의 정렬을 보장한다.

    ##### 클리프 효과와 공급 오버행

    그 초기 클리프 릴리스는 1년간의 락업 후 내부자들이 마침내 유동성을 얻으면서 종종 상당한 매도를 트리거한다. 그러나 모든 언락된 토큰이 즉시 시장에 나오지는 않는다. 공급 오버행(Supply Overhang) 모델은 베스팅 일정과 보유자 행동 가정을 결합하여 단순히 이론적 공급이 아닌 실제 매도 압력을 예상한다. 다른 수령자들은 매우 다른 인센티브를 가진다: 벤처 캐피탈 펀드는 이익 실현이나 리밸런싱을 위해 공격적으로 청산할 수 있고, 팀은 헌신을 보여주거나 자신의 토큰을 망가뜨리지 않기 위해 더 오래 보유할 수 있다.

    ##### 언락에 대한 헤징

    정교한 수령자들은 종종 즉시 매도하기보다 베스팅 배분을 헤지한다. 무기한 선물(제6장에서 다룬 수단)에서 숏 포지션을 취함으로써, 내부자들은 스팟 시장에 토큰을 덤핑하지 않고 현재 가격을 락인할 수 있다. 토큰 가격이 하락하면, 숏 포지션이 이익을 내고 락업된 토큰의 가치 손실을 상쇄한다. 이 전략은 매도 압력을 스팟 시장에서 파생상품 시장으로 이동시킨다. 결과적으로, 주요 언락 이벤트는 파생상품 가격에 가시적인 영향을 줄 수 있다: 펀딩 비율(롱과 숏 트레이더 간의 주기적 지불)이 더 많은 트레이더가 숏으로 가면서 음수로 전환될 수 있고, 선물과 스팟 가격 사이의 갭이 넓어질 수 있다. 트레이더들은 스팟 매도가 억제되어 있을 때도 언락 관련 압력을 예상하기 위해 이러한 신호를 주시한다.

    ##### 선형 대 마일스톤 베스팅

    선형 베스팅은 시간에 따라 점진적이고 예측 가능하게 토큰을 릴리스하여 공급 일정을 모델링하고 전달하기 쉽게 만든다. 마일스톤 기반 베스팅은 대신 사용자 성장, 수익 목표, 기능 출시, 또는 프로토콜 KPI와 같은 특정 달성에 토큰 릴리스를 연결한다. 마일스톤 베스팅은 성과에 인센티브를 더 잘 정렬하지만, 토큰이 실제로 언제 유통될지에 대한 불확실성을 도입하여 공급 예측을 복잡하게 하고 시장이 미래 언락에 가격을 반영하기 어렵게 만든다.

    ### 분배 전쟁: 누가 토큰을 받는가?

    토큰이 어떻게 분배되는지가 누가 DAO를 통제하는지를 결정한다. 내부자에게 너무 많이 주면 금권정치가 만들어진다. 랜덤 사용자에게 너무 많이 주면 무관심한 거버넌스가 된다. 암호화폐 세계는 네 가지 주요 분배 전략을 실험해왔으며, 각각 극적인 성공과 화려한 실패가 있었다.

    #### 소급적 에어드롭

    Uniswap의 전설적인 2020년 에어드롭은 토큰 분배의 황금 표준을 설정했으며, 프로토콜과 상호작용한 거의 모든 지갑에 보상을 주어 즉시 커뮤니티 소유권을 창출했다. 메시지는 명확했다: 초기 채택자들이 프로토콜을 구축하는 데 도움을 주었고 이제 그 일부를 소유한다.

    그러나 성공은 모방과 의도치 않은 결과를 낳았다. 미래 에어드롭이 예상 이벤트가 되자, 사용자 행동이 근본적으로 바뀌었다. 프로토콜과 진정으로 참여하는 대신, 사람들은 잠재적 토큰 보상을 받기 위해서만 사용하기 시작했다. 이것은 수만 개의 지갑을 운영하며 예상 기준을 게임하려는 산업 규모의 **"에어드롭 파밍(Airdrop Farming)"** 운영을 낳았다. 이 역학은 프로토콜이 트랙션을 입증하는 데 사용하는 바로 그 메트릭을 오염시켰다: 사용량 수치, 고유 지갑, TVL이 점점 더 신뢰할 수 없는 지표가 되었고, 종종 진정한 채택보다는 파머들에 의해 인위적으로 부풀려졌다.

    결과는 파괴적인 사이클이다: 프로토콜이 후한 에어드롭을 암시하고(때로는 내부자에게 유출), 이것이 명백한 사용량과 인상적인 메트릭을 유도한다. 이러한 부풀려진 수치는 VC로부터 높은 밸류에이션 펀딩 라운드를 확보하는 데 도움이 된다. 그러나 에어드롭이 발생하고 파밍 인센티브가 사라지면, 활동은 일반적으로 붕괴한다. 지속적인 인센티브 없이 에어드롭 후 의미 있는 참여를 유지한 프로토콜은 소수에 불과하다.

    신진 프로토콜들은 이제 딜레마에 직면한다: 활동을 부트스트랩하고 자금을 조달하기 위해 인위적인 트랙션이 필요하면서, 그 트랙션이 토큰 출시 후 사라질 것이라는 것을 알고 있다. 한편, 진정한 사용자들은 점점 더 제한된 토큰 배분을 두고 정교한 파밍 운영과 경쟁한다. 아이러니가 극명하다: 소유권을 민주화하기 위해 설계된 도구가 부주의하게 그것을 전문화하여, 산업 파머와 진정한 사용자 사이의 새로운 불평등을 만들었다.

    #### 포인트 프로그램

    포인트 프로그램(제7장의 수익률 생성 섹션에서 소개된 포인트 파밍의 한 형태)은 단순한 출시 전 인센티브를 넘어 토큰 출시 후에도 계속 운영되는 정교하고 지속적인 참여 메커니즘으로 진화했다. 전통적인 일회성 에어드롭과 달리, 현대 포인트 프로그램은 "시즌"으로 운영된다. 일반적으로 3-6개월 지속되는 반복 기간으로, 사용자들이 지속적인 활동을 통해 보상을 두고 경쟁한다.

    이 시즌 접근법은 에어드롭 후 이탈 문제를 직접 해결하기 때문에 지배적인 리텐션 전략이 되었다. 토큰 분배 후 참여가 붕괴하는 것을 지켜보는 대신, 프로토콜은 미래 시즌의 약속을 통해 무기한 사용자 활동을 유지할 수 있다. 초기 보상을 받은 후 떠날 수도 있는 사용자들이 대신 후속 분배를 받기 위해 활동적으로 남는다.

    #### 시즌 설계에 대한 두 가지 전략적 접근법

    시즌 모델은 각각 전략적 장점을 가진 기준 투명성에 대한 두 가지 구별되는 접근법을 낳았다:

    ##### 투명한 기준 시즌

    이러한 시즌은 정확한 포인트 공식과 자격 요건을 사전에 공개한다. 사용자들은 얼마나 많은 트랜잭션이 필요한지, 어떤 거래량 임계값을 달성해야 하는지, 또는 어떤 특정 행동이 포인트를 얻는지 정확히 안다. 이 투명성은 예측 가능한 행동을 만들고 프로토콜이 사용자 활동을 TVL 증가, 거래량 유도, 또는 특정 기능 채택 장려 등 원하는 결과로 유도할 수 있게 한다.

    ##### 불투명한 "추측 게임" 시즌

    이러한 시즌은 의도적으로 기준을 모호하게 하여 어떤 행동이 보상받을지에 대한 추측을 만든다. 이 불확실성은 여러 전략적 목적을 제공한다. 최적화를 불가능하게 하여 게이밍을 방지하고, 사용자들이 다른 전략을 시도하면서 더 광범위한 프로토콜 탐색을 장려하며, 미스터리와 기대를 통해 참여를 유지한다. 이러한 시스템은 종종 예상치 못한 행동에 소급적으로 보상한다. 아마도 특정 시간 창에 상호작용한 사용자, 시장 하락 기간에 충성을 보여준 사용자, 또는 덜 인기 있는 기능과 참여한 사용자를 선호할 수 있다.

    ##### 전략적 함의와 시장 영향

    이 시즌 경제는 프로토콜과의 사용자 관계를 근본적으로 변화시킨다. 착취적 파밍 후 이탈 대신, 시즌은 사용자들이 미래 보상을 받을 자격을 유지하기 위해 포지션과 활동을 유지하는 지속적인 "멤버십"을 만든다. 프로토콜은 시즌을 활용하여 새로운 기능을 테스트하고, 행동 데이터를 수집하고, 사용자 락인을 통해 경쟁 해자를 구축할 수 있다.

    시즌 포인트 프로그램의 성공은 새로운 DeFi 프로토콜에 사실상 필수로 만들었으며, 암호화폐를 일회성 인센티브 이벤트의 연속에서 사용자들이 여러 프로토콜에 걸쳐 동시에 포지션을 유지하고 항상 다음 시즌의 보상을 위해 포지셔닝하는 지속적인 "게임"으로 변화시켰다.

## Section IV: A Three-Pillar Structure

=== "EN"

    Token distribution and governance mechanisms are only part of the picture. A DAO can vote to allocate millions in grants or approve major upgrades, but someone needs to write the code, manage treasury operations, and handle the messy real-world tasks that smart contracts cannot perform. This operational reality has given rise to a standardized organizational model involving three distinct but interconnected entities: the DAO, the Foundation, and the Labs company. Think of them as the legislative, executive, and research & development branches of a digital nation.

    ### The Core Entities Explained: Uniswap as Case Study

    The Uniswap ecosystem provides a clean example of this tripartite structure in action and how it can evolve over time as incentives shift.

    **Uniswap Labs** is the for-profit technology company focused on research, development, and shipping products. As the team that originally built the protocol, Labs continues to design and implement major upgrades like Uniswap v4, Unichain, and new hook-based functionality. Historically, Labs also monetized its control over key user-facing interfaces (the main web frontend, wallet, and routing API) by charging an interface fee on swaps routed through its products, with that revenue flowing to Labs rather than the DAO.

    A November 2025 governance proposal aims to realign this model fundamentally. The proposal turns on the protocol's fee switch and routes a portion of LP fees and Unichain sequencer revenue into a UNI burn mechanism, while committing Labs to set its interface, wallet, and API fees to zero. Instead of extracting rent at the interface layer, Labs would focus on protocol growth funded from the DAO treasury via a UNI-denominated "growth budget". In other words, Labs becomes more explicitly a service provider to UNI holders: paid in UNI, contractually tied to token-holder interests, and incentivized to grow protocol usage rather than capture interface fees.

    **The Uniswap Foundation** is a non-profit legal entity created to handle stewardship functions the DAO cannot perform on-chain: running the Protocol Grants Program, supporting governance processes, coordinating ecosystem efforts, and holding certain IP and trademarks on behalf of the community. The Foundation received a large treasury grant from the DAO and, for a time, became the default home for "public goods" work that didn't fit neatly inside Labs or the DAO itself.

    Under this restructuring, most of the Foundation's operational teams (ecosystem support, governance support, and developer relations) are slated to move over to Labs. The Foundation shrinks to a small core group focused on deploying its remaining grants and incentives budget; once that is exhausted, future ecosystem funding is expected to come from the DAO's growth budget administered via Labs under a service-provider agreement with the DAO's legal wrapper (such as DUNI). The Foundation remains a legal and governance scaffold, but much less of an operational center of gravity than it was at launch.

    **The Uniswap DAO** is the ultimate governing body: UNI token holders propose, debate, and vote on protocol-level changes and treasury allocations. The DAO controls the on-chain treasury (denominated largely in UNI), key parameters like protocol fee levels and where they apply, ownership of core contracts (such as the v3 factory), and now the size and terms of Labs' growth budget. Practically, the DAO acts through governance executors and timelocks, while relying on Labs and other ecosystem contributors to draft proposals, write code, and operate infrastructure.

    This separation of powers lets Labs ship code at startup speed, the Foundation (and its successors) provide legal and administrative scaffolding, and the DAO retain final authority over the protocol. The recent shift attempts to tighten incentive alignment by tying Labs' business model more directly to UNI's success and protocol fees, but it also concentrates more execution power inside a single for-profit entity funded by the DAO. The tensions don't disappear; they just move. When Labs and token holders disagree on how aggressive fee burns should be, how much UNI should fund growth, or how centralized Unichain and other "middleware" pieces can be, those conflicts play out through this triangle of DAO, Foundation, and Labs rather than through a single corporate hierarchy.

    ### The Legal Gray Area: What Actually Is a DAO?

    Here's the uncomfortable truth: most DAOs exist in legal limbo. In the eyes of most jurisdictions, a DAO isn't recognized as a distinct legal entity. If a DAO gets sued, who is liable? The token holders, the developers, or the Foundation? The answer is unsettlingly unclear, and this ambiguity carries real risks.

    Some U.S. states now offer onchain-native legal wrappers for DAOs. Vermont created blockchain-based LLCs (BBLLCs), and Wyoming and Tennessee introduced DAO-style LLC statutes that let DAOs register as limited liability companies with token-based governance. More recently, Wyoming went a step further with the DUNA (Decentralized Unincorporated Nonprofit Association), a "digital UNA" designed specifically for nonprofit DAOs, which gives them legal personhood, limited liability, and the ability to sign contracts and pay taxes while tying decision-making to on-chain votes. Uniswap's DUNI wrapper is exactly this: a Wyoming DUNA used as the legal face of Uniswap governance.

    These wrappers solve part of the liability problem, but they come with strings attached: registered agents, ongoing filings, tax and reporting obligations, and, most importantly, a clearly identifiable legal entity that regulators and courts can go after. You gain legal clarity and institutional acceptability, but you give up some of the pseudonymous, jurisdiction-blurred nature that DAOs originally experimented with.

    The regulatory situation is equally murky. Are governance tokens securities under U.S. law? The SEC has suggested that tokens offering "investment returns" likely are, while pure governance tokens might not be. But the line remains blurry. The Howey Test asks whether token buyers expect profits from others' efforts. Many governance tokens arguably fail this test, yet few DAOs have definitive regulatory clarity.

    Enforcement actions have started to test the edges. In the Ooki DAO case, the CFTC argued that token holders voting on governance proposals could be treated as members of an unincorporated association and held collectively liable for the DAO's illegal leveraged trading products. Courts allowed service via forum posts and treated the DAO itself as a suable entity, sending a clear signal that "it's just a DAO" is not a shield against regulation. Most major DAOs now operate in a calculated regulatory gamble: decentralize sufficiently to avoid being labeled securities or unregistered intermediaries, but maintain enough coordination to actually build products. It's a high-wire act that could end badly if regulators decide to systematically crack down.

=== "KO"

    토큰 분배와 거버넌스 메커니즘은 전체 그림의 일부일 뿐이다. DAO는 수백만 달러의 그랜트를 배분하거나 주요 업그레이드를 승인하기 위해 투표할 수 있지만, 누군가가 코드를 작성하고, 재무 운영을 관리하고, 스마트 컨트랙트가 수행할 수 없는 지저분한 현실 세계 작업을 처리해야 한다. 이 운영 현실은 세 개의 구별되지만 상호 연결된 주체를 포함하는 표준화된 조직 모델을 낳았다: DAO, 재단, Labs 회사. 이들을 디지털 국가의 입법, 행정, 연구 개발 부서로 생각하라.

    ### 핵심 주체 설명: 사례 연구로서의 Uniswap

    Uniswap 생태계는 이 삼자 구조가 실제로 어떻게 작동하는지, 그리고 인센티브가 변함에 따라 시간이 지나면서 어떻게 진화할 수 있는지에 대한 깔끔한 예를 제공한다.

    **Uniswap Labs**는 연구, 개발, 제품 출시에 집중하는 영리 기술 회사이다. 원래 프로토콜을 구축한 팀으로서, Labs는 Uniswap v4, Unichain, 새로운 훅 기반 기능과 같은 주요 업그레이드를 계속 설계하고 구현한다. 역사적으로 Labs는 또한 주요 사용자 대면 인터페이스(메인 웹 프론트엔드, 지갑, 라우팅 API)에 대한 통제를 수익화하여 제품을 통해 라우팅되는 스왑에 인터페이스 수수료를 부과했으며, 그 수익은 DAO가 아닌 Labs로 흘러갔다.

    2025년 11월 거버넌스 제안은 이 모델을 근본적으로 재정렬하는 것을 목표로 한다. 제안은 프로토콜의 수수료 스위치를 켜고 LP 수수료와 Unichain 시퀀서 수익의 일부를 UNI 소각 메커니즘으로 라우팅하면서, Labs는 인터페이스, 지갑, API 수수료를 0으로 설정하도록 약속한다. 인터페이스 레이어에서 지대를 추출하는 대신, Labs는 DAO 재무에서 UNI로 표시된 "성장 예산"으로 자금 지원받는 프로토콜 성장에 집중하게 된다. 다시 말해, Labs는 더 명시적으로 UNI 보유자의 서비스 제공자가 된다: UNI로 지급받고, 계약적으로 토큰 보유자 이익에 묶여 있으며, 인터페이스 수수료를 포착하기보다 프로토콜 사용량을 성장시키도록 인센티브를 받는다.

    **Uniswap 재단**은 DAO가 온체인에서 수행할 수 없는 스튜어드십 기능을 처리하기 위해 만들어진 비영리 법인이다: 프로토콜 그랜트 프로그램 운영, 거버넌스 프로세스 지원, 생태계 노력 조율, 커뮤니티를 대신하여 특정 IP와 상표 보유. 재단은 DAO에서 큰 재무 그랜트를 받았고, 한동안 Labs나 DAO 자체 내에 깔끔하게 맞지 않는 "공공재" 작업의 기본 거처가 되었다.

    이 구조 조정에 따라, 재단의 운영 팀 대부분(생태계 지원, 거버넌스 지원, 개발자 관계)은 Labs로 이동할 예정이다. 재단은 남은 그랜트와 인센티브 예산을 배포하는 데 집중하는 작은 핵심 그룹으로 축소된다. 그것이 고갈되면, 미래 생태계 자금은 DAO의 법적 래퍼(예: DUNI)와의 서비스 제공자 계약에 따라 Labs를 통해 관리되는 DAO의 성장 예산에서 오도록 예상된다. 재단은 법적 및 거버넌스 스캐폴드로 남지만, 출시 시점보다 훨씬 덜 운영 중심이 된다.

    **Uniswap DAO**는 궁극적인 통치 기구이다: UNI 토큰 보유자들이 프로토콜 수준의 변경과 재무 배분을 제안하고, 토론하고, 투표한다. DAO는 온체인 재무(주로 UNI로 표시), 프로토콜 수수료 수준과 적용 위치와 같은 핵심 파라미터, 핵심 컨트랙트의 소유권(예: v3 팩토리), 그리고 이제 Labs의 성장 예산 규모와 조건을 통제한다. 실질적으로 DAO는 거버넌스 실행자와 타임락을 통해 행동하면서, 제안 초안 작성, 코드 작성, 인프라 운영은 Labs와 다른 생태계 기여자들에게 의존한다.

    이러한 권력 분립은 Labs가 스타트업 속도로 코드를 출시하고, 재단(과 그 후속)이 법적 및 행정적 스캐폴딩을 제공하고, DAO가 프로토콜에 대한 최종 권한을 유지할 수 있게 한다. 최근의 변화는 Labs의 비즈니스 모델을 UNI의 성공과 프로토콜 수수료에 더 직접적으로 묶어 인센티브 정렬을 강화하려고 시도하지만, DAO가 자금을 대는 단일 영리 주체 내에 더 많은 실행 권한을 집중시키기도 한다. 긴장은 사라지지 않는다; 그냥 이동한다. Labs와 토큰 보유자가 수수료 소각이 얼마나 공격적이어야 하는지, UNI가 성장에 얼마나 자금을 대야 하는지, 또는 Unichain과 다른 "미들웨어" 조각이 얼마나 중앙화될 수 있는지에 대해 동의하지 않을 때, 그 갈등은 단일 기업 계층 구조가 아니라 DAO, 재단, Labs의 삼각형을 통해 전개된다.

    ### 법적 회색 지대: DAO란 정확히 무엇인가?

    여기 불편한 진실이 있다: 대부분의 DAO는 법적 불확실성 속에 존재한다. 대부분의 관할권의 관점에서, DAO는 별개의 법인으로 인정되지 않는다. DAO가 소송을 당하면, 누가 책임이 있는가? 토큰 보유자, 개발자, 아니면 재단? 답은 불안하게도 불명확하며, 이 모호함은 실질적인 위험을 수반한다.

    일부 미국 주는 이제 DAO를 위한 온체인 네이티브 법적 래퍼를 제공한다. 버몬트는 블록체인 기반 LLC(BBLLC)를 만들었고, 와이오밍과 테네시는 DAO가 토큰 기반 거버넌스를 가진 유한 책임 회사로 등록할 수 있게 하는 DAO 스타일 LLC 법안을 도입했다. 더 최근에는 와이오밍이 DUNA(탈중앙화 비법인 비영리 협회, Decentralized Unincorporated Nonprofit Association)로 한 걸음 더 나아갔다. 이는 특히 비영리 DAO를 위해 설계된 "디지털 UNA"로, 법인격, 유한 책임, 계약 체결 및 세금 납부 능력을 부여하면서 의사결정을 온체인 투표에 연결한다. Uniswap의 DUNI 래퍼가 바로 이것이다: Uniswap 거버넌스의 법적 얼굴로 사용되는 와이오밍 DUNA.

    이러한 래퍼는 책임 문제의 일부를 해결하지만, 조건이 따른다: 등록 대리인, 지속적인 신고, 세금 및 보고 의무, 그리고 가장 중요하게, 규제 기관과 법원이 추적할 수 있는 명확히 식별 가능한 법인. 법적 명확성과 제도적 수용성을 얻지만, DAO가 원래 실험했던 익명적이고 관할권이 모호한 성격의 일부를 포기한다.

    규제 상황도 똑같이 모호하다. 거버넌스 토큰이 미국 법에 따른 증권인가? SEC는 "투자 수익"을 제공하는 토큰이 아마 그럴 것이라고 제안했으며, 순수 거버넌스 토큰은 그렇지 않을 수도 있다. 그러나 경계는 모호하게 남아 있다. Howey 테스트는 토큰 구매자들이 타인의 노력으로부터 이익을 기대하는지를 묻는다. 많은 거버넌스 토큰이 아마도 이 테스트에 실패하지만, 확실한 규제 명확성을 가진 DAO는 거의 없다.

    집행 조치가 경계를 테스트하기 시작했다. Ooki DAO 사건에서, CFTC는 거버넌스 제안에 투표하는 토큰 보유자들이 비법인 협회의 구성원으로 취급될 수 있으며 DAO의 불법 레버리지 거래 상품에 대해 집단적으로 책임을 질 수 있다고 주장했다. 법원은 포럼 게시물을 통한 송달을 허용하고 DAO 자체를 소송 가능한 주체로 취급하여, "그것은 그냥 DAO일 뿐"이 규제에 대한 방패가 아니라는 명확한 신호를 보냈다. 대부분의 주요 DAO는 이제 계산된 규제 도박으로 운영된다: 증권이나 미등록 중개인으로 라벨링되는 것을 피할 만큼 충분히 탈중앙화하면서, 실제로 제품을 구축하기 위해 충분한 조율을 유지한다. 규제 기관이 체계적으로 단속하기로 결정하면 나쁘게 끝날 수 있는 아슬아슬한 줄타기다.
