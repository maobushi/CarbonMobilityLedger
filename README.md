# CarbonMobilityLedger
---------------------------------------
mobile_app：[Carbon Drive App - web]()

[![Introduction Movie](http://img.youtube.com/vi/G9VQYpX-wT4/0.jpg)](http://www.youtube.com/watch?v=G9VQYpX-wT4)

## How to run
- Streamlitをインストールし、METAMASK Walletの秘密鍵を"METAMASK_DEV_PRIVATE"という名前で環境変数に格納します。
- streamlit run src/main.pyでlocalで動作します。

## **What It Does**
Project Name:CarbonDrive App
> "Your Miles Matter: Move Smart, Earn Smart"
> 
![image](https://file.notion.so/f/f/cbd8d2ac-f8fa-4a42-ad57-f522c59b7c01/3a48f718-5246-4e2c-87c6-6635bb0ebb82/Sparkle.png?id=a0f540ba-3fcd-47ad-a502-160530e24986&table=block&spaceId=cbd8d2ac-f8fa-4a42-ad57-f522c59b7c01&expirationTimestamp=1700956800000&signature=BcULGbsMAVS85P8KgPdMUtSGidE1WCU-3RonPuYIoLI&downloadName=Sparkle.png)

- **概要**: このプロジェクト "CarbonDrive App" は、EVM互換性のあるパブリックブロックチェーンを使用して、持続可能な移動手段を奨励する「Mobility Carbon Credit」システムを実装します。このシステムでは独自トークンを用いた経済圏を設計することで、自動車を運転することへのインセンティブ、車自体のレベルアップを通じてNFT化された車の価値が変動し、中古車販売価格の下落を防ぐメカニズムを導入します。さらに将来、業界全体において環境性能の高いEVへのシフトを見据え、新規EV購入を促進し、運転を楽しんでいただくためのソリューションを提供します。

## Features
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
- **minting(新規発行)**
新車の購入により新規CBTがmintされます。$\beta$%がUserへ配布され、$(1-\beta)$%がpoolに入ります。ここでは $\beta = 10$%と設定しています。
1年間の新規発行は「その年の新車の購入台数$\times$新車価格」です。

ある$i$年の1年間の新車購入台数を$N_{i}$台とし, 市場成長率を $\alpha$ , 新車$k$の価格を $p_{i}^{k}$ とすると, 
```math
amount~of~mint = \sum^{\infty}_{i = 1} \sum^{K}_{k = 1} \left(p^{k}_{i} \times N_{i} \times \frac{\beta}{100}\right)
```
となります. ここで市場成長率 $\alpha$ = $\frac{p_i N_i}{p_{i-1}N_{i-1}}$である.

Distance Ratio(DR)
| Car Level  |      DR     | Estimation Distance|
|:-----------|------------:|-------------:|
| Level 0    | 0.10CBT/km  | 0km          |
| Level 1    | 0.11CBT/km  | 30,000km     |
| Level 2    | 0.15CBT/km  | 80,000km     |
| Level 3    | 0.50CBT/km  | 130,000km    |

- **Market Supply Side**
新車の購入により

- **Market Demand Side**
CBTの主なユースケースはバッテリーの充電時の支払いに使用できることです。ここで1CBT = 1JPYとして利用できることがCBTの価値を補償するものとなります。


## **The Problem It Solves / Use Case**

- **中古車市場の価格決定**:一般的な中古車価格の決定要因である使用年数やバッテリーの状態以外に、車に対応したレベルが市場価格に影響します。走行距離が長く、車のレベルが高いほど走行によるCBTの還元率とハッテリー充電時のCBT付与率が高まり、このことにより中古車価格の下落率を緩やかにします。
- **新車EVの販売促進**:環境性能の良い車ほど購入時のCBT付与量と走行による基礎的なCBTの獲得効率が高まります。そのためEVに対応した
- **環境問題への対応**: 本システムは、交通による炭素排出を削減し、持続可能な移動手段を普及させることで環境問題に取り組みます。
- **報酬メカニズム**: 環境に優しい行動をトークンで報酬することで、持続可能な行動を促進します。また、

## **Challenges I Ran Into**

- **技術的課題**: EVM互換性を持つAstarとSolidityでのスマートコントラクトの開発における課題。
- **Tokenomics**: トークン経済のバランスと持続可能性の確保。新車販売促進と中古車価格の下落を防ぐメカニズムの設計
- 

## **Technologies I Used**
- **Ethereum Blockchain**: 分散型台帳技術を使用してトランザクションを管理。
- **Solidity**: Ethereumのスマートコントラクトを開発するためのプログラミング言語。
- **streamlit**: データの可視化と分析を行うためのWebアプリケーションフレームワーク。
- **Astar**: EVM互換性を持つパブリックブロックチェーンを構築するためのプラットフォーム。

## **How We Built It**

- **開発プロセス**: まず、システムの概念を定義し、次にSolidityを使用してスマートコントラクトを開発しました。
- **チームワーク**: チームメンバーが各自の専門知識を活用して、プロジェクトの各部分を担当しました。

## **What We Learned**

- **ブロックチェーンの応用**: EthereumとSolidityに関する深い知識。
- **チームワーク**: 複数の専門分野が協力することの重要性と効果。


## **What's Next for Carbon Drive App**

- **個人の環境保護スコア**:CBTを使用して車のレベルを上げるのと同時に、個人は車のレベルを上げた差分の経験値が溜まり、個人の環境保護スコアが上がるようになる。
- **スマートシティへの応用**:電車やバイク、電動キックボード等、モビリティとそのCO2排出量の削減度合いに応じてCBTを発行することで、前述の個人の環境保護スコアをより拡張性の高い指標とすることができる。
- **GorvananceとDAO化**:Utility TokenであるCBTだけでなく、Governance Tokenを
- **コミュニティ構築**: ユーザーとの連携を強化し、より広範なコミュニティを形成。
- **持続可能性の向上**: 環境への影響をさらに減らすための継続的な改善。

### Contact
@maobushi
@uoooo


