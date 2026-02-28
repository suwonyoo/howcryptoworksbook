# Chapter XIV: Quantum Resistance

=== "EN"

    ## Section I: Quantum Computing

    Regular computers work with bits, which are tiny switches that exist in one of two states: either 0 or 1. Quantum computers, however, operate with something quite different called **qubits**. A qubit possesses a remarkable property: it can exist in a blend of both 0 and 1 simultaneously, carrying within it a kind of "maybe" state until the moment you observe it.

    Breaking encryption with regular computers is like finding a needle in a haystack. You have to search through countless possibilities one by one, methodically checking each piece of straw. The haystack is so vast that it would take thousands of years to find the needle, making the task effectively impossible within any reasonable timeframe.

    Breaking encryption with quantum computers is like using a magnet to find that needle. Suddenly, what seemed impossible becomes feasible. The quantum computer's ability to explore many possibilities simultaneously, combined with interference effects that amplify correct answers, acts like that magnet pulling the needle straight to you.

    This is why cryptographers are developing **quantum-resistant encryption**. Think of it as changing the needle to aluminum. Now the magnet can't attract it anymore. These new encryption methods are designed so that even quantum computers lose their special advantage and must return to searching through the haystack piece by piece, just like their classical counterparts.

    However, quantum computers don't make everything faster. They only provide major advantages for certain specific types of problems, like breaking certain codes and speeding up certain search operations.

    ### What's Vulnerable and What's Not

    Today's encryption relies on mathematical problems that are easy to verify but practically impossible to solve backwards. For example, it's easy to multiply two huge numbers together, but extremely difficult to take that final number and figure out what the original two numbers were. This asymmetry is the foundation of most internet security today, with problems that would take regular computers billions of years to crack.

    The quantum threat isn't uniformly devastating across all cryptographic systems. Public key encryption systems like RSA and ECC are most at risk. A quantum algorithm called **Shor's algorithm** can break them by exploiting the mathematical structure these systems rely on. These mathematical patterns have elegant properties that quantum algorithms can exploit.

    Symmetric encryption like AES-256 remains secure with only minor key size adjustments. Hash functions remain viable too, though using longer outputs preserves security against quantum attacks. The key insight is that quantum-resistant approaches use mathematical problems that lack the elegant structure quantum computers can exploit. These alternative problems remain hard even for quantum computers, which is why cryptographers have spent years developing new standards based on them.

    ### What's At Stake

    Today's digital world runs on encrypted communication in ways most people never think about. Every time someone checks their bank balance, sends a private message, makes an online purchase, or logs into their email, encryption protects that information.

    Beyond personal data, encryption secures power grids, air traffic control systems, military communications, and the backbone of the internet itself. It enables secure voting systems, protects journalists' sources, and allows people to communicate safely under oppressive governments.

    The "https" padlock in browsers, the security updates on phones, and even the chip in credit cards all depend on encryption that these machines could theoretically break.

    ### The Timeline Problem

    One of the trickiest aspects is that we don't know exactly when quantum computers will become powerful enough to break current encryption. In October 2025, Google announced a significant milestone with their algorithm called "quantum echoes." The system successfully computed molecular structures in ways that classical supercomputers cannot, demonstrating what experts call "quantum advantage."

    However, current systems can't threaten encryption. Google's breakthrough computed a narrow scientific problem, but breaking modern cryptography would require machines with hundreds of thousands to millions of stable qubits. Today's systems struggle to maintain even smaller numbers in the extremely controlled conditions they need.

    The timeline remains uncertain. Google estimates real-world applications remain about five years away, while quantum computers capable of breaking encryption will take considerably longer.

    To put this in perspective, a quantum computer capable of cracking modern encryption would need specific capabilities. Early estimates suggested it would take about 20 million quantum bits (called "qubits") and 8 hours to crack RSA-2048 encryption. Recent work by Gidney brings this estimate down to fewer than 1 million qubits and less than a week. These estimates assume nearly perfect quantum computers with almost no errors, something today's quantum computers are nowhere near achieving.

    Realistically, most experts seem to agree that we're looking at the early 2030s at the absolute earliest. More likely, it'll be sometime between the mid-2030s and 2040s. It could even take longer if engineers hit unexpected roadblocks or faster if breakthroughs happen quicker because of unforeseen AI progress.

    However, not everyone shares this conservative outlook. In November 2025, Ethereum founder Vitalik Buterin predicted that quantum computers capable of breaking Ethereum's underlying security model could arrive before the next US presidential election in 2028.

    There's also a "steal now, decrypt later" risk where bad actors could be collecting encrypted data today, planning to crack it once powerful quantum computers become available. This makes protecting long-term secrets especially important.

    It's like knowing a big storm is coming but not sure if it's next week or next decade. The smart approach is to start preparing now rather than wait and see.

    ### The Cryptographic Solution

    Cryptographers have been preparing for this "quantum transition" for over a decade. In 2024, the U.S. government approved the first set of new encryption standards designed to resist quantum computers. Think of it like upgrading from mechanical locks to smart locks throughout an entire city. It's a big project, but manageable with proper planning.

    This effort is part of a global, coordinated response led by organizations like the U.S. National Institute of Standards and Technology (NIST). For nearly 10 years, NIST has been running a public competition to vet and select a portfolio of quantum-resistant cryptographic algorithms. The first set of these standards was finalized in 2024, providing a trusted foundation for the industry's transition.

    These new standards include algorithms from different mathematical families. In August 2024, NIST finalized three initial standards based on two distinct approaches: **lattice-based cryptography**, which prioritizes efficiency, and **hash-based signatures**, which prioritize high security confidence through simpler mathematical assumptions. NIST continues evaluating additional approaches as well. Each offers different trade-offs between signature size, speed, and security assumptions. This diversity provides insurance: if one mathematical approach proves vulnerable, the ecosystem can shift to alternatives.

    ### Implementation Timeline

    Major tech companies, governments, and security organizations are already testing and implementing these quantum-resistant systems. Rather than a catastrophic overnight change, we're looking at a gradual, managed transition over the coming decades.

    Critical systems like banking infrastructure, government communications, and power grids will upgrade first, followed by consumer applications. Many organizations are building flexibility into their systems now: the ability to quickly swap out encryption methods like changing the batteries in a device. The goal is that most of these security upgrades can be delivered through regular software updates, though some will require hardware changes too.

    However, blockchains face unique implementation challenges that centralized systems don't encounter. Traditional organizations can mandate upgrades across their infrastructure, pushing updates through internal IT departments. Blockchain networks, by contrast, must coordinate changes across thousands of independent node operators, wallet providers, and users, all without central authority to enforce compliance. This coordination challenge becomes even more complex when considering dormant wallets, potentially lost private keys, and the philosophical tensions around whether networks should force upgrades or risk leaving vulnerable assets exposed.

    While quantum computers pose a real future threat to current encryption, the cybersecurity community is actively preparing solutions. The transition will be gradual and planned for traditional systems, not a sudden crisis, though blockchain networks face unique coordination challenges in implementing these new standards across decentralized systems.

=== "KO"

    ## 섹션 I: 양자 컴퓨팅 (Quantum Computing)

    일반 컴퓨터는 비트(bit)로 작동하는데, 비트는 0 또는 1의 두 가지 상태 중 하나만 가질 수 있는 작은 스위치다. 그러나 양자 컴퓨터(Quantum Computer)는 **큐비트(Qubit)**라고 불리는 완전히 다른 것으로 작동한다. 큐비트는 놀라운 특성을 가지고 있다: 관찰하는 순간까지 0과 1의 혼합 상태, 일종의 "아마도" 상태로 동시에 존재할 수 있다.

    일반 컴퓨터로 암호를 해독하는 것은 건초더미에서 바늘을 찾는 것과 같다. 수많은 가능성을 하나씩 검색하며 각 지푸라기를 체계적으로 확인해야 한다. 건초더미가 너무 방대해서 바늘을 찾는 데 수천 년이 걸리기 때문에, 합리적인 시간 내에 이 작업은 사실상 불가능하다.

    양자 컴퓨터로 암호를 해독하는 것은 자석을 사용해 바늘을 찾는 것과 같다. 갑자기 불가능해 보이던 것이 실현 가능해진다. 많은 가능성을 동시에 탐색하는 양자 컴퓨터의 능력과 정답을 증폭시키는 간섭 효과(Interference Effect)가 결합되어 마치 자석이 바늘을 곧장 끌어당기는 것처럼 작동한다.

    이것이 암호학자들이 **양자 내성 암호화(Quantum-Resistant Encryption)**를 개발하는 이유다. 바늘을 알루미늄으로 바꾸는 것으로 생각하면 된다. 이제 자석이 더 이상 끌어당길 수 없다. 이러한 새로운 암호화 방법은 양자 컴퓨터조차 특별한 이점을 잃고 고전 컴퓨터처럼 건초더미를 하나씩 뒤져야 하도록 설계되었다.

    그러나 양자 컴퓨터가 모든 것을 빠르게 만드는 것은 아니다. 특정 코드 해독과 특정 검색 작업 가속화 같은 특정 유형의 문제에서만 주요한 이점을 제공한다.

    ### 취약한 것과 그렇지 않은 것

    오늘날의 암호화는 검증은 쉽지만 역으로 풀기는 사실상 불가능한 수학 문제에 의존한다. 예를 들어, 두 개의 거대한 숫자를 곱하는 것은 쉽지만, 그 결과 숫자에서 원래 두 숫자가 무엇이었는지 알아내는 것은 극도로 어렵다. 이러한 비대칭성이 오늘날 대부분의 인터넷 보안의 기초이며, 일반 컴퓨터가 해독하는 데 수십억 년이 걸리는 문제들이다.

    양자 위협은 모든 암호화 시스템에 균일하게 치명적이지 않다. RSA와 ECC 같은 공개키 암호화 시스템(Public Key Encryption)이 가장 위험에 처해 있다. **쇼어 알고리즘(Shor's Algorithm)**이라는 양자 알고리즘은 이러한 시스템이 의존하는 수학적 구조를 이용해 해독할 수 있다. 이러한 수학적 패턴은 양자 알고리즘이 악용할 수 있는 우아한 특성을 가지고 있다.

    AES-256 같은 대칭 암호화(Symmetric Encryption)는 약간의 키 크기 조정만으로 안전하게 유지된다. 해시 함수(Hash Function)도 여전히 유효하지만, 더 긴 출력을 사용하면 양자 공격에 대한 보안이 유지된다. 핵심 통찰은 양자 내성 접근 방식이 양자 컴퓨터가 악용할 수 있는 우아한 구조가 없는 수학 문제를 사용한다는 것이다. 이러한 대안적 문제들은 양자 컴퓨터에게도 여전히 어렵기 때문에, 암호학자들은 이를 기반으로 새로운 표준을 개발하는 데 수년을 투자해 왔다.

    ### 무엇이 위태로운가

    오늘날 디지털 세상은 대부분의 사람들이 인식하지 못하는 방식으로 암호화된 통신에 의존한다. 누군가 은행 잔액을 확인하거나, 비공개 메시지를 보내거나, 온라인 구매를 하거나, 이메일에 로그인할 때마다 암호화가 그 정보를 보호한다.

    개인 데이터를 넘어서, 암호화는 전력망, 항공 교통 관제 시스템, 군사 통신, 인터넷 자체의 백본을 보호한다. 안전한 투표 시스템을 가능하게 하고, 기자들의 취재원을 보호하며, 억압적인 정부 하에서 사람들이 안전하게 소통할 수 있게 한다.

    브라우저의 "https" 자물쇠, 휴대폰의 보안 업데이트, 신용카드의 칩까지 모두 이 양자 컴퓨터가 이론적으로 해독할 수 있는 암호화에 의존한다.

    ### 타임라인 문제

    가장 까다로운 측면 중 하나는 양자 컴퓨터가 현재 암호화를 해독할 수 있을 만큼 강력해지는 시점을 정확히 알 수 없다는 것이다. 2025년 10월, 구글은 "양자 에코(Quantum Echoes)"라는 알고리즘으로 중요한 이정표를 발표했다. 이 시스템은 고전 슈퍼컴퓨터가 할 수 없는 방식으로 분자 구조를 성공적으로 계산했으며, 전문가들이 "양자 우위(Quantum Advantage)"라고 부르는 것을 입증했다.

    그러나 현재 시스템은 암호화를 위협할 수 없다. 구글의 돌파구는 좁은 과학적 문제를 계산했지만, 현대 암호학을 해독하려면 수십만에서 수백만 개의 안정적인 큐비트를 가진 기계가 필요하다. 오늘날의 시스템은 극도로 통제된 조건에서도 더 적은 수를 유지하는 데 어려움을 겪고 있다.

    타임라인은 여전히 불확실하다. 구글은 실제 응용이 약 5년 후라고 추정하지만, 암호화를 해독할 수 있는 양자 컴퓨터는 상당히 더 오래 걸릴 것이다.

    이를 관점에서 보면, 현대 암호화를 해독할 수 있는 양자 컴퓨터는 특정 능력이 필요하다. 초기 추정에서는 RSA-2048 암호화를 해독하는 데 약 2,000만 개의 양자 비트(큐비트)와 8시간이 필요하다고 제안했다. Gidney의 최근 연구는 이 추정을 100만 큐비트 미만과 일주일 미만으로 낮췄다. 이러한 추정은 오류가 거의 없는 거의 완벽한 양자 컴퓨터를 가정하는데, 오늘날의 양자 컴퓨터는 이에 근접하지도 못한다.

    현실적으로, 대부분의 전문가들은 가장 빨라도 2030년대 초를 예상하는 것 같다. 더 가능성 있는 것은 2030년대 중반에서 2040년대 사이다. 엔지니어들이 예상치 못한 장애물에 부딪히면 더 오래 걸릴 수 있고, 예상치 못한 AI 발전으로 인해 돌파구가 더 빨리 일어나면 더 빨라질 수도 있다.

    그러나 모든 사람이 이러한 보수적인 전망을 공유하지는 않는다. 2025년 11월, 이더리움 창시자 비탈릭 부테린(Vitalik Buterin)은 이더리움의 기본 보안 모델을 해독할 수 있는 양자 컴퓨터가 2028년 다음 미국 대통령 선거 전에 도착할 수 있다고 예측했다.

    또한 악의적 행위자들이 오늘 암호화된 데이터를 수집하고, 강력한 양자 컴퓨터가 사용 가능해지면 해독할 계획을 세우는 "**지금 수확하고, 나중에 해독하기(Harvest Now, Decrypt Later)**" 위험도 있다. 이것이 장기적인 비밀 보호를 특히 중요하게 만든다.

    다음 주에 올지 다음 10년에 올지 모르지만 큰 폭풍이 온다는 것을 아는 것과 같다. 현명한 접근 방식은 기다리며 지켜보는 것이 아니라 지금부터 준비를 시작하는 것이다.

    ### 암호학적 해결책

    암호학자들은 10년 이상 이 "양자 전환(Quantum Transition)"을 준비해 왔다. 2024년, 미국 정부는 양자 컴퓨터에 저항하도록 설계된 첫 번째 새로운 암호화 표준 세트를 승인했다. 도시 전체에 걸쳐 기계식 잠금장치를 스마트 잠금장치로 업그레이드하는 것으로 생각하면 된다. 큰 프로젝트이지만 적절한 계획으로 관리 가능하다.

    이 노력은 미국 국립표준기술연구소(NIST)와 같은 조직이 이끄는 글로벌 조정 대응의 일부다. 거의 10년 동안 NIST는 양자 내성 암호화 알고리즘의 포트폴리오를 검증하고 선택하기 위한 공개 경쟁을 진행해 왔다. 이러한 표준의 첫 번째 세트는 2024년에 최종 확정되어 업계 전환을 위한 신뢰할 수 있는 기반을 제공했다.

    이러한 새로운 표준에는 다양한 수학적 계열의 알고리즘이 포함된다. 2024년 8월, NIST는 두 가지 다른 접근 방식을 기반으로 세 가지 초기 표준을 최종 확정했다: 효율성을 우선시하는 **격자 기반 암호화(Lattice-Based Cryptography)**와 더 단순한 수학적 가정을 통해 높은 보안 신뢰도를 우선시하는 **해시 기반 서명(Hash-Based Signatures)**이다. NIST는 추가적인 접근 방식도 계속 평가하고 있다. 각각은 서명 크기, 속도, 보안 가정 사이에서 다른 트레이드오프를 제공한다. 이러한 다양성은 보험을 제공한다: 하나의 수학적 접근 방식이 취약한 것으로 판명되면 생태계는 대안으로 전환할 수 있다.

    ### 구현 타임라인

    주요 기술 기업, 정부, 보안 조직들은 이미 이러한 양자 내성 시스템을 테스트하고 구현하고 있다. 재앙적인 하룻밤 변화가 아니라 앞으로 수십 년에 걸친 점진적이고 관리된 전환을 보고 있다.

    은행 인프라, 정부 통신, 전력망과 같은 중요 시스템이 먼저 업그레이드되고, 소비자 애플리케이션이 뒤따른다. 많은 조직들이 지금 시스템에 유연성을 구축하고 있다: 장치의 배터리를 교체하는 것처럼 암호화 방법을 빠르게 교체하는 능력이다. 목표는 이러한 보안 업그레이드의 대부분이 정기적인 소프트웨어 업데이트를 통해 전달될 수 있지만, 일부는 하드웨어 변경도 필요하다는 것이다.

    그러나 블록체인은 중앙화된 시스템이 직면하지 않는 고유한 구현 과제에 직면해 있다. 전통적인 조직은 내부 IT 부서를 통해 업데이트를 푸시하여 인프라 전체에 업그레이드를 의무화할 수 있다. 반면에 블록체인 네트워크는 중앙 권한 없이 준수를 강제하지 않고 수천 명의 독립적인 노드 운영자, 지갑 제공자, 사용자 간에 변경 사항을 조정해야 한다. 이 조정 문제는 휴면 지갑, 잠재적으로 분실된 개인키, 네트워크가 업그레이드를 강제해야 하는지 아니면 취약한 자산을 노출된 채로 둘 위험을 감수해야 하는지에 대한 철학적 긴장을 고려할 때 더욱 복잡해진다.

    양자 컴퓨터는 현재 암호화에 실제적인 미래 위협을 제기하지만, 사이버 보안 커뮤니티는 적극적으로 해결책을 준비하고 있다. 전통적인 시스템의 경우 전환은 갑작스러운 위기가 아니라 점진적이고 계획된 것이지만, 블록체인 네트워크는 탈중앙화된 시스템 전체에 이러한 새로운 표준을 구현하는 데 고유한 조정 문제에 직면해 있다.

=== "EN"

    ## Section II: Blockchain Vulnerability Assessment

    The coordination challenges described above are compounded by a feature unique to blockchains: permanent public records. Every signature ever published on-chain becomes a potential attack surface once quantum computers mature. Traditional financial systems can rotate their encryption keys behind closed doors, but blockchain addresses with exposed public keys remain vulnerable forever unless protocol-level changes intervene. This section examines which blockchain assets face the greatest quantum risk, why some addresses are more vulnerable than others, and what users can do to protect themselves while developers work on network-wide solutions.

    ### Technical Foundation

    Most blockchain networks secure transactions using digital signatures (the cryptographic foundation explained in Chapter I for Bitcoin and Chapter V for custody practices) that rely on mathematical problems classical computers cannot solve efficiently. The quantum threat to these systems comes in two forms, and it helps to think of them through analogy.

    Shor's algorithm is like a master locksmith who can reverse-engineer any lock's blueprint from its face (the public key) and cut a matching key directly. This is catastrophic for the signature schemes that Bitcoin, Ethereum, and Solana use today. Once quantum computers are powerful enough to run Shor's algorithm at scale, they can derive private keys from public keys, breaking the fundamental security assumption of blockchain wallets.

    **Grover's algorithm** resembles a superhuman librarian who must still search through library stacks, but can do so far more efficiently, effectively halving the security strength of hash functions. This is less devastating because the defense is straightforward: use longer hashes. One algorithm breaks mathematical structure entirely; the other just accelerates brute-force search.

    ### Public Key Exposure Models

    Think of it like this: a Bitcoin address is like a safe whose combination (the public key) isn't revealed until someone opens it. Once the safe is opened, anyone listening can record the combination. Today's eavesdroppers can't use that combination to break into safes, but when quantum "lockpicks" arrive, they can replay those recorded combinations to steal whatever remains inside.

    This analogy captures a fundamental principle: quantum computers can break public keys, but they cannot easily break the cryptographic hashes of those keys. This distinction determines which funds are at risk.

    ### Why Legacy Bitcoin Addresses Are More Vulnerable

    Legacy Bitcoin addresses face significantly higher quantum risk for two concrete reasons. First is direct public key exposure through P2PK outputs. Early Bitcoin (2009-2012) frequently used P2PK (Pay-to-Public-Key) outputs that publish the public key directly on the blockchain with no cryptographic protection.

    The transaction literally says "here's the public key, anyone who can prove they control it can spend this." Over 1.5 million BTC (roughly 8.7% of Bitcoin's total supply, yet only 0.025% of UTXOs) remain locked in these completely exposed P2PK outputs, including Satoshi's early mining rewards. This is like having a safe with the combination written on the outside. Quantum computers won't need to break any locks; they can simply read the combination and walk in.

    The second vulnerability comes from address reuse patterns. Early Bitcoin users commonly reused the same address for multiple transactions, a practice that was later discouraged. Each time someone spends from an address, they expose its public key on the blockchain. With address reuse, the first spend reveals the public key, and any remaining balance tied to that key becomes fair game for a future quantum attacker. Many legacy users accumulated large balances on a single address over time, then only spent portions, leaving substantial "change" outputs sitting behind already-exposed public keys. In the public-key-exposure model, those change outputs are effectively pre-targeted for quantum harvest.

    ### Current Standards

    Newer Bitcoin addresses use formats like P2PKH (Pay-to-Public-Key-Hash) and native SegWit (both covered in Chapter I) that only store a hash of the public key on the blockchain. The actual public key stays hidden until you spend your Bitcoin. When combined with the modern practice of using each address only once, this provides much stronger protection against quantum computers.

    Unspent funds in these modern address formats are much more quantum-resilient because the public keys remain hidden. A quantum attacker would first need to crack the hash layer itself, which is much harder than attacking exposed public keys directly.

    Using each address only once also reduces long-term risk. The public key is only revealed when you spend the funds. As long as the transaction confirms before attackers can derive your private key (which takes time even with quantum computers), you're effectively safe in practice. And since you've spent all the funds, there's no remaining balance left on that now-exposed key for future attacks.

    However, Taproot addresses (introduced in Chapter I) present a different exposure pattern. When using the default key-path spend, Taproot embeds a public key directly in the output, placing it in the exposed-key category similar to the vulnerable legacy formats. While Taproot currently holds a relatively small share of Bitcoin's total supply, users should be aware that these addresses don't provide the same quantum protection as hash-based alternatives.

    Ethereum's account model (Chapter II) creates different exposure patterns. Every transaction from an EOA exposes a recoverable public key, but accounts that have never sent transactions remain protected. However, once an Ethereum address sends its first transaction, the public key is permanently exposed for any future deposits to that same address.

    While managing individual addresses has obvious challenges, smart contract wallets mainly provide architectural flexibility rather than an immediate solution to quantum threats. The authentication logic in these wallets lives in upgradeable code instead of being permanently tied to a single signature key, so in principle they could switch to quantum-resistant signature schemes without changing the wallet address. However, this only becomes practical once Ethereum adds efficient built-in support for verifying these new signature types. Today, verifying post-quantum signatures directly on the EVM is technically possible but far too expensive in gas, so this upgrade path remains mostly theoretical rather than something users can deploy at scale. In practice, whether any given smart contract wallet benefits from this flexibility depends entirely on its specific implementation and available upgrade mechanisms.

    Multi-signature wallets (covered in Chapter V) present complex migration challenges, typically requiring all signers to coordinate simultaneous upgrades to post-quantum schemes. Social recovery mechanisms might provide alternative migration paths, though these require careful design to maintain security assumptions.

    ### Dormant and Potentially Lost Wallets

    Dormant addresses with exposed public keys represent significant systemic risk to the broader ecosystem. These include early adopter addresses where the owners may have lost their private keys but already exposed their public keys through past spending activity. They also include abandoned mining addresses from Bitcoin's early era, particularly those used for early block rewards that were subsequently spent, exposing their public keys to future quantum harvest.

    The fundamental challenge lies in distinguishing between genuinely lost funds and dormant but recoverable wallets. Quantum attackers could potentially recover funds from addresses presumed permanently lost: imagine the market chaos if millions of "lost" Bitcoin suddenly became recoverable, creating unexpected supply shocks and complex ownership disputes that could destabilize the entire ecosystem.

    This creates a high-stakes scenario often described as a "**quantum rush**." Should a powerful quantum computer emerge suddenly, it would trigger a frantic race. Malicious actors would rush to crack susceptible addresses and steal exposed funds, while network developers and the community would race to deploy emergency forks to freeze or migrate those same assets. The outcome of such an event would depend heavily on who acts first, introducing a stark game-theoretic dynamic into the security model.

    At current valuations, those at-risk BTC represent over $100 billion in exposed value, effectively creating a massive bounty for whoever achieves quantum supremacy first. This transforms quantum computing development from purely scientific pursuit into strategic competition. Nation-states and well-funded private entities now have a concrete financial incentive, beyond military or intelligence applications, to accelerate their quantum programs: whoever breaks the threshold first gains the ability to seize billions in abandoned or lost Bitcoin before the network can coordinate defensive forks. The race extends beyond who builds the computer to who can extract maximum value before the window closes.

    ### Best Practices

    To protect against future quantum computing threats, users should adopt careful key management practices. For Ethereum, avoid keeping large amounts of funds in an address after its first transaction, since any on-chain signature reveals the public key to potential quantum attacks. Instead, migrate to a fresh, unused address or preferably a smart contract wallet that can be upgraded to post-quantum cryptographic schemes.

    Bitcoin users should similarly avoid address reuse by spending entire UTXOs to fresh addresses, ensuring no value remains tied to previously exposed public keys. While multisig and multi-party computation solutions offer enhanced security today, they don't eliminate quantum risk if the underlying signature scheme remains vulnerable. Their primary value lies in providing an upgrade path to post-quantum algorithms when they become available.

    ### The Protocol-Level Challenge

    While individual users can adopt protective practices, the exposure patterns detailed above reveal a fundamental limitation: personal key management cannot protect the ecosystem as a whole. The massive amount of Bitcoin sitting in exposed legacy outputs, the countless reused addresses from Bitcoin's early days, and Ethereum's account model exposure all require coordinated protocol-level responses.

    No amount of individual vigilance can secure funds whose public keys are already permanently visible on-chain, nor can it prevent the systemic chaos of a potential quantum rush. This reality has driven blockchain developers to move beyond user education toward concrete technical proposals for network-wide quantum resistance. The question is no longer whether blockchains need protocol changes, but rather how to implement them without breaking existing functionality or creating unacceptable economic disruption.

=== "KO"

    ## 섹션 II: 블록체인 취약성 평가

    위에서 설명한 조정 문제는 블록체인 고유의 특성인 영구적인 공개 기록에 의해 복합된다. 체인에 게시된 모든 서명은 양자 컴퓨터가 성숙하면 잠재적인 공격 표면이 된다. 전통적인 금융 시스템은 비공개로 암호화 키를 교체할 수 있지만, 노출된 공개키를 가진 블록체인 주소는 프로토콜 수준의 변경이 개입하지 않는 한 영원히 취약하다. 이 섹션에서는 어떤 블록체인 자산이 가장 큰 양자 위험에 직면해 있는지, 왜 일부 주소가 다른 주소보다 더 취약한지, 개발자들이 네트워크 전체 솔루션을 작업하는 동안 사용자가 자신을 보호하기 위해 무엇을 할 수 있는지 살펴본다.

    ### 기술적 기초

    대부분의 블록체인 네트워크는 고전 컴퓨터가 효율적으로 풀 수 없는 수학 문제에 의존하는 디지털 서명(Digital Signature)을 사용하여 트랜잭션을 보호한다. 이러한 시스템에 대한 양자 위협은 두 가지 형태로 나타나며, 비유를 통해 이해하면 도움이 된다.

    쇼어 알고리즘(Shor's Algorithm)은 자물쇠의 앞면(공개키)에서 설계도를 역설계하고 일치하는 키를 직접 절삭할 수 있는 마스터 자물쇠 제조공과 같다. 이것은 비트코인, 이더리움, 솔라나가 오늘날 사용하는 서명 체계에 치명적이다. 양자 컴퓨터가 쇼어 알고리즘을 대규모로 실행할 만큼 강력해지면, 공개키에서 개인키를 도출하여 블록체인 지갑의 근본적인 보안 가정을 깨뜨릴 수 있다.

    **그로버 알고리즘(Grover's Algorithm)**은 여전히 도서관 서가를 검색해야 하지만 훨씬 더 효율적으로 할 수 있는 초인적인 사서와 같아서, 해시 함수의 보안 강도를 효과적으로 절반으로 줄인다. 방어가 간단하기 때문에 덜 파괴적이다: 더 긴 해시를 사용하면 된다. 한 알고리즘은 수학적 구조를 완전히 깨뜨리고, 다른 알고리즘은 단지 무차별 대입 검색을 가속화할 뿐이다.

    ### 공개키 노출 모델

    이렇게 생각해 보자: 비트코인 주소는 누군가 열기 전까지 조합(공개키)이 공개되지 않는 금고와 같다. 금고가 열리면 듣고 있는 누구나 조합을 기록할 수 있다. 오늘날의 도청자들은 그 조합을 사용해 금고에 침입할 수 없지만, 양자 "락픽"이 도착하면 기록된 조합을 재생해 내부에 남아 있는 것을 훔칠 수 있다.

    이 비유는 근본적인 원리를 포착한다: 양자 컴퓨터는 공개키를 깨뜨릴 수 있지만, 그 키의 암호화 해시를 쉽게 깨뜨릴 수는 없다. 이 구분이 어떤 자금이 위험에 처해 있는지를 결정한다.

    ### 레거시 비트코인 주소가 더 취약한 이유

    레거시 비트코인 주소는 두 가지 구체적인 이유로 양자 위험이 상당히 높다. 첫째는 P2PK 출력을 통한 직접적인 공개키 노출이다. 초기 비트코인(2009-2012)은 암호학적 보호 없이 공개키를 블록체인에 직접 게시하는 P2PK (Pay-to-Public-Key) 출력을 자주 사용했다.

    트랜잭션은 문자 그대로 "여기 공개키가 있고, 이를 통제할 수 있음을 증명하는 누구나 이것을 사용할 수 있다"고 말한다. 150만 BTC 이상(비트코인 총 공급량의 약 8.7%, 그러나 UTXO의 0.025%에 불과)이 사토시의 초기 채굴 보상을 포함하여 이러한 완전히 노출된 P2PK 출력에 잠겨 있다. 이것은 조합이 외부에 적혀 있는 금고를 가진 것과 같다. 양자 컴퓨터는 잠금장치를 깨뜨릴 필요가 없다. 단순히 조합을 읽고 들어갈 수 있다.

    두 번째 취약성은 주소 재사용 패턴에서 온다. 초기 비트코인 사용자들은 일반적으로 여러 트랜잭션에 같은 주소를 재사용했는데, 이는 나중에 권장되지 않게 된 관행이다. 누군가 주소에서 사용할 때마다 블록체인에 공개키를 노출한다. 주소 재사용의 경우, 첫 번째 사용이 공개키를 공개하고, 해당 키에 연결된 나머지 잔액은 미래의 양자 공격자에게 공정한 게임이 된다. 많은 레거시 사용자들은 시간이 지남에 따라 단일 주소에 큰 잔액을 축적한 후 일부만 사용하여, 이미 노출된 공개키 뒤에 상당한 "잔돈" 출력을 남겼다. 공개키 노출 모델에서 이러한 잔돈 출력은 효과적으로 양자 수확의 사전 표적이 된다.

    ### 현재 표준

    최신 비트코인 주소는 블록체인에 공개키의 해시만 저장하는 P2PKH (Pay-to-Public-Key-Hash) 및 네이티브 SegWit(모두 제1장에서 다룸)과 같은 형식을 사용한다. 실제 공개키는 비트코인을 사용할 때까지 숨겨진다. 각 주소를 한 번만 사용하는 현대적 관행과 결합하면 양자 컴퓨터에 대해 훨씬 강력한 보호를 제공한다.

    이러한 현대적 주소 형식의 미사용 자금은 공개키가 숨겨져 있기 때문에 훨씬 더 양자 내성이 있다. 양자 공격자는 먼저 해시 레이어 자체를 깨뜨려야 하는데, 이는 노출된 공개키를 직접 공격하는 것보다 훨씬 어렵다.

    각 주소를 한 번만 사용하면 장기적인 위험도 줄어든다. 공개키는 자금을 사용할 때만 공개된다. 공격자가 개인키를 도출하기 전에 트랜잭션이 확인되는 한(양자 컴퓨터로도 시간이 걸린다), 실제로는 효과적으로 안전하다. 그리고 모든 자금을 사용했기 때문에, 이제 노출된 키에 미래 공격을 위한 잔액이 남아 있지 않다.

    그러나 탭루트(Taproot) 주소(제1장에서 소개됨)는 다른 노출 패턴을 보인다. 기본 키 경로 사용 시, 탭루트는 공개키를 출력에 직접 포함하여 취약한 레거시 형식과 유사하게 노출된 키 범주에 놓이게 된다. 탭루트는 현재 비트코인 총 공급량의 비교적 작은 부분을 보유하고 있지만, 사용자들은 이러한 주소가 해시 기반 대안과 동일한 양자 보호를 제공하지 않는다는 것을 알아야 한다.

    이더리움의 계정 모델(제2장)은 다른 노출 패턴을 만든다. EOA에서의 모든 트랜잭션은 복구 가능한 공개키를 노출하지만, 트랜잭션을 보낸 적이 없는 계정은 보호된다. 그러나 이더리움 주소가 첫 번째 트랜잭션을 보내면, 공개키는 동일한 주소에 대한 미래 예금을 위해 영구적으로 노출된다.

    개별 주소 관리에는 명백한 어려움이 있지만, 스마트 컨트랙트 지갑(Smart Contract Wallet)은 양자 위협에 대한 즉각적인 해결책이 아니라 주로 아키텍처 유연성을 제공한다. 이러한 지갑의 인증 로직은 단일 서명 키에 영구적으로 연결되는 대신 업그레이드 가능한 코드에 있으므로, 원칙적으로 지갑 주소를 변경하지 않고 양자 내성 서명 체계로 전환할 수 있다. 그러나 이것은 이더리움이 이러한 새로운 서명 유형을 검증하기 위한 효율적인 내장 지원을 추가한 후에만 실용적이 된다. 오늘날 EVM에서 직접 포스트 양자 서명을 검증하는 것은 기술적으로 가능하지만 가스 비용이 너무 비싸서, 이 업그레이드 경로는 사용자가 대규모로 배포할 수 있는 것이 아니라 대부분 이론적으로 남아 있다. 실제로 특정 스마트 컨트랙트 지갑이 이 유연성의 혜택을 받는지 여부는 전적으로 특정 구현 및 사용 가능한 업그레이드 메커니즘에 달려 있다.

    다중 서명 지갑(Multi-signature Wallet, 제5장에서 다룸)은 복잡한 마이그레이션 문제를 제시하며, 일반적으로 모든 서명자가 포스트 양자 체계로의 동시 업그레이드를 조정해야 한다. 소셜 복구(Social Recovery) 메커니즘은 대안적인 마이그레이션 경로를 제공할 수 있지만, 보안 가정을 유지하기 위해 신중한 설계가 필요하다.

    ### 휴면 및 잠재적으로 분실된 지갑

    노출된 공개키를 가진 휴면 주소는 더 넓은 생태계에 상당한 시스템적 위험을 나타낸다. 여기에는 소유자가 개인키를 분실했을 수 있지만 과거 지출 활동을 통해 이미 공개키를 노출한 초기 채택자 주소가 포함된다. 또한 비트코인 초기 시대의 버려진 채굴 주소, 특히 초기 블록 보상에 사용된 후 지출되어 공개키가 미래의 양자 수확에 노출된 주소도 포함된다.

    근본적인 문제는 진정으로 분실된 자금과 휴면 상태이지만 복구 가능한 지갑을 구별하는 데 있다. 양자 공격자는 영구적으로 분실된 것으로 추정되는 주소에서 잠재적으로 자금을 복구할 수 있다: 수백만 개의 "분실된" 비트코인이 갑자기 복구 가능해진다면 시장 혼란을 상상해 보라. 예상치 못한 공급 충격과 전체 생태계를 불안정하게 만들 수 있는 복잡한 소유권 분쟁을 만들 수 있다.

    이것은 종종 "**양자 러시(Quantum Rush)**"로 설명되는 고위험 시나리오를 만든다. 강력한 양자 컴퓨터가 갑자기 등장하면 미친 듯한 경쟁이 촉발될 것이다. 악의적 행위자들은 취약한 주소를 해독하고 노출된 자금을 훔치기 위해 서두르고, 네트워크 개발자와 커뮤니티는 동일한 자산을 동결하거나 마이그레이션하기 위한 긴급 포크를 배포하기 위해 경쟁할 것이다. 이러한 이벤트의 결과는 누가 먼저 행동하느냐에 크게 달려 있어 보안 모델에 뚜렷한 게임 이론적 역학을 도입한다.

    현재 가치 평가에서 위험에 처한 BTC는 1,000억 달러 이상의 노출된 가치를 나타내며, 양자 우위를 먼저 달성하는 누구에게나 효과적으로 대규모 현상금을 만든다. 이것은 양자 컴퓨팅 개발을 순수한 과학적 추구에서 전략적 경쟁으로 변환한다. 국가와 자금이 풍부한 민간 기업은 이제 군사 또는 정보 응용을 넘어 양자 프로그램을 가속화할 구체적인 재정적 인센티브를 갖게 되었다: 임계값을 먼저 돌파하는 자는 네트워크가 방어 포크를 조정하기 전에 버려지거나 분실된 비트코인에서 수십억 달러를 압류할 수 있는 능력을 얻는다. 경쟁은 누가 컴퓨터를 만드느냐를 넘어 창이 닫히기 전에 누가 최대 가치를 추출할 수 있느냐로 확장된다.

    ### 모범 사례

    미래의 양자 컴퓨팅 위협으로부터 보호하기 위해 사용자는 신중한 키 관리 관행을 채택해야 한다. 이더리움의 경우, 첫 번째 트랜잭션 후 주소에 많은 양의 자금을 보관하지 않아야 한다. 온체인 서명이 잠재적인 양자 공격에 공개키를 노출하기 때문이다. 대신, 새로운 미사용 주소로 마이그레이션하거나 바람직하게는 포스트 양자 암호화 체계로 업그레이드할 수 있는 스마트 컨트랙트 지갑으로 마이그레이션하라.

    비트코인 사용자도 마찬가지로 전체 UTXO를 새 주소로 사용하여 주소 재사용을 피해야 하며, 이전에 노출된 공개키에 가치가 남아 있지 않도록 해야 한다. 멀티시그 및 다자간 연산(Multi-Party Computation) 솔루션은 오늘날 향상된 보안을 제공하지만, 기본 서명 체계가 취약하면 양자 위험을 제거하지 않는다. 그들의 주요 가치는 포스트 양자 알고리즘이 사용 가능해질 때 업그레이드 경로를 제공하는 데 있다.

    ### 프로토콜 수준 문제

    개별 사용자가 보호 관행을 채택할 수 있지만, 위에 자세히 설명된 노출 패턴은 근본적인 한계를 보여준다: 개인 키 관리로는 전체 생태계를 보호할 수 없다. 노출된 레거시 출력에 있는 대량의 비트코인, 비트코인 초기 시절의 수많은 재사용된 주소, 이더리움의 계정 모델 노출 모두 조정된 프로토콜 수준 대응이 필요하다.

    개인적인 경계로는 이미 온체인에 영구적으로 보이는 공개키를 가진 자금을 보호할 수 없으며, 잠재적인 양자 러시의 시스템적 혼란을 방지할 수도 없다. 이 현실이 블록체인 개발자들로 하여금 사용자 교육을 넘어 네트워크 전체 양자 저항성을 위한 구체적인 기술 제안으로 나아가게 했다. 문제는 더 이상 블록체인이 프로토콜 변경이 필요한지 여부가 아니라, 기존 기능을 깨뜨리거나 용납할 수 없는 경제적 혼란을 만들지 않고 어떻게 구현할 것인가이다.

=== "EN"

    ## Section III: Quantum-Resistance Transition

    Having established the threat landscape and vulnerability patterns, we now turn to how major blockchain networks are responding. Each network faces unique architectural constraints and governance challenges that shape their migration strategies. Bitcoin must balance immutability with security upgrades, while Ethereum leverages its more flexible upgrade culture. The technical solutions exist, but implementing them requires navigating complex social coordination problems that test the limits of decentralized governance.

    ### Bitcoin's Approach

    The Bitcoin developer community is actively working on concrete plans to protect the network against future quantum threats, with several serious proposals now under review. The vulnerable legacy outputs discussed in Section II, including coins from Bitcoin's earliest days, represent a disproportionately large amount of value concentrated in a small number of exposed transactions.

    The technical solutions under consideration are sophisticated, building on Bitcoin's existing upgrade mechanisms. One prominent proposal, **BIP-360**, would introduce a new address type designed specifically for quantum resistance. The approach builds on Taproot's architecture but disables the features that expose public keys, replacing them with quantum-safe alternatives. This represents a gradual approach that could be adopted without breaking existing functionality.

    However, the core challenge isn't technical but social and economic: should Bitcoin force users to migrate, or make it optional? Proposed solutions span a wide spectrum. Jameson Lopp's QBIP proposal outlines a multi-year deprecation plan with phased changes, including a widely publicized "flag day" about five years after activation for invalidating vulnerable spends. Agustín Cruz's more aggressive "QRAMP" protocol proposes hard deadlines for the upgrade, though this faces pushback over potentially making dormant funds unspendable. Other proposals explore commitment schemes allowing current holders to prove ownership and move assets safely, or deadline-based systems with grace periods.

    The debate intensifies when considering what should happen to dormant holdings that can't or won't be moved before quantum computers arrive. Some propose permanently burning the at-risk assets to prevent quantum seizure. Others suggest doing nothing and allowing quantum-equipped actors to claim abandoned coins, treating it as a kind of digital salvage. A third approach would allow vulnerable coins to be claimed but impose transaction limits that slow the drainage process, creating competition among would-be claimants and driving fees to miners rather than letting the value be easily extracted.

    Each option faces significant philosophical resistance within the Bitcoin community. The ethos strongly opposes burning holdings that are rightfully owned, even if the owner is presumed dead or absent. The principle of immutable property rights runs deep in Bitcoin culture; many view Satoshi-era holdings as legitimately belonging to their original owners, and any protocol change that makes them unspendable, whether through burning or redistribution, violates the fundamental promise that "your keys, your coins" means permanent ownership. This creates a painful tension: protecting the network from quantum attack may require violating the very property rights that make Bitcoin valuable in the first place.

    Ultimately, for truly lost or abandoned assets where private keys are genuinely gone, developers face this difficult choice: either these funds will be stolen by whoever possesses quantum computing capabilities first, or they will become unspendable through protective consensus changes. While Satoshi himself discussed in 2010 the need to adopt a new cryptographically sound system in response to a cryptographic break, this solution only works for those who still control their private keys. No consensus has emerged on timelines or enforcement, but Bitcoin Optech continues tracking these debates as they evolve from early concepts toward potential consensus rules.

    ### Ethereum's Approach

    Unlike Bitcoin's philosophical tensions around property rights and coin burning, Ethereum faces primarily technical engineering trade-offs. The community's more flexible upgrade culture allows for iterative solutions, though the practical obstacles remain substantial. The signature schemes currently used by both user accounts and validators would be susceptible to the attacks discussed earlier.

    The upgrade strategy centers on a multi-pronged, staged approach rather than a single protocol-wide switch. For user transactions, EIP-7932 proposes supporting multiple signature algorithms to enable post-quantum schemes while maintaining backward compatibility with existing accounts. Account Abstraction is serving as a key on-ramp, allowing smart wallets to implement these quantum-safe signatures without requiring immediate protocol changes. The Ethereum Foundation is actively funding research into post-quantum multi-signature schemes to address the larger signature sizes that come with quantum-resistant algorithms.

    However, these new algorithms come with significant practical trade-offs. The most immediate challenge is the dramatic increase in data size. A current Ethereum signature is just 65 bytes. Quantum-resistant alternatives range from around 2,400 bytes to over 29,000 bytes depending on the algorithm and security level chosen. That represents a 37x to 450x increase in signature size.

    These size increases directly impact blockchain operation in multiple ways. Transactions become larger, leading to increased storage requirements and blockchain bloat. Higher transaction fees follow naturally from the increased data that must be processed and stored. Slower verification times can also affect block processing and network throughput, presenting a major engineering hurdle for protocol developers who must balance security against usability.

    Beyond user accounts, researchers are exploring alternatives for Ethereum's broader architectural foundations. The cryptographic techniques used for data availability, like KZG commitments discussed in Chapter II, also need quantum-resistant replacements. Hash-based and STARK-style constructions are promising candidates because they only face Grover's more manageable speedup rather than Shor's devastating advantage. The Ethereum Foundation is funding this research, and there are proposals for an emergency recovery fork that could quickly freeze exposed accounts if quantum breakthroughs happen suddenly.

    ### Solana's Approach

    Solana faces a more immediate exposure concern: most Solana account addresses directly reveal the public key from the moment they are created, unlike Bitcoin or Ethereum where the public key can remain hidden until a transaction is made. This means every Solana address is already visible to potential future quantum attackers. In December 2025, the Solana Foundation collaborated with Project Eleven on a threat assessment and a testnet prototype using post-quantum digital signatures, treating this as a forward-looking migration exercise rather than an emergency response.

    The prototype work focuses on stress-testing how quantum-resistant signatures would affect throughput, compute costs, and fees if adopted broadly. Meanwhile, Solana's ecosystem has experimented with opt-in wallet-level protections using hash-based one-time signatures for users who want extra security now. This approach is useful as a stopgap, but not a full network-wide migration plan.

=== "KO"

    ## 섹션 III: 양자 저항성 전환

    위협 환경과 취약성 패턴을 확립한 후, 이제 주요 블록체인 네트워크가 어떻게 대응하고 있는지 살펴본다. 각 네트워크는 마이그레이션 전략을 형성하는 고유한 아키텍처 제약과 거버넌스 문제에 직면해 있다. 비트코인은 불변성과 보안 업그레이드 사이의 균형을 맞춰야 하고, 이더리움은 더 유연한 업그레이드 문화를 활용한다. 기술적 솔루션은 존재하지만, 이를 구현하려면 탈중앙화 거버넌스의 한계를 시험하는 복잡한 사회적 조정 문제를 탐색해야 한다.

    ### 비트코인의 접근 방식

    비트코인 개발자 커뮤니티는 미래의 양자 위협으로부터 네트워크를 보호하기 위한 구체적인 계획을 적극적으로 작업하고 있으며, 여러 심각한 제안이 현재 검토 중이다. 섹션 II에서 논의된 취약한 레거시 출력은 비트코인 초기 시절의 코인을 포함하여 소수의 노출된 트랜잭션에 불균형하게 많은 가치가 집중되어 있다.

    검토 중인 기술 솔루션은 비트코인의 기존 업그레이드 메커니즘을 기반으로 하여 정교하다. 한 가지 두드러진 제안인 **BIP-360**은 양자 저항성을 위해 특별히 설계된 새로운 주소 유형을 도입할 것이다. 이 접근 방식은 탭루트의 아키텍처를 기반으로 하지만 공개키를 노출하는 기능을 비활성화하고 양자 안전 대안으로 대체한다. 이것은 기존 기능을 깨뜨리지 않고 채택할 수 있는 점진적 접근 방식을 나타낸다.

    그러나 핵심 문제는 기술적인 것이 아니라 사회적이고 경제적이다: 비트코인이 사용자에게 마이그레이션을 강제해야 하는가, 아니면 선택적으로 해야 하는가? 제안된 솔루션은 광범위한 스펙트럼에 걸쳐 있다. Jameson Lopp의 QBIP 제안은 활성화 후 약 5년 후에 취약한 지출을 무효화하기 위한 널리 공개된 "플래그 데이"를 포함한 단계적 변경이 있는 다년간 폐기 계획을 설명한다. Agustín Cruz의 더 공격적인 "**QRAMP**" 프로토콜은 업그레이드에 대한 하드 데드라인을 제안하지만, 휴면 자금을 사용할 수 없게 만들 가능성에 대한 반발에 직면해 있다. 다른 제안들은 현재 보유자가 소유권을 증명하고 자산을 안전하게 이동할 수 있도록 하는 약속 체계, 또는 유예 기간이 있는 데드라인 기반 시스템을 탐구한다.

    양자 컴퓨터가 도착하기 전에 이동할 수 없거나 이동하지 않을 휴면 보유 자산에 어떤 일이 발생해야 하는지 고려할 때 논쟁은 심화된다. 일부는 양자 압수를 방지하기 위해 위험에 처한 자산을 영구적으로 소각하자고 제안한다. 다른 사람들은 아무것도 하지 않고 양자 장비를 갖춘 행위자들이 버려진 코인을 청구하도록 허용하여 일종의 디지털 인양으로 취급하자고 제안한다. 세 번째 접근 방식은 취약한 코인을 청구할 수 있도록 허용하되 트랜잭션 제한을 부과하여 배출 과정을 늦추고, 청구자들 간의 경쟁을 만들어 가치가 쉽게 추출되는 대신 수수료를 채굴자에게 유도할 것이다.

    각 옵션은 비트코인 커뮤니티 내에서 상당한 철학적 저항에 직면한다. 이 기풍은 소유자가 사망했거나 부재한 것으로 추정되더라도 정당하게 소유된 보유 자산을 소각하는 것에 강하게 반대한다. 불변의 재산권 원칙은 비트코인 문화에 깊이 뿌리박혀 있다. 많은 사람들은 사토시 시대의 보유 자산이 원래 소유자에게 정당하게 속한다고 보며, 소각이든 재분배든 그것을 사용할 수 없게 만드는 모든 프로토콜 변경은 "당신의 키, 당신의 코인"이 영구적 소유권을 의미한다는 근본적인 약속을 위반한다. 이것은 고통스러운 긴장을 만든다: 양자 공격으로부터 네트워크를 보호하려면 비트코인을 처음부터 가치 있게 만드는 바로 그 재산권을 위반해야 할 수 있다.

    궁극적으로, 개인키가 진정으로 사라진 진정으로 분실되거나 버려진 자산의 경우, 개발자들은 이 어려운 선택에 직면한다: 이러한 자금은 양자 컴퓨팅 능력을 먼저 보유한 누군가에게 도난당하거나, 보호적 합의 변경을 통해 사용할 수 없게 된다. 사토시 자신은 2010년에 암호학적 해독에 대응하여 새로운 암호학적으로 건전한 시스템을 채택할 필요성을 논의했지만, 이 솔루션은 여전히 개인키를 통제하는 사람들에게만 작동한다. 타임라인이나 시행에 대한 합의가 나타나지 않았지만, Bitcoin Optech는 이러한 논쟁이 초기 개념에서 잠재적인 합의 규칙으로 발전하는 것을 계속 추적하고 있다.

    ### 이더리움의 접근 방식

    재산권과 코인 소각을 둘러싼 비트코인의 철학적 긴장과 달리, 이더리움은 주로 기술적 엔지니어링 트레이드오프에 직면해 있다. 커뮤니티의 더 유연한 업그레이드 문화는 반복적인 솔루션을 허용하지만, 실질적인 장애물은 상당하다. 사용자 계정과 검증자 모두가 현재 사용하는 서명 체계는 앞서 논의한 공격에 취약하다.

    업그레이드 전략은 단일 프로토콜 전체 전환이 아닌 다각적이고 단계적인 접근 방식에 중점을 둔다. 사용자 트랜잭션의 경우, EIP-7932는 기존 계정과의 하위 호환성을 유지하면서 포스트 양자 체계를 가능하게 하기 위해 여러 서명 알고리즘을 지원하자고 제안한다. 계정 추상화(Account Abstraction)는 스마트 지갑이 즉각적인 프로토콜 변경 없이 이러한 양자 안전 서명을 구현할 수 있도록 핵심 진입로 역할을 하고 있다. 이더리움 재단은 양자 내성 알고리즘과 함께 제공되는 더 큰 서명 크기를 해결하기 위해 포스트 양자 다중 서명 체계에 대한 연구에 적극적으로 자금을 지원하고 있다.

    그러나 이러한 새로운 알고리즘은 상당한 실질적 트레이드오프를 동반한다. 가장 즉각적인 문제는 데이터 크기의 극적인 증가다. 현재 이더리움 서명은 단 65바이트다. 양자 내성 대안은 선택한 알고리즘과 보안 수준에 따라 약 2,400바이트에서 29,000바이트 이상에 이른다. 이것은 서명 크기가 37배에서 450배 증가하는 것을 나타낸다.

    이러한 크기 증가는 여러 방식으로 블록체인 운영에 직접적인 영향을 미친다. 트랜잭션이 커지면 스토리지 요구 사항이 증가하고 블록체인 팽창이 발생한다. 처리하고 저장해야 하는 데이터가 증가함에 따라 더 높은 트랜잭션 수수료가 자연스럽게 따른다. 느린 검증 시간도 블록 처리와 네트워크 처리량에 영향을 미칠 수 있어, 보안과 사용성 사이의 균형을 맞춰야 하는 프로토콜 개발자에게 주요 엔지니어링 장애물을 제시한다.

    사용자 계정을 넘어, 연구자들은 이더리움의 더 넓은 아키텍처 기반에 대한 대안을 탐구하고 있다. 제2장에서 논의된 KZG 커밋먼트와 같은 데이터 가용성에 사용되는 암호화 기술도 양자 내성 대체물이 필요하다. 해시 기반 및 STARK 스타일 구조는 쇼어의 파괴적인 이점이 아닌 그로버의 더 관리 가능한 가속화에만 직면하기 때문에 유망한 후보다. 이더리움 재단은 이 연구에 자금을 지원하고 있으며, 양자 돌파구가 갑자기 발생할 경우 노출된 계정을 빠르게 동결할 수 있는 긴급 복구 포크에 대한 제안도 있다.

    ### 솔라나의 접근 방식

    솔라나는 더 즉각적인 노출 우려에 직면해 있다: 대부분의 솔라나 계정 주소는 생성 순간부터 공개키를 직접 공개하는데, 이는 공개키가 트랜잭션이 이루어질 때까지 숨겨진 상태로 유지될 수 있는 비트코인이나 이더리움과 다르다. 이것은 모든 솔라나 주소가 이미 잠재적인 미래 양자 공격자에게 보인다는 것을 의미한다. 2025년 12월, 솔라나 재단은 Project Eleven과 협력하여 포스트 양자 디지털 서명(Post-Quantum Digital Signature)을 사용한 위협 평가와 테스트넷 프로토타입을 진행했으며, 이를 긴급 대응이 아닌 미래 지향적 마이그레이션 연습으로 취급했다.

    프로토타입 작업은 양자 내성 서명이 광범위하게 채택될 경우 처리량, 계산 비용, 수수료에 어떤 영향을 미치는지 스트레스 테스트하는 데 중점을 둔다. 한편, 솔라나의 생태계는 지금 추가 보안을 원하는 사용자를 위해 해시 기반 일회용 서명을 사용하는 옵트인 지갑 수준 보호를 실험해 왔다. 이 접근 방식은 임시방편으로 유용하지만 완전한 네트워크 전체 마이그레이션 계획은 아니다.
