# Nguồn các hình minh họa bổ sung (cập nhật 2026)

Các hình dưới đây được lấy từ bài báo gốc để minh họa cho phần nội dung mới.
Mọi hình đều được chú thích kèm nguồn ngay trong sách. Nếu xuất bản thương mại,
cần xin phép tác giả/nhà xuất bản đối với các hình không có giấy phép mở.

| Tệp | Nguồn | Bài báo | Giấy phép |
|---|---|---|---|
| `flashattention_memory_hierarchy.png` | arxiv.org/html/2307.08691v1/figs/flash_attention_diagram.png | Dao, *FlashAttention-2* (arXiv:2307.08691) | arXiv (xem trang bài báo) |
| `ring_attention_overview.png` | ar5iv.labs.arxiv.org/html/2310.01889/assets/figures/merged.png | Liu, Zaharia, Abbeel, *Ring Attention* (arXiv:2310.01889) | arXiv |
| `mha_gqa_mqa_comparison.png` | ar5iv.labs.arxiv.org/html/2305.13245/assets/images/gmq_architecture.png | Ainslie et al., *GQA* (arXiv:2305.13245) | arXiv |
| `mla_vs_mha_gqa_mqa.png` | arxiv.org/html/2405.04434v5/dsattn.png | DeepSeek-AI, *DeepSeek-V2* (arXiv:2405.04434) | arXiv |
| `deepseek_v3_architecture.png` | arxiv.org/html/2412.19437v2/basic_arch.png | DeepSeek-AI, *DeepSeek-V3* (arXiv:2412.19437) | arXiv |
| `chinchilla_isoflop_curves.png` | ar5iv.labs.arxiv.org/html/2203.15556/assets/approach_3_v2.png | Hoffmann et al., *Chinchilla* (arXiv:2203.15556) | arXiv |
| `test_time_vs_pretrain_compute.png` | arxiv.org/html/2408.03314v1/comparing_test_pretrain_v8.png | Snell et al., *Scaling LLM Test-Time Compute* (arXiv:2408.03314) | arXiv |
| `test_time_search_strategies.png` | arxiv.org/html/2408.03314v1/Search_Figure-2.svg (chuyển SVG sang PNG) | Snell et al., *Scaling LLM Test-Time Compute* (arXiv:2408.03314) | arXiv |
| `r1_zero_response_length.png` | nature.com/articles/s41586-025-09422-z (Fig. 1) | DeepSeek-AI, *DeepSeek-R1* (Nature 645, 633–638, 2025) | **CC BY 4.0** |
| `deepseek_r1_pipeline.png` | nature.com/articles/s41586-025-09422-z (Fig. 2) | DeepSeek-AI, *DeepSeek-R1* (Nature 645, 633–638, 2025) | **CC BY 4.0** |
| `smoothquant_migration.png` | ar5iv.labs.arxiv.org/html/2211.10438/assets/intuition.png | Xiao et al., *SmoothQuant* (arXiv:2211.10438) | arXiv |
| `pagedattention_block_table.png` | ar5iv.labs.arxiv.org/html/2309.06180/assets/system-overview.png | Kwon et al., *vLLM / PagedAttention* (arXiv:2309.06180) | arXiv |
| `mooncake_architecture.png` | arxiv.org/html/2407.00079v4/cache_unit_v2.png | Qin et al., *Mooncake* (arXiv:2407.00079) | arXiv |
| `swe_bench_overview.png` | ar5iv.labs.arxiv.org/html/2310.06770/assets/example.png | Jimenez et al., *SWE-bench* (arXiv:2310.06770) | arXiv |

| `fineweb_edu_pipeline.png` | Hình 11 trong bản PDF của bài báo FineWeb (arXiv:2406.17557), cắt từ trang 9 | Penedo et al., *The FineWeb Datasets* (arXiv:2406.17557) | arXiv |

## Hình còn thiếu (đang hiển thị khung chờ trong bản PDF)

Macro `\bookimage{<mã>}{<mô tả>}` trong `style.tex` sẽ tự chèn ảnh khi tệp
`images/<mã>.png` (hoặc `.jpg`) xuất hiện, nên chỉ cần thả ảnh vào thư mục này:

Hiện không còn hình nào thiếu: mọi `\bookimage` trong sách đều đã có ảnh tương ứng.
Nếu sau này thêm `\bookimage{<mã>}` mới, chỉ cần thả ảnh `images/<mã>.png` vào đây là nó
tự xuất hiện trong bản biên dịch.
