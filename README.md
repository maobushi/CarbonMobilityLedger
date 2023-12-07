# CarbonMobilityLedger

[![Introduction Movie](http://img.youtube.com/vi/G9VQYpX-wT4/0.jpg)](http://www.youtube.com/watch?v=G9VQYpX-wT4)

## **What It Does**
"Your Miles Matter: Move Smart, Earn Smart"

<img width="530" alt="image" src="https://github.com/maobushi/CarbonMobilityLedger/assets/28808890/45e11064-9a2f-40e4-b465-f398bcf4f120">


- このプロジェクト "CarbonDrive App" は、EVM互換性のあるパブリックブロックチェーンを使用して、持続可能な移動手段を奨励する「Mobility Carbon Credit」システムを実装します。
- このシステムでは独自トークンを用いた経済圏を設計することで、自動車を運転することへのインセンティブ、車自体のレベルアップを通じてNFT化された車の価値が変動し、中古車販売価格の下落を防ぐメカニズムを導入します。
- さらに将来、業界全体において環境性能の高いEVへのシフトを見据え、新規EV購入を促進し、運転を楽しんでいただくためのソリューションを提供します。

## Features
![carbbon-drive-white](https://github.com/maobushi/CarbonMobilityLedger/assets/28808890/df66f244-73b5-425a-a4bc-218fdf055646)

走行距離と車のレベルに応じて、CarBon Token（CBT）が付与され、そのCBTはバッテリーの給電や植樹事業に使用することができます。
- **CBTの主な機能**;
  - Tokenを入手する
    - **車の購入**: ユーザーは高い環境性能を持つ車（電気自動車、フルハイブリッドカー、マイルドハイブリッドカー）を購入すると、CarBon Token（CBT）が付与されます。
    - **走行による報酬**: 1km走行するごとにCBTを獲得できます。車のレベルに応じて付与されるCBTの比率が変化します。
  - Tokenを使用する
    - **バッテリーの充電**: CBTを電気自動車のバッテリー充電時の支払いに使用することができます。ここでは1CBT = 1JPYとして換算されます。また支払額とレベルに応じてCBTが還元されます。
    - **樹木の植樹**: CBTを使用して、環境保存活動に寄付することができます。具体的には植樹が行われます。ユーザーは植樹への寄付を行うことで、車のレベルを上げることができます。
### Tokenomics
#### OverView
![carbbon-drive-white (3)](https://github.com/maobushi/CarbonMobilityLedger/assets/28808890/f9dd62bf-253b-4a9b-ab06-1dae43cf0f81)

- **minting(新規発行)**

新車の購入により新規CBTがmintされます。 $\beta$ %がUserへ配布され、 $(1-\beta)$ %がpoolに入ります。ここでは $\beta = 10$ %と設定しています。
1年間の新規発行は「その年の新車の購入台数 $\times$ 新車価格」です。

ある $i$ 年の1年間の新車購入台数を $N_{i}$ 台とし, 市場成長率を $\alpha$ , 新車$k$の価格を $p_{i}^{k}$ とし、市場成長率や割引率などを無視した全体での供給量は以下のように表せられる.
```math
\text{Amount~of~Mint} = \sum^{\infty}_{i = 1} \sum^{K}_{k = 1} \left(p^{k}_{i} \times N_{i} \times \frac{\beta}{100}\right)
```
ここで市場成長率 $\alpha$ = $\frac{p_i N_i}{p_{i-1}N_{i-1}}$ である.

また、ある $i$ 年の市場の供給量は以下のようになる
```math
\text{Total Minting in Year } i = \sum_{k = 1}^{K} \left( p_i^k \times N_i \times \frac{\beta}{100} \right)
```


Distance Ratio(DR) (example)
| Car Level  |      DR     | Estimation Distance|
|:-----------|------------:|-------------:|
| Level 0    | 0.10CBT/km  | 0km          |
| Level 1    | 0.11CBT/km  | 30,000km     |
| Level 2    | 0.15CBT/km  | 80,000km     |
| Level 3    | 0.50CBT/km  | 130,000km    |

- **Market Supply Side**
新車の購入によりCBTがPoolされます。この時点では市場へのCBTの供給量0で、あくまでも新車販売の売り上げに裏付けを持ったCBTがpoolされます。
  -  **CBTの獲得(Earning)**
     - CBTは、走行距離と車のレベルに応じて付与されます。
    走行による報酬（Earning through Distance）
     - $DR_i$ ： $l$ レベルの車におけるDistance Ratio (CBT/km)
     - $D$ ：走行距離 (km) 
    走行によるCBTの獲得量は以下のようになります：

    
    $\text{CBT Earning} = DR_{i} \times D$


- **Market Demand Side**
CBTの主なユースケースはバッテリーの充電時の支払いに使用できることです。ここで1CBT = 1JPYとして利用できることがCBTの価値を補償するものとなります。
  -  **CBTの利用(Spending)**
  CBTはバッテリーの充電や車のレベルアップのBurn（植樹事業など）に使用されます。
  ユーザーはバッテリーの充電か車のレベルアップのためにトークンを使用するかを決められます。
  - バッテリーの充電(use)
    - ユーザーがバッテリーの充電を行うことは1CBT = 1JPYとしてCBTを使用する( Use)ことを意味します。これはpoolの裏付けからそのCBTの量に対応する資金が共にpoolから抜けるということになります。これは後述するBurnとは異なり、市場に供給されているCBTの価値は増減せず、維持されます。
  - 樹木の植樹(burn)
    - ユーザーが樹木の植樹を行うことはユーザーが持つCBTがtotal supplyからburnされることを意味します。このことで、これまで車の購入時に新規発行(mint)されたCBTとその裏付け分の価値が変動することになります。具体的には、pool全体でCBTの価値がオリジナルのCBTの価値よりも高まります。
    - また、car levelの増加によるDRの増加とその効果はここでは無視する。

**市場での供給**
- 供給：走行による報酬 (<-裏付けとしての新車購入によるCBTの発行）
- 需要：CBTの使用（バッテリー充電や植樹事業）
市場バランスの数式は以下のようになります：
```math
\text{Market Balance=Total Minting−Total CBT Spending}
```

ユーザーが全てのユーザーが合理的な経済人だと仮定します。すると1つの新車を購入し売却するまでを車のLife Timeとすると、Life Timeにおいて車から得られる価値を最大化することで、個人は将来の効用を最大化するように行動します。この時、ユーザーはuseで使用するCBTの量を最大化することが主問題に対する補題となり、そのような制約の下でユーザーはBurnを合理的に選択します。
　一方で、現実のユーザーは経済学上の意味における合理的な意思決定を行うとは限らないことや、車の運転距離も人によってまちまちであることから、Gamificationを利用することや、後述するGovornance Tokenを導入することで別の市場と接続され、Tokenomicsの維持が見込める。

## **The Problem It Solves / Use Case**

- **中古車市場の価格決定**:一般的な中古車価格の決定要因である使用年数やバッテリーの状態以外に、車に対応したレベルが市場価格に影響します。走行距離が長く、車のレベルが高いほど走行によるCBTの還元率とハッテリー充電時のCBT付与率が高まり、このことにより中古車価格の下落率を緩やかにします。
- **新車EVの販売促進**:環境性能の良い車ほど購入時のCBT付与量と走行による基礎的なCBTの獲得効率が高まります。そのため内燃機関の自動車に比べて、EVやPHVなどの販売の促進になる。このことは自社における内燃機関とEVのシェアだけでなく、市場全体にも当てはまる。各国政府の方針により、今後市場全体での需要増が見込めるEV市場においてTokenomics, Drive to Earnの導入は他社との大きな差別化要因になりうる。
- **環境問題への対応**: 本システムは、交通による炭素排出を削減し、持続可能な移動手段を普及させることで環境問題に取り組みます。
- **報酬メカニズム**: 環境に優しい行動をトークンで報酬することで、持続可能な行動を促進します。

## **Challenges I Ran Into**

- **技術的課題**: EVM互換性を持つAstarとSolidityでのスマートコントラクトの開発における課題。
- **Tokenomics**: トークン経済のバランスと持続可能性の確保。新車販売促進と中古車価格の下落を防ぐメカニズムの設計

## **Technologies I Used**
- **Ethereum Blockchain**: 分散型台帳技術を使用してトランザクションを管理。
- **Solidity**: Ethereumのスマートコントラクトを開発するためのプログラミング言語。
- **streamlit**: データの可視化と分析を行うためのWebアプリケーションフレームワーク。
- **Goerli/Astar**: EVM互換性を持つパブリックブロックチェーンを構築するためのプラットフォーム。
- **Infura**: Ethereumノードをホストするためのプラットフォーム。
- **Metamask**: Ethereumネットワークに接続するためのウォレット。
- **Python**: データ分析と可視化のためのプログラミング言語。
<img width="530" alt="techmap" src="https://github.com/maobushi/CarbonMobilityLedger/assets/28808890/037e0f6b-8129-4583-a5ef-3c216404459b">



## How to run
- Streamlitをインストールし、METAMASK Walletの秘密鍵を"METAMASK_DEV_PRIVATE"という名前で環境変数に格納します。
- streamlit run src/main.pyでlocalで実行します。


## **What's Next for Carbon Drive App**
- Tokenenomicsの充実
  - Governance Tokenの導入：X to Earnの走りであるMove to Earnという概念を作り出したStepnのTokenomicsを参考にGamification/Game-Fiを導入することで、市場でのトークンの価値、時価総額が高まることで、新規ユーザーの参入と頑健なTokenomicsが見込める。さらにこれはStepnのvirtualなスニーカーアイテムとは異なり、RWA:Real World Assetと実生活での需要が存在する点が特に、異なる点であり、ありがちなPonsi化を防ぐ要因となっている点が新しい。
  - Token需要の増加は新車の販売促進にもつながりうる点も特筆すべきで点である。
- **個人の環境保護スコア**:CBTを使用して車のレベルを上げるのと同時に、個人は車のレベルを上げた差分の経験値が溜まり、個人の環境保護スコアが上がるようになる。
- **スマートシティへの応用**:電車やバイク、電動キックボード等、モビリティとそのCO2排出量の削減度合いに応じてCBTを発行することで、前述の個人の環境保護スコアをより拡張性の高い指標とすることができる。
- **GorvananceとDAO化**:Utility TokenであるCBTだけでなく、Governance Tokenを導入することで、CBT市場とGovernance Token市場が接続される。
- **コミュニティ構築**: ユーザーとの連携を強化し、より広範なコミュニティを形成。
- **持続可能性の向上**: 環境への影響をさらに減らすための継続的な改善。
- **環境問題以外への対応**：今回は、Carbon CreditやCarbonの市場に着目したが、環境問題ではなく、MAZDA社へのファンレベルとも読み替えることができ、同様の議論、アーキテクチャが利用できる。その際にはEV以外の内燃機関の自動車などとの関連も見込める。
- **世界展開**:日本市場のみならず、ブロックチェーンを利用することで世界への市場の展開、さらに世界の中古車市場を考慮することができる。また各国、各地域間での貿易の他にトークンのやり取りなどの経済活動がへの発展も考えられる。

## **Examples of Application to the Real World**
- [エコな交通手段で報酬がもらえる「CitiCAP」フィンランドの環境先進都市によるモビリティ活用](https://ideasforgood.jp/2019/11/21/lahti-citicap/)

### Contact
@maobushi
@uoooo


