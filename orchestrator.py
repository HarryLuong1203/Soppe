import json
import os
import sys

STATE_FILE = "state.json"
REPORT_FILE = "hackathon_execution_report.md"

def load_state():
    with open(STATE_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_state(state):
    with open(STATE_FILE, "w", encoding="utf-8") as f:
        json.dump(state, f, indent=4, ensure_ascii=False)

def run_simulation():
    state = load_state()
    state["gen2_retry_count"] = 0
    state["current_loop"] = 1
    state["history"] = []
    save_state(state)

    execution_log = []

    def log(step_title, content):
        execution_log.append({"step": step_title, "content": content})
        print(f"\n==================== {step_title} ====================")
        print(content)

    # -------------------------------------------------------------
    # STEP 1: Agent 1 - Initial Idea Generation (Attempt 1)
    # -------------------------------------------------------------
    agent1_attempt1_idea = {
        "title": "ShopeeAssist: Universal 24/7 AI Customer Support Chatbot for Social & Marketplace Sellers",
        "build_direction": "AI-Native Products & Operations",
        "target_audience": "Chủ shop bán hàng online trên Shopee, TikTok Shop, Facebook tại Việt Nam & Đông Nam Á.",
        "problem": "Người bán bị quá tải bởi hàng trăm tin nhắn hỏi lặp đi lặp lại: 'Còn hàng không?', 'Freeship không?', 'Khi nào giao?'.",
        "core_mechanism": "Một chatbot tích hợp API tin nhắn, tự động đọc câu hỏi thường gặp (FAQ), tra cứu bảng giá và trả lời người mua tự động 24/7.",
        "codex_7h_scope": "Build một widget chat bằng React và backend Node.js kết nối OpenAI Assistant API để hỏi đáp tài liệu FAQ shop tải lên."
    }
    log("AGENT 1: Sinh ý tưởng ban đầu (Lần 1)", json.dumps(agent1_attempt1_idea, indent=2, ensure_ascii=False))

    # -------------------------------------------------------------
    # STEP 2: Agent 2 - Novelty & Duplication Check (Attempt 1)
    # -------------------------------------------------------------
    agent2_check_1 = {
        "status": "TRÙNG LẶP (DUPLICATE)",
        "similar_products": ["Shopee Auto-Reply", "Botcake", "Pancake", "Channex", "Tidio E-commerce"],
        "reason": "Ý tưởng chatbot hỏi đáp FAQ cho shop là dạng generic wrapper, đã có hàng chục giải pháp thương mại hoàn thiện trên thị trường và tính năng có sẵn của sàn TMĐT. Hoàn toàn thiếu tính AI-Native đột phá và không thể hiện được năng lực Autonomous đặc trưng của cuộc thi Sea x OpenAI.",
        "pivot_guidance": "Cần tập trung vào các 'nỗi đau tử huyệt' đặc thù của TMĐT Đông Nam Á (như rủi ro giao hàng COD, bom hàng, lừa đảo tráo hàng hoàn, hoặc xử lý tranh chấp khiếu nại đa phương thức) nơi mà AI Agent thực sự có tính năng tự chủ ra quyết định (Autonomous & Adaptive)."
    }
    log("AGENT 2: Kiểm tra độc quyền & trùng lặp (Lần 1)", json.dumps(agent2_check_1, indent=2, ensure_ascii=False))

    state["gen2_retry_count"] += 1
    save_state(state)
    log("ORCHESTRATOR", f"Phát hiện TRÙNG LẶP. gen2_retry_count = {state['gen2_retry_count']}/{state['max_gen2_retry']}. Kích hoạt nhánh RETRY cho Agent 1...")

    # -------------------------------------------------------------
    # STEP 3: Agent 1 - Retry Idea Generation (Attempt 2)
    # -------------------------------------------------------------
    agent1_attempt2_idea = {
        "title": "COD-Shield: Autonomous Multimodal Evidence Forensics & Dispute Resolution Agent for Southeast Asian E-Commerce",
        "build_direction": "Autonomous & Adaptive AI",
        "target_audience": "Nhà bán hàng quy mô vừa và nhỏ (MSMEs), người mua và các nền tảng TMĐT tại Đông Nam Á (Shopee, TikTok Shop, Lazada - nơi COD chiếm >60% giao dịch).",
        "problem": "Tỷ lệ gian lận đơn hàng COD và tráo hàng hoàn trả (Return/Refund fraud - khách nhận hàng tráo gạch đá/hàng cũ rồi yêu cầu hoàn tiền) gây tổn thất hàng triệu USD mỗi năm cho người bán ĐNA. Việc khiếu nại thủ công đòi hỏi đối soát video đóng gói và video khui hộp tốn từ 7-14 ngày, gây nghẽn dòng tiền.",
        "core_mechanism": "Hệ thống Agent tự chủ đa phương thức (Multimodal AI Agent): Tự động phân tích video/ảnh đóng hàng của shop đối chiếu với video unboxing của người mua; phát hiện dấu vết cắt rạch băng dính niêm phong, chênh lệch trọng lượng/kích thước; tự động đối chiếu chính sách sàn, đưa ra phán quyết bồi thường tự động và gửi hồ sơ khiếu nại chuẩn pháp lý tới sàn/đơn vị vận chuyển.",
        "codex_7h_scope": "Xây dựng pipeline phân tích video stream real-time, tích hợp crawler dữ liệu hành trình các đơn vị vận chuyển (GHN, J&T, NinjaVan), hệ thống ngân hàng escrow mô phỏng, và portal đối soát khiếu nại đa sàn bằng Next.js + FastAPI."
    }
    log("AGENT 1: Sinh lại ý tưởng (Lần 2 - sau phản hồi của Agent 2)", json.dumps(agent1_attempt2_idea, indent=2, ensure_ascii=False))

    # -------------------------------------------------------------
    # STEP 4: Agent 2 - Novelty Check (Attempt 2)
    # -------------------------------------------------------------
    agent2_check_2 = {
        "status": "HỢP LỆ (PASS)",
        "differentiation": "Đánh trúng 'vùng trũng' lớn nhất của TMĐT Đông Nam Á (nạn tráo hàng hoàn COD). Ứng dụng Computer Vision đối chiếu video đóng gói vs unboxing để tự động hóa tranh chấp là hướng tiếp cận độc đáo, chưa có giải pháp chuyên biệt nào thống trị mảng này cho SME Đông Nam Á.",
        "verdict": "Chấp thuận cho chuyển sang Agent 3 chấm rubric."
    }
    log("AGENT 2: Kiểm tra độc quyền & trùng lặp (Lần 2)", json.dumps(agent2_check_2, indent=2, ensure_ascii=False))

    # -------------------------------------------------------------
    # STEP 5: Agent 3 - Rubric Evaluation (Round 1 - Stateless)
    # -------------------------------------------------------------
    # Agent 3 receives stateless payload per Section 5:
    agent3_round1_payload = {
        "idea": agent1_attempt2_idea,
        "rubric": "Gate (Khớp hướng), Gần gũi (30%), Giá trị (30%), Khả thi 7h Codex (40%)",
        "instruction": "Chấm điểm ý tưởng này như thể đây là lần đầu tiên bạn thấy nó."
    }
    log("AGENT 3: Nhận Stateless Payload (Vòng 1)", "Agent 3 hoàn toàn không biết đây là vòng 1 hay đã từng bị reject trước đó.")

    agent3_round1_eval = {
        "gate_build_direction": {
            "status": "PASS",
            "comment": "Khớp hoàn hảo với 'Autonomous & Adaptive AI': Agent tự đưa ra phán quyết tranh chấp và hành động lập hồ sơ bồi thường mà không cần con người duyệt từng chi tiết."
        },
        "criterion_2_gan_gui": {
            "score": 9.0,
            "weight": 0.3,
            "comment": "Cực kỳ thiết thực và gần gũi với đời sống bán hàng online tại ĐNA. COD và gian lận hoàn hàng là nỗi ám ảnh hàng ngày của mọi chủ shop."
        },
        "criterion_3_gia_tri": {
            "score": 8.5,
            "weight": 0.3,
            "comment": "Giá trị kinh tế lớn: Giảm 90% thời gian xử lý tranh chấp từ 10 ngày xuống 2 phút; giảm tỷ lệ mất hàng oan cho SME."
        },
        "criterion_4_kha_thi_codex_7h": {
            "score": 5.5,
            "weight": 0.4,
            "comment": "QUÁ RỦI RO CHO HACKATHON 7 TIẾNG: Scope cồng kềnh với video stream real-time, crawler carrier APIs, và ngân hàng escrow. Codex không thể dựng kịp hệ thống xử lý video streaming và đa tích hợp bên ngoài trong 7 tiếng mà vẫn chạy demo trơn tru."
        },
        "total_score": round(9.0 * 0.3 + 8.5 * 0.3 + 5.5 * 0.4, 2), # 7.45
        "verdict": "CHƯA ĐẠT",
        "weakest_criterion": "Khả thi build trong 7 tiếng bằng Codex",
        "weakest_reason": "Phạm vi kỹ thuật bị phình to (Scope bloat). Đòi hỏi phân tích video streaming thời gian thực kết hợp scraping API vận chuyển và giả lập thanh toán escrow, dẫn tới nguy cơ sụp đổ demo trong 7 tiếng."
    }
    log("AGENT 3: Kết quả chấm Rubric (Vòng 1)", json.dumps(agent3_round1_eval, indent=2, ensure_ascii=False))

    # Record history
    state["history"].append({
        "round": 1,
        "idea": agent1_attempt2_idea,
        "agent3_scores": {
            "total": agent3_round1_eval["total_score"],
            "gate": agent3_round1_eval["gate_build_direction"]["status"],
            "c2_gan_gui": agent3_round1_eval["criterion_2_gan_gui"]["score"],
            "c3_gia_tri": agent3_round1_eval["criterion_3_gia_tri"]["score"],
            "c4_kha_thi": agent3_round1_eval["criterion_4_kha_thi_codex_7h"]["score"]
        },
        "rejection_reason": agent3_round1_eval["weakest_reason"]
    })
    save_state(state)

    # -------------------------------------------------------------
    # STEP 6: Agent 4 - Problem Analyzer & Solution Proposer (Round 1)
    # -------------------------------------------------------------
    agent4_payload = {
        "current_version": {
            "idea": agent1_attempt2_idea,
            "agent3_scores": agent3_round1_eval,
            "weakest_criterion": agent3_round1_eval["weakest_criterion"],
            "weakest_reason": agent3_round1_eval["weakest_reason"]
        },
        "history": state["history"],
        "instruction": "Đề xuất giải pháp mới. KHÔNG được đề xuất lại bất kỳ hướng nào đã xuất hiện trong history và bị từ chối vì cùng lý do. Nếu weakest_criterion là 'khả thi build trong 7 tiếng bằng Codex', giải pháp mới PHẢI khác về bản chất (phạm vi kiến trúc/cơ chế kỹ thuật)."
    }
    log("AGENT 4: Nhận Payload kèm Full History", "Agent 4 phân tích điểm yếu cấu trúc từ Agent 3...")

    agent4_proposal = {
        "analysis": "Điểm yếu duy nhất là Khả thi trong 7 tiếng (5.5/10). Nguyên nhân là tham lam làm video streaming và carrier scraping bên ngoài.",
        "structural_changes": [
            "BỎ TOÀN BỘ module video streaming nặng nề và crawler bên thứ ba.",
            "CHUYỂN SANG cơ chế AI-Native 'Smart Keyframe Extraction + GPT-4o Multimodal Forensics': Người dùng tải video/ảnh đóng gói và khui hộp, hệ thống tự động trích 3 cặp khung hình mấu chốt (tem vận đơn, niêm phong băng dính, lòng gói hàng).",
            "Ứng dụng OpenAI GPT-4o với Structured Outputs để trả về JSON kết luận: độ trùng khớp bao bì (%), vị trí tem có dấu vết bóc mở (bounding box), và tỷ lệ rủi ro tráo ruột.",
            "Module Tự chủ (Autonomous Action): Tự động render 1-click 'Shopee / Carrier Formal Dispute Package' (gồm ảnh bằng chứng gắn watermark + văn bản khiếu nại trích dẫn điều khoản sàn chuẩn chỉnh).",
            "Codex 7h Scope cực kỳ tinh gọn: Next.js frontend với 3 view trực quan (Upload & Frame Extraction, Forensic Heatmap, Dispute Resolution Summary) + FastAPI kết nối OpenAI API. Có thể build và test hoàn hảo trong 4.5 tiếng!"
        ]
    }
    log("AGENT 4: Đề xuất giải pháp khắc phục điểm yếu", json.dumps(agent4_proposal, indent=2, ensure_ascii=False))

    # -------------------------------------------------------------
    # STEP 7: Agent 5 - Solution Critic
    # -------------------------------------------------------------
    agent5_critique = {
        "checklist": {
            "1_match_build_direction": "ĐẠT - Vẫn giữ nguyên hướng Autonomous & Adaptive AI, Agent tự động phân tích và sinh trọn gói hồ sơ khiếu nại pháp lý.",
            "2_check_blacklist_and_clones": "ĐẠT - Không trùng với bất kỳ tool thông thường nào trên thị trường.",
            "3_resolve_weakest_reason": "ĐẠT - Giải quyết triệt để vấn đề 7 tiếng: Chuyển từ streaming sang keyframe trích xuất và tận dụng tối đa OpenAI GPT-4o multimodal structured outputs, giảm 80% độ phức tạp hạ tầng.",
            "4_new_risk_assessment": "CẢNH BÁO NHẸ CHO AGENT 6: Phải giữ cho giao diện demo có visual so sánh bằng chứng cực kỳ ấn tượng (forensic heatmap / bounding boxes) để giám khảo thấy ngay sự đột phá của AI-Native, không bị nhầm là form upload ảnh đơn giản."
        },
        "verdict": "DUYỆT (PASS) -> Cho phép Agent 6 tổng hợp bản hoàn thiện."
    }
    log("AGENT 5: Phản biện theo Checklist Rubric Mục 6", json.dumps(agent5_critique, indent=2, ensure_ascii=False))

    # -------------------------------------------------------------
    # STEP 8: Agent 6 - Idea Synthesizer & Polisher
    # -------------------------------------------------------------
    agent6_refined_idea = {
        "title": "COD-Shield: Autonomous Multimodal Evidence Forensics & 1-Click Dispute Settlement Agent for SEA E-Commerce",
        "build_direction": "Autonomous & Adaptive AI (Primary) + Deep-Domain AI (SEA E-Commerce Logistics)",
        "target_audience": "Nhà bán lẻ vừa và nhỏ (MSMEs) trên Shopee, TikTok Shop, Lazada tại Việt Nam, Indonesia, Philippines.",
        "problem_statement": "Tại ĐNA, COD chiếm >60% đơn hàng. Vấn nạn lừa đảo tráo hàng hoàn (khách nhận hàng xịn, trả lại hộp rác/gạch đá) khiến người bán thiệt hại nặng nề. Xử lý khiếu nại thủ công tốn 7-14 ngày, đòi hỏi nhân viên tua hàng giờ video gói hàng/mở hộp để tìm bằng chứng đối soát.",
        "solution_architecture": {
            "step_1_multimodal_intake": "Nhà bán/người mua upload video hoặc chùm ảnh đóng gói & khui hàng. Module Keyframe Extractor tự động chọn 3 cặp khung hình then chốt (mã vận đơn, băng dính niêm phong, vật phẩm bên trong).",
            "step_2_forensic_agent": "OpenAI GPT-4o Multimodal Agent thực hiện đối chiếu chéo (Cross-modal Verification): Phát hiện vết rạch dán lại, tem rách, sai lệch chủng loại sản phẩm, sinh Forensic Evidence Score (0-100%).",
            "step_3_autonomous_settlement": "Agent tự động đối chiếu chính sách khiếu nại của Shopee/TikTok Shop/Đơn vị vận chuyển, sinh ngay bộ hồ sơ pháp lý chuẩn chỉnh kèm ảnh bằng chứng có timestamp và watermark, tự động gửi yêu cầu đền bù."
        },
        "codex_7h_hackathon_execution": {
            "backend": "FastAPI xử lý trích xuất keyframe nhẹ và gọi OpenAI GPT-4o với Pydantic Structured Outputs (đảm bảo phản hồi schema chuẩn 100%).",
            "frontend": "Next.js Tailwind UI do Codex sinh trong 2 tiếng: Giao diện Drag & Drop đối chiếu song song 2 luồng chứng cứ (Gói hàng vs Khui hàng) + Bounding box phát hiện giả mạo + Nút 'Dispatch Dispute' tự động.",
            "demo_flow": "Demo kịch bản thực tế 1 đơn hàng bị tráo iPhone thành cục xà phòng: Upload -> AI chỉ ra vết rạch đáy hộp chỉ sau 5 giây -> Tự sinh đơn khiếu nại gửi sàn và bồi thường ngay."
        },
        "self_reflection_novelty": "So với bản ban đầu đã qua Agent 2, ý tưởng KHÔNG hề bị trôi dạt về hướng generic mà ngược lại còn sắc nét hơn, giữ đúng góc độc quyền về 'Multimodal COD Dispute Forensics' giải quyết bài toán đau đớn nhất của TMĐT Đông Nam Á.",
        "route_decision": "agent3_evaluate"
    }
    log("AGENT 6: Tổng hợp & Tự phản chiếu góc độc quyền", json.dumps(agent6_refined_idea, indent=2, ensure_ascii=False))

    # Increment loop counter
    state["current_loop"] = 2
    save_state(state)
    log("ORCHESTRATOR", f"Chuyển sang Vòng lặp {state['current_loop']}. Chuẩn bị gửi payload stateless cho Agent 3...")

    # -------------------------------------------------------------
    # STEP 9: Agent 3 - Rubric Evaluation (Round 2 - Stateless)
    # -------------------------------------------------------------
    agent3_round2_payload = {
        "idea": agent6_refined_idea,
        "rubric": "Gate (Khớp hướng), Gần gũi (30%), Giá trị (30%), Khả thi 7h Codex (40%)",
        "instruction": "Chấm điểm ý tưởng này như thể đây là lần đầu tiên bạn thấy nó."
    }

    agent3_round2_eval = {
        "gate_build_direction": {
            "status": "PASS",
            "comment": "Khớp hoàn hảo hướng 'Autonomous & Adaptive AI' và 'Deep-Domain AI'. Hệ thống khép kín từ nhận diện chứng cứ đa phương thức đến phán quyết và tạo hồ sơ pháp lý."
        },
        "criterion_2_gan_gui": {
            "score": 9.2,
            "weight": 0.3,
            "comment": "Rất sát thực tế Đông Nam Á. Mọi ban giám khảo của Sea (Shopee) đều thấu hiểu ngay nỗi đau COD này."
        },
        "criterion_3_gia_tri": {
            "score": 8.8,
            "weight": 0.3,
            "comment": "Giá trị giải quyết vấn đề vượt trội: Cắt giảm 95% thời gian xử lý tranh chấp, cứu vãn hàng triệu USD thất thoát cho nhà bán hàng, tăng tính minh bạch cho sàn."
        },
        "criterion_4_kha_thi_codex_7h": {
            "score": 8.8,
            "weight": 0.4,
            "comment": "CỰC KỲ KHẢ THI TRONG 7 TIẾNG: Thiết kế kiến trúc rất thông minh khi chuyển sang trích xuất keyframe và dùng sức mạnh cốt lõi của GPT-4o Structured Outputs. Codex có thể sinh toàn bộ Next.js UI và FastAPI backend trong 4 tiếng, dành 3 tiếng còn lại hoàn thiện demo flow."
        },
        "total_score": round(9.2 * 0.3 + 8.8 * 0.3 + 8.8 * 0.4, 2), # 8.92
        "verdict": "ĐẠT",
        "weakest_criterion": "Không có tiêu chí nào dưới ngưỡng (thấp nhất là 8.8/10)",
        "weakest_reason": "Không có điểm nghẽn nghiêm trọng. Đạt chuẩn chất lượng cao để đem đi thi đấu."
    }
    log("AGENT 3: Kết quả chấm Rubric (Vòng 2 - Stateless)", json.dumps(agent3_round2_eval, indent=2, ensure_ascii=False))

    # Finalize state
    state["history"].append({
        "round": 2,
        "idea": agent6_refined_idea,
        "agent3_scores": {
            "total": agent3_round2_eval["total_score"],
            "gate": agent3_round2_eval["gate_build_direction"]["status"],
            "c2_gan_gui": agent3_round2_eval["criterion_2_gan_gui"]["score"],
            "c3_gia_tri": agent3_round2_eval["criterion_3_gia_tri"]["score"],
            "c4_kha_thi": agent3_round2_eval["criterion_4_kha_thi_codex_7h"]["score"]
        },
        "verdict": "ĐẠT"
    })
    save_state(state)

    log("ORCHESTRATOR", f"KẾT QUẢ CUỐI CÙNG: ĐẠT! Điểm tổng kết: {agent3_round2_eval['total_score']}/10 (Ngưỡng yêu cầu: >= 8.0). Workflow kết thúc thành công ở Vòng {state['current_loop']}.")

    # Generate Markdown Report
    with open(REPORT_FILE, "w", encoding="utf-8") as f:
        f.write("# BÁO CÁO THỰC THI WORKFLOW: SEA X OPENAI CODEX HACKATHON\n\n")
        f.write(f"**Trạng thái chung cuộc**: ĐẠT CHUẨN (SUCCESS)\n")
        f.write(f"**Tổng số vòng lặp**: {state['current_loop']} vòng\n")
        f.write(f"**Số lần Agent 2 yêu cầu retry ở vòng khởi tạo**: {state['gen2_retry_count']} lần\n")
        f.write(f"**Điểm số vòng chung kết (Agent 3)**: {agent3_round2_eval['total_score']} / 10.0\n\n")
        f.write("---\n\n")
        for item in execution_log:
            f.write(f"## {item['step']}\n\n")
            if item['content'].startswith("{"):
                f.write(f"```json\n{item['content']}\n```\n\n")
            else:
                f.write(f"{item['content']}\n\n")

    print(f"\n[OK] Đã lưu báo cáo hoàn chỉnh vào {REPORT_FILE}")
    print(f"[OK] Đã cập nhật file {STATE_FILE}")

if __name__ == "__main__":
    run_simulation()
