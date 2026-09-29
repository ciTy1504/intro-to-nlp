# Rà soát `llm_research_reading_list_2026.txt` (tháng 9/2026)

Tài liệu này ghi lại kết quả đối chiếu danh sách đọc với arXiv khi cập nhật bản thảo:
những link bị sai, những tiêu đề không khớp, và các bài được bổ sung thêm vào sách.

## 1. Link sai trong danh sách gốc

| Mục trong danh sách | ID trong danh sách | Thực tế ID đó là bài gì | ID đúng |
|---|---|---|---|
| ReST^EM | `2312.08935` | **Math-Shepherd**: Verify and Reinforce LLMs Step-by-step without Human Annotations | `2312.06585` — *Beyond Human Data: Scaling Self-Training for Problem-Solving with Language Models* |
| Gemini | `2312.11830` | *Hopf orbits and the first ECH capacity* (hình học symplectic) | `2312.11805` — *Gemini: A Family of Highly Capable Multimodal Models* |
| GKD | `2306.08507` | *Qubit efficient quantum algorithms for the vehicle routing problem* | `2306.13649` — *On-Policy Distillation of Language Models: Learning from Self-Generated Mistakes* |
| LM Evaluation Harness | `2403.13762` | *When Cars meet Drones: Hyperbolic Federated Learning...* | `2405.14782` — *Lessons from the Trenches on Reproducible Evaluation of Language Models* |
| Muon is Scalable for LLM Training | `2502.XXXXX` (để trống) | — | `2502.16982` |

## 2. Tiêu đề không khớp với ID

| ID | Tiêu đề trong danh sách | Tiêu đề thật |
|---|---|---|
| `2406.04879` | A Deep Dive into the Trade-Offs of **Parameter-Efficient Fine-Tuning** | A Deep Dive into the Trade-Offs of **Parameter-Efficient Preference Alignment Techniques** (ACL 2024) |
| `2312.12740` | Fine-tuning Large Language Models for **Domain Specific Applications** | Fine-tuning Large Language Models for **Adaptive Machine Translation** |

## 3. Đã kiểm chứng là có thật (các bài mới, dễ nhầm là bịa)

- `2510.01631` — *Demystifying Synthetic Data in LLM Pre-training* (Kang et al., Meta, 10/2025).
- `2602.22495` — *Reinforcement-aware Knowledge Distillation for LLM Reasoning* (Zhang et al., 2/2026).
- `2408.08147` — *P/D-Serve: Serving Disaggregated Large Language Model at Scale* (Huawei).

## 4. Trích dẫn bịa đã bị xóa khỏi `Tex/references.bib`

Bản thảo cũ có hai mục không tồn tại, được dùng để trích dẫn phần GRPO:

- `verl2024` — "VERL: Vision-Enhanced Reinforcement Learning Framework for LLM-based Agents" (không tồn tại).
  Framework verl thật được mô tả trong *HybridFlow: A Flexible and Efficient RLHF Framework* (`2409.19256`).
- `grpo2024` — "GRPO: Generalized Reward Policy Optimization..." (không tồn tại).
  GRPO thật được giới thiệu trong *DeepSeekMath* (`2402.03300`).

Ngoài ra đã sửa: tác giả sai của *Tree of Thoughts* và *Mixtral of Experts*, và lỗi `and and others`
trong mục `chung2022scaling` (lỗi này khiến BibTeX dừng giữa chừng khi biên dịch).

### 4b. Rà soát nhóm PEFT (chương Tinh chỉnh)

Đối chiếu với arXiv cho thấy **3 mục nữa không tồn tại** — ID arXiv của chúng trỏ sang các bài
hoàn toàn khác lĩnh vực. Đã xóa khỏi `references.bib` và bỏ trích dẫn trong bài:

| Khóa | Tiêu đề trong bib | ID đó thực ra là bài gì |
|---|---|---|
| `gupta2022s4adapter` | S4-Adapter: Leveraging Structured State-Space Models... (`2210.11750`) | *Generative Range Imaging for Learning Scene Priors of 3D LiDAR Data* |
| `hu2022sparsellora` | Sparse LoRA: Low-Rank and Sparse Adaptation... (`2211.04403`) | *Neutrino mass and leptogenesis in a hybrid seesaw model* |
| `ben-zaken2022ln-tuning` | LayerNorm tuning... (`2206.01726`) | *Average-case analysis of the Gaussian Elimination with Partial Pivoting* |

Hai mục `wang2022ipt` (IPT) và `jia2022promptadapter` (PromptAdapter) không tra được bài tương ứng
nên cũng đã bỏ.

**Bài thật nhưng bị gán sai tác giả / năm** — đã sửa lại theo arXiv:

| Khóa | Tác giả đúng |
|---|---|
| `buczak2023krona` (KronA) | Edalati, Tahaei, Kobyzev, Partovi Nia, Clark, Rezagholizadeh (`2212.10650`) |
| `he2021laddersidetuning` (LST) | Sung, Cho, Bansal (`2206.06522`) |
| `chen2022adamixture` (AdaMix) | Wang, Agarwal, Mukherjee, Liu, Gao, Awadallah, Gao (`2205.12410`) |
| `ma2022unipelt` (UniPELT) | Mao, Mathias, Hou, Almahairi, Ma, Han, Yih, Khabsa (`2110.07577`) |
| `gheini2022warp` (WARP) | Hambardzumyan, Khachatrian, May (`2101.00121`, ACL 2021) |
| `hu2023llmpeft` (khảo sát PEFT) | Xu, Xie, Qin, Tao, Wang (`2312.12148`) |
| `zhang2021phm` (PHM) | Zhang Aston, Tay, Zhang Shuai, Chan, Luu, Hui, Fu (`2102.08597`) |
| `sung2022fishmask` (Fish-Mask) | Sung Yi-Lin, Nair, Raffel — *Training Neural Networks with Fixed Sparse Masks* (`2111.09839`) |
| `he2022towards` | He Junxian, Zhou, Ma, Berg-Kirkpatrick, Neubig — *Towards a Unified View of PEFT* (`2110.04366`) |
| `liu2021p` (P-Tuning v1) | Liu Xiao, Zheng, Du, Ding, Qian, Yang, Tang (`2103.10385`) |
| `liu2021ptuningv2` | Liu Xiao, Ji, Fu, Tam, Du, Yang, Tang (`2110.07602`) |
| `wang2022text` (E5) | Wang Liang, Yang, Huang, Jiao, Yang, Jiang, Majumder, Wei (`2212.03368`) |
| `wang2022textembeddings` | Neelakantan et al., OpenAI (`2201.10005`) |
| `su2021rope` / `su2021roformer` | Su, Lu, Pan, Murtadha, Wen, Liu (`2104.09864`) — hai khóa trùng nội dung |

Một lỗi nội dung đi kèm: bản cũ giải thích **WARP** là "Weighted Adapter-Routing Prompting" --
tên này không tồn tại. WARP thật là **Word-level Adversarial ReProgramming**; phần mô tả đã được viết lại.

## 5. Các bài bổ sung ngoài danh sách (đã đưa vào sách)

Những bài này lấp các khoảng trống mà danh sách gốc chưa có:

- **Kiến trúc:** MQA (`1911.02150`), DeepSeekMoE (`2401.06066`), cân bằng tải không loss phụ (`2408.15664`),
  Position Interpolation (`2306.15595`), Multi-Token Prediction (`2404.19737`), RMSNorm, SwiGLU (`2002.05202`),
  Kimi K2 (`2507.20534`), Qwen3 (`2505.09388`).
- **Tối ưu hóa:** Muon gốc (blog Keller Jordan), benchmark bộ tối ưu (`2509.02046`) — bài này cho thấy mức
  tăng tốc thực tế so với AdamW được tinh chỉnh kỹ nhỏ hơn nhiều so với các con số thường được trích dẫn.
- **Dữ liệu:** khử trùng lặp (`2107.06499`), dữ liệu hữu hạn (`2305.16264`), WRAP (`2401.16380`), Phi (`2306.11644`).
- **Hậu huấn luyện:** DAPO (`2503.14476`), Dr. GRPO (`2503.20783`), GSPO (`2507.18071`) — ba cải tiến quan trọng
  của GRPO sau DeepSeek-R1.
- **Chưng cất:** Sequence-level KD (`1606.07947`).
- **Phục vụ:** Orca (OSDI 2022), DistServe (`2401.09670`), Medusa (`2401.10774`), EAGLE (`2401.15077`),
  SGLang (`2312.07104`).
- **Đánh giá:** Chatbot Arena (`2403.04132`), SWE-bench Verified (OpenAI, 2024).
- **PEFT:** DoRA (`2402.09353`), DAPT/TAPT (`2004.10964`).

## 6. Bản đồ danh sách đọc → chương mục

Xem **Phụ lục A** trong sách (`Tex/appendix_reading_map.tex`): bảng ánh xạ từng bài báo sang mục
tương ứng, kèm năm câu hỏi nên đặt ra khi đọc mỗi paper.
