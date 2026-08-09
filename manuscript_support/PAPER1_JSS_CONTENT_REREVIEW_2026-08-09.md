# SCAA-PLC 面向 JSS 的投稿前内容复审报告

**复审日期：** 2026-08-09  
**审阅角色：** SCI/JSS 软件工程与二进制分析方向审稿人  
**审阅范围：** 主文、补充材料、C1--C18 claim matrix、v5 方法验证脚本及落地结果  
**明确暂缓：** JSS 模板迁移、作者 affiliation、Declarations、版面、浮动体排布、图形美观和 LaTeX 格式  
**复审结论：** `NEEDS_MAJOR_CONTENT_REVISION_BEFORE_JSS_SUBMISSION`

## 1. 总结

- **CRITICAL：2**
- **MAJOR：8**
- **MINOR：5**
- **内容评分：4/10**
- **投稿建议：** 暂不提交 JSS；先关闭两项内容阻断，再进入格式迁移。

本轮修订取得了实质进展。生产 SA-001 与 ungated probe 已正确分离；GEB 的 353 TP、263 TN 和 OpenPLC 的 735 个 probe-only FN 可以从行级结果复算。S3 与 S6 的混淆矩阵确实完全相同，第二流水线的 10 张卡、6,657 条关系、20 条不确定性记录和输出哈希也与落地文件一致。原报告中“scope gate 预先决定 portability 结果”“EC6 未定义相关性被写成 0”“六槽位被当作六个独立预测构念”等问题已关闭或显著收窄。

然而，数值正确不等于核心方法得到有效验证。当前论文的中心贡献是 evidence-card reporting method，但现有三个 RQ 分别验证一个命名约定、一个由字段定义强烈决定的编码比较，以及一个作者编写的适配器能否填入同一记录结构。它们没有验证 evidence card 相比聚合表或原始日志是否提高审查正确性、效率、可追溯性或错误发现能力。与此同时，核心证据包既未提供审稿访问入口，也尚不能脱离项目外部硬编码路径复现。因此当前版本仍存在两个投稿阻断项。

### 最优先的三项行动

1. **发布可供审稿访问且可 clean-room 复现的自包含 artifact。** 必须消除项目外路径依赖，补齐 license、固定版本、校验和、环境和一键复现入口。
2. **增加一个非结构自证式的有效性评价。** 若继续把 auditability 作为中心贡献，优先进行 reviewer/analyst utility study；至少应有独立审查者完成预定义的 claim-tracing 任务。
3. **按当前 RQ 重新定义评估总体。** 2,353 个“function-label-available”样本是旧分类任务遗留筛选条件，与新 RQ 不一致；tool-output/card accounting 应覆盖全部 2,431 个样本，source-role 任务应按 source-oracle availability 单独选样。

## 2. 已复算和已关闭事项

| 项目 | 复审结果 | 判定 |
|---|---|---|
| GEB production/ungated predicate | 353 TP、263 TN、0 FP、0 FN | 数值通过 |
| OpenPLC ungated probe | v2: 359 FN；v3: 376 FN；合计 735；production 均为 `OUT_OF_SCOPE` | 旧 scope-gate 问题关闭 |
| S2/S3/S6 tool-output task | 三者均为 1,873 TP、480 TN | 数值通过，但任务由 EC1 定义直接决定 |
| S3/S6 source-role task | 两者均为 TP=451、FP=24、FN=637、TN=761 | 数值通过 |
| Source-role signature ambiguity | S2/S3/S6 的 1,873 行均处于 target-ambiguous signature | 边界披露正确；效度有限 |
| EC1/EC2/EC3/EC5 co-fill | 2,353 行中 0 个状态不一致 | 数值通过 |
| Cross-pipeline package | 10 张卡、6,657 条关系、20 条 uncertainty rows | 数值通过 |
| Cross-pipeline diversity | 全部 GCC/x86-64；9 个 O0，1 个 project-O2；10 张卡的 EC 状态模式相同 | 不构成独立 compiler/vendor 验证 |
| v5 output hashes | `V5_JSS_METHOD_VALIDATION_RESULT.json` 中列出的 9 个输出哈希全部匹配 | 完整性通过 |
| 36/36 validator | 检查文件存在、输出哈希、指定计数、关键词边界和编译日志 | 只证明内部一致性，不证明研究效度 |

## 3. Dimension 1：宏观逻辑、贡献链和方法效度

| # | 具体发现与证据 | 严重度 | 建议行动 | SCAA-PLC 收益 | 实施成本 | 过度主张风险 |
|---|---|---|---|---|---|---|
| C1 | 核心方法贡献尚未被非结构自证式实验验证。主文第 302 行将 auditability 操作化为“traceability from a reported field to its sample, hash, tool output, rule, uncertainty code, and execution log”，但 RQ1 只测一个 `dt_FB_` 命名规则，RQ2 的 tool-output target 与 EC1 的定义直接同源，RQ3 则由作者编写适配器填充预定字段。第 585 行也明确承认没有 reviewer/security-analyst task。四项贡献中的第 1 项因此没有对应的效果验证。 | **CRITICAL** | 增加受控 reviewer/analyst task：让独立参与者在 aggregate-only/raw-log/evidence-card 条件下完成“定位证据来源、区分无证据与否定、发现越界主张、核对 hash/规则”等任务；采用交叉、随机、counterbalanced 设计，报告正确率、时间、校准度和置信区间。若无法做人类研究，至少增加独立审查者的 trace-query benchmark，并把论文降格为“design and feasibility study”，不得暗示 utility。 | 直接验证论文最核心的 auditability 构念，使 Contribution 1 有对应证据。 | 高；完整研究通常需要伦理审批、任务设计、招募和功效分析。轻量专家审查为中等。 | **高。** 当前只能声称结构化 traceability by construction，不能声称提高审查质量或 usefulness。 |
| C2 | Artifact 既不可供审稿访问，也不是自包含。主文第 452、619 行明确写明无公共 archive/DOI；`build_jss_method_validation.py` 第 37--44 行把第二流水线输入指向 `ROOT.parents[1] / "_scaa_evidence_build_project"`，结果 JSON 第 10--12 行保存的是 `EXTERNAL_INPUT_ROOT/...`。这与论文的可审计、可复现中心主张直接冲突。 | **CRITICAL** | 提交前提供匿名 reviewer URL 或按期刊政策提供持久公开 DOI；把所有允许发布的输入复制到 artifact 内部或提供可验证下载器，改用包内相对路径，补齐 `LICENSE`、third-party notice、环境锁定、checksums、README、one-command reproduction 和 clean-room 日志。 | 使审稿人能够核对 C1--C18，并把“hash-addressed local package”升级为真正可复查证据。 | 中；若第三方输入许可清晰，约 1--3 天。 | **高。** 未完成前不可写“available”“released”“reproducible package”。 |
| M1 | 当前评价总体仍由已删除的 function-classification 任务决定。第 237 行称 78 行因“function classification cannot score them”而排除，但三个新 RQ 均不进行 function classification。tool-output availability 和 evidence-card construction 本可覆盖 2,431 行；source-role task 应按 source/oracle availability 选样。 | **MAJOR** | 为每个 RQ 单独定义 inclusion/exclusion flow：card/tool-output accounting 使用全部 2,431 行；source-rule 使用具有可靠 source mapping 的行；仅历史 classifier diagnostics 才使用 function label。重建卡片、oracle 和相关表，并报告 78 行在新任务中的去向。 | 去除旧任务遗留选择偏差，强化“unsupported samples 不被隐藏”的核心论点。 | 中；需重跑 v3/v4/v5 并同步所有计数。 | 中高。维持 2,353 时只能声称“label-available subset”，不能把它当作方法总体。 |
| M2 | 六槽位和 U01--U14 的内容效度仍未建立。第 332、364 行直接定义字段和 taxonomy，但没有字段来源、需求分析、独立编码、专家评审、饱和度或跨工具覆盖过程。S3=S6 只能说明 PLC-BEAD 上的状态分区冗余，不能证明六个 provenance categories 必要、充分或易于解释。 | **MAJOR** | 给出 schema derivation protocol：从 EUBA、provenance、SE reporting standards 和真实失败样本导出设计需求；由至少两名独立编码者对失败/证据类型编码，报告分歧处理和一致性；用外部流水线检验新类别率、无法归类率和 slot/query coverage。 | 把“作者定义的六格表”提升为有内容效度的 reporting schema。 | 中高。 | **高。** 当前只能称“chosen provenance categories”，不能称完整 taxonomy 或通用 schema。 |
| M3 | RQ3 的“record portability”证据更接近 adapter smoke test。第 512 行只包含 10 个 OpenPLC-derived ELF；输出显示全部为 GCC/x86-64、9 个 O0，且所有卡均为 `filled/partial/filled/partial/filled/filled`。脚本第 376--381 行还直接赋予若干 slot 固定状态。没有样本选择协议、负例、未知字段、适配失败率或独立实现。 | **MAJOR** | 二选一：A）加入独立 compiler/vendor/architecture corpus，预先定义映射规则、contract invariants、失败条件和 coverage；B）若不扩展，统一改称“second-pipeline contract instantiation/smoke test”，删除 headline 中的 portability/transfer 推断，并把 RQ3 降为 implementation feasibility。 | 避免把“能写一个 adapter”误写成可移植方法，并使外部效度表述可防守。 | A 高；B 低。 | **高。** 现有证据不支持 compiler/vendor/schema portability。 |
| M4 | RQ1 的数据边界已正确收窄，但作为论文第二项贡献仍过重。第 117 行称 production rule 与 probe “validates both”，实际是同一 snapshot 中回顾性观察到的单一 lexical convention；正文未说明 SA-001 的规则发现集与验证集是否分离。 | **MAJOR** | 将 RQ1 定位为 boundary-aware method 的 worked validity case，而非普遍规则贡献。补充 rule-development provenance；最好在共享 inferred program names 上做 GEB/OpenPLC 配对分析，并将规则发现与确认样本分离或明确标为 post-hoc confirmation。 | 把零误差结果从易受质疑的“完美规则”转化为可信的 scope-boundary 示例。 | 低至中。 | 中高。不可写成 compiler-independent accuracy 或 prospective validation。 |
| M5 | 转向 JSS 后，软件工程 reporting-method 的最近工作覆盖不足。当前只引用 Sim 2003、通用 provenance 和 Evaluation Cards，未覆盖 SE 实验报告指南、报告实践实证研究及 metadata-driven experimentation。尤其 ICSE 2026 FoSE 的 metadata-driven experimentation 与本文“结构化、机器可解释的实验元数据”高度接近。 | **MAJOR** | 至少加入并正面对比：Kitchenham et al. 2008 的 reporting-guideline evaluation；Cerqueira Revoredo et al. 2021 的 SE experiment reporting practice；Santana et al. 2026 的 metadata-driven experimentation；artifact availability/reproducibility 文献。对 Evaluation Cards 应比较 schema derivation、stakeholder validation、deployment scale 与 SCAA-PLC 的 per-binary/per-read 特性。 | 强化 JSS 社群定位，明确真正的新颖轴是 PLC-binary observation/uncertainty/read provenance，而不是泛化的“card”概念。 | 低至中。 | **高。** 未补充时可能被判为对既有 reporting schema 的领域化、小幅增量。 |
| M6 | 主文和补充材料仍保留旧叙事。主文第 172 行仍写“ablation separating symbol-derived signal from benchmark metadata”；补充材料保留 across-fold spread、weighted summary、C2--C5/C9 历史 baseline claims 和 C18 自赋“scoped-ready verdict”；F4 第 295 行仍把 `fold_0 diagnostic-band characterization` 写作本文替代表述。 | **MAJOR** | 投稿补充材料只保留支持当前 RQ 的协议、行级结果、claim matrix 和复现说明。将历史 spread/baseline/内部 verdict 移到 artifact 的 `history/`，不作为 submission supplement 内容；更新 F4 替代表述。 | 减少审稿人被旧分类论文线索带偏的风险，使 claim surface 与主文一致。 | 低。 | 中。虽然均有免责声明，保留它们仍会引发“究竟哪篇论文”的疑问。 |
| M7 | Running example 在引言第 105 行和方法第 356 行出现，但没有进入 Evaluation。读者看不到三张具体卡如何支持或阻止一项审查结论。 | **MAJOR** | 在 Evaluation 增加一张三案例 trace 表：raw observation → rule/provenance → EC state → U-code → oracle/allowed conclusion；再给出一个错误 aggregate claim 如何被 card 拒绝的例子。 | 让 reporting method 的实际审查价值可见，并直接验证端到端 trace chain。 | 低。 | 低，只需避免把案例可追溯性写成人类效用。 |
| M8 | 论文过度依赖否定式边界，正向保证不够集中。类似“not semantic recovery / not vulnerability detection / not analyst utility”在摘要、引言、数据、方法、评价、讨论和结论重复出现；第 545 行虽总结结果，但没有用可检验 invariant 概括方法实际保证什么。 | **MAJOR** | 在方法开头定义 3--4 个正向 contract invariants，例如 trace completeness、uncertainty closure、hash-consistent joins、unsupported-not-negative；Evaluation 逐一报告通过率和失败实例。将重复免责声明集中在 scope table、每个高风险结果的首次解释和 limitations。 | 提高论文说服力，避免审稿人读完只记得“什么都不做”。 | 低至中。 | 低。正向保证必须严格限制在可自动核验的 contract 层。 |

## 4. Dimension 2：写作细节与章节组织

整体英文已明显收敛，摘要、引言、RQ、评价和结论的数值边界一致。没有发现大段重复的旧 baseline 叙事进入主结果。不过，以下内容仍需精修。

| # | 发现 | 严重度 | 修改建议 |
|---|---|---|---|
| W1 | `SCAA-PLC` 直到第 302 行才展开为 `Symbol-Consistent Auditable Analysis for PLC binaries`，摘要和引言并不自包含。 | **MINOR** | 在摘要首次出现时展开，或不再把它作为需解释的缩写。 |
| W2 | 第 593 行“For cyber-physical systems research ...”是 TCPS 路线残留；本文不评价 CPS/physical process，并已转向 JSS reporting method。 | **MINOR** | 改为面向 empirical software evaluation/review 的用途，或删除。 |
| W3 | Abstract 连续堆叠 oracle、735 FN、schema、10/6,657/20 和三项否定边界，中心 take-away 被数字淹没。 | **MINOR** | 保留一个 rule-transfer 数字、一个 schema 结论和一个 adapter 规模；用一句话明确“what the method guarantees”。 |

## 5. Dimension 3：英文语法和表述精度

未发现系统性的冠词、主谓一致或时态错误。需要修改的一处明确表述为：

| # | 原文 | 规则 | 严重度 | 建议改写 |
|---|---|---|---|---|
| G1 | 第 285 行：`Every relation and uncertainty SHA256 joins to the corresponding row ...` | **G4：一句一个主要意思，避免歧义复合修饰。** | **MINOR** | `The SHA-256 value in every relation and uncertainty record matches the corresponding native-manifest entry.` |

另有一项 **MINOR** 参考文献内容准确性问题：`refs.bib` 第 220--228 行的 EUBA 作者列表含 `David Hannasch`，而 Sandia 官方记录列的是 `James W. Foulk`。这不是排版问题，应在后续内容修订中核对 DOI `10.2172/1832314` 的完整作者元数据。

## 6. Banned-vocabulary 与 em-dash 全文扫描

已对 `main.tex` 625 行和 `supplementary.tex` 329 行执行完整、大小写不敏感扫描，而非抽样。

- Unicode em-dash `—`：**0**
- 技能禁用词/短语（包括 `innovative`、`pioneering`、`superior`、`remarkable`、`notably`、`yielding`、`reveal`、`underscore`、`general-purpose` 等）：**0**
- 无条件 SOTA、`we solve`、`we are the first`、`outperform`：**0**

该项通过。

## 7. Dimension 4/5：本轮按要求暂缓

- **LaTeX/JSS 格式：DEFERRED**
- **图件视觉质量和版面：DEFERRED**
- **作者 affiliation、Declarations、CRediT、Highlights、投稿元数据：DEFERRED**

本报告不以当前仍为 ACM/TCPS 类文件、页数、浮动体、字体或版面情况扣分。上述工作应在内容门禁通过后进行。

## 8. Section-by-section 复审

| 章节 | 结论 | 投稿前动作 |
|---|---|---|
| Abstract | 数值和边界已同步；中心保证不够突出。 | 压缩数字，加入正向 contract guarantee；artifact 发布后补 URL/DOI。 |
| Introduction | 从 TCPS 案例稿转向 reporting-method 稿已完成；四贡献与三 RQ 中 Contribution 1 缺少效果评价。 | 将 utility/trace-query evaluation 映射到 Contribution 1；将 RQ1 降为 validity case。 |
| Background/Related Work | PLC/binary 方向较完整，JSS reporting-method 文献不足。 | 补 SE reporting guidelines、metadata-driven experimentation 和 artifact reproducibility；深化与 Evaluation Cards/EUBA 的差异。 |
| Dataset and Protocol | 边界披露诚实，但 2,353 样本筛选与新 RQ 不匹配。 | 为每个 RQ 重建 inclusion flow，优先使用全 2,431 card population。 |
| Framework | 字段、U-code 和构造顺序清楚；schema derivation/content validity 不足。 | 增加设计需求、来源、独立编码/专家验证和 contract invariants。 |
| Evaluation | 所有新数值可复算；现有实验主要证明内部一致性和可填充性。 | 增加非自证式 utility/traceability outcome；重新表述 schema comparison 和 adapter test。 |
| Discussion | 对限制的披露充分，是当前稿件的优点。 | 减少重复否定，明确哪些局限通过哪项未来研究关闭。 |
| Conclusion | 与正文结果一致，没有 vulnerability/SBOM/SCA 过度主张。 | 若不加外部 corpus，把 `portability` 统一降为 `bounded instantiation`。 |
| Supplement | 技术细节充分，但保留过多已退出主线的历史指标和 claims。 | 提交版删除历史 spread、baseline 和内部 ready verdict；历史留 artifact。 |

## 9. 三个投稿阻断决策

| 决策 | 审稿建议 | 证据基础 | SCAA-PLC 收益 | 成本 | 过度主张风险 | 推荐动作 |
|---|---|---|---|---|---|---|
| Artifact package | **必须做，提交前完成。** | 论文中心是 auditability/reproducibility，但主文明确只有本地包，脚本还读取项目外输入。JSS 官方范围要求主张有证据，并支持 Open Science material。 | 关闭 C2，使所有行级证据可审查。 | 中 | 未发布时高 | 先制作匿名/审稿访问固定包；按 blind policy 决定是否立即公开 DOI。代码建议 Apache-2.0/MIT/BSD-3-Clause 三选一；作者生成数据可用 CC BY 4.0；第三方 PLC-BEAD 不重复授权，只记录来源和版本。 |
| Analyst/reviewer utility study | **若继续投 JSS 方法型论文，强烈建议，且优先级高于扩充更多同类二进制。** | EUBA 已对 uncertainty 与人类任务进行验证；Evaluation Cards 也有 stakeholder interviews 和大规模部署。当前论文只把 inspectable 定义为 artifact traceability。 | 直接关闭 C1，证明 evidence card 的实际价值。 | 中高/高 | 不做却声称 usefulness 时极高 | 首选 counterbalanced within-subject reviewer task；若专家难招，先做独立 expert content-validity + trace-query study，并明确是初步效用证据。 |
| Independent vendor/compiler corpus | **推荐，但可在严格降级 RQ3 后暂不做。** | 当前 10 样本全部 GCC/x86-64，9 个 O0，且同属 OpenPLC 相关路径。 | 支撑 schema portability 和外部效度。 | 高 | 维持 portability headline 时高 | 有资源则加入至少一个非 OpenPLC compiler/vendor 或不同 architecture，并预注册 mapping/failure rules；无资源则把 RQ3、摘要和结论统一改为 `second-pipeline contract instantiation`，不再作为 portability 贡献。 |

### 推荐路线

**路线 A：继续投 JSS，推荐。** 先完成自包含 artifact，再增加 reviewer/analyst utility study；若资源允许，再加入独立 compiler/vendor corpus。JSS 官方 Aims & Scope 明确接收“methods and tools for empirical software engineering research”，因此不需要补 plant model 或 physical-process experiment 来证明 venue fit。当前问题是方法证据强度，不是 JSS 主题不匹配。

**路线 B：不增加人类/独立审查评价。** 可保留为 bounded design-and-feasibility case study，但必须把 `method validity`、`schema economy` 和 `record portability` 进一步降级为 `contract definition`、`observed state-partition equivalence` 和 `adapter smoke test`。该路线可以更快投稿，但作为 JSS regular paper 的新颖性和有效性风险仍高。

## 10. 建议的内容门禁

进入 JSS 格式迁移前，建议同时满足：

1. reviewer-accessible artifact 有固定 URL、版本、license、checksum 和 clean-room reproduction log；
2. 所有 v5 输入均位于包内或能由受控下载脚本获取，不再依赖 `EXTERNAL_INPUT_ROOT`；
3. 三个 RQ 各自的 evaluation population 与 target 对齐，旧 function-label gate 不再控制新任务总体；
4. auditability 至少有一项独立、非 by-construction outcome；
5. RQ3 根据是否有独立 corpus，在 `portability` 与 `bounded instantiation` 中作唯一选择；
6. 投稿 supplement 删除已退出贡献链的历史 baseline/spread/internal-ready claims；
7. 补齐 JSS reporting-method 最近工作并重写 novelty matrix。

满足 1--7 后，才建议执行 JSS 模板、affiliation、Declarations 和最终版面轮次。

## 11. 检索依据

- [Journal of Systems and Software, Aims & Scope](https://www.sciencedirect.com/journal/journal-of-systems-and-software)：覆盖 empirical software engineering 的方法和工具，要求文章提供证据支持主张，并支持 Open Science material。
- [Santana et al., Toward Metadata-Driven Experimentation in Software Engineering, ICSE 2026 FoSE](https://conf.researchr.org/details/icse-2026/icse-2026-future-of-software-engineering/23/Toward-Metadata-Driven-Experimentation-in-Software-Engineering-A-Vision-for-Reproduc)：与结构化、机器可解释的实验元数据定位高度接近。
- [Cerqueira Revoredo et al., A Study into the Practice of Reporting Software Engineering Experiments, EMSE 2021](https://doi.org/10.1007/s10664-021-10007-3)：直接研究 SE 实验报告指南及其实践缺口。
- [Evaluation Cards: An Interpretive Layer for AI Evaluation Reporting](https://arxiv.org/abs/2606.09809)：以文献综述、stakeholder interviews 和大规模部署验证 reporting layer。
- [Sandia EUBA](https://www.sandia.gov/research/publications/details/exploring-explicit-uncertainty-for-binary-analysis-euba-2021-11-01/)：与二进制分析不确定性及人类分析任务最接近。
- [Publish or perish, but do not forget your software artifacts](https://doi.org/10.1007/s10664-020-09851-6)：支持持久 archive、唯一标识符和可用 artifact 的必要性。
