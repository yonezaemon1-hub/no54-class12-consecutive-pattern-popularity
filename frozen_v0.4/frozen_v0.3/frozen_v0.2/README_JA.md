# No.54 — Claude独立監査用パッケージ v0.2

**研究者:** Ryutaro Yonezu — Independent Researcher  
**日付:** 2026-11-05  
**対象:** 連続パターン123・231・312を回避する順列における321・132・213の出現回数と漸近割合  
**公開:** HOLD（公開不可）  
**新規性:** INCONCLUSIVE（未確定）  
**外部独立AI監査:** 未実施  
**人間査読:** 未実施  
**ライセンス:** All rights reserved

## 最初に読む順番

1. `CLAUDE_AUDIT_REQUEST.md` — Claudeに依頼する監査指令。既存のPASS判定は信用せず独立検証すること。
2. `No54_v0.1_PROOF_AUDIT_20261105.md` — 主張と証明。原稿はバイト単位で保存。
3. `No54_v0.2_ADVERSARIAL_AUDIT_20261105.md` — 内部攻撃監査と既知の弱点。原稿から変更なし。
4. `No54_v0.1_VERIFY_20261105.py` と `No54_v0.1_INDEPENDENT_ATTACK_20261105.py` — 計算検証器。
5. `SHA256SUMS_PACKAGE.txt` — パッケージ内全ファイルのSHA256（この一覧自身を除く）。

## 主要定理（監査すべき主張）

`A_n=Av_n(123,231,312)` は **連続パターン回避** とする。`E_n` を Euler zigzag number、`N_n(p)` を全 `A_n` における連続パターン `p` の総出現回数とすると、全 `n>=3` に対し

- `|A_n| = n E_{n-1}`（既知）
- `N_n(321) = E_{n+1} - 2E_n`（候補主張）
- `N_n(132)=N_n(213)=((n-2)nE_{n-1}-E_{n+1}+2E_n)/2`
- 元の研究で用いる正規化 `N_n(p)/(n|A_n|)` の極限：321は `4/pi^2`、132・213は `1/2-2/pi^2`

## 監査上の注意

- 積分作用素、円周差変換、総数の公式、Euler数列 `E_{n+1}-2E_n` 自体は先行研究にある。そこを新規性として主張しない。
- 直接列挙は `n=3..9` のみ、別方式の有理数積分検証は `n=3..22` のみ。
- `n=10,20,40,60,100,120` の表示値は**候補定理から作った予測値**であり、独立検算ではない。
- v0.1原稿第7節の計算の説明は、v0.2攻撃監査第I節の訂正に従って読む。
- 独立監査では数学的正誤と新規性を分離し、疑わしければFAIL/INCONCLUSIVEとする。
- **Claudeへ提供する監査資料であって、論文公開版ではない。** GitHub・Zenodo登録、配布は未許可。

## オフライン再現

Python 3.10+ 標準ライブラリだけで実行できる。

```
python -I No54_v0.1_VERIFY_20261105.py
python -I No54_v0.1_INDEPENDENT_ATTACK_20261105.py
```

Windows PowerShell 5.1では、同梱スクリプトでハッシュ検証後に再実行可能：

```
powershell.exe -NoProfile -ExecutionPolicy Bypass -File .\RUN_WINDOWS_AUDIT.ps1
```

このZIP作成環境での再実行はPASS。ただし**Windows実機でのPASSは未確認**。
