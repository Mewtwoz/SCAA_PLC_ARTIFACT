# SCAA-PLC JSS 内容复审修订与 Artifact 构建报告

**日期：** 2026-08-09  
**Evidence label:** `DERIVED_EVIDENCE`  
**依据：** `PAPER1_JSS_CONTENT_REREVIEW_2026-08-09.md`

## 1. 本轮结论

本轮完成了复审中可由现有数据、代码和实验环境闭合的内容项，并避免以内部一致性替代人类效用证据。核心变化是将当前评价总体从旧的 2,353 个“function-label-available”样本改为按研究任务分别定义：卡片和工具输出使用全部 2,431 个样本；source-role 任务使用 1,876 个具有可靠 Structured Text 映射的样本；2,353 子集仅保留为历史分类诊断范围。

稿件的 RQ3 已由 `record portability` 降为 `bounded second-pipeline contract instantiation`。10 个 OpenPLC/radare2 样本只支持第二流水线契约实例化，不再承担跨编译器、跨厂商或跨架构外部泛化证明。RQ1 也被限定为同一快照上的 post-hoc lexical validity case，不再把 GEB 零误差写成前瞻性准确率。

## 2. 新增实验与结果

新实验包位于：

`09_paper1_experiment_evidence/v6_jss_content_validation/`

主要结果如下：

| 检查面 | 结果 |
|---|---:|
| 全量 feature rows | 2,431 |
| 全量 evidence cards | 2,431 |
| 原 2,353 张卡片回归差异 | 0 |
| source-oracle 可评分行 | 1,876 |
| 当前 uncertainty rows | 4,176 |
| tool-output task | 2,431 行；S2/S3/S6 均 1.000 |
| source-role task | 1,876 行；S3/S6 balanced accuracy 0.692033，macro F1 0.637565 |
| GEB validity case | 353 TP，264 TN，0 FP，0 FN |
| OpenPLC ungated probe | 735 个 source-positive FN；production rule 仍为 out of scope |
| contract invariants | 5/5 PASS，全部 0 failure |

五项正向不变量的核验面为：2,431 个 binary/card identity hash、4,176 个弱 EC1--EC5 槽位的不确定性闭合、555 个 CODESYS unsupported-not-negative 状态、1,876 个 source hash trace，以及 6,677 个第二流水线 relation/uncertainty manifest joins。

新增三个端到端 trace case：

- `geb_ARRAY_HAV`：GEB lexical rule 与显式 `FUNCTION_BLOCK` source syntax 一致；
- `geb_AIN`：显式 `FUNCTION` source-negative contrast，EC4 为 partial/U09b；
- `codesys__ARRAY_ABS`：configured `nm` tool gap，EC1--EC5 保持 partial，并记录 U01/U02/U11/U13。

这些案例证明可追溯链按契约存在，但不证明审稿人或分析员因此更准确、更快速。

## 3. 对复审问题的处理

### C1：非自证式效用评价

已新增 counterbalanced independent-reviewer trace-task protocol 与空白任务表，覆盖证据定位、unsupported/negative 区分、hash/rule 核验和越界主张识别。由于本轮没有获授权的参与者、伦理结论或真实人类结果，文件保持 `TEMPLATE_ONLY`，正文继续明确 human utility 未验证。该 CRITICAL 项得到研究设计准备，但尚未被虚构为已闭合实验。

### C2：Artifact 自包含性与审稿访问

已生成 GitHub-ready release candidate：

`08_split_paper1_plc_binary_analysis/artifact_package/SCAA_PLC_JSS_ARTIFACT_v1/`

包内使用相对路径，包含 SHA-256 payload manifest、环境说明、一键验证器、clean-room 日志、第三方通知、任务模板和上游 PLC-BEAD acquisition verifier。原始 PLC-BEAD 二进制/源码没有被再分发，因为检查到的上游快照没有明确 `LICENSE` 文件。公开 URL、release tag、DOI 和作者批准的 code/data license 仍需人工完成，因此正文没有提前声称 artifact 已公开。

### M1--M8 与 MINOR

- M1：完成 2,431 全量重建和 RQ-specific inclusion flow。
- M2：增加 schema design requirements、真实 failure families、category coverage 与 content-validity boundary；没有把未观察 U-code 写成 saturation。
- M3：RQ3 全文降为 bounded instantiation/smoke test。
- M4：RQ1 全文改为 same-snapshot post-hoc validity case。
- M5：补入 Kitchenham et al. 2008、Cerqueira Revoredo et al. 2021、Santana et al. 2026、Heumüller et al. 2020，并重写 novelty boundary。
- M6：提交版 supplement 删除历史 weighted completeness、across-fold spread、classifier claims 和 internal-ready verdict；对应文件仅放入 artifact `history/`。
- M7：Evaluation 新增三案例 trace table 与被拒绝 aggregate claim。
- M8：方法与 Evaluation 新增五项正向 contract invariants。
- W1：摘要首次展开 SCAA-PLC。
- W2：删除 CPS 路线遗留表述。
- W3：摘要以 full-population accounting 和 contract guarantee 为中心。
- G1：拆分并澄清 relation/uncertainty SHA-256 join 句子。
- EUBA：按 Sandia 官方作者列表将误写的 `David Hannasch` 修正为 `James W. Foulk`。

## 4. 修改文件

- `08_split_paper1_plc_binary_analysis/tex/main.tex`
- `08_split_paper1_plc_binary_analysis/tex/supplementary.tex`
- `08_split_paper1_plc_binary_analysis/tex/refs.bib`
- `09_paper1_experiment_evidence/v6_jss_content_validation/build_jss_content_validation.py`
- `09_paper1_experiment_evidence/v6_jss_content_validation/` 下的 v6 数据、报告和验证输出
- `09_paper1_experiment_evidence/v6_jss_content_validation/build_jss_artifact_package.py`
- `08_split_paper1_plc_binary_analysis/artifact_package/SCAA_PLC_JSS_ARTIFACT_v1/`

## 5. 必须由人工完成的决策

1. **Artifact code license：** 建议 BSD-3-Clause 或 MIT；Codex 未获授权代替作者作出法律许可。
2. **Artifact derived-data license：** 建议 CC BY 4.0；需作者确认版权与第三方边界。
3. **GitHub 上传：** 上传整个 `SCAA_PLC_JSS_ARTIFACT_v1` 目录，创建固定 release tag，并把 URL/commit SHA 返回给 Codex。
4. **持久 DOI：** 建议把固定 GitHub release 归档到 Zenodo 后再更新正文。
5. **Human utility study：** 若继续以方法型 JSS regular paper 为目标，应在伦理/机构流程允许后执行已提供的 reviewer task；在此之前不得写 utility improvement。
6. **独立 taxonomy validation：** 至少两名独立编码者或领域专家对 failure/evidence categories 做编码和分歧处理后，才能提升“chosen provenance categories”的内容效度措辞。

## 6. 编译状态

当前活动 WSL shell 中未发现 `latexmk`、`pdflatex`、`xelatex` 或 `lualatex`，因此本轮没有声称新 TeX 已成功编译。旧 PDF 不作为本轮内容修订的构建证据。待 TeX 工具路径恢复后，应重新执行 main/supplement 两次编译、参考文献解析、undefined reference/citation 扫描和 overfull box 检查；格式迁移仍按用户要求延后到下次内容复审通过之后。

## 7. 当前门禁判断

`CONTENT_EVIDENCE_STRENGTHENED_ARTIFACT_READY_WITH_HUMAN_ACTIONS`

本轮已经显著提高总体对齐、正向可检验保证、案例可追溯性和 artifact 可核验性，没有降低工作量或把限制伪装成结果。JSS 内容门禁仍受两项人工条件约束：可访问的固定 artifact URL/license，以及真实独立 reviewer/analyst 评价（或进一步把论文明确限定为 design-and-feasibility study）。
