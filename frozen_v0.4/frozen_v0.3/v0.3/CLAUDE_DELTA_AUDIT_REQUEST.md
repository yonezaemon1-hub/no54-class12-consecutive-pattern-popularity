# Claudeへ: No.54 v0.3 差分監査指令 (公開HOLD)

数学部分の再監査を最初から無条件に繰り返すのではなく、まず次の限定監査を実施してください。

1. `SHA256SUMS_v0.3.txt` の全ファイルを照合する。`frozen_v0.2/SHA256SUMS_PACKAGE.txt` の元の11個の期待値も再チェックする。
2. `verify_delta_v0.3.py` を実行し、v0.1とv0.3の**第8節以外はバイト一致**、旧12ファイルが凍結されていることを確認する。添付の `DIFF_SECTION8_v0.2_to_v0.3.patch` と実際のdiffを照合する。
3. 文献第8節に追加された3点を評価する: (i) Class 12 が連続回避 `Av(123,231,312)` であることと未解決パターン132,213,321 / 正規化が `(n|A_n|)`、(ii) EKP §7 Theorem 7.5の射程が総数 `nE_{n-1}` までであること、(iii) Zhao 2014の通常パターンと本稿の連続パターンの定義が異なること。
4. ChatGPT側が一次資料を見たという記録を、あなた（Claude）や著者自身が見たと誤記していないかを確認する。自分でアクセス不能なら未確認と明記する。
5. 数学に変更がないことを確認できた場合、前回の**MODEL/PROOF/COMPUTATION PASSは前回の独立監査に依拠して維持**、今回については『数学差分なし』と報告。数学再実行を行った場合だけ、その範囲を新たに報告する。
6. `REFERENCES` を『Claude本人の確認』と『出典をリンクで特定しChatGPTが確認した項目』に分ける。`NOVELTY=INCONCLUSIVE`, `RELEASE=HOLD`のまま。

**出力要求:** `PACKAGE/DIFF/REFERENCES/ATTRIBUTION/NOVELTY/OVERALL/RELEASE` の判定表（PASS, PARTIAL, FAIL, INCONCLUSIVE）。疑義があれば具体的な節・行・差分を指摘してください。人間査読済みと書かないでください。今回のZIPをGitHub/Zenodoへアップロードしないでください。
